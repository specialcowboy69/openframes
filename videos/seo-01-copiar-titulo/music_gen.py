import sys, time, os
import numpy as np
import soundfile as sf
import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration

SECONDS = float(sys.argv[1]) if len(sys.argv) > 1 else 8.0
OUT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/music.wav"
PROMPT = sys.argv[3] if len(sys.argv) > 3 else (
    "minimal modern electronic groove, clean subtle pulse, no melody, "
    "low-key tech background music, no drums hit, instrumental"
)

torch.set_num_threads(os.cpu_count() or 4)
print("loading model...", flush=True)
t0 = time.time()
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
model.eval()
print(f"model ready in {time.time()-t0:.1f}s", flush=True)

inputs = processor(text=[PROMPT], padding=True, return_tensors="pt")
with torch.no_grad():
    t1 = time.time()
    audio = model.generate(**inputs, do_sample=True, guidance_scale=3.0,
                           max_new_tokens=int(SECONDS * 50))
    gen = time.time() - t1

sr = model.config.audio_encoder.sampling_rate
data = audio[0, 0].numpy().astype(np.float32)
sf.write(OUT, data, sr)
print(f"generated {len(data)/sr:.1f}s audio in {gen:.1f}s -> {OUT} (sr={sr})", flush=True)
