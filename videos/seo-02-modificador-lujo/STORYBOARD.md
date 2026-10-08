---
format: 1080x1920
duration: 29.8s
message: "Dónde va el modificador depende del tipo de tienda; y en lujo, nunca se usa"
arc: Hook → Regla → Ejemplo → Razón → Giro → Advertencia → CTA
audience: gente que hace SEO o marketing digital en redes
mode: collaborative
---

**Regla de montaje:** cada escena dura exactamente lo que dura su clip de voz
(**escena = clip**). No hay silencios entre frases: la voz va continua de principio a fin.

**Capa de sonido:** música de fondo (`assets/music/track.wav`, volumen 0.18) + pista de
efectos `assets/sfx/sfx.wav` (volumen 0.5), generada con `tools/sfx.py` y anclada a la
aparición de cada elemento.

**Regla de diseño:** el peso lo llevan los gráficos (ventana de navegador, tarjeta de
resultado, iconos SVG, cursor). El texto en pantalla queda reducido al mínimo: solo el que
es el propio tema del vídeo (la URL, el título) y los subtítulos karaoke.

**Regla de movimiento:** entradas con `fromTo` y asentamiento **`power3.out`** (nunca rebote);
cada elemento aparece **cuando la voz lo nombra** (tiempos por palabra del karaoke); el
**escenario entra con la escena**. Detalle en `DESIGN.md` §4.

**Transiciones:** una primaria (`push-slide`) + dos acentos (`zoom-through` en el giro,
`blur-crossfade` en el lujo). Animan la capa interna `#sN-in` y extienden la cola de la escena
saliente; **el audio no se toca** → cero silencios.

| Corte | `transition_in` | Dur. | Por qué |
|---|---|---|---|
| F1→F2 | `push-slide` ↑ | 0,45 s | primaria |
| F2→F3 | `push-slide` ↑ | 0,40 s | primaria |
| F3→F4 | `crossfade` | 0,40 s | mismo contexto (URL → título) |
| F4→F5 | `push-slide` ↑ | 0,40 s | punto nuevo |
| F5→F6 | `zoom-through` | 0,50 s | clímax: el giro |
| F6→F7 | `blur-crossfade` | 0,50 s | el lujo: contención |
| F7→F8 | `push-slide` ↓ | 0,30 s | la caída (F8 dura 1,2 s) |
| F8→F9 | `crossfade` | 0,35 s | continuidad |
| F9→F10 | `crossfade` | 0,50 s | outro |

## Frame 1 — Hook (0,000 – 4,226 s)

- scene: ventana de navegador con `tutienda.com/zapatillas-baratas` y dos veredictos (↑ verde / ↓ rojo)
- sfx: whoosh + 3 pops (ventana, chip, cada veredicto)
- voiceover: "El mismo modificador de la URL suma o resta. Depende de dónde lo pongas."

## Frame 2 — La regla (4,226 – 7,981 s)

- scene: la misma ventana; un marcador `+` señala el final de la barra de direcciones y la etiqueta `-baratas` entra deslizándose hasta ahí
- sfx: whoosh, tick (marcador), pop (etiqueta)
- voiceover: "En comercio electrónico, el modificador se coloca al final de la URL."

## Frame 3 — Ejemplo (7,981 – 11,626 s)

- scene: se escribe la URL (cursor parpadeante) y aparece `-baratas` tal cual; un check confirma que entra sin retocar
- sfx: whoosh + 2 ticks + ding (check)
- voiceover: "En la URL, la búsqueda entra tal cual: zapatillas baratas."

## Frame 4 — El título (11,626 – 15,192 s)

- scene: tarjeta de resultado dentro de la ventana (google.com/search): título azul con "baratas" resaltado en acento
- sfx: whoosh, pop (tarjeta), tick (resaltado)
- voiceover: "El título, en cambio, suena natural: zapatillas baratas para correr."

## Frame 5 — Por qué al final (15,192 – 18,441 s)

- scene: dos barras comparadas: la corta (`-baratas`) se llena de golpe, la larga se arrastra; un ojo y una aguja las interpretan
- sfx: whoosh + 2 swoosh (llenado rápido y lento)
- voiceover: "¿Por qué el modificador al final? Es corto, se lee rápido."

## Frame 6 — Giro (18,441 – 20,699 s)

- scene: triángulo de aviso rojo a gran tamaño, con onda expansiva y el sello NUNCA
- sfx: thud (golpe grave) + pop + buzz
- voiceover: "Pero hay un caso donde no lo deberías usar nunca."

## Frame 7 — Lujo (20,699 – 23,490 s)

- scene: gema dorada + etiqueta "barato" tachada en rojo + ✕
- sfx: ding (lujo), tick, thud (tachado), pop (✕)
- voiceover: "En el lujo, el comprador ve barato como mala calidad."

## Frame 8 — Consecuencia (23,490 – 24,693 s)

- scene: resultados de búsqueda que se desplazan hacia arriba mientras el cursor baja de largo; nuestro resultado se apaga. Sin una sola palabra
- sfx: whoosh, swoosh (scroll), click (clic perdido)
- voiceover: "Por eso pierdes el clic."

## Frame 9 — Resumen (24,693 – 27,546 s)

- scene: dos paneles con carrito de compra: flecha verde arriba / flecha roja abajo
- sfx: pop, swoosh arriba, pop, swoosh abajo
- voiceover: "Ese mismo modificador te suma o te quita clientes."

## Frame 10 — CTA (27,546 – 29,779 s)

- scene: marcador de guardado grande con onda + botón GUARDA ESTO
- sfx: pop, ding, pop (botón)
- voiceover: "Guarda esto antes de tu próxima optimización."
