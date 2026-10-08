# WORKFLOW — proceso de producción de un vídeo

Proceso estándar, paso a paso, para producir un vídeo de la serie. Repetible.
Herramienta: **HyperFrames** (`npx hyperframes@0.8.138`), HTML → vídeo.
Sistema visual y sonoro: **`DESIGN.md`** (léelo antes de tocar una composición).

---

## 0. Entorno (una sola vez por sesión)

```bash
sudo apt-get update && sudo apt-get install -y ffmpeg unzip    # ffmpeg obligatorio; unzip para el navegador del render
npx hyperframes browser ensure                                  # navegador para el render
```

- El sandbox **se reconstruye entre sesiones**: `apt`/`pip` se pierden (ffmpeg, unzip, Chrome).
  El workspace (`/workspace/...`) sí persiste.
- La toolchain propia vive en **`.openhands/tools/`** (sin trackear): `voice_pipeline.py`,
  `retime.py`, `sfx.py`, `diag_one.py` y `music_bed.wav`.
- Sin `unzip`, el render falla con un `▲ Something went wrong` **sin detalle** (la descarga de
  Chrome no puede descomprimirse). Con `--debug` sí se ve la causa.

## 1. Ruta

Todo vídeo de la serie es **faceless-explainer**: sin cámara, sin web, visuales inventados.
Formato 9:16, español, voz en off.

## 2. Guion

- **Hook en los primeros segundos.** Sin intro, sin logo.
- **Una sola idea por vídeo.** Si hay más, se parte en otro vídeo.
- **Definir la jerga antes de usarla.**
- Frases cortas (6-10 palabras), ritmo hablado.
- **Sin datos inventados**; los números salen del material del usuario.
- CTA de **guardar**.
- **Piensa en gráfico, no en rótulo**: cada línea del guion debería poder ilustrarse con una
  forma (D25). Si no se te ocurre el gráfico, la línea probablemente sobra.

Documentos: `BRIEF.md` (qué/para quién), `SCRIPT.md` (guion por líneas),
`STORYBOARD.md` (plan frame a frame).

## 3. Crear el proyecto

```bash
npx hyperframes init "videos/<proyecto>" --non-interactive \
  --example=blank --skill=faceless-explainer
```

## 4. Voz en off (Fish Audio, voz oficial `Pablo`)

Un `.wav` por línea de `SCRIPT.md` (líneas con 4 espacios de sangría):

```bash
FISH_API_KEY="$FISH_API_KEY" python3 .openhands/tools/voice_pipeline.py \
  --dir videos/<proyecto> --ref 1bd666ea8ada44c789e0fec21cf78f33 \
  --tail 0.08 --min-frame 0
```

- Voz en uso: **`Pablo`** (oficial de Fish Audio, es-ES, masculina, *brisk*). Otra voz = otro `--ref`.
- `--tail 0.08`: recorta la cola de silencio para que la voz vaya continua.
- `--min-frame 0`: **escena = clip**, sin relleno.
- El script deja los timings en `.openhands/tools/voice-timing.json`.
- Endpoint por si hay que depurar a mano: `POST https://api.fish.audio/v1/tts` con
  `{"text","reference_id","format":"wav","model":"s2.1-pro"}`.

## 5. Timings y frames

- **Escena = clip**: cada escena dura exactamente lo que dura su frase. **No hay silencios.**
  (Decisión D23, pedido explícito del usuario.)
- Como la voz es rápida, las escenas salen de **1,2 a 4,2 s**. Antes eran 3-5 s con relleno mudo.
- Duración total = suma de los clips. Objetivo 30-40 s (V2 quedó en 29,8 s; se acepta).
- La animación de cada escena **no puede durar más que la escena**.

## 6. Montaje de la composición (`index.html`)

- Raíz: `data-composition-id="main"`, `data-duration="<total>"`, `data-width="1080"`, `data-height="1920"`.
- Cada escena: `<section class="scene clip" id="sN" data-start data-duration>` con CSS propio
  `position:absolute; inset:0`. (La clase `.clip` sola **no** da caja completa.)
