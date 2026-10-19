#!/usr/bin/env python3
"""Mide el desfase sonido/imagen del render FINAL (no de la composicion).

Criterio de aceptacion (lo que el dueno comprueba):
  * cortes (whoosh):  |audio - imagen| <= 0,04 s en los 10 cortes.
  * cues de elemento:|audio - imagen| <= 0,06 s en la zona (caja) del elemento.

Se mide SIEMPRE sobre los ficheros finales:
  - Imagen: cambios reales de los fotogramas de renders/video.mp4 (30 fps).
  - Audio:  ataques/arranques en assets/sfx/sfx.wav.

  - El instante visual de un CORTE es el INICIO PERCEPTIBLE de la transicion
    (primera subida por encima del 30 % del pico de cambio de la banda central
    dentro de su ventana TR), no el data-start nominal de la escena.
    El corte nominal sale de la tabla TR de index.html: la transicion n arranca
    en S[n] y dura d; el whoosh se ata al inicio perceptible, no a S[n].
  - El whoosh de cada corte se localiza por filtro adaptado (su cresta subiente
    es caracteristica); asi no lo confunde el ataque de otro efecto.
  - Cada cue de elemento se mide dentro de la CAJA real del elemento (no en toda
    la pantalla) y su audio es el ataque transitorio mas cercano. El instante
    nominal del cue se recalcula con la MISMA formula de index.html (S + DUR por
    longitud de palabra), no cableado.

Uso:
  python3 medir_sync.py [--dir <dir del video>] [--video ruta.mp4] [--sfx ruta.wav]
"""
import argparse
import pathlib
import re
import subprocess
import wave

import numpy as np

FPS = 30
W, H = 160, 284

# La lista de cues NO se cablea: se lee de assets/sfx/events.json (todo evento
# con "cue" que no sea el whoosh de transicion). El instante nominal se
# recalcula con la MISMA formula cue() de index.html.
WHOOSH_KINDS = {"whoosh"}


def read_events(video_dir, S, lines, durs):
    """Eventos de elemento (todo menos el whoosh de transicion), con su instante
    nominal. Los que declaran "cue" se anclan con la MISMA formula cue() de
    index.html; los "local" a S[escena-1] + local. Se deduplican por instante
    (un mismo cue con dos efectos -pop+ding- se mide una sola vez)."""
    import json
    ev = json.loads((video_dir / "assets" / "sfx" / "events.json").read_text(encoding="utf-8"))
    out, seen = [], set()
    for e in ev:
        if e["kind"] in WHOOSH_KINDS:
            continue
        scene = int(e["scene"])
        if "cue" in e:
            word = e["cue"][0]
            occ = int(e["cue"][1]) if len(e["cue"]) > 1 else 1
            off = float(e.get("offset", 0.0))
            t = cue_time(S, durs, lines, scene, word, occ) + off
            tag = f"{word}{'' if occ == 1 else '#' + str(occ)}@s{scene}" + (f"+{off:g}" if off else "")
            key = (scene, "cue", word, occ, round(off, 3))
        else:
            t = S[scene - 1] + float(e["local"])
            tag = f"local {e['local']:g}@s{scene}"
            key = (scene, "local", round(e["local"], 3))
        if key in seen:
            continue
        seen.add(key)
        out.append((t, scene, tag, "cue" in e))
    return sorted(out)


def zone_box(D, f0):
    """Caja del elemento: region donde se concentra el cambio de imagen cerca del
    cue nominal. Devuelve (x0,y0,x1,y1) o None si el cambio es global (no
    localizable: transicion encima). D = lista de |dif| por fotograma."""
    i0, i1 = max(0, f0 - 1), min(len(D), f0 + 4)
    C = np.sum(D[i0:i1].astype(np.int32), axis=0)
    if C.max() <= 1e-6:
        return None
    m = C >= max(0.35 * C.max(), 4.0)
    ys, xs = np.where(m)
    if len(xs) < 6:
        return None
    x0, x1 = int(xs.min()), int(xs.max()) + 1
    y0, y1 = int(ys.min()), int(ys.max()) + 1
    if (x1 - x0) * (y1 - y0) > 0.55 * W * H:
        return None
    return x0, y0, x1, y1


