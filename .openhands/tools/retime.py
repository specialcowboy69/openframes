#!/usr/bin/env python3
"""Re-tima una composicion de openframes desde los timings reales de la voz.

Uso:  python3 retime.py --dir <dir del video> [--timing <json>]

Hace tres cosas:
  1. Reescribe los data-start / data-duration de index.html (raiz, escenas, pistas de
     voz, barra de progreso, karaoke, musica), el array S del timeline y el prog-fill.
  2. Reconstruye la cama musical a la duracion total (bucle con crossfade + fade out),
     partiendo de una copia intacta de la pista original.
  3. Regenera el TRANSCRIPT del karaoke con las palabras del guion y timings anclados
     a las pausas reales de cada clip.
"""
import argparse
import json
import os
import re
import subprocess
import sys

TAIL = 0.08
NOISE = "-40dB"
MIN_GAP = 0.12
HERE = os.path.dirname(os.path.abspath(__file__))


def fmt(x):
    s = f"{x:.3f}".rstrip("0").rstrip(".")
    return s + ".0" if "." not in s else s


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def gaps_of(path):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af",
                          f"silencedetect=noise={NOISE}:d={MIN_GAP}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", err)]
    en = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", err)]
    return list(zip(st, en))


def sub(pattern, repl, text, label):
    text, n = re.subn(pattern, repl, text)
    if n != 1:
        sys.exit(f"{label}: esperaba 1 sustitucion, he hecho {n}")
    print(f"  ok  {label}")
    return text


def patch_html(path, timing):
    html = open(path, encoding="utf-8").read()
    total = fmt(timing["total"])
    html = sub(r'(id="root" data-composition-id="main" data-start=")[^"]*(" data-duration=")[^"]*(")',
               rf"\g<1>0\g<2>{total}\g<3>", html, "root")
    for n in sorted(int(k) for k in timing["scene"]):
        html = sub(rf'(id="s{n}" data-start=")[^"]*(" data-duration=")[^"]*(")',
                   rf'\g<1>{fmt(timing["start"][str(n)])}\g<2>{fmt(timing["scene"][str(n)])}\g<3>',
                   html, f"escena s{n}")
    order = sorted(int(k) for k in timing["clip"])
    for n in order:
        start_n = timing["start"][str(n)]
        # la cola de cada clip ya es silencio: recortar 2 ms evita que el linter
        # lea como solape el hecho de que los clips se toquen exactamente
        if n == order[-1]:
            dur = timing["clip"][str(n)]
        else:
            dur = round(timing["start"][str(n + 1)] - start_n - 0.002, 3)
        html = sub(rf'(id="vo-{n:02d}" class="clip" data-start=")[^"]*(" data-duration=")[^"]*(")',
                   rf"\g<1>{fmt(start_n)}\g<2>{fmt(dur)}\g<3>", html, f"voz vo-{n:02d}")
    html = sub(r'(id="prog" data-start=")[^"]*(" data-duration=")[^"]*(")',
               rf"\g<1>0\g<2>{total}\g<3>", html, "progress")
    html = sub(r'(data-composition-id="caption-pill-karaoke" data-composition-src="[^"]*" data-start=")'
               r'[^"]*(" data-duration=")[^"]*(")', rf"\g<1>0\g<2>{total}\g<3>", html, "karaoke")
    html = sub(r'(id="music" class="clip" data-start=")[^"]*(" data-duration=")[^"]*(")',
               rf"\g<1>0\g<2>{total}\g<3>", html, "music")
    html = sub(r'(id="sfx" class="clip" data-start=")[^"]*(" data-duration=")[^"]*(")',
               rf"\g<1>0\g<2>{total}\g<3>", html, "sfx")
    order = sorted(int(k) for k in timing["start"])
    html = sub(r'(const S = \[)[^\]]*(\];)',
               r"\g<1>" + ", ".join(fmt(timing["start"][str(i)]) for i in order) + r"\g<2>",
               html, "array S")
    html = sub(r'(tl\.fromTo\("#prog-fill", \{ scaleX: 0 \}, \{ scaleX: 1, duration: )[0-9.]+(, ease: "none" \})',
               rf"\g<1>{total}\g<2>", html, "prog-fill")
    open(path, "w", encoding="utf-8").write(html)


