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

- **Seek-safe siempre:** estado inicial en CSS y animación con GSAP `.to()`; los rellenos con
  `fromTo` explícito. Nunca `.from()`, ni contadores numéricos, ni `Date.now()`/`Math.random()`.
- Entradas disponibles: `fade-up` / `fade-up-sm` (subida suave), `pop` (`scale .7→1`, `back.out(2)`),
  `slide-x` (deslizamiento lateral), `fill` (`scaleX 0→1`), `fade-in`.
- **Una aparición = un gesto.** Nada de animaciones decorativas que no acompañen a un elemento.
- **La animación no puede durar más que su escena** (escena = clip): el último cambio termina
  ~0,35 s antes del corte.

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
