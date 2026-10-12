# STORYBOARD — mkt-01 «Responde con vídeo (Old Spice 2010)»

Serie **Casos de estudio marketing** · Pieza **mkt-01** · **11 beats · 121 palabras · ≈37,5 s** ·
1080×1920 · faceless · voz en off es-ES (`Pablo`) · subtítulos karaoke. La dirección de arte está en
`DIRECCION.md` y el brief en `DIRECCION-ARTE-BRIEF.md`. Formato calcado de
`videos/seo-06-canibalizacion/STORYBOARD.md`.

**Todos los tiempos son RELATIVOS al inicio de su beat** (los absolutos los fija la voz con
`retime.py`). Los identificadores son los del `index.html`; el CSS de los elementos nuevos está en
`DIRECCION.md` §8.

**Regla en las 11 escenas:** el escenario (móvil / tarjeta / cadena / rejilla / set / panel) está
visible desde el fotograma 0 y **solo se asienta** (`rise()`); nace en opacidad 0 solo el contenido.
Sin `.from()`, sin `Math.random`, sin `Date.now`, sin contar hacia arriba (`setNum(sel, txt, t)` fija el
número en un salto discreto). Ayudantes: `put`, `rise`, `draw`, `grow`, `bar`, `typeWords`, `typeChars`,
`swap`, `setNum`. Los elementos que se revelan llevan la clase del kit `.fade-in` (estado inicial en
CSS); el resto usa `fromTo`/`.to()`.

**Recurso propio:** el **comentario que se convierte en vídeo** (burbuja → clip-respuesta). No se
reutiliza la **SERP etiquetada** de V5 ni la **balanza** de V6. **Ejemplo único:** la tienda de ropa
(B7-B9), de `SCRIPT.md`. **La pieza no usa rojo**: no hay pérdida ni error real.

---

## Desviaciones justificadas del contrato

- **Banda segura (`.s-in`).** El contrato §3 fija `padding: 300px 74px 470px`; esta pieza usa
  **`padding: 300px 74px 700px`** (`index.html`). Se subió a propósito para que el bloque de contenido
  **no quede bajo la píldora del karaoke** (la píldora va a `bottom:470` y ocupa ~y 1230-1450). Es una
  desviación **solo de margen y más conservadora** que el contrato: no viola la banda segura 15-75 %
  (288-1440). Se mantiene tal cual; queda documentada aquí por indicación de la verificación.

---

## B1 · Gancho — «La estrategia que usó esta conocida marca, la puedes usar tú también.»

- **Qué se ve:** papel claro a pantalla completa (**fotograma 0 = miniatura**). El **hilo de comentarios
  en el móvil**; en el hilo, la **burbuja destacada se abre** y de ella sale el **clip-respuesta** con su
  botón de reproducción. El callout **«ESTA MARCA»** apunta al móvil. Todo está montado en el fotograma 0
  y solo se asienta: **nada se desvanece ni entra tarde**.
- **Elementos:** `#s1-in` · `#s1-kicker` (`.kicker`) · `#s1-label` (`.callout`, relleno de acento) ·
  `#s1-phone` (`.phone`) · `#s1-thread` (`.cthread`) · `#s1-cm1`, `#s1-cm2` (`.cmsg`) · `#s1-bubble`
  (`.cbubble.hot`) · `#s1-clip` (`.replyclip`).
- **Receta (rel):** `rise("#s1-phone", at(1,0.0),{y:30})` · `rise("#s1-thread", at(1,0.0),{y:30})` ·
  `rise("#s1-bubble", at(1,0.0),{y:20})` · `rise("#s1-kicker", at(1,0.0),{y:20})` ·
  `put("#s1-label", at(1,0.0),{x:-20})` ·
  `fromTo("#s1-bubble",{scale:1},{scale:1.05,dur:0.2,ease:"power2.out"}, at(1,1.05))` →
  `to("#s1-bubble",{scale:1,dur:0.2,ease:"power2.inOut"}, at(1,1.45))` (la burbuja «se abre») ·
  `put("#s1-clip", at(1,1.15),{scale:0.6,y:20})` (el clip emerge).
