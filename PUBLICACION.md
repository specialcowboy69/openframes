# Publicación: copy, plataformas y reglas

Reglas vigentes para publicar los vídeos de la serie. Última revisión: 2026-10-19.

> **La fuente de verdad del estado es n8n, no la cola.** El campo `status` de
> `content/video-queue/queue.json` dice `scheduled` desde que se **encola** el trabajo, y no se
> actualiza solo cuando sale. Para saber si un vídeo está publicado de verdad hay que consultar la
> Action de estado con el `jobId`. Así se comprobó, por ejemplo, que MK2 sí había salido en los
> cuatro canales cuando la cola aún decía otra cosa.

## El copy (leyenda)

- Texto **breve y relacionado con el vídeo**: el gancho y el dato útil, sin relleno.
- **2 o 3 hashtags como máximo, y nada más.**
- **Nada de avisos de autoría** ("hecho con IA", "OpenHands", "producido por un agente de IA"): no va
  en la leyenda, ni en el vídeo, ni en los rótulos. V1 y V2 lo llevan porque se publicaron antes de
  esta regla; no se repite.
- El CTA de la serie es **"Guarda esto"**.
- La leyenda **se genera a partir del `SCRIPT.md`** del vídeo (mismo tema, misma promesa, mismo CTA).
- **Nunca se teclea a mano al lanzar la publicación**: se lee del campo `caption` de la entrada del
  vídeo en la cola y se pasa tal cual. Teclear los inputs a mano ya provocó un incidente (se publicó
  un `PLACEHOLDER` como leyenda).

Plantilla:

    <1-2 frases con el gancho del vídeo>
    <1 frase con el dato útil>
    Guarda esto.
    #hashtag1 #hashtag2 #hashtag3

## Plataformas

| Plataforma | Portada | Ruta | Estado |
|---|---|---|---|
| Instagram | **no** | `/video_reels` (sin portada) | activo |
| Facebook | **no** | `/video_reels` (sin portada) | activo |
| TikTok | no | — | **activo desde 2026-10-14** |
| YouTube | no | — | **activo desde 2026-10-14** |

- **Las cuatro plataformas se publican por este flujo.** La nota antigua de "YouTube y TikTok ya se
  publicaron fuera de este flujo, no reintentar" quedó obsoleta: MK2 (14/10/2026) salió en los
  cuatro canales con `platforms: instagram,facebook,tiktok,youtube`.
- Instagram y Facebook se suben **sin portada** (`include_cover=false`), que es lo que enruta a
  `/video_reels`. TikTok y YouTube no usan portada.
- La ruta `/videos` (con portada) exigiría que la portada estuviera en un host de medios aprobado
  (`media.urltovideo.es` o el R2 autorizado): n8n rechaza las URLs de GitHub Releases con
  `400 cover_url must use an approved HTTPS media host...`.
- El `video_url` sí puede ser un asset de GitHub Releases: está aceptado.

### Dos formas de publicar en las cuatro

1. **Una sola entrada con las cuatro plataformas** (`platforms: instagram,facebook,tiktok,youtube`).
   Es lo que se usa desde `seo-05-intencion-de-busqueda` en adelante.
2. **Dos entradas para el mismo vídeo**: una `instagram,facebook` y otra `tiktok,youtube` con el slug
   acabado en `-tiktok-youtube`. Se usó una vez (`ga4-01-instalar-sin-duplicar`), por si hay que
   reintentar solo una pareja de plataformas sin tocar la otra.

## Cómo se lanza

1. Entrada del vídeo en la cola de `hypervideo` con `status: needs_review`, `outputs.render` (MP4
   público), `outputs.cover` y `caption`.
2. Action **`HyperFrames publish Reel (manual)`** (`publish-reel.yml`) con `slug`, `caption` (leída
   de la cola), `publish_at`, `platforms` y `confirmation: PUBLICAR <slug>`.
   - La Action **reserva** el job en `main` antes de llamar a n8n (dedupe).
   - El actor del run debe ser el dueño del repo; el token del entorno es `specialcowboy69`, así que
     pasa la validación.
3. Respuesta esperada del webhook: `ok: true`, `created: 1` y el `jobId` dentro de `jobs`. Eso
   confirma que está **encolado**, no publicado.
4. **La hora se pasa en la Action** (`publish_at`), no se guarda en la cola: el campo de la cola
   aparece a `null` incluso en vídeos ya publicados. La convención de la serie es las **17:30 de
   Madrid**.
5. Estado: Action **`HyperFrames check Reel status (manual)`** (`check-reel-status.yml`), solo
   lectura, pasando el `jobId`.

## Estado de las publicaciones

| Vídeo | Slug en la cola | jobId | Estado |
|---|---|---|---|
| V6 | `seo-06-canibalizacion` | `reel-seo-06-canibalizacion-38254098140` | consultar con la Action |
| MK1 | `mkt-01-responde-con-video` | `reel-mkt-01-responde-con-video-38412545962` | consultar con la Action |
| **MK2** | `mkt-02-google-ads-trafico-correcto` | `reel-mkt-02-google-ads-trafico-correcto-38581643205` | **`published` en los 4 canales (14/10/2026, 17:30 Madrid)** |
| MK3 | — (sin entrada todavía) | — | **pendiente de publicar** |

- La cola marca `scheduled` los tres primeros, pero eso solo refleja el encolado. **MK2 está
  confirmado como publicado**; V6 y MK1 hay que confirmarlos con la Action de estado.
- **MK3** (`videos/mkt-03-anuncios-de-ataque`) está renderizado y verificado, pero **no tiene entrada
  en la cola**: hay que crearla con su `caption` antes de lanzar nada.

## Si el paso del webhook falla después de reservar

La reserva ya está escrita en `main` y el item queda en `publishing`. **No relanzar a ciegas**:
comprobar antes con la Action de estado.

- Si el job no existe en n8n (`status: not_found`), la reserva se reconcilia (item a `needs_review`,
  borrar `publish_attempt`) y se puede reintentar.
- Si el job existe, **no** se reenvía: se espera o se arregla en n8n.

## Credenciales

El webhook está detrás de Cloudflare Access. `CF_ACCESS_CLIENT_ID` / `CF_ACCESS_CLIENT_SECRET`
viven como secrets del repo `hypervideo`; el agente no los tiene, por eso **nunca llama al webhook
directamente**: siempre a través de la Action.

## Medios y nomenclatura

- Formato: **1080×1920, 30 fps, H.264 + AAC**.
- Vídeo local: **Release público de GitHub** en `specialcowboy69/openframes`, tag `video-<slug>`,
  assets `<slug>.mp4` y `<slug>-cover.png`. **No usar R2** para esta ruta.
- Vídeo renderizado en la VPS: **R2** o `media.urltovideo.es` (hosts aprobados para portada).
- Los renders pesados no se guardan en el repositorio; el MP4 final de cada pieza sí (es lo que
  consume la publicación).

## Histórico de lo que se aprendió

- **2026-10-09**: los inputs de la Action se tecleaban a mano y se publicó un `PLACEHOLDER` como
  leyenda. Desde entonces el `caption` se lee siempre de la cola.
- **2026-10-14**: MK2 se publicó en los cuatro canales. La cola se quedó en `scheduled`; se
  corrigió a mano y de ahí la regla de arriba: **la cola no es la verdad final**.
- **2026-10-19**: se documenta por primera vez el estado real de las publicaciones y se retira la
  nota de "YouTube y TikTok no reintentar", ya que ambos funcionan por este flujo.