- **Todo `<audio>` con `data-start` necesita `id`**, o el render sale **mudo**.
- Animación **seek-safe**: estado inicial en CSS + GSAP `.to()`. Nada de `.from()`, contadores,
  `Date.now()` ni `Math.random()`. Registrar `window.__timelines = window.__timelines || {}` antes de asignar.
- Componentes y clases: **`DESIGN.md` §3**. Nada de URLs sueltas: siempre dentro de la ventana de
  navegador.
- Zonas seguras 9:16: nada crítico en el 15 % superior ni el 25 % inferior.

## 7. Efectos de sonido

```bash
python3 .openhands/tools/sfx.py --dir videos/<proyecto>
```

- 9 efectos sintetizados (whoosh, pop, tick, click, swoosh, ding, thud, buzz) mezclados en
  `assets/sfx/sfx.wav`, anclados a la aparición de cada elemento. Vocabulario: `DESIGN.md` §5.
- Entra en la composición como un único `<audio id="sfx">` (track 4, `data-volume="0.5"`).
- Determinista (PRNG con semilla): el mismo vídeo suena igual siempre.

## 8. Subtítulos karaoke

```bash
npx hyperframes add caption-pill-karaoke
```

- Montado como sub-composición (`<template>` + CSS con selector `[data-composition-id=...]`,
  script en IIFE, registra su propio `window.__timelines`), montado con `data-composition-src`.
- El `TRANSCRIPT` por palabra lo genera `retime.py` con los timings **anclados a las pausas reales**
  de cada clip (mejor que el reparto proporcional a ciegas).

## 9. Música

- Cama en `assets/music/track.wav`, `<audio id="music" data-volume="0.18">`. Nunca por encima de la voz.
- `retime.py` la reconstruye a la duración total partiendo de la copia intacta
  (`.openhands/tools/music_bed.wav`, extraída de git): bucle con `acrossfade=d=1.5` + `afade` de salida.
- El modelo local `facebook/musicgen-small` tiene un **límite duro de ~30 s** por generación; para
  más, generar ≤28 s y empalmar.

## 10. Re-timar todo de una vez

```bash
python3 .openhands/tools/retime.py --dir videos/<proyecto>
```

Reescribe **de golpe**: raíz, escenas, pistas de voz, `prog`, karaoke, música, sfx, el array `S` y
el `prog-fill`; reconstruye la música; y regenera el `TRANSCRIPT` del karaoke.
No re-timarlo a mano: son 30 valores que se desincronizan.

## 11. Verificar

```bash
npm run check      # lint + runtime + layout + motion + contraste WCAG
```

- **Cero errores** antes de renderizar. Los avisos de "sub-composiciones" son esperados
  (composición en un solo archivo, decisión D10).
- **No hay revisión visual directa**: comprobar con `check` (layout a 9 muestras) y, si hace falta,
  contar píxeles por escena para confirmar que ninguna sale en negro:
  `ffmpeg -i frame.png -f rawvideo -pix_fmt rgb24 - | <clasificar por color>`.
- Opcional: `npx hyperframes snapshot --at t1,t2`.

## 12. Render y preview

```bash
npx hyperframes render -o renders/video.mp4
HYPERFRAMES_PREVIEW_HOST=0.0.0.0 npx hyperframes preview --background --port 12000 --no-open
```

- El preview **debe** escuchar en `0.0.0.0` o el proxy externo da **502**.
- Los renders largos, **en primer plano**: en segundo plano el navegador del render falla.
- **Parar el preview antes de editar el HTML** (`preview --stop`): el Studio reescribe
  `index.html` (mete `data-hf-id`, redondea duraciones y trocea elementos). Relanzarlo al terminar.

## 13. Publicar

Se publica en orden cuando un vídeo depende del anterior (V2 va después de V1).

