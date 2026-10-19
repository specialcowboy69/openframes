# Estado actual y traspaso

Documento de entrada para cualquier agente que empiece a trabajar en este proyecto.
Última actualización: 2026-10-19. Los detalles de fondo están en `AGENTS.md`,
`WORKFLOW.md`, `PUBLICACION.md`, `DESIGN.md`, `DECISIONS.md` y `.openhands/memory/MEMORY.md`.

## Qué es esto

Producción de vídeos verticales (1080×1920, 30 fps, H.264 + AAC) para redes: serie SEO y línea
«Casos de estudio marketing». Faceless, voz en off en español (Fish Audio, voz `Pablo`), subtítulos
karaoke, música y efectos. Herramienta: HyperFrames (HTML → vídeo). Repositorio público:
`specialcowboy69/openframes`.

**Regla dura:** nada de avisos de autoría («hecho con IA», «OpenHands») en leyendas, vídeos ni
rótulos. Sin consentimiento expreso del dueño, no se añaden.

## Estado de las piezas

| Pieza | Estado |
|---|---|
| V1, V2, V3, V5, GA1 | publicadas |
| V6, MK1 | enviadas a publicar el 13/10; estado real por confirmar con la Action |
| MK2 | **publicada en los cuatro canales** el 14/10 a las 17:30 (Madrid) |
| MK3 | **terminada y verificada**; Release publicada; **falta la entrada en la cola y el lanzamiento** |

## Infraestructura (importante, cambió en octubre)

- **OpenHands ya no se usa en el cloud.** Corre **autohospedado en la VPS** (`srv1430096`,
  7,8 GB de RAM, 2 núcleos, 34 GB libres, 4 GB de swap) con `openhands serve`, accesible por túnel
  SSH al puerto 3000. Plan completo en `docs/despliegue-openhands-vps.md`.
- **El modelo es `deepseek-flash`** (V4.1, visión nativa) por API. El modelo «superior»,
  `deepseek-v4-pro`, **no soporta imágenes**. Para mirar fotogramas, siempre `deepseek-flash`.
- **El agente VE imágenes**: adjuntos en la conversación funcionan en la instalación local. Se usó
  para revisar fotogramas. Este era el motivo de todo el cambio de infraestructura.
- **Secretos**: `DEEPSEEK_API_KEY` y `GITHUB_TOKEN` viven como secretos de la interfaz, se cargan
  **al empezar la conversación** (una conversación abierta antes no los ve). El `GITHUB_TOKEN` es un
  PAT fine-grained con `Contents` y `Actions` de escritura sobre `openframes` y `hypervideo`.
  **Nunca** se imprime ni se escribe en el repo.
- **Los renders pesados** siguen en el renderer de n8n de la VPS (webhook
  `hyperframes-build-render`). No se renderiza en el contenedor del agente.
- **Worktrees**: no hay soporte nativo, pero valen `git worktree add ../wt-<pieza> -b <pieza>`.
  Para que el agente los vea, `openhands serve --mount-cwd` debe lanzarse desde el **directorio
  padre** de los worktrees.

## Pendiente, por orden

1. **MK3**: crear la entrada en la cola de `hypervideo` (`status: needs_review`) con su `caption`,
   la URL del MP4 de la Release y el CSV generado con `stringifyCsv`. Después, lanzar la Action.
2. **Confirmar V6 y MK1** con la Action de estado (`check-reel-status.yml`) y su `jobId`; la cola
   los marca `scheduled`, que solo significa «encolado».
3. **Sincronizar la cola**: el `status` de `queue.json` no se actualiza solo al publicar. Habría que
   hacer que la Action escriba el resultado al terminar. Vive en `hypervideo`.
4. **MK3.5**: siguiente pieza de la línea de marketing, sin empezar.

## Trampas conocidas

- **La cola no es la verdad.** `scheduled` = encolado. El estado real se lee con la Action.
- **`publish_at` no está en la cola**: se pasa en la Action. Convención: 17:30 Madrid.
- **El CSV de la cola usa LF**: generarlo con `stringifyCsv` (node). Con el módulo `csv` de Python
  sale CRLF y ensucia el diff.
- **Nunca se llama al webhook a mano**: siempre por la Action, que tiene las credenciales de
  Cloudflare Access y hace la reserva anti-duplicados.
- **`.openhands/` está en `.gitignore`**: sus ficheros ya están versionados, pero cualquier añadido
  nuevo requiere `git add -f`, y hay que elegir qué se sube (nada de secretos).
- **Un render a la vez**: 2 núcleos. Dos renders simultáneos se estrangulan.
- **Las herramientas de la casa** están en `.openhands/tools/`: `medir_sync.py`,
  `verificar_montaje.py`, `sfx.py`, `retime.py`, `transiciones.py`, `publicar_reel.py`,
  `voice_pipeline.py`, `diag_one.py`, `voice-timing.json`, `music_bed.wav`.

## Cómo arrancar una conversación nueva

> Estás en el repositorio de producción de vídeos. Lee `AGENTS.md`, `docs/estado-actual.md`,
> `PUBLICACION.md`, `WORKFLOW.md` y `.openhands/memory/MEMORY.md`. Después dime en cinco líneas:
> qué es el proyecto, las reglas duras, el estado de las piezas y lo que está pendiente.
