# Project memory — HyperFrames workspace

## User's content workspace (this repo)
- `content/IDEAS.md` — backlog of video ideas for the user's social account (V1..V10).
- `content/videos/<project>/` — one HyperFrames project per video.

## Git / repo (durable)
- The user's content lives in **`specialcowboy69/openframes`** (own repo). `content/` is
  an **independent git repo nested inside the hyperframes clone**; remote `origin` =
  `https://github.com/specialcowboy69/openframes.git`, branch `main`, identity
  `openhands <openhands@all-hands.dev>`.
- Docs in that repo: `README.md`, `PROFILE.md` (working style + expected results),
  `WORKFLOW.md` (production process), `DECISIONS.md` (decision log), `IDEAS.md` (backlog).
- **Push works only because the `openhands-ai` GitHub App was installed on that repo.**
  The env `GITHUB_TOKEN` is a GitHub App user token (`ghu_`) scoped to its installations;
  it can read public repos but only WRITE where the App is installed. It **cannot create
  repos or change visibility** (`Resource not accessible by integration`).
- So: to write to a new repo, install the app first:
  `https://github.com/apps/openhands-ai/installations/new` → select the repo.
- Never push to the clone's own remote (`heygen-com/hyperframes`).
- Repo was set public to unblock the first push; **the user must set it back to private
  manually** (Settings → General → Danger Zone → Change visibility).
- Push command that works: `git -c credential.helper='!gh auth git-credential' push`
  with `GH_TOKEN="$GITHUB_TOKEN"` exported.

## User content preferences
- **NUNCA añadir avisos de "hecho con IA" / "OpenHands" en captions, vídeos ni texto publicado.**
  (2026-10-08) El usuario lo rechazó expresamente ("sobraba bastante") y pidió que no vuelva a pasar
  **sin su consentimiento**. Regla general: **no añadir al contenido publicable nada que el usuario no
  haya pedido**; si creo que falta un texto, se pregunta antes.
- Faceless explainer, voz en off en español, formato 9:16, 30–40 s.
- Tono directo y didáctico. **Definir la jerga en pantalla antes de usarla.**
- CTA de guardar. Todo debe entenderse en mudo (texto en pantalla siempre).
- Nicho: marketing digital, SEO, SEM, IA, Google.

## Environment quirks (cost real time to learn)
- `bun` NOT installed. Node 24 + `npx hyperframes@0.8.138` works fine.
- Installed via `sudo apt-get` (passwordless sudo available): ffmpeg, unzip, espeak-ng.
- Local TTS: `pip install kokoro-onnx soundfile`. Spanish voice = `ef_dora`, always pass `--lang es`. `--speed` supported (1.0 default; 1.08 used). Model downloads on first call.
- Not signed into HeyGen → local engines only. MusicGen (music) needs transformers+torch (not installed).
- Chrome = `/usr/bin/chromium`; beginFrame unavailable → screenshot fallback, but render still works (~56 s for a 42 s video). `/dev/shm` is only 64 MB; renders still succeeded.
- `npx hyperframes preview --background --port <p> --no-open` + `--status` / `--stop`. Work hosts map port 12000→work-1, 12001→work-2.
- **External access needs a 0.0.0.0 bind.** `preview` defaults to `127.0.0.1` → the work-host proxy returns **502 Bad Gateway**. Set `HYPERFRAMES_PREVIEW_HOST=0.0.0.0` when starting it. Verify with `awk '$2 ~ /:2EE0$/{print $2}' /proc/net/tcp` (0100007F=localhost, 00000000=all). `python3 -m http.server <p> --bind 0.0.0.0` is a good fallback for viewing/downloading files.
- **El render necesita `unzip`.** Sin él, la descarga de `chrome-headless-shell` falla ("no zip archiver is available") y el síntoma visible es un `▲ Something went wrong` **sin detalle**; además `browser ensure` se **queda colgado**. Diagnóstico: `render --debug` sí imprime la causa real. Solución: `sudo apt-get install -y unzip` y reintentar (la primera vez descarga Chrome).
- Un `apt-get` lanzado en segundo plano puede quedar en estado `T` (stopped) y retener `/var/lib/dpkg/lock-frontend` → hay que terminarlo con `sudo kill -9 <pid>` (con `kill` normal da "operation not permitted" si es de root).
- Render local: `npx --yes hyperframes@0.8.138 render -o renders/video.mp4` (~1 min para 37,8 s a 1080×1920 en 4 cores). El propio render baja el audio hasta quedar bajo −1 dBTP.
- Verificación rápida del resultado: `ffprobe` (duración/resolución/audio) + `ffmpeg -af volumedetect` (media ≈ −17 dB ⇒ voz y música presentes) + extraer fotogramas con `ffmpeg -ss <t> -frames:v 1`.
- Karaoke con timings reales: `silencedetect` de cada clip y anclar cada pausa a la frontera de palabra más cercana (mejor que el reparto proporcional a ciegas).

