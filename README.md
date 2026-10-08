# openframes

Producción de vídeo corto (9:16) para redes sobre marketing digital, SEO, SEM, IA y
Google. Faceless, voz en off, frames de 3-5 s, subtítulos karaoke y música.

Hecho con [HyperFrames](https://hyperframes.heygen.com/) (HTML → vídeo).

## Estructura

```
README.md                    Este archivo
PROFILE.md                   Forma de trabajar y resultados esperados
WORKFLOW.md                  Proceso de producción, paso a paso
DESIGN.md                    Sistema visual y sonoro (paleta, componentes, movimiento, efectos)
DECISIONS.md                 Registro de decisiones (fecha, motivo, alternativas)
IDEAS.md                     Backlog de ideas (una idea = un vídeo)
videos/<proyecto>/           Un proyecto de vídeo por carpeta
  BRIEF.md                   Qué es y para quién
  SCRIPT.md                  Guion bloqueado (voz en off)
  STORYBOARD.md              Plan frame a frame
  index.html                 La composición (el vídeo en sí)
  assets/voice/              Clips de voz en off (uno por frase)
  assets/music/track.wav     Cama musical
  assets/sfx/sfx.wav         Efectos de sonido
  compositions/components/   Bloques (subtítulos karaoke)
  renders/video.mp4          Vídeo final
```

## Vídeos

| ID | Título | Duración | Estado |
|----|--------|----------|--------|
| V1 | Por qué copiar el título del nº1 no funciona | 42,5 s | Publicado |
| V2 | Dónde colocar el modificador (y el error de lujo) | 29,8 s | Renderizado |

V2 se publica **después** de V1 (da por sabido qué es un "modificador").

## Cómo se produce cada vídeo

1. Guion para redes (hook, una idea, jerga definida antes de usarla).
2. **Escena = clip**: cada frase dura lo que dura su audio, sin silencios
   (`SCRIPT.md` + `STORYBOARD.md`).
3. Voz en off con **Fish Audio** (voz oficial `Pablo`, español) — `tools/voice_pipeline.py`.
4. Montaje de la composición (HyperFrames) **a base de gráficos**, no de rótulos: ventana de
   navegador, tarjetas de resultado, iconos SVG, cursor (ver `DESIGN.md`).
5. **Efectos de sonido** en cada aparición (`tools/sfx.py`) + subtítulos karaoke.
6. Música, por debajo de la voz.
7. Re-timado de todo con `tools/retime.py`.
8. `check` (lint + runtime + layout + motion + contraste) y render a MP4.

## Convenciones

- Formato 9:16 (1080×1920), faceless, español.
- CTA de guardar. Se entiende **sin sonido** por karaoke + gráficos, no por acumular texto.
- Paleta: fondo oscuro, **un solo acento** verde ácido, rojo para advertencias y dorado para lujo.
