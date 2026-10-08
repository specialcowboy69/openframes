# DESIGN — sistema visual y sonoro de la serie

Documento vivo: **cómo se ve y cómo suena** cualquier vídeo de la serie. Si un vídeo se
sale de aquí, la excepción se anota en `DECISIONS.md`.

Referencia montada: **`videos/seo-02-modificador-lujo/`** (V2), que es donde se estrenó
todo esto (decisiones D23–D25).

---

## 0. Principio rector: menos texto, más gráfico

> **El peso lo lleva el gráfico.** El texto en pantalla se reserva a lo que *es* el tema
> del vídeo (una URL, un título de resultado), a los rótulos de contexto y a los
> subtítulos. Todo lo que se pueda decir con una forma, se dice con una forma.

Sustituciones por defecto:

| Antes (texto) | Ahora (gráfico) |
|---|---|
| Una URL suelta | **Ventana de navegador** con semáforo, candado y barra de direcciones |
| "suma / resta" | Flechas ↑ verde y ↓ roja |
| "pierdes el clic" | **SERP que se desplaza + cursor** que pasa de largo y resultado que se apaga |
| "mala calidad" | Tachado rojo + ✕ |
| "más / menos clientes" | Carrito con flecha arriba (verde) / abajo (roja) |
| "guarda esto" (titular) | **Marcador de guardado** grande con onda |
| Nota gris que repite la voz | **Se elimina** |

El vídeo sigue entendiéndose en mudo, pero ahora por **subtítulos karaoke + gráficos**,
no por acumulación de texto.

---

## 1. Lienzo y paleta

| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#0a0a0f` | Fondo |
| `--ink` | `#f5f5f7` | Texto principal |
| `--muted` | `#8b8b99` | Rótulos y texto secundario |
| `--accent` | `#c8ff3d` | **Único acento**: lo correcto, lo que suma |
| `--warn` | `#ff5a5a` | Lo malo, el aviso, el tachado |
| `--gold` | `#ffd166` | Solo lujo (gema) |
| `--panel` | `#14141a` | Superficies (ventana, paneles) |
| `--chrome` | `#1c1c24` | Barra superior del navegador |
| `--field` | `#0e0e14` | Barra de direcciones |
| `--line` | `#26262e` | Bordes (3–5 px) |
| Claro | `#eef1f5` / `#16181c` | Cuerpo de la SERP: el único bloque claro del vídeo |

- **Un solo acento por escena.** Verde = bien, rojo = mal, dorado = lujo. Nunca dos acentos compitiendo.
- Lienzo 1080×1920. Escena con `padding: 300px 74px 470px`.
- **Zonas seguras:** nada crítico en el 15 % superior ni el 25 % inferior (ahí van la barra de progreso arriba y la píldora karaoke abajo).

## 2. Tipografía

- **Inter** (400/600/700/800/900) para todo el texto.
- **JetBrains Mono** (600/800) para lo que representa una URL, una etiqueta de precio o código.
- Jerarquía real: **componente gráfico > rótulo > subtítulo**. Los titulares grandes de texto están retirados (solo el cierre del CTA los usa).
- Rótulo (*kicker*): 28 px, 700, `letter-spacing: 0.28em`, mayúsculas, color `--muted`, con un punto de color.

## 3. Kit de componentes

Todo es CSS + SVG inline (sin imágenes externas: el render no depende de la red salvo las fuentes).

| Componente | Clases | Para qué |
|---|---|---|
| Ventana de navegador | `.browser` › `.chrome` › `.lights` | Presentar cualquier URL: **nunca una URL suelta** |
| Barra de direcciones | `.addr` (+ `.lock`, `.base`, `.dim`, `.mod`, `.caret`, `.plus`) | Mostrar dónde vive el modificador, escribirlo, marcar la posición |
| Tarjeta de resultado | `.serpbody` › `.result` › `.fav`, `.crumb`, `.rtitle`, `.skeleton` | El título tal como se ve en Google |
| Lista que se desplaza | `.scroller` › `.inner` › `.res` (`.res.ours`) | "El usuario pasa de largo" sin una palabra |
| Cursor | `.cursor` | Señalar y clicar |
| Veredicto | `.verdict.up` / `.verdict.down` | Suma / resta |
| Barras comparadas | `.bars` › `.bar.short` / `.bar.long` | Rapidez de lectura |
| Etiqueta | `.tag` (+ `.strike`) | Precio o palabra tachada |
| Iconos grandes | `.duo .p`, `.savewrap`, `.warnwrap` | Carrito, marcador, triángulo de aviso |
| Rótulo | `.kicker` (+ `.dot`, `.warn`) | Contexto mínimo |
| CTA | `.cta` | Botón píldora |

