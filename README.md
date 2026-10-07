# openframes

Producción de vídeo corto (9:16) para redes sobre marketing digital, SEO, SEM, IA y
Google. Faceless, voz en off, frames de 3-5 s, subtítulos karaoke y música.

Hecho con [HyperFrames](https://hyperframes.heygen.com/) (HTML → vídeo).

## Estructura

```
IDEAS.md                     Backlog de ideas (una idea = un vídeo)
README.md                    Este archivo
videos/<proyecto>/           Un proyecto de vídeo por carpeta
  BRIEF.md                   Qué es y para quién
  SCRIPT.md                  Guion bloqueado (voz en off)
  STORYBOARD.md              Plan frame a frame
  index.html                 La composición (el vídeo en sí)
  assets/voice/              Clips de voz en off
  assets/music/track.wav     Cama musical
  compositions/components/   Bloques (subtítulos karaoke)
  renders/video.mp4          Vídeo final
```

## Vídeos

| ID | Título | Duración | Estado |
|----|--------|----------|--------|
| V1 | Por qué copiar el título del nº1 no funciona | 42,5 s | Renderizado |
| V2 | Dónde colocar el modificador (y el error de lujo) | 34,5 s | Renderizado |

V2 se publica **después** de V1 (da por sabido qué es un "modificador").

## Cómo se produce cada vídeo

1. Guion para redes (hook, una idea, jerga definida antes de usarla).
2. Frames de 3-5 s (`SCRIPT.md` + `STORYBOARD.md`).
3. Voz en off local (Kokoro, español).
4. Montaje de la composición (HyperFrames).
5. Subtítulos karaoke.
6. Música (MusicGen local), por debajo de la voz.
7. `check` (lint + runtime + layout + motion + contraste) y render a MP4.

## Convenciones

- Formato 9:16 (1080×1920), faceless, español.
- CTA de guardar. Todo debe entenderse sin sonido (texto en pantalla).
- Paleta: fondo oscuro, un acento verde ácido (y rojo para advertencias).