- **Rótulo en pantalla:** kicker **«GANCHO»**; callout **«ESTA MARCA»** (acento relleno con tinta).
- **Sonido:** whoosh 0,0 (entra el hilo) · pop 0,60 · swoosh_up 1,15 (el clip) · ding 2,60.
- **Salida:** **desplazamiento continuo ↑ 0,35 s**.

## B2 · El caso — «En 2010, Old Spice respondió con vídeos a comentarios de fans y famosos.»

- **Qué se ve:** papel claro. La **tarjeta del caso** con el año **2010** y el **logotipo de Old Spice**
  (tinta sobre tarjeta clara); al lado, un **comentario de un fan se convierte en clip-respuesta**: el
  caso como prueba.
- **Elementos:** `#s2-in` · `#s2-kicker` · `#s2-card` (`.card`) · `#s2-year` (`.yearbadge` «2010») ·
  `#s2-brand` (`.brandmark`, logotipo tipográfico) · `#s2-cm` (`.cbubble`) · `#s2-clip` (`.replyclip`) ·
  `#s2-cover` (`.cover`, pieza de transición).
- **Receta (rel):** `rise("#s2-card", at(2,0.0))` · `put("#s2-kicker", at(2,0.06),{dur:0.4})` ·
  `put("#s2-year", at(2,0.30),{scale:0.8})` · `put("#s2-brand", at(2,0.95),{y:20})` ·
  `put("#s2-cm", at(2,1.30),{x:-24})` · `put("#s2-clip", at(2,1.75),{scale:0.6})`.
- **Rótulo en pantalla:** kicker **«EL CASO»**; logotipo **«OLD SPICE»** (tinta `#14141a` sobre tarjeta
  `#ffffff`) · año **«2010»**.
- **Nota:** el logotipo de la marca de consumo va **autorizado por el dueño (2026-10-12)**; mientras, se
  representa solo con su nombre escrito como logotipo (tinta sobre tarjeta clara), sin arroba ni afiliación.
- **Sonido:** pop 0,20 · tick 0,55 (el año) · pop 0,95 (la marca) · pop 1,30 · ding 2,30.
- **Salida:** **objeto que cubre (`.cover`) 0,45 s** — el panel `#20202a` crece desde la tarjeta de marca
  y despeja la escena oscura.

## B3 · El mecanismo — «Un equipo grababa cada respuesta en minutos, en torno a dos días y medio.»

- **Qué se ve:** escena oscura. La **cadena de producción** de una respuesta: **COMENTARIO → GUION →
  PROMPTER → CÁMARA**, cuatro estaciones unidas por **flechas que se dibujan** una tras otra; al pie, el
  chip **«EN MINUTOS»**. La cadena es la respuesta que se fabrica en serie.
- **Elementos:** `#s3-in` · `#s3-kicker` · `#s3-card` (`.card`) · `#s3-chain` (`.chain`) · `#s3-st1`
  (burbuja), `#s3-st2` (`.sheet`), `#s3-st3` (`.prompter`), `#s3-st4` (cámara) — todas `.station` ·
  `#s3-a1`, `#s3-a2`, `#s3-a3` (`.chainarrow`, SVG) · `#s3-note` (`.chip` «EN MINUTOS»).
- **Receta (rel):** `rise("#s3-card", at(3,0.0))` · `put("#s3-kicker", at(3,0.06),{dur:0.4})` ·
  `put("#s3-st1", at(3,0.30),{x:-30})` · `draw("#s3-a1", at(3,0.55),0.25)` ·
  `put("#s3-st2", at(3,0.80),{x:-30})` · `draw("#s3-a2", at(3,1.05),0.25)` ·
  `put("#s3-st3", at(3,1.30),{x:-30})` · `draw("#s3-a3", at(3,1.55),0.25)` ·
  `put("#s3-st4", at(3,1.80),{x:-30})` · `put("#s3-note", at(3,2.40),{y:16})`.
