# Publicación: copy, plataformas y reglas

Reglas vigentes para publicar los vídeos de la serie. Última revisión: 2026-10-08.

## El copy (leyenda)

- Texto **breve y relacionado con el vídeo**: el gancho y el dato útil, sin relleno.
- **2 o 3 hashtags como máximo, y nada más.**
- **Nada de avisos de autoría** ("hecho con IA", "OpenHands", "producido por un agente de IA"): no va en la leyenda, ni en el vídeo, ni en los rótulos. V1 y V2 lo llevan porque se publicaron antes de esta regla; no se repite.
- El CTA de la serie es **"Guarda esto"**.
- La leyenda **se genera a partir del `SCRIPT.md` del vídeo** (mismo tema, misma promesa, mismo CTA).
- **Nunca se teclea a mano al lanzar la publicación**: se lee del campo `caption` de la entrada del vídeo en la cola de `specialcowboy69/hypervideo` y se pasa tal cual. Teclear los inputs a mano ya provocó un incidente (se publicó un `PLACEHOLDER` como leyenda).

Plantilla:

    <1-2 frases con el gancho del vídeo>
    <1 frase con el dato útil>
    Guarda esto.
    #hashtag1 #hashtag2 #hashtag3

Ejemplo (V3, "Qué es la autoridad"):

    Tu web no sube por el contenido: sube por la autoridad, y la autoridad son los enlaces que otras webs te dan. Compruébala en Search Console → Enlaces.
    Guarda esto antes de escribir el próximo artículo.
    #SEO #MarketingDigital #PosicionamientoWeb

## Plataformas

| Plataforma | Portada | Ruta | Estado |
|---|---|---|---|
| Instagram | **no** | `/video_reels` (sin portada) | activo |
| Facebook | **no** | `/video_reels` (sin portada) | activo |
| YouTube | — | — | ya publicado fuera de este flujo: **no reintentar** |
| TikTok | — | — | ya publicado fuera de este flujo: **no reintentar** |

- Instagram y Facebook se suben **siempre sin portada** (`include_cover=false`), que es lo que enruta a `/video_reels`.
- La ruta `/videos` (con portada) exigiría que la portada estuviera en un host de medios aprobado (`media.urltovideo.es` o el R2 autorizado): n8n rechaza las URLs de GitHub Releases con `400 cover_url must use an approved HTTPS media host without credentials, query, port or fragment`.
- El `video_url` sí puede ser un asset de GitHub Releases: está aceptado para Instagram y Facebook.
- **YouTube y TikTok no se reintentan.**

## Cómo se lanza

1. Entrada del vídeo en la cola de `hypervideo` con `status: needs_review`, `outputs.render` (MP4 público), `outputs.cover` y `caption`.
2. Action `HyperFrames publish Reel (manual)` (`publish-reel.yml`) con `slug`, `caption` (leída de la cola), `publish_at`, `platforms: instagram,facebook`, `include_cover: false` y `confirmation: PUBLICAR <slug>`.
   - La Action **reserva** el job en `main` antes de llamar a n8n (dedupe).
   - El actor del run debe ser el dueño del repo; el token del entorno es `specialcowboy69`, así que pasa la validación.
3. Respuesta esperada del webhook: `ok: true`, `created: 1` y el `jobId` dentro de `jobs`. Eso confirma que está **encolado**, no publicado.
4. Estado: Action `HyperFrames check Reel status (manual)` (`check-reel-status.yml`), solo lectura, pasando el `jobId`.

## Si el paso del webhook falla después de reservar

La reserva ya está escrita en `main` y el item queda en `publishing`. **No relanzar a ciegas**: comprobar antes con la Action de estado.

- Si el job no existe en n8n (`status: not_found`), la reserva se reconcilia (item a `needs_review`, borrar `publish_attempt`) y se puede reintentar.
- Si el job existe, **no** se reenvía: se espera o se arregla en n8n.

## Credenciales

El webhook está detrás de Cloudflare Access. `CF_ACCESS_CLIENT_ID` / `CF_ACCESS_CLIENT_SECRET` viven como secrets del repo `hypervideo`; el agente no los tiene, por eso **nunca llama al webhook directamente**: siempre a través de la Action.

## Pendiente del lado de n8n (solo si algún día se quiere publicar desde GitHub a YouTube/TikTok)

1. Permitir los hosts `github.com`, `release-assets.githubusercontent.com` y `objects.githubusercontent.com` en el allowlist de hosts de medios, y aplicar la validación a la URL enviada, no a la del redirect (los assets de Release devuelven 302 a una URL firmada con query).
2. Seguir el redirect al descargar y aceptar `application/octet-stream`; al subir a YouTube/TikTok forzar `Content-Type: video/mp4` y nombre `<slug>.mp4`.
3. No cachear la URL firmada del redirect (caduca en ~1 h).
4. Activar los workers de YouTube/TikTok (hoy `503 platform_not_configured`) y aceptar `youtube`/`tiktok` en `platforms` más los campos `youtube_title`, `youtube_description`, `tiktok_text`.
