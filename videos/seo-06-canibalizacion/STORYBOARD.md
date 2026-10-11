# STORYBOARD — V6 «Canibalización de palabras clave»

**Sustituye al plan anterior.** La dirección de arte está en `DIRECCION.md` y el brief en
`DIRECCION-ARTE-BRIEF.md`. Pieza: **12 beats · 165 palabras · ~41,5 s** · 1080×1920 · voz `Pablo`.
Formato calcado de `seo-05-intencion-de-busqueda/STORYBOARD.md`.

**Todos los tiempos son RELATIVOS al inicio de su beat** (los absolutos los fija la voz con
`retime.py`). Los identificadores son los del `index.html`; el CSS de los elementos nuevos está en
`DIRECCION.md` §8.

**Regla en las 12 escenas:** el escenario (fondo + ventana / tarjeta / panel / balanza) está visible
desde el fotograma 0 y **solo se asienta** (`rise()`); nace en opacidad 0 solo el contenido. Sin
`.from()`, sin `Math.random`, sin `Date.now`, sin contar hacia arriba (`setNum(sel, txt, t)` fija el
número en saltos discretos). Ayudantes: `put`, `rise`, `draw`, `grow`, `bar`, `typeWords`, `swap`,
`setNum`.

**Consulta de ejemplo única (mono): «instalación de luz»** (B2, B6, B7, B9). En B5 conviven dos
consultas del mismo tema, para ilustrar intenciones distintas: «instalación de luz» (contratar) y
«precio instalación de luz» (informarse). Ejemplo único: página de servicio frente a artículo con
precios (`01-fuentes.md` §6). No se repite «cafetera» ni ninguno de los ejemplos de V1-V3.

---

## B1 · Gancho — «Un día Google muestra una página tuya en los resultados y al siguiente, otra.»

- **Qué se ve:** papel claro a pantalla completa. Ventana de navegador con la consulta y, debajo, la
  SERP con **dos fichas tuyas** resaltadas y el resto en esqueleto. Un distintivo **«TURNO»** salta de
  una ficha a la otra y el tinte verde se enciende en la activa: se están turnando. Nada de pantalla
  vacía: la ventana, la consulta y las dos fichas ya están en el fotograma 0 (nacen visibles en CSS y
  solo se asientan con `rise()`); lo único que se anima es el turno.
- **Elementos:** `#s1-in` · `#s1-kicker` · `#s1-win` (`.browser` › `.chrome`/`.lights`/`.addr`) ·
  `#s1-q` (`.q`, mono) · `#s1-list` (`.serpbody`) · `#s1-oa`, `#s1-ob` (`.pcard.ours`) ·
  `#s1-ta`, `#s1-tb` (`.tint`) · `#s1-markA`, `#s1-markB` (`.turnmark`) · `#s1-sk1..3` (esqueletos).
- **Receta (rel):** `rise("#s1-win", at(1,0.0))` · `put("#s1-kicker", at(1,0.06),{dur:0.4})` ·
  `rise("#s1-q", at(1,0.0),{y:14,dur:0.35})` · `rise("#s1-oa", at(1,0.0),{y:24})` ·
  `rise("#s1-ob", at(1,0.0),{y:24})` · `#s1-ta` arranca en `opacity:1` (CSS) y `#s1-tb` en 0 ·
  `put("#s1-markA", at(1,0.70),{scale:0.7,dur:0.35})` · `swap("#s1-ta","#s1-tb", at(1,1.10))` +
  `swap("#s1-markA","#s1-markB", at(1,1.10))` · vuelven a cambiar en `at(1,2.00)`.
- **Rótulo en pantalla:** kicker **«EN GOOGLE»**; distintivo **«TURNO»**.
- **Sonido:** whoosh 0,0 (entrada) · pop 0,7 (el distintivo «TURNO») · tick 1,1 · tick 2,0 (los turnos).
- **Salida:** **desplazamiento continuo ↑ 0,35 s**.

