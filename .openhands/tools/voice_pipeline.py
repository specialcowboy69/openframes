#!/usr/bin/env python3
"""Voz (Fish Audio) + recorte de colas + timings, para un video de openframes.

Uso:  python3 voice_pipeline.py --dir <dir del video> --ref <reference_id>

Genera assets/voice/NN.wav y NN.txt a partir de las lineas de guion de SCRIPT.md
(lineas con 4 espacios de sangria), recorta el silencio de cola y deja un JSON de
timings que consume retime.py.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

API = "https://api.fish.audio/v1/tts"
MODEL = "s2.1-pro"
NOISE = "-40dB"
MIN_GAP = 0.12
HERE = os.path.dirname(os.path.abspath(__file__))


def script_lines(script_md):
    text = open(script_md, encoding="utf-8").read()
    lines = [m.group(1).strip() for m in re.finditer(r"^    (\S.*)$", text, re.M)]
    if not lines:
        sys.exit(f"No he encontrado lineas de guion en {script_md}")
    return lines


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", path], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def speak(text, ref, key, out_path):
    payload = json.dumps({"text": text, "reference_id": ref,
                          "format": "wav", "model": MODEL}).encode()
    req = urllib.request.Request(API, data=payload, headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=240) as resp:
            audio = resp.read()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:300]
        sys.exit(f"Fish Audio HTTP {exc.code} en '{text[:40]}...': {body}")
    if len(audio) < 1000:
        sys.exit(f"Respuesta demasiado corta para '{text[:40]}...': {len(audio)} bytes")
    with open(out_path, "wb") as fh:
        fh.write(audio)


def trailing_silence(path):
    """Inicio del silencio FINAL del clip, o None si el clip acaba con voz.

    silencedetect emite silence_start / silence_end. Una pausa interna NO es la cola:
    solo cuenta si el silencio llega al final del fichero. Ojo: tomar el ultimo
    silence_start a secas trunca el clip en la ultima coma del guion.
    """
    proc = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af",
                           f"silencedetect=noise={NOISE}:d={MIN_GAP}", "-f", "null", "-"],
                          capture_output=True, text=True)
    events = re.findall(r"(silence_start|silence_end): ([0-9.]+)", proc.stderr)
    if not events:
        return None
    kind, last = events[-1]
    if kind == "silence_start":
        return float(last)
    if duration(path) - float(last) <= 0.05 and len(events) >= 2 and events[-2][0] == "silence_start":
        return float(events[-2][1])
    return None


def trim(path, tail):
    """Recorta la cola a `tail` s. Nunca alarga: si no hay silencio suficiente, deja el clip entero."""
    dur = duration(path)
    start = trailing_silence(path)
    if start is None or start + tail >= dur:
        return dur
    target = round(start + tail, 3)
    tmp = path + ".tmp.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", path, "-t", str(target),
                    "-c:a", "pcm_s16le", tmp], check=True)
    os.replace(tmp, path)
    return duration(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--tail", type=float, default=0.18)
    ap.add_argument("--min-frame", type=float, default=3.0)
    ap.add_argument("--timing", default=os.path.join(HERE, "voice-timing.json"))
    args = ap.parse_args()

    key = os.environ.get("FISH_API_KEY")
    if not key:
        sys.exit("Falta FISH_API_KEY en el entorno")

    vdir = os.path.join(args.dir, "assets", "voice")
    os.makedirs(vdir, exist_ok=True)
    lines = script_lines(os.path.join(args.dir, "SCRIPT.md"))

    clip, scene, start, cursor = {}, {}, {}, 0.0
    for i, line in enumerate(lines, 1):
        wav = os.path.join(vdir, f"{i:02d}.wav")
        print(f"[{i:02d}/{len(lines)}] {line[:58]}")
        speak(line, args.ref, key, wav)
        with open(os.path.join(vdir, f"{i:02d}.txt"), "w", encoding="utf-8") as fh:
            fh.write(line + "\n")
        clip[i] = round(trim(wav, args.tail), 3)
        scene[i] = round(max(args.min_frame, clip[i]), 3)
        start[i] = round(cursor, 3)
        cursor = round(cursor + scene[i], 3)

    timing = {"clip": clip, "scene": scene, "start": start,
              "total": round(cursor, 3), "voice_ref": args.ref}
    with open(args.timing, "w", encoding="utf-8") as fh:
        json.dump(timing, fh, indent=2)

    print(f"\n{'L':<4}{'clip':>8}{'escena':>9}{'inicio':>9}{'fin':>9}")
    for i in clip:
        print(f"{i:02d}  {clip[i]:>7.3f}{scene[i]:>9.3f}{start[i]:>9.3f}{start[i] + scene[i]:>9.3f}")
    print(f"\nTOTAL = {cursor:.3f} s   clips {min(clip.values()):.3f}-{max(clip.values()):.3f} s")
    print(f"timings -> {args.timing}")
    if max(clip.values()) > 5.0:
        print("  AVISO: algun clip supera 5 s; habria que partir ese frame")


if __name__ == "__main__":
    main()
