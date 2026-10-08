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
| D16 | 2026-10-07 | **V1 no se toca**: se descarta su reescritura porque ya está publicado | Evitar dejar el `SCRIPT.md` de un vídeo publicado desalineado con el render | Reescribir V1 y volver a montarlo |
| D17 | 2026-10-07 | **V2 reescrito por claridad**: hook anclado a "URL", conectores explícitos en el giro (L6→L7), "no lo deberías usar nunca", "zapatillas baratas" | El guion era críptico: jerga sin definir, sujetos elididos y un salto de referente entre "un caso" y "Lujo:" | Dejar el guion original |
| D18 | 2026-10-07 | V2: "e-commerce" → **"comercio electrónico"** en la voz (y el kicker en pantalla) | Castellano y accesibilidad para público no técnico ("no es muy grave", pero suma) | Mantener el anglicismo |
| D19 | 2026-10-07 | V2 con **voz clonada de Fish Audio** ("Consultor Digital") y montaje **re-timado** a partir de las duraciones reales de los clips | Al cambiar la voz cambian las duraciones; los timings deben salir del audio y no del papel | Mantener los timings antiguos (habrían desincronizado voz e imagen) |
| D20 | 2026-10-07 | Karaoke con timings **anclados a las pausas reales** de cada clip (y fin del clip) | Mejor sincronía que el reparto proporcional a ciegas; el audio ya existe, así que se puede medir | Mantener el reparto proporcional (D07) |
| D21 | 2026-10-08 | V2: se cambia el **clon propio** por la voz **oficial** de Fish Audio `Pablo` (`1bd666ea8ada44c789e0fec21cf78f33`) | El audio de origen del clon venía `quality_passed: false` (*multi speaker*) → riesgo de voz inestable; una voz oficial es limpia y consistente | Mantener el clon propio |
| D22 | 2026-10-08 | El recorte de cola de la voz solo se aplica si el silencio **llega al final del clip** | Bug real: tomar el último `silence_start` a secas cortó la línea 2 en una pausa interna y la dejó de 3,7 s en 1,3 s | Recortar por el último `silence_start` (trunca en la última coma del guion) |
| D23 | 2026-10-08 | **Escena = clip**: cada escena dura exactamente lo que su audio (fuera el relleno a 3 s) | El usuario pidió quitar los silencios en los que el vídeo corría sin voz | Mantener el mínimo de 3 s por escena (dejaba 1,8 s mudos en las frases cortas) |
| D24 | 2026-10-08 | Capa de **efectos de sonido** propia (`assets/sfx/sfx.wav`), sintetizada y anclada a cada aparición | El usuario los pidió; sin librería de samples, sintetizarlos con `tools/sfx.py` es determinista, gratis y reproducible | No tener efectos |
| D25 | 2026-10-08 | **Menos texto, más gráfico**: ventana de navegador (F1–F4), SERP con cursor y scroll (F8), iconos SVG (F6, F7, F9, F10) | El usuario señaló que casi todo lo que había en pantalla era texto; un gráfico se lee de un vistazo en vertical | Seguir con rótulos y titulares |

## Notas operativas aprendidas (no son decisiones de contenido)

- El token del entorno es de la App **`openhands-ai`** y **solo escribe donde la App
  está instalada**. Hubo que instalar la App en `openframes` para poder hacer push.
- Esa App **no tiene permiso de administración**: no puede crear repos ni cambiar su
  visibilidad (para eso hace falta un PAT).
- El preview del Studio debe escuchar en `0.0.0.0`
  (`HYPERFRAMES_PREVIEW_HOST=0.0.0.0`) o el proxy externo devuelve **502**.
- **La portada rompe el publicador de n8n**: con `include_cover=true` el webhook responde
  sin ningún job (`{"jobs":[]}`) y la Action de estado devuelve `not_found`. Se publica con
  `include_cover=false`; la portada se queda en `outputs.cover` para cuando el endpoint se
  arregle. Le pasó a V1 y a V2.
- **Un fallo posterior a la reserva bloquea el reintento**: el ítem queda en `publishing` y
  el siguiente intento muere en la reserva (sin volver a llamar a n8n — la salvaguarda
  funciona). Para reintentar hay que reconciliar antes: comprobar el `jobId` con la Action
  de estado y, si está `not_found`, liberar la reserva (`publish_attempt`, `needs_review`).