## B2 · El fenómeno — «Las dos compiten por la misma búsqueda y se acaban quitando fuerza entre ellas.»

- **Qué se ve:** la **balanza de dos platos**; las dos fichas caen en los platos y el beam bascula
  ±6° sin parar. Debajo, la **barra que se reparte**: dos mitades que se reparten la «fuerza» y se la
  vuelven a repartir, pero el total no sube para nadie.
- **Elementos:** `#s2-in` · `#s2-kicker` · `#s2-balance` (`.scale`) › `#s2-beam` (`.beam` con
  `.plank`, `.pivot`, `.fiel`) › `#s2-seatL`/`#s2-seatR` (`.seat`) · `#s2-a`, `#s2-b` (`.pcard`) ·
  `#s2-split` (`.splitbar`) › `#s2-splitA`, `#s2-splitB` (`.seg.l`/`.seg.r`), `#s2-knob` (`.knob`) ·
  `#s2-cover` (`.cover`, pieza de transición).
- **Receta (rel):** `rise("#s2-balance", at(2,0.0))` · `put("#s2-kicker", at(2,0.06),{dur:0.4})` ·
  `put("#s2-a", at(2,0.20),{y:-30})` · `put("#s2-b", at(2,0.40),{y:-30})` ·
  `fromTo("#s2-beam", {rotation:0}, {rotation:-6, dur:0.5}, at(2,0.70))` →
  `to("#s2-beam", {rotation:6, dur:0.5}, at(2,1.30))` → `to("#s2-beam", {rotation:-3, dur:0.5}, at(2,1.90))`
  (basculación **finita**, nunca `repeat`/`yoyo`) · `bar("#s2-splitA", at(2,0.90), 0.45)` +
  `bar("#s2-splitB", at(2,0.90), 0.55)` · reparto al revés en `at(2,1.60)` (`#s2-splitA`→0,55,
  `#s2-splitB`→0,45 y `#s2-knob` se corre).
- **Rótulo en pantalla:** kicker **«EL FENÓMENO»**; chip mono con la consulta. La barra va sin texto.
- **Sonido:** pop 0,2 y 0,4 (fichas) · thud 0,7 (pesa) · tick 1,6 (reparto).
- **Salida:** **objeto que cubre (`.cover`) 0,45 s** — panel `#20202a` que crece desde la balanza y
  despeja la escena oscura.

## B3 · La consecuencia — «Y el resultado es que ninguna de las dos consigue la posición que podría.»

- **Qué se ve:** escena oscura. Una escala vertical de **posición** y una marca que **intenta subir
  y vuelve a caer, dos veces**; las dos fichas se quedan abajo; el indicador de posición cae y no
  sube. Es la lectura de «no consigue la posición que podría». Sin cifras: la caída se marca con un
  **↓**, no con un número.
- **Elementos:** `#s3-in` · `#s3-kicker` · `#s3-card` (`.card`, panel `#20202a`) · `#s3-ladder`
  (track vertical + etiqueta «POSICIÓN») · `#s3-mark` (marca, `warn`) · `#s3-pos` (indicador `↓`, mono) ·
  `#s3-a`, `#s3-b` (`.pcard`).
- **Receta (rel):** `rise("#s3-card", at(3,0.0))` · `put("#s3-kicker", at(3,0.06),{dur:0.4})` ·
  `put("#s3-ladder", at(3,0.20),{y:30})` · `put("#s3-mark", at(3,0.50),{y:20})` ·
  `fromTo("#s3-mark", {y:0}, {y:-60, dur:0.5}, at(3,0.90))` → `to("#s3-mark", {y:0, dur:0.5}, at(3,1.40))`
  (primer intento fallido) · segundo intento `at(3,1.90)`/`at(3,2.50)` · `put("#s3-a", at(3,1.00))` ·
  `put("#s3-b", at(3,1.15))` · `setNum("#s3-pos","↓", at(3,2.60))`.