- **Rótulo en pantalla:** kicker **«EL MECANISMO»**; etiquetas **COMENTARIO / GUION / PROMPTER /
  CÁMARA**; chip **«EN MINUTOS»**.
- **Sonido:** whoosh 0,0 · tick 0,55 · tick 1,05 · tick 1,55 · click 1,80 (la cámara) · ding 2,40.
- **Salida:** **desplazamiento continuo ↑ 0,45 s** (oscuro → claro; sin `clip-path`).

## B4 · La escala — «En total, 186 vídeos y casi seis millones de reproducciones el primer día.»

- **Qué se ve:** papel claro. La **rejilla de clips diminutos crece** hasta la cifra **186**; después el
  **foco se cierra en un solo clip** (la respuesta es personal), y la pastilla **«6 M · EL DÍA 1»**
  resume las reproducciones del primer día. La cifra aparece de golpe (`setNum`), nunca contando.
  La rejilla es **representativa** (4 filas × 8 = 32 clips, dentro de la banda segura); **el total lo
  dice la cifra 186**, que es el dato real: el muro no se dibuja mosaico a mosaico.
- **Elementos:** `#s4-in` · `#s4-kicker` · `#s4-card` (`.card`) · `#s4-num` (`.bignum`) · `#s4-numlab`
  (`.statlab` «VÍDEOS») · `#s4-grid` (`.clipgrid`) con `#s4-g1`… (`.mini`) · `#s4-stat` (`.pill.accent`
  «6 M · EL DÍA 1») · `#s4-focus` (`.minifocus`) · `#s4-plabel` (`.chip` «UNA RESPUESTA, PERSONAL»).
- **Receta (rel):** `rise("#s4-card", at(4,0.0))` · `put("#s4-kicker", at(4,0.06),{dur:0.4})` ·
  `typeWords("#s4-grid .mini", at(4,0.20),0.035)` (la rejilla se llena en cascada) ·
  `setNum("#s4-num","186", at(4,1.20))` · `put("#s4-numlab", at(4,1.20),{y:12})` ·
  `put("#s4-stat", at(4,1.70),{scale:0.8})` ·
  `to("#s4-grid",{opacity:0.22,dur:0.5,ease:"power2.out"}, at(4,2.20))` ·
  `put("#s4-focus", at(4,2.30),{scale:0.6})` · `put("#s4-plabel", at(4,2.70),{y:16})`.
- **Rótulo en pantalla:** kicker **«LA ESCALA»**; cifra **186** · etiqueta **VÍDEOS** · pastilla
  **«6 M · EL DÍA 1»** · chip **«UNA RESPUESTA, PERSONAL»**.
- **Sonido:** pop 0,20 · tick 0,60 · ding 1,20 (el 186) · pop 1,70 (el 6 M) · swoosh_up 2,30 (el foco) ·
  ding 2,70.
- **Salida:** **desplazamiento continuo ↑ 0,40 s**.

## B5 · La lección — «La lección: responder por su nombre, rápido y con humor.»

- **Qué se ve:** papel claro. Tres **etiquetas** que se asientan una tras otra: **POR SU NOMBRE ·
  RÁPIDO · CON HUMOR**; la tercera lleva el relleno de acento como remate. Cada una con su icono (nombre,
  rayo, sonrisa).
- **Elementos:** `#s5-in` · `#s5-kicker` · `#s5-card` (`.card`) · `#s5-t1`, `#s5-t2` (`.lesstag`) ·
  `#s5-t3` (`.lesstag.accent`).
- **Receta (rel):** `rise("#s5-card", at(5,0.0))` · `put("#s5-kicker", at(5,0.06),{dur:0.4})` ·
  `put("#s5-t1", at(5,0.25),{x:-30})` · `put("#s5-t2", at(5,0.70),{x:-30})` ·
  `put("#s5-t3", at(5,1.15),{x:-30,scale:0.88})`.