def rebuild_music(video_dir, total):
    out = os.path.join(video_dir, "assets", "music", "track.wav")
    src = os.path.join(HERE, "music_bed.wav")
    if not os.path.exists(src):
        src = out
        print(f"  AVISO: sin {src} intacto; reuso la pista actual (puede tener un bache de fade)")
    tmp = out + ".new.wav"
    fade_st = max(0.0, total - 1.6)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-i", src, "-filter_complex",
                    f"[0:a][1:a]acrossfade=d=1.5[c];[c]afade=t=out:st={fade_st:.2f}:d=1.6[o]",
                    "-map", "[o]", "-t", str(total), "-c:a", "pcm_s16le", tmp], check=True)
    os.replace(tmp, out)
    print(f"  ok  musica -> {duration(out):.3f} s (objetivo {total})")


def gen_transcript(video_dir, comp_path, timing):
    text = open(os.path.join(video_dir, "SCRIPT.md"), encoding="utf-8").read()
    lines = [m.group(1).strip() for m in re.finditer(r"^    (\S.*)$", text, re.M)]
    entries = []
    for i, line in enumerate(lines, 1):
        p = os.path.join(video_dir, "assets", "voice", f"{i:02d}.wav")
        dur = duration(p)
        sp_end = dur - TAIL
        gaps = [(a, b) for a, b in gaps_of(p) if b <= sp_end - 0.01]
        words = line.split()
        weights = [len(w) + 1 for w in words]
        W = sum(weights)
        speech = sp_end - sum(b - a for a, b in gaps)
        q, acc = [0.0], 0
        for w in weights:
            acc += w
            q.append(acc / W * speech)
        gpos, prev = [], 0.0
        for a, b in gaps:
            gpos.append(a - prev)
            prev += b - a
        shift = [0.0] * (len(words) + 1)
        for (a, b), pos in zip(gaps, gpos):
            j = min(range(len(q)), key=lambda k: abs(q[k] - pos))
            shift[j] += b - a
        cum = 0.0
        for k in range(len(words)):
            s = timing["start"][str(i)] + q[k] + cum
            cum += shift[k]
            e = timing["start"][str(i)] + q[k + 1] + cum
            entries.append((words[k], round(s, 3), round(max(e, s + 0.05), 3)))
        print(f"  L{i:02d}  {dur:.3f}s  pausas={len(gaps)}  palabras={len(words)}")

    body = ",\n".join(f'        {{ text: "{t.replace(chr(34), chr(92) + chr(34))}", '
                      f"start: {fmt(s)}, end: {fmt(e)} }}" for t, s, e in entries)
    new_array = "var TRANSCRIPT = [\n" + body + "\n      ];"
    html = open(comp_path, encoding="utf-8").read()
    html = sub(r"var DURATION = [0-9.]+;", f"var DURATION = {fmt(timing['total'])};", html, "DURATION")
    html = sub(r'(data-timeline-locked="" data-start="0" data-duration=")[0-9.]+(")',
               rf"\g<1>{fmt(timing['total'])}\g<2>", html, "karaoke duration")
    html = sub(r"(?s)var TRANSCRIPT = \[.*?\n      \];", new_array, html, "TRANSCRIPT")
    open(comp_path, "w", encoding="utf-8").write(html)
    print(f"  ok  {len(entries)} palabras en el karaoke")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--timing", default=os.path.join(HERE, "voice-timing.json"))
    ap.add_argument("--comp", default="compositions/components/caption-pill-karaoke.html")
    args = ap.parse_args()

    timing = json.load(open(args.timing, encoding="utf-8"))
    total = timing["total"]
    print(f"Timings de {args.timing}  (total {total} s, voz {timing.get('voice_ref')})\n")
    print("index.html:")
    patch_html(os.path.join(args.dir, "index.html"), timing)
    print("musica:")
    rebuild_music(args.dir, total)
    print("karaoke:")
    gen_transcript(args.dir, os.path.join(args.dir, args.comp), timing)
    print(f"\nRe-timado completo. TOTAL = {total} s")


if __name__ == "__main__":
    main()