- **Rótulo en pantalla:** kicker **«LA CONSECUENCIA»**; anotación **«POSICIÓN»**; indicador **↓**.
- **Sonido:** whoosh 0,0 · thud 0,9 y 1,9 (choca, no sube) · buzz 2,6.
- **Salida:** **revelado circular 0,45 s** (`clip-path` sobre `#s4-in` desde la marca; r ≥ 1500).

## B4 · El nombre — «Eso es lo que llaman la canibalización de palabras clave, y sí tiene arreglo.»

- **Qué se ve:** papel claro. Entra el término en grande (**CANIBALIZACIÓN** / DE PALABRAS CLAVE) y,
  debajo, la balanza **empatada** (beam a 0): las dos fichas siguen igualadas. Una pastilla de acento
  anuncia que **sí tiene arreglo** (prepara B10-B11).
- **Elementos:** `#s4-in` · `#s4-kicker` · `#s4-card` (`.card`) · `#s4-term` (`.title`, spans
  `.w`) · `#s4-sub` · `#s4-balance` (`.scale` mini) › `#s4-beam` · `#s4-fix` (`.pill accent`).
- **Receta (rel):** `rise("#s4-card", at(4,0.0))` · `put("#s4-kicker", at(4,0.06),{dur:0.4})` ·
  `typeWords("#s4-term .w", at(4,0.30), 0.06)` · `put("#s4-sub", at(4,0.90),{y:30})` ·
  `rise("#s4-balance", at(4,0.50))` · `fromTo("#s4-beam", {rotation:-4}, {rotation:0, dur:0.6}, at(4,1.10))`
  (queda **empatada**) · `put("#s4-fix", at(4,1.70),{scale:0.86})`.
- **Rótulo en pantalla:** kicker **«EL NOMBRE»**; el término; pastilla **«SÍ TIENE ARREGLO»**.
- **Sonido:** pop 0,3 (término) · pop 0,9 · ding 1,7 (`sí tiene arreglo`).
- **Salida:** **desplazamiento continuo ↑ 0,40 s**.

## B5 · El matiz — «Dos páginas tuyas pueden tratar el mismo tema sin competir, si buscan cosas distintas.»

- **Qué se ve:** dos fichas que empiezan solapadas y **se separan**; cada una con **su propia
  consulta** del mismo tema (`#s5-qa` «instalación de luz», de contratar; `#s5-qb` «precio
  instalación de luz», de informarse) y su etiqueta. Al buscar cosas distintas, no compiten.
- **Elementos:** `#s5-in` · `#s5-kicker` · `#s5-card` (`.card`) · `#s5-a`, `#s5-b` (`.pcard`) ·
  `#s5-qa` («instalación de luz») · `#s5-qb` («precio instalación de luz») (`.chip` mono) ·
  `#s5-la` (`.tag`, «CONTRATAR») · `#s5-lb` (`.tag`, «INFORMARSE»).
- **Receta (rel):** `rise("#s5-card", at(5,0.0))` · `put("#s5-kicker", at(5,0.06),{dur:0.4})` ·
  `fromTo("#s5-a", {x:0}, {x:-44, dur:0.6}, at(5,0.30))` · `fromTo("#s5-b", {x:0}, {x:44, dur:0.6}, at(5,0.40))` ·
  `put("#s5-qa", at(5,0.50),{y:-20})` · `put("#s5-qb", at(5,0.95),{y:-20})` ·
  `put("#s5-la", at(5,1.25),{scale:0.8})` · `put("#s5-lb", at(5,1.55),{scale:0.8})`.
- **Rótulo en pantalla:** kicker **«EL MATIZ»**; chips **«instalación de luz»** y **«precio
  instalación de luz»**; etiquetas **CONTRATAR** / **INFORMARSE** (distintas de las de V5).
- **Sonido:** pop 0,5 y 0,95 (consultas) · pop 1,25 y 1,55 (etiquetas) · ding 1,85.
- **Salida:** **desplazamiento continuo ↑ 0,35 s**.