1. **Commit + push** del contenido a `openframes` (repo público; `content` de git = este repo).
2. **Alojar el MP4**: Release pública en `openframes`, tag `video-<slug>`, assets
   `<slug>.mp4` + `<slug>-cover.png` (portada = fotograma representativo). Esa URL es la que
   consume Instagram; **no** se usa R2/Cloudflare para este camino.
3. **Cola**: añadir la entrada en `specialcowboy69/hypervideo`
   (`content/video-queue/queue.json` + `video-queue.csv`) con `status: needs_review`,
   `outputs.render` (URL del .mp4), `outputs.cover` y el `caption`. Push a `main`.
4. **Disparar** la Action manual **`HyperFrames publish Reel (manual)`** (`publish-reel.yml`) con
   `slug`, `caption`, `publish_at` (`now` o ISO futuro), `platforms` y
   `confirmation: PUBLICAR <slug>`. La Action reserva el job en `main` (dedupe) y luego llama a n8n.
   **Nunca llamar al webhook a mano.**
5. Verificar: run de la Action + `reel_status` en la cola.

### 13.1 Si falla

- **La portada rompe n8n.** Con `include_cover=true` el webhook responde `{"jobs":[]}` y n8n dice
  `not_found`; el último paso falla con *"The n8n response did not confirm this Reel job"*.
  Reintentar con **`include_cover=false`** (la portada se queda en `outputs.cover`, solo se omite en
  el envío). Le pasó a V1 y a V2. El MP4 de n8n no se revienta por la portada.
- Un intento fallido deja el ítem en **`publishing`** y eso **bloquea duplicados** (el siguiente
  intento falla en la reserva y se salta la llamada a n8n: salvaguarda correcta, **no insistir**).
  Para reconciliar: consultar el `jobId` con **`HyperFrames check Reel status (manual)`**; si n8n
  devuelve `not_found`, borrar `publish_attempt`, volver a `status: needs_review` y anotar el fallo
  en `notes`; después ya se puede reintentar.
- **El CSV de la cola usa LF.** Reescribirlo con `stringifyCsv` de
  `scripts/schedule-instagram-reel.mjs`; con el `csv` de Python sale CRLF y el diff ensucia el
  fichero entero.
- `publish_at: now` solo pide publicación inmediata: la aceptación deja `reel_status: pending` y
  Meta publica después. El estado final se lee con el workflow de estado.

---

## Ciclo de cambio (una vez el vídeo ya existe)

```bash
npx hyperframes preview --stop                 # 1. el Studio no debe tocar el fichero
# 2. editar index.html / guion / assets
python3 .openhands/tools/voice_pipeline.py ...  # 3. si cambia el guion
python3 .openhands/tools/sfx.py --dir ...       # 4. si cambian los tiempos
python3 .openhands/tools/retime.py --dir ...    # 5. re-timar
npm run check && npx hyperframes render -o renders/video.mp4
npx hyperframes preview --background --port 12000 --no-open   # 6. devolver el preview
```

## Checklist final

- [ ] Guion con hook, una idea, jerga definida, CTA de guardar.
- [ ] **Escena = clip**: sin silencios; total 30-40 s (o justificado).
- [ ] Voz Fish Audio (`Pablo`) en español, ritmo de redes.
- [ ] **El peso lo llevan los gráficos** (ventana de navegador, iconos, cursor); el texto es mínimo.
- [ ] Se entiende **sin sonido** (karaoke + gráficos).
- [ ] **Efectos de sonido** en cada aparición; música por debajo de la voz.
- [ ] Karaoke con la palabra activa resaltada y timings reales.
- [ ] Zonas seguras respetadas.
- [ ] `check` con **0 errores** y contraste WCAG AA.
- [ ] MP4 renderizado y preview para revisión.
- [ ] `DESIGN.md`, `DECISIONS.md`, `IDEAS.md` y `STORYBOARD.md` actualizados.