- **Rótulo en pantalla:** kicker **«LA LECCIÓN»**; etiquetas **POR SU NOMBRE / RÁPIDO / CON HUMOR**.
- **Sonido:** pop 0,25 · pop 0,70 · pop 1,15 · ding 1,70.
- **Salida:** **desplazamiento continuo ↑ 0,35 s**.

## B6 · Tu versión — «Tú no necesitas comprar anuncios, solo un móvil.»

- **Qué se ve:** papel claro. El **móvil en un trípode** (el set) y el cartel **«PRESUPUESTO DE
  ANUNCIO»** que se **tacha en tinta** —no en rojo: no es un error, es lo que *no hace falta*—. Cierra la
  pastilla **«SOLO UN MÓVIL»**.
- **Elementos:** `#s6-in` · `#s6-kicker` · `#s6-card` (`.card`) · `#s6-tripod` (`.tripod`, SVG) ·
  `#s6-phone` (`.phone`, reutilizado) · `#s6-sign` (`.sign` «PRESUPUESTO DE ANUNCIO») · `#s6-strike`
  (`.strike`, SVG, se dibuja con `draw`) · `#s6-pill` (`.pill.accent` «SOLO UN MÓVIL»).
- **Receta (rel):** `rise("#s6-card", at(6,0.0))` · `put("#s6-kicker", at(6,0.06),{dur:0.4})` ·
  `put("#s6-tripod", at(6,0.25),{y:24})` · `put("#s6-phone", at(6,0.45),{y:24})` ·
  `put("#s6-sign", at(6,0.85),{x:-24})` · `draw("#s6-strike", at(6,1.30),0.35)` ·
  `put("#s6-pill", at(6,1.60),{scale:0.86})`.
- **Rótulo en pantalla:** kicker **«TU VERSIÓN»**; cartel **«PRESUPUESTO DE ANUNCIO»** (tachado en tinta)
  · pastilla **«SOLO UN MÓVIL»**.
- **Sonido:** thud 0,25 (el trípode) · pop 0,45 · swoosh_down 1,30 (el tachado) · ding 1,60.
- **Salida:** **desplazamiento continuo ↑ 0,40 s**.

## B7 · El ejemplo — «Por ejemplo, en tu tienda de ropa una clienta pregunta cómo combinar una chaqueta.»

- **Qué se ve:** papel claro. Una **tienda** (percha con chaqueta dibujada con `draw`) y la **barra de
  comentario** donde una **clienta teclea** —carácter a carácter— **«¿Cómo combino esta chaqueta?»**. Es
  la única pieza de ejemplo de la línea.
- **Elementos:** `#s7-in` · `#s7-kicker` · `#s7-card` (`.card`) · `#s7-store` (`.store`) · `#s7-hanger`
  (`.hanger`, SVG) · `#s7-chat` (`.chatbar`) · `#s7-q` (`.qt`, texto tecleado con `typeChars`).
- **Receta (rel):** `rise("#s7-card", at(7,0.0))` · `put("#s7-kicker", at(7,0.06),{dur:0.4})` ·
  `rise("#s7-store", at(7,0.0),{y:30})` · `draw("#s7-hanger", at(7,0.35),0.5)` ·
  `put("#s7-chat", at(7,0.85),{y:24})` · `typeChars("#s7-q", at(7,1.30),0.05)`.
- **Rótulo en pantalla:** kicker **«EL EJEMPLO»**; la pregunta tecleada (JetBrains Mono).
- **Sonido:** pop 0,20 · pop 0,85 · tecleo (`key`, 14 clics, loc. 1,30-2,60, **ganancia 0,35**) · ding 2,80.
- **Salida:** **barrido de color (`.sweep`) 0,45 s** — banda de acento sesgada con **`x:0` explícito**;
  entra la escena oscura de los dos destinos (claro → oscuro).

## B8 · La doble ganancia — «Respondes con un vídeo corto y otros también lo ven.»

- **Qué se ve:** escena oscura. El **clip-respuesta** en el centro; una **horquilla que se dibuja** hacia
  dos tarjetas: **PARA ELLA** (un avatar) y **PARA EL RESTO** (varios avatares que se revelan). La misma
  respuesta vale dos veces.