## B6 · La causa — «Compiten cuando las dos páginas ofrecen la misma respuesta a la misma consulta.»

- **Qué se ve:** una pastilla con la consulta y, debajo, **dos fichas que convergen hasta
  superponerse**; el **solape** se resalta (la «misma respuesta»). Esa coincidencia es la causa.
- **Elementos:** `#s6-in` · `#s6-kicker` · `#s6-card` (`.card`) · `#s6-qpill` (`.chip accent`) ·
  `#s6-a`, `#s6-b` (`.pcard`) · `#s6-overlap` (bloque de solape) · `#s6-lab` (`.tag`,
  «MISMA RESPUESTA»).
- **Receta (rel):** `rise("#s6-card", at(6,0.0))` · `put("#s6-kicker", at(6,0.06),{dur:0.4})` ·
  `put("#s6-qpill", at(6,0.20),{y:-24})` · `put("#s6-a", at(6,0.50),{x:-30})` ·
  `put("#s6-b", at(6,0.75),{x:30})` · convergen en `at(6,1.30)` (`#s6-a`→x 18, `#s6-b`→x −18) ·
  `put("#s6-overlap", at(6,1.70),{scale:0.7})` · `put("#s6-lab", at(6,2.00),{y:20})`.
- **Rótulo en pantalla:** kicker **«LA CAUSA»**; pastilla con la consulta; **«MISMA RESPUESTA»**.
- **Sonido:** pop 0,2 · pop 0,5 y 0,75 · thud 1,3 (encaja el solape) · pop 1,7.
- **Salida:** **desplazamiento continuo ↑ 0,40 s**.

## B7 · El ejemplo — «Tu página de servicio y un artículo tuyo compiten por la misma búsqueda.»

- **Qué se ve:** **dos ventanas de navegador** una frente a otra —la página de servicio y el artículo—
  y una consulta común encima. Cada dirección se teclea (mono).
- **Elementos:** `#s7-in` · `#s7-kicker` · `#s7-card` (`.card`) · `#s7-q` (`.chip` mono) ·
  `#s7-winA` (`.browser`, `.addr` `/servicios/instalacion-de-luz`) · `#s7-winB` (`.browser`, `.addr`
  `/blog/precio-instalacion-de-luz`) · spans `.w` en cada `.addr`.
- **Receta (rel):** `rise("#s7-card", at(7,0.0))` · `put("#s7-kicker", at(7,0.06),{dur:0.4})` ·
  `put("#s7-q", at(7,0.20),{y:-24})` · `put("#s7-winA", at(7,0.50),{y:40})` ·
  `put("#s7-winB", at(7,0.80),{y:40})` · `typeWords("#s7-winA .w", at(7,1.00), 0.05)` ·
  `typeWords("#s7-winB .w", at(7,1.40), 0.05)`.
- **Rótulo en pantalla:** kicker **«EL EJEMPLO»**; las dos direcciones (mono).
- **Sonido:** pop 0,2 · pop 0,5 y 0,8 · tick 1,1.
- **Salida:** **continuidad por forma 0,45 s** — `#s7-winB` termina coincidiendo con `#s8-win`.

## B8 · El resultado — «Google alterna entre las dos y ninguna de ellas acaba en la primera posición.»

- **Qué se ve:** la SERP con la consulta; arriba, el primer puesto (ajeno) y, debajo, **tus dos
  fichas**, con el tinte de resalte **pasando de una a la otra** varias veces. Ninguna sube: las dos
  se quedan por debajo del primero.
- **Elementos:** `#s8-in` · `#s8-kicker` · `#s8-win` (`.browser` › `.serpbody`) · `#s8-top`
  (`.result`) · `#s8-pa`, `#s8-pb` (`.pcard.ours`) · `#s8-ta`, `#s8-tb` (`.tint`).
