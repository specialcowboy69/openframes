#!/usr/bin/env python3
"""Efectos de sonido para un video de openframes: los sintetiza y los mezcla en
una sola pista (assets/sfx/sfx.wav) anclada a los tiempos de cada aparicion.

Uso:  python3 sfx.py --dir <dir del video> [--timing <json>] [--gain <x>]

Los efectos son deterministicos (PRNG con semilla fija), asi que el render se
repite igual. Los tiempos salen del array S de index.html mas el desfase local de
cada animacion.

Modo cues (retrocompatible). Si un evento de assets/sfx/events.json declara
"cue" en lugar de "local", el efecto se ata al instante en que la voz nombra esa
palabra, calculado con el MISMO reparto por longitud de palabra que usa el
karaoke y el helper cue() de index.html (S[n-1] + DUR[n-1]*len_previas/len_linea).
Asi, si la pieza rehace sus cues, el sonido se mueve con ellos:

    {"scene": 2, "cue": ["Alec"],        "kind": "pop", "gain": 0.65}
    {"scene": 2, "cue": ["2010", 1],     "kind": "tick", "gain": 0.70}
    {"scene": 3, "cue": ["buscan"], "offset": 0.045, "kind": "key", "gain": 0.35}

El "offset" (opcional, en segundos) es el desfase propio del elemento dentro del
cue (p. ej. el caracter i de un tecleo con stagger, o una linea de tachado que se
dibuja 0,3 s despues); por defecto 0. Los eventos con "local" (o los proyectos sin
"cue") se anclan exactamente igual que siempre: S[scene-1] + local.
"""
import argparse
import json
import math
import os
import random
import re
import wave

SR = 44100
HERE = os.path.dirname(os.path.abspath(__file__))

# Inicio de cada escena (debe coincidir con el array S de index.html)
S = [0, 4.226, 7.981, 11.626, 15.192, 18.441, 20.699, 23.49, 24.693, 27.546]

# (escena, desfase local, efecto, ganancia)
EVENTS = [
    (1, 0.15, "whoosh", 0.55), (1, 0.72, "pop", 0.75), (1, 1.30, "pop", 0.60), (1, 1.85, "pop", 0.60),
    (2, 0.11, "whoosh", 0.45), (2, 0.61, "tick", 0.70), (2, 1.30, "pop", 0.75),
    (3, 0.11, "whoosh", 0.45), (3, 0.45, "tick", 0.60), (3, 1.00, "tick", 0.60), (3, 1.60, "ding", 0.55),
    (4, 0.11, "whoosh", 0.45), (4, 0.45, "pop", 0.60), (4, 1.40, "tick", 0.60),
    (5, 0.06, "whoosh", 0.45), (5, 0.45, "swoosh_up", 0.60), (5, 1.05, "swoosh_up", 0.45),
    (6, 0.20, "thud", 0.85), (6, 0.50, "pop", 0.45), (6, 1.05, "buzz", 0.45),
    (7, 0.10, "ding", 0.60), (7, 0.45, "tick", 0.60), (7, 1.25, "thud", 0.75), (7, 1.75, "pop", 0.55),
    (8, 0.05, "whoosh", 0.55), (8, 0.20, "swoosh_up", 0.55), (8, 0.75, "click", 0.70),
    (9, 0.25, "pop", 0.65), (9, 0.65, "swoosh_up", 0.55), (9, 1.25, "pop", 0.65), (9, 1.65, "swoosh_down", 0.55),
    (10, 0.20, "pop", 0.70), (10, 0.55, "ding", 0.60), (10, 1.15, "pop", 0.65),
]


def env_bell(t, dur, attack=0.006, power=2.0):
    if t < attack:
        return t / attack
    return max(0.0, (1 - (t - attack) / max(1e-6, dur - attack))) ** power


def env_exp(t, tau):
    return math.exp(-t / tau)


def render(kind, rng):
    """Devuelve (samples, duracion) del efecto."""
    if kind == "pop":
        dur, out = 0.13, []
        for i in range(int(SR * dur)):
            t = i / SR
            f = 900 + 1500 * (t / dur)
            out.append(0.9 * math.sin(2 * math.pi * f * t) * env_exp(t, 0.035))
        return out
    if kind == "tick":
        dur, out = 0.045, []
        for i in range(int(SR * dur)):
            t = i / SR
            out.append(0.8 * math.sin(2 * math.pi * 2600 * t) * env_exp(t, 0.008))
        return out
    if kind == "click":
        dur, out = 0.06, []
        for i in range(int(SR * dur)):
            t = i / SR
            noise = rng.uniform(-1, 1) * 0.5
            out.append((0.7 * math.sin(2 * math.pi * 1500 * t) + noise) * env_exp(t, 0.010))
        return out
    if kind in ("whoosh", "swoosh_up", "swoosh_down"):
        dur = 0.36
        out, lp = [], 0.0
        for i in range(int(SR * dur)):
            t = i / SR
            p = t / dur
            if kind == "whoosh":
                amp, cutoff = math.sin(math.pi * p) ** 0.8, 0.10 + 0.25 * math.sin(math.pi * p)
            elif kind == "swoosh_up":
                amp, cutoff = p ** 0.6, 0.04 + 0.34 * p
            else:
                amp, cutoff = (1 - p) ** 0.6, 0.38 - 0.34 * p
            lp += cutoff * (rng.uniform(-1, 1) - lp)
            out.append(1.5 * lp * amp)
        return out
    if kind == "ding":
        dur, out = 0.75, []
        for i in range(int(SR * dur)):
            t = i / SR
            s = math.sin(2 * math.pi * 1568 * t) + 0.45 * math.sin(2 * math.pi * 2349 * t)
            out.append(0.55 * s * env_exp(t, 0.16))
        return out
    if kind == "thud":
        dur, out = 0.32, []
        for i in range(int(SR * dur)):
            t = i / SR
            f = 88 - 40 * (t / dur)
            s = math.sin(2 * math.pi * f * t)
            s += 0.25 * rng.uniform(-1, 1) * (1 - t / dur) ** 6
            out.append(1.0 * s * env_exp(t, 0.055))
        return out
    if kind == "buzz":
        dur, out = 0.30, []
        for i in range(int(SR * dur)):
            t = i / SR
            sq = 1.0 if math.sin(2 * math.pi * 175 * t) >= 0 else -1.0
            trem = 0.55 + 0.45 * math.sin(2 * math.pi * 26 * t)
            out.append(0.42 * sq * trem * env_bell(t, dur, 0.01, 1.4))
        return out
    if kind == "key":
        # Pulsacion de tecla: transitorio corto y mecanico. PRNG propio y con
        # semilla fija para no alterar la secuencia de los efectos existentes.
        r = random.Random(20261012)
        dur, out, lp = 0.045, [], 0.0
        for i in range(int(SR * dur)):
            t = i / SR
            n = r.uniform(-1, 1)
            lp += 0.55 * (n - lp)
            s = 0.45 * math.sin(2 * math.pi * 1750 * t) + 0.7 * lp
            out.append(0.9 * s * env_exp(t, 0.006))
        return out
    raise ValueError(kind)


