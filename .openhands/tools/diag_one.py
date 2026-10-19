#!/usr/bin/env python3
"""Diagnostico: genera UNA linea sin recortar y muestra su perfil de silencios.

Uso: python3 diag_one.py <reference_id> <texto>
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import voice_pipeline as vp

ref, line = sys.argv[1], sys.argv[2]
out = "/tmp/diag.wav"
vp.speak(line, ref, os.environ["FISH_API_KEY"], out)
print(f"texto   : {line}")
print(f"bytes   : {os.path.getsize(out)}")
print(f"duracion: {vp.duration(out):.3f} s")
err = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af",
                      "silencedetect=noise=-40dB:d=0.12", "-f", "null", "-"],
                     capture_output=True, text=True).stderr
events = [l.strip() for l in err.splitlines() if "silence_" in l]
print(f"silencios ({len(events)}):")
for e in events:
    print("   ", e)
