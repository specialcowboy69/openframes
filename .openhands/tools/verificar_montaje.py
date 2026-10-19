#!/usr/bin/env python3
"""Verifica un montaje SIN ver la imagen.

Uso:  python3 verificar_montaje.py --dir <dir del video>

Dos comprobaciones, las dos obligatorias antes de dar un montaje por bueno:

1. CRUCES: por fotograma a 30 fps y con umbral de luminancia FIJO (25, el fondo
   ronda 13), mide el tramo continuo mas largo sin contenido en cada transicion.
   Barra: <= 0,15 s (4-5 fotogramas). Se descarta el umbral relativo a la media:
   una superficie grande y clara sube la media y descarta filas que si tienen
   contenido (falsos positivos y negativos).
2. AUDIO: huecos de silencio > 0,12 s por debajo de -48 dBFS. La voz de la serie
   va continua: el numero tiene que ser CERO.

Lee S y TR del index.html del proyecto.
"""
import argparse
import os
import re
import struct
import subprocess
import sys

W, H = 1080, 1920
FPS = 30
DARK = 25.0          # luminancia de "hay algo"
EMPTY = 4.0          # % de filas con contenido por debajo del cual el cuadro esta vacio
MAX_EMPTY = 0.15     # s
MAX_GAP = 0.12       # s
GAP_DB = 0.004       # -48 dBFS


def read_arrays(video_dir):
    html = open(os.path.join(video_dir, "index.html"), encoding="utf-8").read()
    s = re.search(r"const S = \[([^\]]*)\]", html)
    tr = re.search(r"const TR = \[(.*?)\];", html, re.S)
    if not s or not tr:
        sys.exit("no encuentro los arrays S / TR en index.html")
    starts = [float(x) for x in s.group(1).split(",")]
    trans = [(int(a), kind, float(d)) for a, kind, d in
             re.findall(r'\[\s*(\d+)\s*,\s*"(\w+)"\s*,\s*([0-9.]+)\s*\]', tr.group(1))]
    return starts, trans


def coverages(video, t0, dur):
    p = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t0:.3f}", "-t", f"{dur:.3f}",
                        "-i", video, "-vf", f"fps={FPS}", "-f", "rawvideo",
                        "-pix_fmt", "gray", "-"], capture_output=True)
    buf, size, out = p.stdout, W * H, []
    for i in range(len(buf) // size):
        f = buf[i * size:(i + 1) * size]
        hit = sum(1 for y in range(H) if sum(f[y * W:(y + 1) * W][::8]) / (W / 8) > DARK)
        out.append(100.0 * hit / H)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    args = ap.parse_args()
    video = os.path.join(args.dir, "renders", "video.mp4")
    if not os.path.exists(video):
        sys.exit(f"no existe {video}: renderiza antes")

    starts, trans = read_arrays(args.dir)

    print(f"{'cruce':<11}{'tramo vacio':>12}{'min':>8}   veredicto")
    worst = 0.0
    for n, kind, d in trans:
        cov = coverages(video, starts[n] - 0.10, d + 0.20)
        run = best = 0
        for c in cov:
            run = run + 1 if c < EMPTY else 0
            best = max(best, run)
        secs = best / FPS
        worst = max(worst, secs)
        print(f"F{n}->F{n + 1:<6}{secs:>11.2f}s{min(cov):>7.1f}%   "
              f"{'ok' if secs <= MAX_EMPTY else 'LARGO'}")
    print(f"peor tramo sin contenido: {worst:.2f} s (barra: <= {MAX_EMPTY} s)")

    p = subprocess.run(["ffmpeg", "-v", "error", "-i", video, "-map", "0:a:0", "-ac", "1",
                        "-ar", "48000", "-f", "f32le", "-"], capture_output=True)
    n = len(p.stdout) // 4
    vals = struct.unpack(f"<{n}f", p.stdout)
    step = 2400
    env = [((sum(v * v for v in vals[i:i + step]) / step) ** 0.5)
           for i in range(0, n - step, step)]
    gaps, start = [], None
    for i, v in enumerate(env):
        if v < GAP_DB and start is None:
            start = i
        elif v >= GAP_DB and start is not None:
            if (i - start) * 0.05 > MAX_GAP:
                gaps.append((start * 0.05, i * 0.05))
            start = None
    print(f"audio: {len(env) * 0.05:.2f} s · huecos > {MAX_GAP} s por debajo de -48 dBFS: "
          f"{len(gaps)}")
    for a, b in gaps[:5]:
        print(f"    {a:.2f}s -> {b:.2f}s ({b - a:.2f}s)")

    ok = worst <= MAX_EMPTY and not gaps
    print("\n" + ("MONTAJE OK" if ok else "REVISAR: hay cruces o huecos fuera de barra"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