- **Receta (rel):** `rise("#s8-win", at(8,0.0))` · `put("#s8-kicker", at(8,0.06),{dur:0.4})` ·
  `put("#s8-top", at(8,0.15))` · `put("#s8-pa", at(8,0.30),{y:22})` · `put("#s8-pb", at(8,0.55),{y:22})` ·
  `#s8-ta` arranca en `opacity:1` · `swap("#s8-ta","#s8-tb", at(8,1.10))` → `at(8,1.80)` →
  `at(8,2.50)` (tres turnos, sin que ninguno llegue arriba).
- **Rótulo en pantalla:** kicker **«EL RESULTADO»** (la SERP no lleva etiquetas de intención: eso era
  de V5).
- **Sonido:** pop 0,15 y 0,3 · tick 1,1 / 1,8 / 2,5 (los turnos) · thud 2,7.
- **Salida:** **barrido de color (`.sweep`) 0,45 s** — banda de acento sesgada, `x:0` explícito.

## B9 · Cómo verlo — «En Search Console puedes ver dos páginas tuyas compitiendo por la misma búsqueda.»

- **Qué se ve:** escena oscura con el **panel de Search Console** claro: encabezado **Rendimiento**,
  pestañas **Consultas / Páginas** (activa Páginas) y **dos filas iguales** —dos direcciones tuyas—
  unidas por una marca de duplicado.
- **Elementos:** `#s9-in` · `#s9-kicker` · `#s9-panel` (`.panel` › `.phead`, `#s9-tabs`
  (`.sctabs`), `#s9-q` (`.chip` mono), `#s9-r1`, `#s9-r2` (`.prow.dup`), `#s9-dup` (marca de
  duplicado)) · `#s9-sweep` (`.sweep`, pieza de transición entrante).
- **Receta (rel):** `rise("#s9-panel", at(9,0.0))` · `put("#s9-kicker", at(9,0.06),{dur:0.4})` ·
  `put("#s9-tabs", at(9,0.20))` · `put("#s9-q", at(9,0.40))` · `put("#s9-r1", at(9,0.70),{x:-30})` ·
  `put("#s9-r2", at(9,0.90),{x:-30})` · `put("#s9-dup", at(9,1.60),{scale:0.8})`.
- **Rótulo en pantalla:** kicker **«CÓMO VERLO»**; encabezado **RENDIMIENTO**; pestañas
  **CONSULTAS / PÁGINAS**; las dos direcciones (mono).
- **Sonido:** pop 0,2 y 0,4 · pop 0,7 y 0,9 · ding 1,6.
- **Salida:** **desplazamiento continuo ↑ 0,40 s** (revisar el fotograma medio: se sale de oscuro).

## B10 · El arreglo — «Se arregla separando bien las dos intenciones o fusionando las dos páginas en una.»

- **Qué se ve:** dos fichas y una **flecha de fusión** que se **dibuja** hacia una superviviente; la
  otra se **atenúa**. Dos pastillas dan las dos salidas: **separar intenciones** o **fusionar en una**.
- **Elementos:** `#s10-in` · `#s10-kicker` · `#s10-card` (`.card`) · `#s10-a`, `#s10-b` (`.pcard`) ·
  `#s10-fuse` (`.fusearw` con `path`) · `#s10-survivor` (`.pcard.ours`) · `#s10-optA`, `#s10-optB`
  (`.pill`).
- **Receta (rel):** `rise("#s10-card", at(10,0.0))` · `put("#s10-kicker", at(10,0.06),{dur:0.4})` ·
  `put("#s10-a", at(10,0.20),{x:-30})` · `put("#s10-b", at(10,0.35),{x:30})` ·
  `draw("#s10-fuse", at(10,0.80), 0.5)` · `to("#s10-b", {opacity:0.42, dur:0.5}, at(10,1.40))` ·
  `put("#s10-survivor", at(10,1.50),{scale:0.7})` · `put("#s10-optA", at(10,2.00),{y:20})` ·
  `put("#s10-optB", at(10,2.35),{y:20})`.