## Fish Audio TTS — FUNCIONA (2026-10-07): voz oficial `Pablo` en uso
- **Resuelto:** el usuario cargó $10 de crédito de API (`cumulative_top_up: "10"`). La generación ya funciona.
- **Voz en uso (V2):** **`Pablo`** — voz **oficial** de Fish Audio (`author: Fish Official`), masculina, es-ES, *brisk*, `state: trained`, `reference_id 1bd666ea8ada44c789e0fec21cf78f33`.
- El **clon propio** ("Consultor Digital", `1bd666ea8ada44c789e0fec21cf78f33`) se **descartó**: su audio de origen venía `quality_passed: false` (*multi speaker*, 0.5745). No está borrado; puede recuperarse si se reentrena con audio limpio.
- Generación por lotes: parsear las líneas de `SCRIPT.md` con `^    (\S.*)$` y POSTear cada una (`format: wav`).
- Los clips de Fish Audio vienen con ~0,12–0,37 s de silencio de cola → recortar la cola (**0,08 s** en V2, para que la voz vaya continua; 0,18 s si se quiere más aire). `-t` no alarga un wav: para alargar hay que rellenar con `apad`.
- **Ojo con el recorte:** una cola solo cuenta si el silencio **llega al final del fichero**. Un clip que acaba con voz pero tiene una pausa interna rompe el atajo "último `silence_start`" y trunca el audio (pasó: la línea 2 quedó de 3,7 s en 1,3 s).
- Toolchain reutilizable en **`.openhands/tools/`** (sin trackear, sobrevive a los reinicios): `voice_pipeline.py` (voz + recorte + timings), `retime.py` (re-tima index.html + karaoke + música + sfx), `sfx.py` (efectos), `diag_one.py` (diagnóstico de una línea) y `music_bed.wav` (cama musical intacta, extraída de git). `/tmp` se vacía en cada arranque: no guardar ahí nada que importe.
- **Voz continua (escena = clip):** `voice_pipeline.py --tail 0.08 --min-frame 0`. `retime.py` recorta 2 ms la duración declarada de cada clip de voz para que el linter no lea como solape que los clips se toquen exactamente.
- **Efectos de sonido:** `sfx.py` sintetiza 9 tipos (pop, tick, click, whoosh, swoosh_up/down, ding, thud, buzz) y los mezcla en `assets/sfx/sfx.wav`. Determinista (PRNG con semilla fija) y gratis. En la composición entra como un único `<audio id="sfx">` (track 4, `data-volume` 0.5).
- **`sfx.py` ya no está cableado a V2** (2026-10-08): lee el array `S` del `index.html` del proyecto y los eventos de `assets/sfx/events.json` (si no existe, usa los 34 de V2). Verificado que V2 sigue dando su pista **byte a byte** (md5 igual).
- **ORDEN OBLIGATORIO de la cadena (V3):** `voice_pipeline.py` → `sfx.py` → `retime.py` → **`transiciones.py`** → `check` → `render`. `retime.py` reescribe las duraciones de escena a `escena = clip` y **borra la cola** que necesitan las transiciones; sin re-aplicarla, la escena saliente desaparece a mitad del cruce. La cadena es idempotente (verificado con `diff`).
- **Herramientas nuevas en `.openhands/tools/`:** `transiciones.py` (extiende la cola de las escenas salientes leyendo el array `TR` del index.html) y `verificar_montaje.py` (QA sin ojos: tramo continuo sin contenido por cruce, con umbral de luminancia **fijo** a 30 fps, barra ≤ 0,15 s + huecos de silencio > 0,12 s bajo −48 dBFS, barra cero). Sale con código 1 si falla.
- **La métrica de cobertura con umbral RELATIVO engaña:** una superficie grande y clara sube la media y descarta filas que sí tienen contenido (me hizo ver un hueco que no existía y tapar otro que sí). Usar umbral fijo (25).
- **Toda escena necesita escenario** (`.card`, `.authcard` o el marco de navegador) desde `t=0`, y si el contenido es escaso, envolverlo en tarjeta: si no, el push deja el lienzo sin contenido (F5/F8 de V3 caían a 2-3 %). Los push sobre escenas oscuras, **cortos (0,25 s)**.
- **V3 montado con esta voz** (`videos/seo-03-autoridad`, 32,05 s, 10 frames): `check` 0 errores, contraste 41/41, peor tramo sin contenido 0,13 s, 0 huecos. Los 14 avisos de lint son `studio_missing_editable_id` (editabilidad en Studio), igual que V2.
- **El Studio reescribe index.html:** con `preview` corriendo, HyperFrames mete `data-hf-id`, redondea duraciones y parte elementos (llegó a trocear `#prog` en `prog-split-*` con `data-duration="0"`). Parar el preview (`preview --stop`) antes de editar y relanzarlo después.
- **No puedo ver imágenes (confirmado por 3 vías el 2026-10-09).** El visor de ficheros dice "Displaying image content" pero no llega nada; el navegador local (tras instalarle Chrome) y el remoto guardan la captura en un fichero y a mí solo me llega la **ruta**. Es el canal de entrada de imágenes del modelo/plataforma, no las herramientas: **no se arregla desde el sandbox**. Por tanto la QA es "sin ojos": `npm run check` (layout a 9 muestras, motion, contraste) + contar píxeles por escena para confirmar que cada escena dibuja lo previsto y no sale en negro.
- **Lo que sí "veo" sin ojos**: (a) **OCR** con `tesseract -l spa+eng` → lee rótulos, la URL de la barra, subtítulos y permite comprobar que no hay avisos de IA; (b) **mapa de brillo** ASCII → `ffmpeg -i f.png -vf scale=60:30 -pix_fmt gray -f rawvideo -` y mapear los bytes a `' .:-=+*#%@'` → se distingue la estructura (banda clara central = tarjeta, marcos oscuros) y se detectan escenas vacías o cruces en blanco; (c) métricas con `ffprobe` (`volumedetect`, `silencedetect`). Para revisión estética: generar una **hoja de contactos** y que la mire el dueño.
- **Instalaciones que se pierden en cada reinicio** (reponer cuando haga falta): `sudo apt-get install -y ffmpeg tesseract-ocr tesseract-ocr-spa` y `npx playwright install chrome` (sin él, el navegador local falla con `Chromium distribution 'chrome' is not found`).
- **Instagram desde el sandbox**: el perfil público da `302 → /accounts/login/` y luego `429` (no hay credenciales de Meta aquí); el endpoint público `/p/<código>/embed/captioned/` **sí responde 200**, así que con la URL de un post se puede intentar sacar la leyenda (texto/DOM) o la URL del MP4.
- V2 montado con esta voz; V1 sigue publicado con Kokoro.
- **2026-10-07 (histórico):** el primer test dio 402 por crédito 0; la clave siempre fue válida (clave mala = 401). El crédito de API es **independiente** del plan de la web de fish.audio.
- Endpoint: `POST https://api.fish.audio/v1/tts`, headers `Authorization: Bearer $FISH_API_KEY`,
  `Content-Type: application/json`. Body:
  `{"text": "...", "reference_id": "1bd666ea8ada44c789e0fec21cf78f33", "format": "wav", "model": "s2.1-pro"}`.
