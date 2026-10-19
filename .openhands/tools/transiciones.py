#!/usr/bin/env python3
"""Extiende la cola de cada escena saliente con la duracion de su transicion.

Uso:  python3 transiciones.py --dir <dir del video>

Lee el array TR del index.html del proyecto ([[escena, tipo, duracion], ...]) y
suma la duracion a la data-duration de esa escena, para que siga viva durante el
cruce sin tocar los <audio>.

DEBE ejecutarse DESPUES de retime.py: retime reescribe data-duration a
escena = clip y borra esta extension.
"""
import argparse
import os
import re
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    args = ap.parse_args()

    path = os.path.join(args.dir, "index.html")
    html = open(path, encoding="utf-8").read()
    m = re.search(r"const TR = \[(.*?)\];", html, re.S)
    if not m:
        sys.exit("no encuentro el array TR en index.html")

    tr = re.findall(r'\[\s*(\d+)\s*,\s*"(\w+)"\s*,\s*([0-9.]+)\s*\]', m.group(1))
    if not tr:
        sys.exit("el array TR no tiene entradas reconocibles")

    print(f"{'escena':<8}{'antes':>8}{'+':>7}{'despues':>9}  tipo")
    for n, kind, d in tr:
        n, d = int(n), float(d)
        pat = re.compile(rf'(id="s{n}" data-start="[^"]*" data-duration=")([^"]*)(")')

        def bump(mm, d=d, n=n, kind=kind):
            before = float(mm.group(2))
            after = round(before + d, 3)
            print(f"s{n:<7}{before:>8.3f}{d:>7.2f}{after:>9.3f}  {kind}")
            return f"{mm.group(1)}{after}{mm.group(3)}"

        html, count = pat.subn(bump, html)
        if count != 1:
            sys.exit(f"s{n}: {count} coincidencias (esperaba 1)")

    open(path, "w", encoding="utf-8").write(html)
    print(f"\n{len(tr)} colas extendidas")


if __name__ == "__main__":
    main()