def zone_onset(D, box, f0):
    """Primer fotograma con cambio en la caja, arrancando antes del cue, mas
    diagnosticos de fiabilidad.

    Umbral bajo (10 % del pico) para captar el INICIO del cambio, no el 30 % que
    usa el corte (donde la rampa lenta de la transicion importa).

    Devuelve (t, pico, rise, edge) o None si no hay cambio apreciable:
      pico = magnitud del cambio (px) -> senal debil = medida no fiable;
      rise = fotogramas del 10 % al 90 % del pico -> >3 = ataque gradual
             (un trazo que se dibuja, una opacidad lenta): el inicio perceptible
             no se puede fechar con precision;
      edge = el primer fotograma con cambio cae en el borde de la ventana
             (probable contagio de la animacion anterior)."""
    x0, y0, x1, y1 = box
    dz = np.array([D[i][y0:y1, x0:x1].mean() for i in range(len(D))])
    lo = max(1, f0 - int(0.12 * FPS))
    hi = min(len(dz) - 1, f0 + int(0.30 * FPS))
    if hi - lo < 3:
        return None
    base = float(np.median(dz[max(0, lo - 10):lo]))
    pico = float(dz[lo:hi].max())
    if pico < base + 0.02:
        return None
    thr = base + max(0.01, (pico - base) * 0.10)
    over = np.where(dz[lo:hi] > thr)[0]
    j = int(over[0])
    hi90 = base + 0.9 * (pico - base)
    o90 = np.where(dz[lo:hi] >= hi90)[0]
    rise = (int(o90[0]) - j + 1) if len(o90) else (hi - lo)
    edge = j <= 1 or j >= hi - lo - 2
    return (lo + j + 1) / FPS, pico, rise, edge


def read_source(video_dir):
    html = (video_dir / "index.html").read_text(encoding="utf-8")
    S = [float(x) for x in re.search(r"const S = \[([^\]]*)\]", html).group(1).split(",")]
    TR = [(int(a), k, float(d)) for a, k, d in re.findall(
        r'\[\s*(\d+)\s*,\s*"(\w+)"\s*,\s*([0-9.]+)\s*\]',
        re.search(r"const TR = \[(.*?)\];", html, re.S).group(1))]
    lines = re.findall(r'"((?:[^"\\]|\\.)*)"',
                       re.search(r"const LINES = \[(.*?)\];", html, re.S).group(1))
    durs = [float(x) for x in re.search(r"const DUR = \[([^\]]*)\]", html).group(1).split(",")]
    return S, TR, lines, durs


def cue_time(S, durs, lines, n, word, occ=1):
    nz = lambda w: re.sub(r"[^a-z0-9áéíóúüñ]", "", w.lower())
    words = [w for w in re.split(r"\s+", lines[n - 1]) if w]
    total = sum(len(w) for w in words)
    goal, acc, seen = nz(word), 0, 0
    for w in words:
        if nz(w) == goal:
            seen += 1
            if seen == occ:
                return S[n - 1] + durs[n - 1] * (acc / total)
        acc += len(w)
    return S[n - 1]


def image_cut(mad, suelo, T, d):
    """Inicio perceptible de la transicion: 1er fotograma > 30 % del pico de cambio."""
    i0 = max(1, int((T - 0.25) * FPS))
    i1 = min(len(mad) - 2, int((T + d + 0.50) * FPS))
    if i1 - i0 < 5:
        return None, 0.0
    seg = mad[i0:i1]
    pico = float(seg.max())
    if pico < suelo + 0.25:
        return None, pico
    thr = suelo + (pico - suelo) * 0.30
    return (i0 + 1 + int(np.argmax(seg > thr))) / FPS, pico


def whoosh_template():
    """Plantilla del whoosh: su cresta subiente (0..0,30 s). El tramo final se
    solapa con otros efectos; la cresta lo identifica sola. Se lee del propio
    sintetizador de la casa (sfx.render) para no duplicar el sonido."""
    import sfx
    rng = __import__("random").Random(0)
    tpl = np.array(sfx.render("whoosh", rng)) ** 2
    tpl = np.sqrt(np.convolve(tpl, np.ones(441) / 441, "same"))[::int(sfx.SR * 0.01)][:30]
    return tpl / np.linalg.norm(tpl)