- Same user pipeline otherwise (measure with ffprobe → 3-5 s frames → karaoke → music → check → render).
- ~$15 per 1M UTF-8 bytes; one video ≈ <2 cents.

## Environment resets (important)
- The sandbox is rebuilt between sessions: **apt/pip installs are LOST** (ffmpeg, kokoro,
  torch), but the workspace (`/workspace/...`) and `/tmp` **persist**.
- On resume, verify: `which ffmpeg`; if missing, `sudo apt-get update && sudo apt-get install -y ffmpeg`.
  Reinstall to render: `pip install kokoro-onnx soundfile` and `pip install transformers torch numpy`.

## Publicación (copy y plataformas) — reglas del dueño (2026-10-08)
- **Copy**: texto breve relacionado con el vídeo + **2-3 hashtags**, y nada más. **Sin avisos de autoría** ("hecho con IA"/"OpenHands") en leyenda, vídeo ni rótulos (V1/V2 los llevan por ser anteriores a la regla). CTA de la serie: "Guarda esto". El texto se genera desde el `SCRIPT.md`.
- **Instagram y Facebook: siempre sin portada** (`include_cover=false` → ruta `/video_reels`). Con portada iría a `/videos`, pero n8n rechaza la portada alojada en GitHub Releases (`400 cover_url must use an approved HTTPS media host`); para esa ruta la portada tendría que estar en `media.urltovideo.es`/R2 autorizado. El `video_url` de GitHub Releases **sí** se acepta para IG/FB.
- ~~**YouTube y TikTok: publicados fuera de este flujo; NO reintentar subidas** (orden del dueño, 2026-10-08)~~ **SUPERADA el 2026-10-09 y confirmada el 2026-10-14**: las cuatro plataformas publican por este flujo (MK2 salió en todas).
- **La leyenda nunca se teclea a mano**: se lee del campo `caption` del item de la cola de `hypervideo`. Incidente real: un reintento manual pasó `caption="PLACEHOLDER"` y n8n lo encoló tal cual.
- Documento completo en el repo: `PUBLICACION.md` (raíz de openframes).