- **Elementos:** `#s8-in` · `#s8-kicker` · `#s8-card` (`.card`) · `#s8-clip` (`.replyclip`) · `#s8-fork`
  (`.fork`, SVG, se dibuja con `draw`) · `#s8-her` (`.destcard` «PARA ELLA») · `#s8-others` (`.destcard`
  «PARA EL RESTO» con `.avatars`) · `#s8-sweep` (`.sweep`, pieza de transición entrante).
- **Receta (rel):** `rise("#s8-card", at(8,0.0))` · `put("#s8-kicker", at(8,0.06),{dur:0.4})` ·
  `put("#s8-clip", at(8,0.20),{scale:0.6})` · `draw("#s8-fork", at(8,0.75),0.4)` ·
  `put("#s8-her", at(8,1.15),{x:-24})` · `put("#s8-others", at(8,1.45),{x:24})` ·
  `typeWords("#s8-others .avatars i", at(8,1.85),0.06)`.
- **Rótulo en pantalla:** kicker **«LA DOBLE GANANCIA»**; **PARA ELLA / PARA EL RESTO**.
- **Sonido:** pop 0,20 · swoosh_up 0,75 (la horquilla) · pop 1,15 · pop 1,45 · ding 2,00.
- **Salida:** **desplazamiento continuo ↑ 0,40 s** (oscuro → claro; revisar el fotograma medio).

## B9 · La práctica — «Empieza por las tres preguntas que más te repiten.»

- **Qué se ve:** papel claro. La **lista de tres preguntas repetidas** de la tienda; cada fila recibe su
  **marca de vídeo** (clip + «VÍDEO») en secuencia. El criterio de partida: responder las tres primeras.
- **Elementos:** `#s9-in` · `#s9-kicker` · `#s9-card` (`.card`) · `#s9-list` (`.qlist`) · `#s9-r1`,
  `#s9-r2`, `#s9-r3` (`.qrow`) · `#s9-v1`, `#s9-v2`, `#s9-v3` (`.vmark`, acento relleno).
- **Receta (rel):** `rise("#s9-card", at(9,0.0))` · `put("#s9-kicker", at(9,0.06),{dur:0.4})` ·
  `put("#s9-r1", at(9,0.20),{x:-30})` · `put("#s9-r2", at(9,0.45),{x:-30})` ·
  `put("#s9-r3", at(9,0.70),{x:-30})` · `put("#s9-v1", at(9,0.95),{scale:0.7})` ·
  `put("#s9-v2", at(9,1.20),{scale:0.7})` · `put("#s9-v3", at(9,1.45),{scale:0.7})`.
- **Rótulo en pantalla:** kicker **«LA PRÁCTICA»**; las tres preguntas (mono) · marcas **«VÍDEO»**.
- **Sonido:** pop 0,20 · pop 0,45 · pop 0,70 · tick 0,95 · tick 1,20 · tick 1,45.
- **Salida:** **desplazamiento continuo ↑ 0,40 s**.

## B10 · El cierre — «Tus clientes ya te dicen qué contenido quieren.»

- **Qué se ve:** papel claro. Cuatro **burbujas de comentarios** llegan con **preguntas que ya han escrito
  tus clientes**; al pie, el chip **«TUS CLIENTES YA PREGUNTAN»**. Las preguntas ya están servidas.
- **Elementos:** `#s10-in` · `#s10-kicker` · `#s10-card` (`.card`) · `#s10-bubbles` (`.bubbles`) ·
  `#s10-b1`, `#s10-b2`, `#s10-b3`, `#s10-b4` (`.cmsg` con `.cbubble`) · `#s10-hint` (`.chip`).
- **Receta (rel):** `rise("#s10-card", at(10,0.0))` · `put("#s10-kicker", at(10,0.06),{dur:0.4})` ·
  `put("#s10-b1", at(10,0.15),{y:24,rot:-2})` · `put("#s10-b2", at(10,0.35),{y:24,rot:2})` ·
  `put("#s10-b3", at(10,0.55),{y:24,rot:-2})` · `put("#s10-b4", at(10,0.75),{y:24,rot:2})` ·
  `put("#s10-hint", at(10,1.00),{y:16})`.