def whoosh_score(env, tpl):
    L = len(tpl)
    score = np.full(len(env) - L, -1.0)
    for k in range(len(env) - L):
        nrm = np.linalg.norm(env[k:k + L])
        if nrm > 1e-6:
            score[k] = float(env[k:k + L] @ tpl) / nrm
    return score


def whoosh_at(score, vis, win=0.08):
    """Whoosh mas verosimil dentro de +-win s de `vis` (filtro adaptado)."""
    k0 = max(0, int((vis - win) * 100))
    k1 = min(len(score), int((vis + win) * 100) + 1)
    if k1 <= k0:
        return None, 0.0
    seg = score[k0:k1]
    k = k0 + int(np.argmax(seg))
    return (k / 100.0, float(score[k])) if seg.max() > 0.5 else (None, float(seg.max()))


def load_audio(path, hop_s=0.01):
    w = wave.open(str(path), "rb")
    sr, ch, n = w.getframerate(), w.getnchannels(), w.getnframes()
    raw = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32)
    if ch > 1:
        raw = raw.reshape(-1, ch).mean(axis=1)
    hop = int(sr * hop_s)
    return np.sqrt(np.convolve(raw ** 2, np.ones(hop) / hop, "same"))[::hop]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=".")
    ap.add_argument("--video", default=None)
    ap.add_argument("--sfx", default=None)
    args = ap.parse_args()
    P = pathlib.Path(args.dir).resolve()
    video = pathlib.Path(args.video) if args.video else P / "renders" / "video.mp4"
    sfxw = pathlib.Path(args.sfx) if args.sfx else P / "assets" / "sfx" / "sfx.wav"

    env = load_audio(sfxw)
    wsc = whoosh_score(env, whoosh_template())

    buf = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video),
                          "-vf", f"fps={FPS},scale={W}:{H},format=gray", "-f", "rawvideo", "-"],
                         capture_output=True).stdout
    fr = np.frombuffer(buf, dtype=np.uint8).astype(np.int16)
    NF = len(fr) // (W * H)
    fr = fr[:NF * W * H].reshape(NF, H, W)
    mad = np.abs(np.diff(fr[:, int(0.14 * H):int(0.72 * H), :], axis=0)).mean(axis=(1, 2))
    suelo = float(np.median(mad))

    DD = np.clip(np.abs(np.diff(fr, axis=0)), 0, 255).astype(np.uint8)

    S, TR, lines, durs = read_source(P)
    TRd = {n: d for n, _k, d in TR}          # TR[n] = transicion hacia la escena n+1

    def in_transition(m, t):
        """El cue cae dentro de la transicion de entrada de su escena: la imagen
        se mueve en bloque y no se puede aislar el elemento."""
        return m > 1 and t < S[m - 1] + TRd.get(m - 1, 0.0) + 0.02

    print(f"video {video}   ({NF} fotogramas, {NF / FPS:.2f} s)")
    print(f"sfx   {sfxw}\n")
    print("CORTES (whoosh)   objetivo |a-i| <= 0,04 s")
    print(f"{'corte':<7}{'T=TR':>8}{'tipo':>7}{'d':>6}{'imagen':>9}{'whoosh':>9}{'a-i':>9}  ver")
    ok = tot = 0
    for n, kind, d in TR:
        T = S[n]
        vis, pico = image_cut(mad, suelo, T, d)
        if vis is None:
            print(f"B{n + 1:<6}{T:8.3f}{kind:>7}{d:6.2f}{'n/d':>9}")
            tot += 1
            continue
        a, sc = whoosh_at(wsc, vis)
        tot += 1
        if a is None:
            print(f"B{n + 1:<6}{T:8.3f}{kind:>7}{d:6.2f}{vis:9.3f}{'--':>9}{'':>9}"
                  f"  FALTA whoosh (score {sc:.2f})")
            continue
        da = a - vis
        good = abs(da) <= 0.04
        ok += good
        print(f"B{n + 1:<6}{T:8.3f}{kind:>7}{d:6.2f}{vis:9.3f}{a:9.3f}{da:+9.3f}  "
              f"{'OK' if good else 'FALLA'}  (s={sc:.2f})")
    print(f"cortes dentro de barra: {ok}/{tot}")

    evs = read_events(P, S, lines, durs)
    # Un pulso a <80 ms de otro (tecleo, cuenta) no se puede aislar del vecino ni
    # en audio ni en imagen: se mide solo el primero de la racha y los demas se
    # declaran sub-eventos de la secuencia.
    rows = []
    for k, (t, sc, g, isc) in enumerate(evs):
        prev = t - evs[k - 1][0] if k > 0 else 9.9
        nxt = evs[k + 1][0] - t if k + 1 < len(evs) else 9.9
        dense = prev < 0.08 or nxt < 0.08
        skip = dense and prev < 0.08
        rows.append((t, sc, g, isc, skip, dense))

    def measure(t, scene, tag):
        """(nota, vis, a, da); nota != None y da == None -> no fiable (se deja)."""
        f0 = int(round(t * FPS))
        if in_transition(scene, t):
            return "cue dentro de la transicion de entrada: no fiable, se deja", None, None, None
        box = zone_box(DD, f0)
        on = zone_onset(DD, box, f0) if box else None
        if env[max(0, int((t - 0.15) * 100)):int((t + 0.15) * 100)].max() < 10.0:
            return "sin sonido propio en la ventana", None, None, None
        k0 = max(3, int((t - 0.09) * 100))
        k1 = min(len(env) - 1, int((t + 0.09) * 100))
        slope = env[k0:k1] - env[k0 - 3:k1 - 3]
        a = (k0 + int(np.argmax(slope))) / 100.0
        gradual = float(slope.max()) < 800.0
        if gradual:
            m0, m1 = int((t - 0.15) * 100), int((t + 0.10) * 100)
            mn = float(env[m0:m1].min())
            idx = [i for i in range(m0, m1) if env[i] <= mn + max(2.0, 0.03 * mn)]
            a = (idx[-1] if idx else m0) / 100.0
        if on is None:
            why = ("cambio no localizable (global)" if box is None
                   else "sin cambio detectable en la caja")
            return why + ": no fiable, se deja", None, a, None
        vis, pico, rise, edge = on
        da = a - vis
        if not (pico >= 3.0 and rise <= 2 and not edge):
            why = []
            if pico < 3.0:
                why.append("senal debil")
            if rise > 2:
                why.append("ataque gradual")
            if edge:
                why.append("primer cambio en el borde (contagio)")
            return "; ".join(why) + ": no fiable, se deja", vis, a, da
        return None, vis, a, da

    def show(rows, titulo, barra):
        print(f"\n{titulo}   objetivo |a-i| <= {barra} s")
        print(f"{'evento':<20}{'nominal':>8}{'imagen':>9}{'audio':>9}{'a-i':>9}  ver")
        ok = med = 0
        for t, scene, tag, skip, dense in rows:
            if skip:
                print(f"{tag:<20}{t:8.3f}{'n/d':>9}{'--':>9}{'':>9}"
                      f"  sub-evento de secuencia densa (<80 ms): no aislable, se deja")
                continue
            why, vis, a, da = measure(t, scene, tag)
            if da is None:
                print(f"{tag:<20}{t:8.3f}{('n/d' if vis is None else '%.3f' % vis):>9}"
                      f"{('--' if a is None else '%.3f' % a):>9}{'':>9}  {why}")
                continue
            good = abs(da) <= barra
            ok += good
            med += 1
            ver = "OK" if good else "REV"
            if a < vis - 0.04:
                ver += "  <-- audio >40 ms ANTES de la imagen"
            if dense:
                ver += "  *secuencia (base)"
            print(f"{tag:<20}{t:8.3f}{vis:9.3f}{a:9.3f}{da:+9.3f}  {ver}")
        print(f"dentro de barra: {ok}/{med} medibles  ({len(rows) - med} no medibles/fiables, se dejan)")
        return ok, med

    cues = [(t, s, g, sk, dn) for t, s, g, isc, sk, dn in rows if isc]
    locs = [(t, s, g, sk, dn) for t, s, g, isc, sk, dn in rows if not isc]
    show(cues, "CUES de elemento por ZONA (caja del render)", 0.06)
    show(locs, "LATIDOS locales por ZONA (informativos, sin cue de voz)", 0.06)


if __name__ == "__main__":
    main()