- **Rótulo en pantalla:** kicker **«EL ARREGLO»**; pastillas **«SEPARAR INTENCIONES»** y
  **«FUSIONAR EN UNA»**.
- **Sonido:** pop 0,2 y 0,35 · swoosh_up 0,8 (la flecha) · pop 1,5 · ding 2,35.
- **Salida:** **desplazamiento continuo ↑ 0,35 s**.

## B11 · La regla — «Dos páginas tuyas compitiendo por lo mismo: ninguna gana, así que deja solo una.»

- **Qué se ve:** papel claro. La frase **NINGUNA GANA** y, debajo, **una sola ficha firme**; la otra
  se retira. La balanza vuelve, pequeña, con **un plato vacío** (callback de la metáfora). Cierra con
  la regla.
- **Elementos:** `#s11-in` · `#s11-kicker` · `#s11-card` (`.card`) · `#s11-rule` (`.title`, spans
  `.w`) · `#s11-card1` (`.pcard.ours`, la superviviente) · `#s11-card2` (`.pcard`, la que se va) ·
  `#s11-balance` (`.scale` mini) › `#s11-beam` · `#s11-survivor-tag` (`.pill`, «DEJA SOLO UNA»).
- **Receta (rel):** `rise("#s11-card", at(11,0.0))` · `put("#s11-kicker", at(11,0.06),{dur:0.4})` ·
  `typeWords("#s11-rule .w", at(11,0.20), 0.06)` · `put("#s11-card1", at(11,0.60),{scale:0.8})` ·
  `to("#s11-card2", {opacity:0, x:-40, dur:0.5}, at(11,0.90))` · `rise("#s11-balance", at(11,0.40))` ·
  `fromTo("#s11-beam", {rotation:4}, {rotation:-6, dur:0.6}, at(11,1.10))` (un plato se vacía) ·
  `put("#s11-survivor-tag", at(11,1.50),{scale:0.8})`.
- **Rótulo en pantalla:** kicker **«LA REGLA»**; frase **NINGUNA GANA**; pastilla **«DEJA SOLO UNA»**.
- **Sonido:** pop 0,2 · thud 0,9 (se va una) · ding 1,5.
- **Salida:** **desplazamiento continuo ↑ 0,40 s** (`cut 0,00` es la alternativa).

## B12 · CTA — «Guarda esto antes de escribir o de revisar la próxima página de tu web.»

- **Qué se ve:** escena oscura. **Marcador de guardado** grande en acento con **onda** que se dibuja
  alrededor, el rótulo **«Guarda esto»** y, pequeño, el logo de Google. Cierra la pieza.
- **Elementos:** `#s12-in` · `#s12-card` (`.card`, panel `#20202a`) · `#s12-mark` (`.cta-mark`) ·
  `#s12-label` (`.cta-label`) · `#s12-wave` (`.savewave`) · `#s12-logo` (`.tile.google`).
- **Receta (rel):** `rise("#s12-card", at(12,0.0))` · `put("#s12-mark", at(12,0.05),{scale:0.5,dur:0.5})` ·
  `put("#s12-label", at(12,0.60),{scale:0.86,dur:0.5})` · `draw("#s12-wave", at(12,1.00), 0.5)` ·
  `put("#s12-logo", at(12,1.40),{scale:0.6,dur:0.45})`.
- **Rótulo en pantalla:** **«Guarda esto»** (96 px).
- **Sonido:** pop 0,05 · ding 0,7 · swoosh_up 1,0.
- **Salida:** — (fin).

---

## Recursos

