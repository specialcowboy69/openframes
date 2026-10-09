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
| D26 | 2026-10-08 | **Transiciones en todos los cortes**: `push-slide` como primaria + `zoom-through` (clímax, F5→F6) y `blur-crossfade` (lujo, F6→F7) como acentos | Nuevo enfoque pedido por el usuario ("nivel de montaje"). La doctrina del framework: sin transiciones las escenas se sienten cortes secos, y la transición **es** la salida | Dejar los cortes secos |
| D27 | 2026-10-08 | Las transiciones animan una **capa interna** (`#sN-in`) y **extienden la cola** del saliente (`data-duration += dur.`), nunca el clip | El clip es del framework: manda la visibilidad. Extender la cola hace que ambos convivan en el cruce **sin tocar los `<audio>`** → cero silencios (regla dura del usuario) | Animar el clip y arriesgar el ciclo de vida; o usar overlays |
| D28 | 2026-10-08 | **`power3.out` como asentamiento; fuera `back.out(2)`** | La doctrina del framework es explícita: el rebote es *"el turn-off nº 1 en vídeos hechos por agentes"* y casi nunca se ejecuta bien. V2 lo usaba en el `pop` | Mantener el rebote "porque da energía" |
| D29 | 2026-10-08 | **Revelado sincronizado con la voz** (tiempos por palabra del karaoke) y **escenario desde t=0** | Medido: con el marco entrando a 0,3–0,4 s la escena **llegaba vacía** al cruce (cobertura del lienzo 3,1 % → 11,1 % tras el arreglo). Volcar todo al principio es el fallo "PowerPoint" | Meter todo en el primer 25 % |
| D30 | 2026-10-08 | **No** usar `data-layout-allow-overflow` para silenciar los avisos de layout de las transiciones | El atributo es heredado: silenciaría también los chequeos de texto (`text-clipping`, `foreground-over-panel`) de toda la escena. Los avisos son `info` y `check` pasa | Silenciarlos y perder cobertura de QA |
| D31 | 2026-10-08 | **Toda escena necesita un escenario** (una tarjeta o marco) presente desde `t=0`; el contenido revelado va a la voz | Medido en V3: F5 y F8 son solo barras finas sobre oscuro y durante su push el lienzo se quedaba sin contenido (2-3 %). Con tarjeta-contenedor el cruce aguanta. En V2 el fallo era el mismo (el marco entraba a 0,3-0,4 s) | Escenas sin superficie: entran vacías al cruce |
| D32 | 2026-10-08 | Medir la cobertura del lienzo con **umbral fijo** (luminancia > 25) y **por fotograma**, y juzgar por el **tramo continuo sin contenido** (barra: ≤ 0,15 s) | La cobertura con umbral *relativo* engaña: una superficie grande y clara sube la media y descarta filas que sí tienen contenido (me hizo diagnosticar un hueco donde no lo había, y tapar uno donde sí) | Umbral relativo: falsos positivos y negativos |
| D33 | 2026-10-08 | `tools/sfx.py` lee el array `S` del **`index.html` del proyecto** y los eventos de **`assets/sfx/events.json`**; si no existe, usa los de V2 | El tool tenía S y EVENTS cableados a V2: reutilizarlo en V3 habría reescrito la pista de V2 con los tiempos de V3. Verificado que V2 sigue dando la **misma pista byte a byte** (md5 igual) | Duplicar el tool por vídeo |
| D34 | 2026-10-08 | **El copy de publicación es breve: texto del vídeo + 2-3 hashtags, sin avisos de autoría** | Decisión del dueño (2026-10-08). V1 y V2 llevaban una línea de autoría porque son anteriores a la regla; no se repite. El copy se genera desde el `SCRIPT.md` y el CTA es "Guarda esto" | Leyendas largas con 5 hashtags y aviso de IA |
| D35 | 2026-10-08 | **Instagram y Facebook se publican siempre sin portada** (`include_cover=false` → ruta `/video_reels`) | Medido: n8n rechaza la portada de GitHub Releases con `400 cover_url must use an approved HTTPS media host`. La ruta `/videos` con portada exigiría alojarla en `media.urltovideo.es`/R2 autorizado. El `video_url` de GitHub sí se acepta | Reintentar con portada y perder el encolado |
| D36 | 2026-10-08 | **YouTube y TikTok quedan fuera de este flujo: no reintentar** | El dueño los publicó por su cuenta (2026-10-08) y pidió expresamente no reintentar nada hacia esas plataformas | Reintentar subidas ya hechas |
| D37 | 2026-10-08 | **La leyenda nunca se teclea a mano: se lee del campo `caption` de la cola de `hypervideo`** | Incidente real: en un reintento manual se pasó el input `caption` como `PLACEHOLDER` y n8n lo encoló tal cual. La cola es la fuente de verdad del texto | Pasar los inputs a mano |

## Notas operativas aprendidas (no son decisiones de contenido)

- **Orden obligatorio de la cadena de montaje**: `voice_pipeline.py` → `sfx.py` →
  `retime.py` → **re-aplicar las colas de las transiciones** → `check` → `render`. `retime.py`
  reescribe las duraciones de escena a `escena = clip`, así que **borra** la extensión de cola
  que necesitan las transiciones: si no se re-aplica, la escena saliente desaparece en seco en
  mitad del cruce.

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