## Publicar: la cadena y sus trampas
- Se publica con la Action **`publish-reel.yml`** de `specialcowboy69/hypervideo` (dispatch por API). NO se llama al webhook a mano: `CF_ACCESS_CLIENT_ID/SECRET` viven en los secrets de ese repo y el agente no los tiene.
- La Action **reserva el job en `main`** (item → `publishing` + `publish_attempt`) antes de llamar a n8n. Requiere que el item esté en `status: needs_review` y sin `publish_attempt`, pide el input `confirmation: PUBLICAR <slug>` y que `outputs.render` sea un `.mp4` HTTPS público; registra `scheduled` + jobId.
- El workflow valida que el actor sea el dueño del repo. **El token del entorno ES `specialcowboy69`** (User, no App), así que el dispatch pasa la validación.
- Respuesta válida del webhook: `{"ok":true,"created":1,"jobs":[{"jobId":...,"status":"pending","platforms":[...]}]}`. `created` positivo = **encolado**, no publicado.
- **Si el paso del webhook falla después de reservar**, el item queda en `publishing` y no se puede relanzar a ciegas. Comprobar con la Action **`check-reel-status.yml`** (solo lectura, input `job_id`): si devuelve `not_found`, se reconcilia la reserva (item a `needs_review`, borrar `publish_attempt`) y se reintenta; si existe, no se reenvía.
- Los logs de los runs se leen con **`curl -sL`**; con urllib da **401** porque el endpoint redirige a S3 y reenvía la cabecera `Authorization`.
- Crear la entrada de la cola yo mismo funciona (token con escritura en `hypervideo`): se editan `content/video-queue/queue.json` y `content/video-queue/video-queue.csv` desde la API (PUT con `sha`), con `status: needs_review`. **El CSV usa LF**: generarlo con `stringifyCsv` de `scripts/schedule-instagram-reel.mjs` (node); con el módulo `csv` de Python sale **CRLF** y ensucia el diff entero.
- Para YouTube/TikTok haría falta además: allowlist de hosts de GitHub en n8n (`github.com`, `release-assets.githubusercontent.com`, `objects.githubusercontent.com`), validar la URL enviada y no la del redirect (302 con query firmada), seguir redirects, aceptar `application/octet-stream` y forzar `video/mp4` + nombre `<slug>.mp4` al subir, activar los workers (hoy `503 platform_not_configured`) y añadir `youtube_title`/`youtube_description`/`tiktok_text` al esquema de la cola y al bridge.
- **Hosting**: renders del VPS → **Cloudflare R2** (URL pública); renders locales (nuestro caso) → **GitHub Release público** (tag `video-<slug>`, assets `<slug>.mp4` + `<slug>-cover.png`); el runbook dice *no* usar R2/Cloudflare en esa vía. `openframes` es **público** y sirve de hosting. Ojo: Cloudflare **Access** (auth de n8n) ≠ Cloudflare **R2** (almacenamiento).
- **Facebook vuelve a fallar (GA1, 2026-10-09)**: job en `partial_error`, Instagram `published` y Facebook `error`. Mismo patrón que V2 y que `lanzamiento-seo-cero-a-cien-enlaces`: es el token/permisos de la **Página** en n8n, no el vídeo. La ruta de lectura no expone el detalle (`facebook_error` vacío) ni el `instagram_media_id`. Arreglo: reautorizar la credencial de Facebook de la Página "Agencia Marketing Digital Espana" (1008229502375842) en el flujo `programacion de reels` (`x8etUYlUWqCCONxW`); desde el sandbox no se puede.
- **La Action de estado (`check-reel-status.yml`, 369319277) es de solo lectura** (`permissions: contents: read`): imprime el JSON del estado en su log (jobId, status, platform_status, instagram_status, facebook_status…) pero **no** escribe en la cola. El endpoint de logs exige `Accept: application/vnd.github+json`; con `vnd.github.raw` devuelve `InvalidAuthenticationInfo`.
- **YouTube y TikTok YA publican (2026-10-09, tras el arreglo en n8n)**: el webhook acepta Releases de openframes para esos destinos. Job nuevo `reel-ga4-01-instalar-sin-duplicar-tiktok-youtube-37988371777`: `pending` con `media_status: staging` y `source_video_url` conservada. Como el item de GA4-01 ya estaba `scheduled`, se creó una **entrada nueva en la cola con slug propio** (`ga4-01-instalar-sin-duplicar-tiktok-youtube`) y se lanzó la Action con `platforms: tiktok,youtube` (opción que añadí al workflow + allowlist del publicador). El detalle del estado expone ahora `media_status` y bloques `youtube`/`tiktok` con `upload_started` y `review_required`.
- **Posible desfase horaria en `publish_at`**: el job de YT/TikTok se aceptó hacia las 14:39 UTC pero quedó con `publish_at 20:38:56Z` (~6 h después). Revisar en n8n.
- **n8n es accesible DIRECTAMENTE desde el sandbox** (2026-10-09): `https://n8n.urltovideo.es/webhook/...` responde sin credenciales de Cloudflare Access, así que se puede consultar. El webhook de estado acepta **GET**: `?jobId=<job>` da el detalle (platform_status, cover_status, caption…) y cualquier otro valor en `job_id` da el **resumen global** (`total`, `counts`, `platformCounts`, `recent`). Para publicar, seguir usando la Action (salta el dedupe si se llama a mano).
- **Por qué YouTube/TikTok no publican (GA1, 2026-10-09)**: el webhook **sí** los admite. Responde HTTP 400 `"YouTube/TikTok require a direct URL on an approved media host."` con `created:0` (no crea job). GitHub Releases sirve por redirección y no está en la lista de hosts aprobados; para Instagram y Facebook sí vale. Haría falta un host directo aprobado (el de R2 que usa el VPS).
- **Facebook no es la ruta, es la fecha (2026-10-09)**: los 9 jobs de n8n (todos `cover_status: not_requested`, misma ruta sin portada) muestran que Facebook **funcionó hasta el 29-09-2026** (22, 28 y 29 de septiembre: published) y **falla desde el 30-09-2026** (30-09, 07-10, 08-10, 08-10, 09-10: error), 5 fallos seguidos con la misma ruta. Por tanto NO es `/video_reels` frente a `/videos` ni el vídeo: algo se rompió entre el 29 y el 30 de septiembre (lo más probable, caducidad del token de Página de Meta, que dura ~60 días, o cambio de permisos/rol). Instagram va 9/9. Para confirmar hay que leer el cuerpo del error de Meta en la ejecución fallida de n8n: `facebook_error` viene vacío, o sea que n8n no lo guarda — conviene loguear la respuesta de Meta para que los fallos se autodiagnostiquen.
- **Facebook falla de forma crónica**: resumen de n8n → 9 jobs: Instagram **9/9 published**, Facebook **3 published / 5 error**. Es el token/permisos de la Página en n8n, no los vídeos.
- **TikTok y YouTube (intento 2026-10-09, GA1)**: el lado GitHub ya los admite — añadí las opciones al `publish-reel.yml` (`instagram,facebook,tiktok,youtube`…) y la lista de plataformas de `scripts/schedule-instagram-reel.mjs` (mapea `tiktok`/`youtube`) — pero **n8n todavía los rechaza**: la reserva se completa y el envío falla en «Send reserved Reel to n8n». Publicar ahí exige tocar n8n. Si eso pasa, el item queda en `publishing` y hay que **reconciliarlo** (status `needs_review`, quitar `publish_attempt` y `outputs.reel_publish`, y el `status` del CSV) antes de reintentar.
- **La reserva exige**: el item en `queue.json` **y** en `video-queue.csv` (exactamente uno por slug), `status: needs_review`, `outputs.render` con URL HTTPS terminada en `.mp4`, `caption` no vacío, y sin `publish_attempt` ni `outputs.reel_publish`.
- **Cuentas**: FB Page «Agencia Marketing Digital Espana» (`1008229502375842`); IG `crecimientosc` (`17841435854263931`).
- **Ojo con el propio polling** de runs: quedarse con un run **nuevo** (comparar ids antes/después), no con `runs[0]`; si no, se lee el log del run anterior y se sacan conclusiones falsas.
- **V2 publicado** el 2026-10-08 (job `reel-seo-02-modificador-lujo-37786555312`, `ok:true, created:1`): **Instagram PUBLISHED**, **Facebook error** (`partial_error`, 403 de Meta; mismo patrón que `lanzamiento-seo-cero-a-cien-enlaces`). Se arregla en n8n (workflow `programacion de reels`, ID `x8etUYlUWqCCONxW`, permisos del token de la Página), **no** desde el sandbox.
- **Higiene del remote (resuelto 2026-10-08)**: el `origin` de `openframes` ya **no** lleva token embebido (se limpió con `git remote set-url origin https://github.com/specialcowboy69/openframes.git`). Para empujar, token en línea: `git push https://${GITHUB_TOKEN}@github.com/specialcowboy69/openframes.git HEAD:main`, y redactar la salida con `sed -E 's/(ghu_|ghp_|ghs_)[A-Za-z0-9_]+/<redacted>/g'`. Si `git push` se queda pidiendo contraseña, el remote ha vuelto a quedarse con un token viejo.