| Recurso | Tipo | Origen |
|---|---|---|
| Ventana de navegador, chrome, semáforo, candado, barra de direcciones | HTML/CSS | Reutilizado (kit) |
| Tarjeta de resultado, SERP, esqueletos, cursor, barra de progreso, kicker, CTA, tiles | HTML/CSS | Reutilizado (kit) |
| Panel de datos, filas, pestañas, logo de Google, iconos lupa/check/marcador/flecha | HTML/SVG | Reutilizado (GA4 / kit) |
| **Balanza de dos platos** (`.scale` › `.beam`/`.pivot`/`.fiel`/`.seat`) | HTML/CSS | **Nuevo** |
| **Escala de posición** (`.ladder` › `.lab`/`.mark`/`.pos`) | HTML/CSS | **Nuevo** |
| **Barra que se reparte** (`.splitbar` › `.seg.l`/`.seg.r`/`.knob`) | HTML/CSS | **Nuevo** |
| **Ficha de página** (`.pcard`, `.pcard.ours`, `.pcard.faded`) | HTML/CSS | **Nuevo** |
| **Tinte de turno** (`.tint`) y distintivo **«TURNO»** (`.turnmark`) | HTML/CSS | **Nuevo** |
| **Flecha de fusión** (`.fusearw`) y **onda de guardado** (`.savewave`) | SVG | **Nuevo** |
| Pestañas y fila duplicada de Search Console (`.sctabs`, `.prow.dup`, `#s9-dup`) | HTML/CSS/SVG | **Nuevo** |
| Capas de transición `.cover` y `.sweep`, recorte `clip-path` | HTML/CSS | **Nuevo** (piezas propias) |
| Collage (manos, personas, objetos) | PNG con transparencia | **Descartado**: no hay material |
| Render, vídeo con alfa o 3D | — | No se necesita |

## Ritmo y sonido por beat

| # | Movimiento o lectura | Entrada | Desarrollo | Lectura | Transición | Efectos (rel) |
|---|---|---|---|---|---|---|
| B1 | Movimiento | 0,0-0,4 | 0,4-1,6 | 1,6-2,4 | 0,35 | whoosh 0,0 · pop 0,7 · tick 1,1 y 2,0 |
| B2 | Movimiento | 0,0-0,4 | 0,4-1,9 | 1,9-2,6 | 0,45 | pop 0,2 y 0,4 · thud 0,7 · tick 1,6 |
| B3 | Movimiento | 0,0-0,5 | 0,5-2,5 | 2,5-fin | 0,45 | whoosh 0,0 · thud 0,9 y 1,9 · buzz 2,6 |
| B4 | Lectura | 0,0-0,3 | 0,3-1,7 | 1,7-fin | 0,40 | pop 0,3 y 0,9 · ding 1,7 |
| B5 | Movimiento | 0,0-0,5 | 0,5-1,6 | 1,6-fin | 0,35 | pop 0,5 · 0,95 · 1,25 · 1,55 · ding 1,85 |
| B6 | Movimiento | 0,0-0,5 | 0,5-2,0 | 2,0-fin | 0,40 | pop 0,2 y 0,5 y 0,75 · thud 1,3 · pop 1,7 |
| B7 | Lectura | 0,0-0,5 | 0,5-1,6 | 1,6-fin | 0,45 | pop 0,2 · 0,5 · 0,8 · tick 1,1 |
| B8 | Movimiento | 0,0-0,6 | 0,6-2,5 | 2,5-fin | 0,45 | pop 0,15 y 0,3 · tick 1,1/1,8/2,5 · thud 2,7 |
| B9 | Lectura | 0,0-0,4 | 0,4-1,6 | 1,6-fin | 0,40 | pop 0,2 y 0,4 · pop 0,7 y 0,9 · ding 1,6 |
| B10 | Movimiento | 0,0-0,4 | 0,4-1,5 | 1,5-fin | 0,35 | pop 0,2 y 0,35 · swoosh_up 0,8 · pop 1,5 · ding 2,35 |
| B11 | Lectura | 0,0-0,4 | 0,4-1,5 | 1,5-fin | 0,40 | pop 0,2 · thud 0,9 · ding 1,5 |
| B12 | Lectura | 0,0-0,5 | 0,5-1,4 | 1,4-fin | — | pop 0,05 · ding 0,7 · swoosh_up 1,0 |