def load_scene_starts(video_dir, fallback):
    """El array S real del proyecto (asi el tool no queda cableado a un video)."""
    html = open(os.path.join(video_dir, "index.html"), encoding="utf-8").read()
    m = re.search(r"const S = \[([^\]]*)\]", html)
    return [float(x) for x in m.group(1).split(",")] if m else fallback


def load_cue_source(video_dir, fallback):
    """S, LINES y DUR del proyecto, tal cual los usa index.html (karaoke/cue())."""
    html = open(os.path.join(video_dir, "index.html"), encoding="utf-8").read()
    m = re.search(r"const S = \[([^\]]*)\]", html)
    starts = [float(x) for x in m.group(1).split(",")] if m else fallback
    lm = re.search(r"const LINES = \[(.*?)\];", html, re.S)
    dm = re.search(r"const DUR = \[([^\]]*)\]", html)
    lines = re.findall(r'"((?:[^"\\]|\\.)*)"', lm.group(1)) if lm else []
    durs = [float(x) for x in dm.group(1).split(",")] if dm else []
    return starts, lines, durs


def _nz(w):
    return re.sub(r"[^a-z0-9áéíóúüñ]", "", w.lower())


def cue_time(starts, lines, durs, n, word, occ=1):
    """Instante absoluto del cue: mismo reparto por longitud que el karaoke."""
    words = [w for w in re.split(r"\s+", lines[n - 1]) if w]
    total = sum(len(w) for w in words)
    goal, acc, seen = _nz(word), 0, 0
    for w in words:
        if _nz(w) == goal:
            seen += 1
            if seen == occ:
                return starts[n - 1] + durs[n - 1] * (acc / total)
        acc += len(w)
    raise ValueError(f"cue no encontrado: linea {n}, palabra {word!r}, ocurrencia {occ}")


def load_events(video_dir):
    """Eventos del proyecto si trae assets/sfx/events.json; si no, los de V2.

    Cada evento es un dict con {"scene", "kind", "gain"} y bien "local" (segundos
    desde el arranque de su escena) o "cue" (["palabra", ocurrencia]) con un
    "offset" opcional. Ver el docstring del modulo para el modo cues.
    """
    path = os.path.join(video_dir, "assets", "sfx", "events.json")
    if not os.path.exists(path):
        return [{"scene": s, "local": t, "kind": k, "gain": g} for s, t, k, g in EVENTS]
    return json.load(open(path, encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--timing", default=os.path.join(HERE, "voice-timing.json"))
    ap.add_argument("--gain", type=float, default=1.0)
    args = ap.parse_args()

    starts, lines, durs = load_cue_source(args.dir, S)
    events = load_events(args.dir)
    total = json.load(open(args.timing, encoding="utf-8"))["total"]
    n = int(SR * total)
    track = [0.0] * n
    rng = random.Random(20261008)

    for e in events:
        scene, kind, gain = int(e["scene"]), e["kind"], float(e["gain"])
        if "cue" in e:
            word = e["cue"][0]
            occ = int(e["cue"][1]) if len(e["cue"]) > 1 else 1
            abs_t = cue_time(starts, lines, durs, scene, word, occ) + float(e.get("offset", 0.0))
        else:
            abs_t = starts[scene - 1] + float(e["local"])
        samples = render(kind, rng)
        start = int(SR * abs_t)
        peak = max(1e-9, max(abs(x) for x in samples))
        scale = (gain * args.gain) / peak
        for i, v in enumerate(samples):
            j = start + i
            if j < n:
                track[j] += v * scale

    peak = max(1e-9, max(abs(x) for x in track))
    if peak > 0.92:
        track = [x * (0.92 / peak) for x in track]

    out = os.path.join(args.dir, "assets", "sfx", "sfx.wav")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with wave.open(out, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(b"".join(
            int(max(-1.0, min(1.0, x)) * 32767).to_bytes(2, "little", signed=True) for x in track))
    print(f"{len(events)} efectos -> {out}")
    print(f"duracion {total} s  ({n} muestras)  pico {peak:.3f}")


if __name__ == "__main__":
    main()