## Local music / BGM
- After `pip install transformers torch`, `facebook/musicgen-small` works locally (no auth).
- **Hard limit ~30 s per generation.** Longer → `IndexError: index out of range in self` (position embeddings). Generate a ≤28 s segment and loop it: `ffmpeg ... acrossfade=d=1.5` two copies, then `atrim` + `afade` to the target length.
- Speed on this 4-core box: ~6 s of compute per 1 s of audio (28 s took ~247 s).
- Duck under voice: `-filter_complex "[1:a]volume=0.22[m];[0:a]asplit=2[v][sc];[m][sc]sidechaincompress=threshold=0.03:ratio=8:attack=15:release=350[d];[v][d]amix=inputs=2:duration=first:normalize=0[out]"` — then `-c:v copy -c:a aac`.
- In a composition, an `<audio>` supports `data-volume` (linear 0–1) and needs an `id`. Prefer storing the bed at `assets/music/track.wav` and referencing it so Studio/preview renders include music.

## HyperFrames gotchas
- An `<audio>` with `data-start` **must have an `id`** or it renders SILENT (lint error `media_missing_id`).
- Caption components (`npx hyperframes add caption-pill-karaoke`) install as FULL standalone HTML docs under `compositions/components/`, sized 1920×1080. To mount one *inside* a composition: convert it to a `<template>` sub-composition (scope CSS with `[data-composition-id="..."]`, wrap its script in an IIFE so its `var tl` does not clash with the host's `const tl`, keep it registering its own `window.__timelines["<id>"]`), then mount with `data-composition-src`. `caption-pill-karaoke` needs per-word `{text,start,end}` (its `TRANSCRIPT`); approximate from line durations proportional to `len(word)+1`. There are 17 `caption-*` blocks + `per-word-rise`/`per-word-crossfade` in the registry, plus the 35-identity `embedded-captions` catalog (talking-head, needs matting) and per-preset `caption-skin.html`.
- `.clip` alone is not a full-frame box in a user project; a scene needs its own `position:absolute; inset:0`. The framework's shared `.clip` CSS is not guaranteed present in a hand-written file.
- Single-file composition with nested timed `<section>`s yields many warnings (`nested_structure_needs_subcomposition`, `timeline_track_too_dense`) — 15 with 11 scenes + progress + captions. Preferred architecture: scenes as sub-compositions in `compositions/*.html`, each wrapped in `<template>` with scoped CSS and `window.__timelines["<id>"]`, mounted in index via `data-composition-src` + `data-start`. Render works without this, but it is what lint wants.
- Seek-safe animation: set the initial state in CSS, animate with GSAP `.to()`. Avoid `.from()` and numeric count-ups.
- **El escenario nunca se anima con opacity** (lección de GA1, 2026-10-09): si la tarjeta o el marco de una escena nace en `opacity: 0` y se anima con `put()`, durante el primer ~0,5 s no hay nada claro en pantalla y **los cruces se quedan vacíos** (peor tramo 0,40 s frente a la barra de 0,15 s). Patrón bueno: el escenario nace **visible** (sin `.pop`) y solo se asienta con un helper `rise(sel, t)` que hace `fromTo(sel, {y:40}, {y:0})` **sin tocar la opacidad**; los hijos sí usan `put()`.
- **El verificador de montaje mide píxeles CLAROS** (luminancia > 25 sobre 255): agrandar tarjetas oscuras no sube el porcentaje. Los paneles deben superar el umbral (`.gcard`/`.code` a `#20202a`, no `--panel` #14141a) y conviene subir el tipo (`.txt` 56 px, `.chip` 44 px, `.step` 50 px, kicker 32 px). Su corte está en ~4 % de cobertura mínima por cruce.
- **Tras reconstruir las escenas hay que rehacer la cadena entera** (lección de GA1 v2, 2026-10-09): al reemplazar la región de escenas se pierden las **colas extendidas** que añade `transiciones.py` (`data-duration += d`); entonces la escena saliente desaparece justo al empezar el cruce y el lienzo queda **negro** (cobertura ~2 % y tramo vacío de 0,2-0,3 s). Orden obligatorio tras tocar escenas o timeline: `retime.py` → `transiciones.py` → `check` → render.
- **Qué mide el verificador de montaje**: por fila, la media de luminancia (muestreando 1 de cada 8 px) debe superar **25**; la cobertura es el % de filas que pasan y un fotograma cuenta como vacío si baja de ~4 %. El fondo (#0a0a0f) ronda 13; los paneles `#26262e` ~38; las filas del karaoke **no** pasan (píldora oscura con texto fino), así que el subtítulo no cuenta como contenido ni ayuda en los cruces.
- **`assets/music/` no lo crea `init`** → si falta, `retime.py` revienta al reconstruir la música (`ffmpeg ... track.wav.new.wav`, exit 254). `mkdir -p assets/music` antes de la cadena.
- **`events.json` es por proyecto**: si falta, `sfx.py` reutiliza los 34 eventos de V2 (anclajes equivocados). Formato `[{"scene":1,"local":0.0,"kind":"whoosh","gain":0.45}, …]`, generado a mano desde los `put()` del timeline.
- Always `window.__timelines = window.__timelines || {}` before assigning (the blank scaffold omits this and would throw).

## HyperFrames: doctrina de montaje (skills en disco)
- **Las skills están en disco, no son invocables**: `/home/openhands/.openhands/cache/plugins/hyperframes-6421da44161cdd87/skills/` (`faceless-explainer`, `hyperframes-animation` con `transitions/`, `rules/`, `blueprints/`, `hyperframes-creative`, `hyperframes-core`, `media-use`...). Leerlas con `cat`/`sed` en vez de `invoke_skill`.
- **Regla de oro de montaje:** *toda* composición multi-escena lleva **transiciones**; sin ellas las escenas se sienten como cortes secos. Y **la transición ES la salida**: prohibido animar elementos hacia fuera salvo en el último frame (la única excepción).
- **Registro de transiciones Tier-B** (sin DOM extra): `crossfade`, `blur-crossfade` (default calm), `push-slide` (LEFT/RIGHT/UP/DOWN), `zoom-through` (default high), `squeeze`; `cut`/`none` para saltar. Máx 2 s. Elegir **una primaria (60-70 %)** + 1-2 acentos; la apertura la más distintiva, el clímax la más audaz, el outro la más simple.
- **Mecánica**: `transitions.mjs inject` **extiende la cola** del frame saliente (`#el-<id>`, `data-duration`) y anima ambos wrappers a la vez en T. Los `<audio>` **no se tocan** → las transiciones **no crean silencios** (compatible con la regla del usuario).
- **Doctrina de movimiento (Parte 2, "load-bearing"):**
  - **Smooth beats bouncy: `power3` es el default.** Nada de `back.out`/`bounce.out`/`elastic.out` como entrada por defecto — es "*el turn-off nº1*" de vídeos hechos por agentes. **OJO: nuestro `pop` usaba `back.out(2)` → hay que cambiarlo.**
  - **Revelado secuencial en el ~50 % final, sincronizado con la VO.** No volcar todo en el primer 25 %: ese es *el* fallo "PowerPoint/slideshow".
  - **Nada de "breathing" ni pans/zooms lentos en la segunda mitad** ("antes nada de movimiento que mal movimiento"). La única vivacidad permitida es **subtle jitter** de baja amplitud (`sine-wave-loop`) o SVG interno vivo.
  - **Entradas con `fromTo`** (estado inicial explícito); no fiarse de un CSS oculto. Nada de CSS `transition`/`@keyframes` ni `repeat`/`yoyo`.
  - Cortes internos (dentro de un frame) = **velocity-matched** (`cut-catalog.md`): zoom-through / inverse, cut-the-curve, waterfall cut.
- **Fuente autoritativa de timings = `index.html`** (`data-start` / `data-duration` de cada escena + `data-duration` raíz). `SCRIPT.md` y `STORYBOARD.md` pueden estar desfasados: el SCRIPT de V2 sumaba 40,0 s cuando el render real es **34,47 s**. Verificar siempre contra la composición antes de dar timings por buenos.

## Montaje: cómo se implementa y cómo se verifica sin ojos (V2 v7)
- **Receta en `index.html`**: (1) cada escena envuelve su contenido en `<div class="s-in" id="sN-in">`
  y `.scene` queda solo como caja (`position:absolute; inset:0; overflow:hidden`); (2) la cola del
  saliente se extiende `data-duration += dur. de la transición`; (3) un array `TR` emite los dos
  tweens en `T = S[n]`. Los `<audio>` **nunca** se tocan → cero silencios.
- **Sincronía con la voz**: los tiempos por palabra están en el `TRANSCRIPT` de
  `compositions/components/caption-pill-karaoke.html` (lista plana `{text,start,end}` con tiempos
  **absolutos**). Es la fuente de verdad para decidir cuándo revelar cada elemento.
- **Verificación sin ojos (patrón reutilizable)**, todo con ffmpeg + Python, sin ver imágenes:
  - **Cobertura del lienzo** por fotograma (fracción de filas por encima de `media+6`). Señal clave:
    si en mitad de un cruce cae a ~3 %, **la escena entrante llega vacía**. Tras meter el escenario
    en t=0 subió a ~11 %.
  - **Perfil de bandas por filas** para ver que el contenido se desplaza en un push (a las 4,40 s
    el contenido de F1 ya había subido 343 px).
  - **Envolvente RMS** (ventanas de 0,05 s) para confirmar **0 huecos de silencio**.
- **Trampas del diagnóstico**:
  - Comparar regiones equivocadas en un push (la mitad visible del saliente es la **contraria**).
  - Muestrear píxeles sueltos: con fondo tan oscuro domina el negro y todo "parece igual". Usar
    medias por fila o cobertura, no diferencias de píxeles.
  - **Los renders NO son deterministas**: dos renders idénticos difieren ya ~0,003 de media en la
    envolvente; y un **ffmpeg distinto** (el sandbox se reconstruye) desplaza la ganancia global
    ~4 %. No concluir "el audio cambió" por eso: comprobar `git status` sobre los assets de audio.
- **`data-layout-allow-overflow`**: no usarlo para callar los avisos `info` de layout de las
  transiciones (el atributo es heredado y silencia también los chequeos de texto de la escena).
- Después de un reset del sandbox: `sudo apt-get install -y ffmpeg unzip` y
  `npx hyperframes browser ensure` (sin `unzip` falla la descarga del chrome-headless-shell).
  `animation-map.mjs` de la skill se cuelga (intenta lanzar navegador): no contar con él.
- **Mojibake**: escribir ficheros con heredoc puede doble-codificar acentos (`â€”`, `Ă±`, `did÷ctico`).
  Reparación por línea probando codecs `latin-1`/`cp1252`/`iso-8859-2`/`cp1250` y aceptando solo el
  candidato que devuelve UTF-8 válido *y* reduce las firmas. Comprobar con `grep -c "Ã"`.

## Guiones V1/V2 — reescritura de claridad (2026-10-07)
- Motivo: el usuario los encontró "crípticos y poco claros". Fallos: jerga usada antes de definirla (contra D03/IDEAS), sujetos/verbos elididos, conclusiones sin premisa ("Exacto.", non-sequitur "Y no es tu contenido"), líneas de 15 palabras.
- **V1: DESCARTADO.** Ya está publicado (release `video-seo-01-copiar-titulo`), así que su `SCRIPT.md` se **revirtió** al estado publicado. La versión mejorada de V1 (y su contradicción interna L8/L9 resuelta como "libertad de orden") queda en el transcript de la conversación por si algún día se re-renderiza.
- **V2: guion reescrito en `SCRIPT.md`.** Decisiones aprobadas con el cliente:
  - Hook anclado a "URL" ("El mismo modificador de la URL suma o resta…"), porque el espectador puede no haber visto V1.
  - L6 corregido: "no lo deberías usar nunca". L7 abre con **"En el lujo,"**, sustituyendo la etiqueta suelta "Lujo:" que era la yuxtaposición denunciada. "lujo" aparece UNA sola vez.
  - "zapatillas barato" → **"zapatillas baratas"** (petición del cliente). Coste: se pierde el matiz "URL sin concordancia".
  - "e-commerce" → **"comercio electrónico"** en la voz. Sin "Y" inicial; sin verbo comodín "va" (aparecía ×3).
  - 10 líneas, timings reales (34,47 s) intactos, 98 palabras (~2,8 pal./s).
- **PENDIENTE (montaje; NO hecho, requiere aprobación).** En `videos/seo-02-modificador-lujo/index.html`: kicker F2 `E-COMMERCE`→`COMERCIO ELECTRÓNICO`; `-barato`→`-baratas` en F2/F3/F4; F6 `donde no lo uses nunca.`→`donde no lo deberías usar nunca.`; (opcional) kicker F9 `LA MISMA PALABRA`→`EL MISMO MODIFICADOR`. NO tocar el `barato` de F1/F5/F7 (la voz usa "barato" en L7).
- **PENDIENTE (assets):** regenerar `assets/voice/01..10.txt/.wav` + el `TRANSCRIPT` del karaoke con las líneas nuevas y re-medir (actualizar el `data-duration` de los `<audio>`).
- Método: red de subagentes (3 auditores → 2 guionistas → 2 verificadores).
- **Voz oficial: `Pablo`** (Fish Audio, es-ES, brisk; `reference_id` `1bd666ea8ada44c789e0fec21cf78f33`, documentada en
  `WORKFLOW.md` §4). **No usar el clon de la voz del dueño**: lo retiró el 2026-10-11 y va a
  actualizarlo. Ritmo medido de Pablo: **3,98 palabras/s** (muestra de 3 líneas) → el guion de 188
  palabras queda en ~47 s.

## V5 «Intención de búsqueda» — publicación (2026-10-11)
- MP4 en la Release pública de openframes: tag `video-seo-05-intencion-de-busqueda`, asset
  `seo-05-intencion-de-busqueda.mp4`, sha256 `3e8e599c9db16284…`. La Release es el alojamiento
  público de las piezas renderizadas en local (**no** R2 ni el panel de Cloudflare).
- Cola de hypervideo: entrada `seo-05-intencion-de-busqueda` en `queue.json` **y** en
  `video-queue.csv`. El `reserve` de la Action manual exige: estado `needs_review` sin intento
  previo, exactamente una fila por slug en ambos ficheros, URL pública de MP4 en `outputs.render`,
  y `confirmation: PUBLICAR <slug>`. El CSV se lee/escribe por columnas (`slug`, `status`, …): la
  fila debe existir antes de lanzar la acción.
- Run `38146591990` (success, actor specialcowboy69) → job de n8n
  `reel-seo-05-intencion-de-busqueda-38146591990` aceptado con instagram, facebook, tiktok y
  youtube, y sin portada (`cover_status: not_requested` en las cuatro). Publicado con `publish_at:
  now`.
- **Pendiente:** confirmar el resultado por canal (se esperan Instagram/YouTube/TikTok correctos;
  Facebook sigue dependiendo del token de la Página, roto desde el 30-09-2026).

## Lecciones de HyperFrames de esta tanda (V5)
- **Transiciones con `xPercent`:** si el CSS del elemento arranca con `transform: translateX(…)`,
  GSAP lo interpreta como `x` y `xPercent` pasa a ser **aditivo** → el barrido acaba en
  `translateX(0)` y **cubre el cuadro entero** (medido: 72-86 % de verde). Solución: `x: 0`
  explícito en el `fromTo`. Un barrido debe ser una banda (40 % de alto, sesgada), nunca `inset: 0`.
- **Primer fotograma = miniatura del reel.** Publicamos sin portada, así que el fotograma 0 es la
  miniatura en Instagram, TikTok y YouTube. Medirlo antes de dar por buena una escena: el gancho
  anterior tenía 18,7/255 de luminancia y 33 % de filas con contenido (cuadro negro); el nuevo está
  en 230/100 %.
- **El webhook de estado de n8n puede no responder mientras procesa un trabajo** (timeouts de
  90-200 s sin cuerpo, y también en la raíz del dominio). No significa que la cola haya fallado:
  reintentar más tarde o leer el estado con la Action «check Reel status».
- Servir material de revisión (audio, MP4, fotogramas) con `python3 -m http.server <p> --bind
  0.0.0.0 --directory <dir>` funciona por los hosts de trabajo, y es la forma más rápida de que el
  dueño lo vea: no se puede reproducir audio ni vídeo desde el propio chat.

## n8n caído: el VPS vive, el hostname no (2026-10-11)
- Síntoma: `https://n8n.urltovideo.es/` no responde (HTTP 000 / timeout) **también desde un runner
  de GitHub**, no solo desde el sandbox. Pero `https://72.61.161.99/` (la IP del VPS, `-k`) contesta
  **HTTP 404 en 0,3 s**: el servidor está levantado.
- Lectura: el problema es el **túnel/proxy de Cloudflare de ese hostname** (n8n va detrás de
  Cloudflare Access), no la instancia ni el VPS. Revisar cloudflared / el DNS-proxy de
  `n8n.urltovideo.es`.
- Consecuencia práctica: cualquier llamada a n8n (webhooks de publicación o de estado) se queda
  sin respuesta mientras dure. **No es que la cola haya fallado**: el trabajo puede seguir aceptado.
- Estado de V5 al cortar: run `38146591990` success, job de n8n
  `reel-seo-05-intencion-de-busqueda-38146591990` aceptado con instagram, facebook, tiktok y youtube
  y sin portada; `pending` / `media_status: staging`. **Sin confirmar el resultado por canal.** La
  Action «check Reel status» (input `job_id`) sí funciona para leerlo… cuando n8n vuelva.
- Recordatorio del runbook: no volver a lanzar la publicación del mismo slug (`reserve` la rechaza
  porque ya está en `scheduled`); si el trabajo se perdió, reconciliar con una entrada nueva.

## V6 «Canibalización de palabras clave» — construido (2026-10-11)
- Guion dictado por el dueño en dos rondas: 11 líneas · 142 palabras. La línea 7 va a 18 palabras por
  texto expreso del dueño y no se parte. Voz Pablo: 40,27 s reales (más lenta que la estimación de
  3,98 pal./s, que daba 35,7 s). Decisión D38: 0,27 s por encima del techo de 40 s de la banda.
- Proyecto en videos/seo-06-canibalizacion/: index.html con 11 escenas (s1-s11) y la timeline en
  window.__timelines["main"] — la clave es "main", no el id del proyecto: lo exigen retime.py y el
  lint. Karaoke como subcomposición; assets/sfx/events.json + sfx.wav; renders/video.mp4 + 11 frames.
- Cadena: voice_pipeline.py (--dir/--ref/--timing) -> index.html -> sfx.py -> retime.py ->
  transiciones.py -> check -> render -> verificar_montaje.py. Todas aceptan --dir.
- Para renderizar hacen falta: unzip instalado (si no: "no zip archiver is available" al descargar su
  Chrome headless) y npx hyperframes@0.8.138 browser ensure una vez.
- Ojo con voice_pipeline.py --min-frame 3.0: rellena los clips cortos y rompe "escena = clip" (dejó
  0,40 s sin voz tras la línea 8). Igualar scene al clip real en timing.json y rehacer la cadena.
- Verificación adversarial del vídeo: 0 graves / 3 medios / 7 leves; los medios corregidos
  (escena=clip, dato real de duración, fotograma plano del cover) y 6 leves cosméticos anotados.
- Red de subagentes con contextos separados (fuentes, continuidad, contrato, guion, plan visual,
  sincronización y dos verificaciones) más pases de corrección. Funciona, pero el subagente
  web-researcher NO tiene acceso a disco: sus informes hay que guardarlos a mano.

## Lección de entorno (2026-10-11): el sandbox se puede reconstruir A MITAD de sesión
- No solo entre sesiones: en esta tanda se reconstruyó con la sesión abierta y se llevó /tmp y los
  paquetes instalados (ffmpeg, unzip). Síntomas: el servidor de revisión devuelve 502 y ffmpeg
  desaparece. Reinstalar: sudo apt-get update && sudo apt-get install -y ffmpeg unzip.
- Por eso el material de revisión ya no vive en /tmp: la página con el vídeo y los fotogramas está en
  /workspace/v6preview (persistente y fuera del repositorio), servida con
  python3 -m http.server 12000 --bind 0.0.0.0 --directory /workspace/v6preview.
- El http.server de Python no soporta peticiones por rangos: el MP4 se descarga entero de una vez
  (6,5 MB), así que hay que darle tiempo y no fiarse de un curl que corte por timeout.
