# DECISIONS — registro de decisiones

Una fila por decisión: qué se decidió, por qué, y qué alternativas se descartaron.
Se añade al final; lo más reciente abajo. Fecha en formato AAAA-MM-DD.

| # | Fecha | Decisión | Motivo | Alternativas descartadas |
|---|-------|----------|--------|--------------------------|
| D01 | 2026-10-06 | Rutar como **faceless-explainer** | No hay cámara ni web que capturar; los visuales se inventan | talking-head-recut (no hay footage), product-launch-video (no hay web) |
| D02 | 2026-10-06 | **Dividir** el resumen original en 2 vídeos: V1 (autoridad) y V2 (colocación del modificador + lujo) | 4 escenarios no caben en 30-40 s | Un solo vídeo largo |
| D03 | 2026-10-06 | Reescribir V1 una 3ª vez para **definir la jerga en pantalla** ("autoridad", "modificador") | El espectador se perdía: se usaba jerga sin explicarla | Dar por sabidos los términos |
| D04 | 2026-10-06 | Aceptar **~42 s** en V1 (40,8 s de voz) | El contenido no cabía en 30-40 sin recortar ideas | Recortar el ejemplo A/B para bajar a 30-35 s |
| D05 | 2026-10-06 | Pasar de 7 a **11 frames de 3-5 s** | Más cortes = más dinamismo y retención | Dejar 7 frames (cuatro de 6-8 s, más estáticos) |
| D06 | 2026-10-06 | Subtítulos **karaoke** (`caption-pill-karaoke`) | Complementa el texto cinético sin duplicar en exceso; accesible en mudo | Verbatim completo (se solapaba con el texto grande), solo palabras clave |
| D07 | 2026-10-06 | Timings de karaoke **aproximados** (proporcionales a la duración de cada línea) | Suficiente con el ritmo regular de Kokoro; sin dependencias extra | Transcribir con whisper/parakeet |
| D08 | 2026-10-06 | Colocar la píldora **sobre y≈1230-1450** y mover la barra de progreso arriba | Evitar la zona que tapa la interfaz de TikTok/Reels | Píldora pegada al borde inferior (quedaría tapada) |
| D09 | 2026-10-06 | Música **local offline** (MusicGen) a volumen 0.18 bajo la voz | Gratis, sin licencias, sin depender de terceros | HeyGen (requiere sesión), pistas de librería (licencias) |
| D10 | 2026-10-06 | **No** refactorizar a sub-composiciones | El vídeo ya funciona; el refactor no aporta valor visible | Refactor (mejora Studio/lint, pero coste sin beneficio pedido) |
| D11 | 2026-10-06 | **Quitar** el `@handle` del frame final | Petición directa | Dejar un texto de marca alternativo |
| D12 | 2026-10-06 | Guardar todo en un repo propio, **privado**, `openframes` | Persistencia y continuidad entre sesiones; no mezclar con el repo de HeyGen | Usar el clon de `heygen-com/hyperframes`, o no versionar |
| D13 | 2026-10-06 | `content/` como **repo git independiente** (anidado en el clon de HyperFrames) | Versionar el contenido sin tocar el repo ajeno | Repo fuera del workspace (más frágil), commitear en el repo de HeyGen |
| D14 | 2026-10-06 | Identidad de commits: `openhands <openhands@all-hands.dev>` | Consistencia y trazabilidad del agente | Usar tu nombre/email de GitHub |
| D15 | 2026-10-06 | Documentar **perfil, decisiones y proceso** en este repo | No repetir explicaciones en cada sesión futura | Confiar solo en el contexto de la conversación |

## Notas operativas aprendidas (no son decisiones de contenido)

- El token del entorno es de la App **`openhands-ai`** y **solo escribe donde la App
  está instalada**. Hubo que instalar la App en `openframes` para poder hacer push.
- Esa App **no tiene permiso de administración**: no puede crear repos ni cambiar su
  visibilidad (para eso hace falta un PAT).
- El preview del Studio debe escuchar en `0.0.0.0`
  (`HYPERFRAMES_PREVIEW_HOST=0.0.0.0`) o el proxy externo devuelve **502**.