Se alterna movimiento con lectura: B1 mov · B2 mov · B3 mov · B4 lec · B5 mov · B6 mov · B7 lec ·
B8 mov · B9 lec · B10 mov · B11 lec · B12 lec. **Un efecto por aparición**, nunca por palabra.

---

## Ritmo — tiempos estimados por beat

Estimación de planificación: **165 palabras / 3,98 palabras por segundo = 41,46 s** (velocidad de la
voz oficial). Las líneas de 14 palabras ≈ 3,52 s; las de 13 ≈ 3,27 s. `retime.py` sustituirá estos
valores por los reales de `voice_pipeline.py`; el total objetivo es **~41-42 s**.

| Beat | Pal. | Dur. estimada | Inicio estimado | Fin estimado |
|---|---|---|---|---|
| B1 | 14 | 3,52 | 0,00 | 3,52 |
| B2 | 14 | 3,52 | 3,52 | 7,04 |
| B3 | 14 | 3,52 | 7,04 | 10,55 |
| B4 | 14 | 3,52 | 10,55 | 14,07 |
| B5 | 14 | 3,52 | 14,07 | 17,59 |
| B6 | 13 | 3,27 | 17,59 | 20,85 |
| B7 | 13 | 3,27 | 20,85 | 24,12 |
| B8 | 14 | 3,52 | 24,12 | 27,64 |
| B9 | 13 | 3,27 | 27,64 | 30,90 |
| B10 | 14 | 3,52 | 30,90 | 34,42 |
| B11 | 14 | 3,52 | 34,42 | 37,94 |
| B12 | 14 | 3,52 | 37,94 | **41,46** |

**Total estimado: 41,46 s** (margen hasta ~41-42 s). Ninguna escena baja de 3,2 s (mínimo del
contrato: 1,2 s) ni supera 4,2 s, así que no hay que partir ni repartir ninguna línea.

## Reparto de rótulos

| Beat | Kicker (32 px, mayúsculas) | Etiquetas / rótulos en pantalla |
|---|---|---|
| B1 | EN GOOGLE | distintivo **TURNO** |
| B2 | EL FENÓMENO | chip de consulta (mono) |
| B3 | LA CONSECUENCIA | anotación **POSICIÓN** + indicador **↓** |
| B4 | EL NOMBRE | término **CANIBALIZACIÓN DE PALABRAS CLAVE** · pastilla **SÍ TIENE ARREGLO** |
| B5 | EL MATIZ | chips de consulta · etiquetas **CONTRATAR** / **INFORMARSE** |
| B6 | LA CAUSA | pastilla de consulta · **MISMA RESPUESTA** |
| B7 | EL EJEMPLO | direcciones (mono): `/servicios/instalacion-de-luz` · `/blog/precio-instalacion-de-luz` |
| B8 | EL RESULTADO | — (la SERP no lleva etiquetas) |
| B9 | CÓMO VERLO | encabezado **RENDIMIENTO** · pestañas **CONSULTAS / PÁGINAS** · dos direcciones (mono) |
| B10 | EL ARREGLO | **SEPARAR INTENCIONES** · **FUSIONAR EN UNA** |
| B11 | LA REGLA | **NINGUNA GANA** · pastilla **DEJA SOLO UNA** |
| B12 | — (CTA) | **Guarda esto** (96 px) |

Regla: rótulos **nominales en mayúsculas, sin numerar** (decisión de `DIRECCION.md` §10), **nunca
repiten la voz**. La consulta va siempre en JetBrains Mono.

## Revisión antes de dar por bueno el vídeo

Un fotograma de lectura de cada escena · los instantes intermedios de las cuatro transiciones con
tratamiento especial (`cover` B2→B3, `circle` B3→B4, `forma` B7→B8, `sweep` B8→B9) · entradas,
salidas y superposiciones · **luminancia y % de filas con contenido del fotograma 0** (miniatura:
≥ 200/255 y ≈ 100 %) · legibilidad a tamaño móvil · alineación de texto e interfaces · sincronía con
la voz · y el MP4 completo en movimiento.