- **Rótulo en pantalla:** kicker **«EL CIERRE»**; chip **«TUS CLIENTES YA PREGUNTAN»**.
- **Sonido:** pop 0,15 · pop 0,35 · pop 0,55 · pop 0,75 · ding 1,00.
- **Salida:** **corte directo** (claro → oscuro).

## B11 · CTA — «Guarda esto y responde al próximo comentario con un vídeo.»

- **Qué se ve:** escena oscura. **Marcador de guardado** grande en acento con la **onda** que se dibuja
  alrededor, el rótulo **«Guarda esto»** y, al pie, el **motivo de la pieza** (burbuja de comentario →
  clip). Cierra la pieza enlazando la CTA con la metáfora.
- **Elementos:** `#s11-in` · `#s11-card` (`.card`) · `#s11-mark` (`.cta-mark`) · `#s11-label`
  (`.cta-label`) · `#s11-wave` (`.savewave`) · `#s11-motif` (`.cmotif` con `.cbubble` + `.replyclip`).
- **Receta (rel):** `rise("#s11-card", at(11,0.0))` · `put("#s11-mark", at(11,0.05),{scale:0.5,dur:0.5})` ·
  `put("#s11-label", at(11,0.55),{scale:0.86,dur:0.5})` · `draw("#s11-wave", at(11,0.95),0.5)` ·
  `put("#s11-motif", at(11,1.45),{scale:0.7})`.
- **Rótulo en pantalla:** **«Guarda esto»** (96 px). Sin kicker.
- **Sonido:** pop 0,05 · ding 0,55 · swoosh_up 0,95 · pop 1,45.
- **Salida:** — (fin).

---

## Recursos

| Recurso | Tipo | Origen |
|---|---|---|
| Fuentes, voz `Pablo`, música, efectos, karaoke, barra de progreso | — | Reutilizado (kit) |
| `.scene`, `.s-in`, `.kicker` (+`.dot`), `.card`, `.chip`, `.pill`, `.tag`, `.tile`, `.rowc` | HTML/CSS | Reutilizado (kit) |
| Marcador de guardado + onda (`.cta-mark`, `.cta-label`, `.savewave`) | HTML/SVG | Reutilizado (kit / GA4) |
| **Móvil con hilo de comentarios** (`.phone`, `.cthread`, `.cmsg`, `.cbubble`) | HTML/CSS | **Nuevo** |
| **Clip-respuesta** (`.replyclip` con `.play`, `.clipbar`) | HTML/CSS/SVG | **Nuevo** |
| **Callout** (`.callout`) y **logotipo de marca** (`.brandmark`), **año** (`.yearbadge`) | HTML/CSS | **Nuevo** (logotipo tipográfico, **autorizado por el dueño (2026-10-12)**) |
| **Cadena de producción** (`.chain`, `.station`, `.chainarrow`, `.sheet`, `.prompter`) | HTML/CSS/SVG | **Nuevo** |
| **Muro de clips** (`.clipgrid`, `.mini`, `.minifocus`) y **cifra** (`.bignum`, `.statlab`) | HTML/CSS | **Nuevo** |
| **Etiquetas de la lección** (`.lesstag`) | HTML/CSS/SVG | **Nuevo** |
| **Set** (`.tripod`, `.sign`, `.strike`) | HTML/CSS/SVG | **Nuevo** |
| **Tienda** (`.store`, `.hanger`, `.chatbar`) | HTML/CSS/SVG | **Nuevo** |
| **Reparto a destinos** (`.fork`, `.destcard`, `.avatars`) | HTML/CSS/SVG | **Nuevo** |
| **Lista de preguntas** (`.qlist`, `.qrow`, `.vmark`) | HTML/CSS/SVG | **Nuevo** |
| **Burbujas sobre claro** (`.bubbles`) y **motivo del cierre** (`.cmotif`) | HTML/CSS | **Nuevo** |
| Capas de transición `.cover` y `.sweep`, recorte `clip-path` | HTML/CSS | **Nuevo** (piezas propias) |
| Collage (manos, personas, objetos) o imágenes de red | PNG | **Descartado**: no hay material y la marca va como logotipo tipográfico |
| Render, vídeo con alfa o 3D | — | No se necesita |