**Repertorio de iconos SVG** (`fill`/`stroke` = `currentColor`, siempre): candado, flecha
arriba/abajo, check, aspa, triángulo de aviso, gema, etiqueta, carrito, ojo, aguja, marcador,
lupa. Todos inline; el color lo hereda del contenedor (así el mismo icono sirve en verde o rojo).

**Barra de progreso** (`.progress` › `.progress-fill`): 6 px arriba, `scaleX 0→1` durante todo el vídeo.

## 4. Movimiento

Fuente autoritativa: las skills de HyperFrames (`hyperframes-animation` → `motion-language.md`,
`transitions/` y `rules/`). La doctrina es dura: no es cuestión de gusto.

### 4.1 Doctrina

- **Suave gana a rebotón.** El asentamiento por defecto es **`power3.out`** (cola larga, sin
  sobrepasar). `back.out` / `bounce` / `elastic` están **prohibidos** como entrada: son el
  *turn-off nº 1* de los vídeos hechos por agentes. Para una llegada rápida, `expo.out`.
  (V2 usaba `back.out(2)` en el `pop`: corregido.)
- **Revelado secuencial, sincronizado con la voz.** Cada elemento aparece **cuando la voz lo
  nombra**, no todo al principio. Volcar la escena en el primer 25 % es *el* fallo
  "PowerPoint". Los tiempos por palabra salen del karaoke (`TRANSCRIPT` del componente de
  subtítulos): es la fuente de verdad de cuándo se dice cada cosa.
- **El escenario entra con la escena.** El marco (la ventana de navegador, la tarjeta) es el
  suelo de la escena, no un revelado, y **toda escena necesita uno**: si su contenido es escaso
  (unas barras finas), hay que envolverlo en una tarjeta. Si entra tarde —o si no existe— la
  escena **llega vacía** durante el cruce: medido en V2 (marco a los 0,3-0,4 s → 3,1 % del lienzo
  con contenido) y en V3 (F5/F8 sin tarjeta → 2-3 % en mitad del push). Lo que va a la voz es el
  contenido (URL, modificador, veredictos, barras), no el marco.
- **Nada de "breathing"** (escalar en bucle para fingir vida) ni pan/zoom lentos en la segunda
  mitad: marean y abaratan. *Antes nada de movimiento que mal movimiento.* La única vivacidad
  permitida es un *subtle jitter* de baja amplitud.
- **Entradas con `fromTo`** (estado inicial explícito), nunca confiando solo en un CSS oculto.
  Prohibido CSS `transition`/`@keyframes` y `repeat`/`yoyo`: se desincronizan del reloj del render.
- **La animación no dura más que su escena** y el último cambio cierra antes del corte.

Clases CSS de estado inicial (la animación las sobrescribe): `fade-in`, `fade-up`,
`fade-up-sm`, `pop`, `slide-x`, `fill`.

### 4.2 Transiciones entre escenas

*Toda* composición multi-escena lleva transiciones: sin ellas las escenas se sienten como
cortes secos. Y **la transición ES la salida**: no se anima nada hacia fuera (salvo el último
frame, que sí puede cerrar).

Registro disponible (Tier-B: solo transform/opacidad/filtro sobre el envoltorio, sin DOM extra):

| Transición | Energía | Cuándo |
|---|---|---|
| `push-slide` (↑ ↓ ← →) | media | **primaria**: "siguiente punto" |
| `crossfade` | cualquiera | continuidad: "esto sigue" |
| `blur-crossfade` | calma | fondos que chocan; registro *premium* |
| `zoom-through` | alta | **clímax**: lo más audaz |
| `squeeze` | media | cambio de sección |
| `cut` | — | saltar (excepcional) |

