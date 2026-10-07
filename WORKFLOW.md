# WORKFLOW — proceso de producción de un vídeo

Proceso estándar, paso a paso, para producir un vídeo de la serie. Repetible.
Herramienta: **HyperFrames** (`npx hyperframes@0.8.138`), HTML → vídeo.

---

## 0. Entorno (una sola vez)

```bash
sudo apt-get install -y ffmpeg unzip espeak-ng          # ffmpeg es obligatorio
pip install kokoro-onnx soundfile                        # voz en off local (español)
pip install transformers torch numpy                     # música local (MusicGen)
npx hyperframes browser ensure                           # navegador para el render
```

## 1. Ruta

Todo vídeo de la serie es **faceless-explainer**: sin cámara, sin web, visuales
inventados. Formato 9:16, español, voz en off.

## 2. Guion

- **Hook en los primeros segundos.** Sin intro, sin logo.
- **Una sola idea por vídeo.** Si hay más, se parte en otro vídeo.
- **Definir la jerga antes de usarla** ("esto es el modificador: la palabra extra…").
- Frases cortas (6-10 palabras), ritmo hablado.
- **Sin datos inventados**; los números salen del material del usuario.
- CTA de **guardar**.

Documentos: `BRIEF.md` (qué/para quién), `SCRIPT.md` (guion por líneas),
`STORYBOARD.md` (plan frame a frame).

## 3. Crear el proyecto

```bash
npx hyperframes init "content/videos/<proyecto>" --non-interactive \
  --example=blank --skill=faceless-explainer
```

## 4. Voz en off (Kokoro, local)

Una línea por bloque; se genera un `.wav` por línea:

```bash
npx hyperframes tts assets/voice/01.txt --voice ef_dora --lang es --speed 1.08 \
  -o assets/voice/01.wav
```

- Voz en español disponible: **`ef_dora`**. Siempre `--lang es`.
- `--speed 1.08` para ritmo de redes.
- Medir duración de cada clip: `ffprobe -v error -show_entries format=duration -of csv=p=0 <wav>`.

## 5. Timings y frames

- Cada frame dura **3-5 s**; si un clip de voz es más corto, se **rellena con pausa**
  (el texto se queda en pantalla) para no bajar de 3 s.
- Cada frame de voz empieza donde empieza su frame visual.
- Duración total = suma de los frames. Objetivo 30-40 s.

## 6. Montaje de la composición (`index.html`)

- Raíz: `data-composition-id="main"`, `data-duration="<total>"`, `data-width="1080"`
  `data-height="1920"`.
- Cada escena: `<section class="scene clip" data-start data-duration>` con CSS propio
  `position:absolute; inset:0`. (La clase `.clip` sola **no** da caja completa.)
- **Todo `<audio>` con `data-start` necesita `id`**, o el render sale **mudo**.
- Animación **seek-safe**: estado inicial en CSS + GSAP `.to()`. Nada de `.from()` ni
  contadores. Nada de `Date.now()`/`Math.random()`.
- Registrar: `window.__timelines = window.__timelines || {};` antes de asignar.
- Zonas seguras 9:16: nada crítico en el 15% superior ni el 25% inferior.

## 7. Subtítulos karaoke

```bash
npx hyperframes add caption-pill-karaoke
```

El bloque viene como documento completo 1920×1080. Hay que:
- convertirlo en sub-composición `<template>` (CSS con selector
  `[data-composition-id="caption-pill-karaoke"]`, script dentro de un **IIFE** para que
  su `var tl` no choque con el `const tl` del host);
- ajustar a 1080×1920 y a la paleta (píldora oscura, palabra activa en acento);
- meter su `TRANSCRIPT` con timings **por palabra** (se aproximan repartiendo la
  duración de cada línea proporcional a `len(palabra)+1`);
- montarlo en `index.html` con `data-composition-src`.

## 8. Música

```bash
python3 music_gen.py <segundos> /tmp/seg.wav "prompt de estilo"
```

- Modelo local `facebook/musicgen-small`. **Límite ~30 s por generación**; para más,
  generar ≤28 s y empalmar con `ffmpeg ... acrossfade=d=1.5`, luego `atrim` + `afade`.
- Guardar como `assets/music/track.wav` y añadir en la composición:
  `<audio id="music" data-volume="0.18" data-start="0" data-duration="<total>" src=...>`.
- Volumen 0.18: se oye, pero **nunca tapa la voz**.

## 9. Verificar

```bash
npx hyperframes check          # lint + runtime + layout + motion + contraste WCAG
```

- **Cero errores** antes de renderizar; los avisos de "sub-composiciones" son esperados
  (composición en un solo archivo, decisión D10).
- Opcional: `npx hyperframes snapshot --at t1,t2` para revisar frames concretos.

## 10. Render y preview

```bash
npx hyperframes render -o renders/video.mp4
HYPERFRAMES_PREVIEW_HOST=0.0.0.0 npx hyperframes preview --background --port 12000 --no-open
```

- El preview **debe** escuchar en `0.0.0.0` o el proxy externo da **502**.

## 11. Publicar y guardar

- Publicar la serie **en orden** cuando un vídeo depende del anterior.
- Commit + push del contenido a `openframes` (repo propio, privado).

---

## Checklist final

- [ ] Guion con hook, una idea, jerga definida, CTA de guardar.
- [ ] Frames de 3-5 s; total 30-40 s (o justificado).
- [ ] Voz en off en español, ritmo de redes.
- [ ] Texto en pantalla: se entiende **sin sonido**.
- [ ] Karaoke con la palabra activa resaltada.
- [ ] Música por debajo de la voz.
- [ ] Zonas seguras respetadas.
- [ ] `check` con **0 errores** y contraste WCAG AA.
- [ ] MP4 renderizado y preview para revisión.
- [ ] Backlog (`IDEAS.md`) y decisiones (`DECISIONS.md`) actualizados.