## Ritmo y sonido por beat

| # | Movimiento o lectura | Entrada | Desarrollo | Lectura | Transición | Efectos (rel) |
|---|---|---|---|---|---|---|
| B1 | Movimiento | 0,0-0,4 | 0,4-1,6 | 1,6-fin | 0,35 | whoosh 0,0 · pop 0,60 · swoosh_up 1,15 · ding 2,60 |
| B2 | Movimiento | 0,0-0,4 | 0,4-1,8 | 1,8-fin | 0,45 | pop 0,20 · tick 0,55 · pop 0,95 · pop 1,30 · ding 2,30 |
| B3 | Movimiento | 0,0-0,5 | 0,5-2,4 | 2,4-fin | 0,45 | whoosh 0,0 · tick 0,55 / 1,05 / 1,55 · click 1,80 · ding 2,40 |
| B4 | Movimiento | 0,0-0,4 | 0,4-2,4 | 2,4-fin | 0,40 | pop 0,20 · tick 0,60 · ding 1,20 · pop 1,70 · swoosh_up 2,30 · ding 2,70 |
| B5 | Lectura | 0,0-0,4 | 0,4-1,5 | 1,5-fin | 0,35 | pop 0,25 · pop 0,70 · pop 1,15 · ding 1,70 |
| B6 | Movimiento | 0,0-0,4 | 0,4-1,4 | 1,4-fin | 0,40 | thud 0,25 · pop 0,45 · swoosh_down 1,30 · ding 1,60 |
| B7 | Lectura | 0,0-0,5 | 0,5-2,4 | 2,4-fin | 0,45 | pop 0,20 · pop 0,85 · tick 1,30 · ding 2,80 |
| B8 | Movimiento | 0,0-0,4 | 0,4-1,7 | 1,7-fin | 0,40 | pop 0,20 · swoosh_up 0,75 · pop 1,15 · pop 1,45 · ding 2,00 |
| B9 | Movimiento | 0,0-0,4 | 0,4-1,3 | 1,3-fin | 0,40 | pop 0,20 · pop 0,45 · pop 0,70 · tick 0,95 / 1,20 / 1,45 |
| B10 | Movimiento | 0,0-0,3 | 0,3-1,1 | 1,1-fin | 0,00 | pop 0,15 · pop 0,35 · pop 0,55 · pop 0,75 · ding 1,00 |
| B11 | Lectura | 0,0-0,5 | 0,5-1,4 | 1,4-fin | — | pop 0,05 · ding 0,55 · swoosh_up 0,95 · pop 1,45 |

Se alterna movimiento con lectura: B1 mov · B2 mov · B3 mov · B4 mov · B5 lec · B6 mov · B7 lec ·
B8 mov · B9 mov · B10 mov · B11 lec. **Un efecto por aparición**, nunca por palabra.

---

## Ritmo — tabla medida con la voz real

Total del guion: **121 palabras**. Duración real de la voz (suma de los clips, `assets/voice/timing.json`):
**37,52 s** → **121 / 37,52 ≈ 3,22 palabras/s**. (La estimación previa de 3,5 pal./s era la de V6, D38;
con `Pablo` y sin tocar su velocidad, esta pieza va algo más despacio, a 3,22 pal./s: las frases llevan
más pausas internas.) Los tiempos definitivos los fija `voice_pipeline.py` y los aplica `retime.py`; toda
la animación está en tiempos **relativos** al inicio de su beat.