Reglas de reparto: **una primaria (60-70 %)** + 1-2 acentos. La apertura, la más distintiva;
el clímax, la más audaz; el outro, la más simple. Duración 0,3-0,5 s (máx. 2 s) **ajustada a la
longitud de la escena**: en una escena de 1,2 s, 0,3 s.

Cómo se implementa en `index.html`:

1. Cada escena envuelve su contenido en `<div class="s-in" id="sN-in">`. **Las transiciones
   animan esa capa interna, nunca el clip**, que es de quien manda la visibilidad.
2. La cola del saliente se extiende: `data-duration += duración de la transición`.
3. El array `TR` del script declara cada cruce; el bucle emite los dos tweens en `T = S[n]`.
4. Los `<audio>` **no se tocan nunca** → las transiciones no crean silencios.

Mapa de V2 (10 escenas):

| Corte | Transición | Dur. | Por qué |
|---|---|---|---|
| F1→F2 | `push-slide` ↑ | 0,45 s | primaria: siguiente punto |
| F2→F3 | `push-slide` ↑ | 0,40 s | primaria |
| F3→F4 | `crossfade` | 0,40 s | F3 y F4 son el mismo contexto (URL → título) |
| F4→F5 | `push-slide` ↑ | 0,40 s | punto nuevo |
| F5→F6 | **`zoom-through`** | 0,50 s | **clímax**: el giro del aviso |
| F6→F7 | `blur-crossfade` | 0,50 s | el caso de lujo: contención, *premium* |
| F7→F8 | `push-slide` ↓ | 0,30 s | la caída; corta, porque F8 dura 1,2 s |
| F8→F9 | `crossfade` | 0,35 s | continuidad |
| F9→F10 | `crossfade` | 0,50 s | outro: cierre suave |

**Verificación sin ojos** (obligatoria antes de dar un montaje por bueno):
`check` en verde; **ningún tramo > 0,15 s sin contenido en los cruces**, medido **por fotograma
a 30 fps con umbral de luminancia fijo (25)** — con umbral relativo a la media el propio fondo
claro falsea el cálculo (D32); perfil de bandas por filas para ver que el contenido se desplaza;
y envolvente RMS del audio para confirmar **cero huecos** de silencio.

## 5. Sonido

| Capa | Archivo | Volumen | Nota |
|---|---|---|---|
| Voz | `assets/voice/NN.wav` | 1.0 | 1 clip por línea, **escena = clip** |
| Música | `assets/music/track.wav` | `0.18` | Nunca por encima de la voz |
| Efectos | `assets/sfx/sfx.wav` | `0.5` | Un único `<audio id="sfx">` (track 4) |

- **Voz**: Fish Audio, voz oficial **`Pablo`** (`reference_id 1bd666ea8ada44c789e0fec21cf78f33`),
  modelo `s2.1-pro`, wav. Cola recortada a **0,08 s** → la voz va continua, sin silencios.
- **Efectos**: los sintetiza `tools/sfx.py` (deterministas, gratis, sin librería de samples) y los
  mezcla en una sola pista anclada al array `S` de `index.html`.

Vocabulario sonoro (9 tipos):

| Efecto | Carácter | Se usa para |
|---|---|---|
| `whoosh` | aire | entra una escena o un bloque grande |
| `pop` | burbuja | aparece un chip, tarjeta o panel |
| `tick` | clic corto | resaltar, escribir, marcar posición |
| `click` | clic con ruido | el clic del cursor |
| `swoosh_up` / `swoosh_down` | barrido | llenarse, subir / bajar |
| `ding` | campana | acierto, check, lujo |
| `thud` | golpe grave | aviso, error, tachado |
| `buzz` | zumbido | negación |

Regla: **un efecto por aparición** (ganancia 0,25–0,85), nunca uno por palabra. Añadir un
efecto = añadir una línea a `EVENTS` en `tools/sfx.py` y regenerar la pista.

## 6. Cierre

Todos los vídeos terminan en CTA de **guardar**, con un gesto gráfico (marcador + onda),
no con un titular. Ver `PROFILE.md`.