| Beat | Pal. | Dur. real (s) | Inicio (s) | Fin (s) |
|---|---|---|---|---|
| B1 | 12 | 3,576 | 0,000 | 3,576 |
| B2 | 13 | **4,551** | 3,576 | 8,127 |
| B3 | 14 | 3,855 | 8,127 | 11,982 |
| B4 | 13 | **4,690** | 11,982 | 16,672 |
| B5 | 10 | 3,576 | 16,672 | 20,248 |
| B6 | 8 | 2,601 | 20,248 | 22,849 |
| B7 | 14 | 4,087 | 22,849 | 26,936 |
| B8 | 10 | 2,647 | 26,936 | 29,583 |
| B9 | 9 | 2,461 | 29,583 | 32,044 |
| B10 | 8 | 2,322 | 32,044 | 34,366 |
| B11 | 10 | 3,158 | 34,366 | **37,524** |

**Total: 121 palabras · 37,52 s** (dentro de la banda 30-40 s). **Cuadre:** la suma de palabras de la
tabla es 12+13+14+13+10+8+14+10+9+8+10 = **121** = `assets/voice/*.txt` = carrera del karaoke = `SCRIPT.md`.

**Excepciones de duración (medidas).** La escena más corta mide **2,322 s** (B10; el mínimo del contrato es
1,2 s) y **dos escenas superan el techo de 4,2 s** del contrato §5: **B2 = 4,551 s** y **B4 = 4,690 s**,
por el ritmo real de la voz en esas dos frases (13 palabras, más pausas internas). **No se parten** —la
locución está grabada y no se toca—: misma excepción aceptada en V6 (D38); ver `DECISIONS.md` D39. El resto
queda por debajo de 4,2 s (máximo: B7 = 4,087 s).

**Excepción del beat (medida).** Cinco de las once líneas superan el beat de **6-10 palabras** del
contrato §3: L1 = 12 · L2 = 13 · L3 = 14 · L4 = 13 · L7 = 14 (todas ≤ 14). Es texto dictado por el dueño y
no se redistribuye; ver `DECISIONS.md` D40.

## Reparto de rótulos

| Beat | Kicker (32 px, mayúsculas) | Etiquetas / rótulos en pantalla |
|---|---|---|
| B1 | GANCHO | callout **ESTA MARCA** (acento relleno + tinta) |
| B2 | EL CASO | logotipo **OLD SPICE** (tinta sobre tarjeta clara) · año **2010** |
| B3 | EL MECANISMO | **COMENTARIO / GUION / PROMPTER / CÁMARA** · chip **EN MINUTOS** |
| B4 | LA ESCALA | cifra **186** · **VÍDEOS** · pastilla **6 M · EL DÍA 1** · chip **UNA RESPUESTA, PERSONAL** |
| B5 | LA LECCIÓN | **POR SU NOMBRE / RÁPIDO / CON HUMOR** |
| B6 | TU VERSIÓN | **PRESUPUESTO DE ANUNCIO** (tachado en tinta) · pastilla **SOLO UN MÓVIL** |
| B7 | EL EJEMPLO | **¿Cómo combino esta chaqueta?** (mono, tecleada) |
| B8 | LA DOBLE GANANCIA | **PARA ELLA / PARA EL RESTO** |
| B9 | LA PRÁCTICA | las tres preguntas (mono) · marcas **VÍDEO** |
| B10 | EL CIERRE | chip **TUS CLIENTES YA PREGUNTAN** |
| B11 | — (CTA) | **Guarda esto** (96 px) |

Regla: rótulos **nominales en mayúsculas, sin numerar** (decisión de `DIRECCION.md` §10), **nunca
repiten la voz**. Las preguntas/comentarios van en JetBrains Mono (lo que alguien *escribe*).

## Revisión antes de dar por bueno el vídeo

Un fotograma de lectura de cada escena · los instantes intermedios de las transiciones con
tratamiento especial (`cover` B2→B3 y `sweep` B7→B8; el corte final B10→B11 es directo) · entradas, salidas y
superposiciones · **luminancia y % de filas con contenido del fotograma 0** (miniatura: ≥ 200/255 y
≈ 100 %) · legibilidad a tamaño móvil · alineación de texto e interfaces · sincronía con la voz · y el
MP4 completo en movimiento.
