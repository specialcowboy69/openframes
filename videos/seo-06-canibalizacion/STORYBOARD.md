# STORYBOARD — V6 «Canibalización de palabras clave»

**Sustituye al plan anterior.** La dirección de arte está en `DIRECCION.md` y el brief en
`DIRECCION-ARTE-BRIEF.md`. Pieza: **11 beats · 142 palabras · ~35,7 s** · 1080×1920 · voz `Pablo`.
Formato calcado de `seo-05-intencion-de-busqueda/STORYBOARD.md`.

**Todos los tiempos son RELATIVOS al inicio de su beat** (los absolutos los fija la voz con
`retime.py`). Los identificadores son los del `index.html`; el CSS de los elementos nuevos está en
`DIRECCION.md` §8.

**Regla en las 11 escenas:** el escenario (fondo + ventana / tarjeta / panel / balanza) está visible
desde el fotograma 0 y **solo se asienta** (`rise()`); nace en opacidad 0 solo el contenido. Sin
`.from()`, sin `Math.random`, sin `Date.now`, sin contar hacia arriba (`setNum(sel, txt, t)` fija el
número en saltos discretos). Ayudantes: `put`, `rise`, `draw`, `grow`, `bar`, `typeWords`, `swap`,
`setNum`.

**Consulta de ejemplo única (mono): «instalación de luz»** (B2, B6, B7, B9). En B5 conviven dos
consultas del mismo tema, para ilustrar intenciones distintas: «instalación de luz» (contratar) y
«precio instalación de luz» (informarse). Ejemplo único: página de servicio frente a artículo con
precios (`01-fuentes.md` §6). No se repite «cafetera» ni ninguno de los ejemplos de V1-V3.

---

## B1 · Gancho — «Este error te hará bajar posiciones en Google. No lo hagas.»

- **Qué se ve:** papel claro a pantalla completa (**fotograma 0 = miniatura**). Un **aviso** grande
  —placa `warn` rellena con tinta encima— y una **flecha de posición** que **gira hacia abajo**: bajar
  posiciones es el error real que señala la línea. El aviso, la flecha y el kicker ya están montados
  en el fotograma 0 (nacen visibles en CSS y solo se asientan con `rise()`); lo que se mueve es el
  giro de la flecha y el asentamiento de las piezas, **nada se desvanece ni entra tarde**.
- **Elementos:** `#s1-in` · `#s1-kicker` · `#s1-warn` (`.warnbadge`, `#b3161b` con tinta `#f5f5f7`) ·
  `#s1-arrow` (`.posarrow`, SVG `↓`).
- **Receta (rel):** `rise("#s1-warn", at(1,0.0),{y:20})` · `rise("#s1-arrow", at(1,0.0),{y:20})` ·
  `rise("#s1-kicker", at(1,0.0),{y:20})` ·
  `fromTo("#s1-arrow", {rotation:0}, {rotation:90, dur:0.5, ease:"power2.in"}, at(1,0.35))` →
  `to("#s1-arrow", {rotation:96, dur:0.16}, at(1,0.95))` (giro finito, sin `repeat`/`yoyo`).
- **Rótulo en pantalla:** kicker **«EL ERROR»**; aviso `warn` (relleno con tinta encima); flecha **↓**.
- **Sonido:** whoosh 0,0 (entrada) · pop 0,45 (el aviso) · thud 1,05 (la flecha cae) · buzz 1,90.
- **Salida:** **desplazamiento continuo ↑ 0,35 s**.

## B2 · El fenómeno — «Dos páginas de tu sitio web pueden estar compitiendo por la misma búsqueda.»

- **Qué se ve:** la **balanza de dos platos**: las dos fichas tuyas caen en los platos y, al competir
  por la misma búsqueda, el fiel bascula ±6° sin parar. Debajo, la **barra que se reparte**: dos
  mitades que se reparten, pero el total no sube para nadie.
- **Elementos:** `#s2-in` · `#s2-kicker` · `#s2-balance` (`.scale`) › `#s2-beam` (`.beam` con
  `.plank`, `.pivot`, `.fiel`) › `#s2-seatL`/`#s2-seatR` (`.seat`) · `#s2-a`, `#s2-b` (`.pcard`) ·
  `#s2-split` (`.splitbar`) › `#s2-splitA`, `#s2-splitB` (`.seg.l`/`.seg.r`), `#s2-knob` (`.knob`) ·
  `#s2-cover` (`.cover`, pieza de transición).
- **Receta (rel):** `rise("#s2-balance", at(2,0.0))` · `put("#s2-kicker", at(2,0.06),{dur:0.4})` ·
  `put("#s2-a", at(2,0.18),{y:-30})` · `put("#s2-b", at(2,0.34),{y:-30})` ·
  `fromTo("#s2-beam", {rotation:0}, {rotation:-6, dur:0.45}, at(2,0.55))` →
  `to("#s2-beam", {rotation:6, dur:0.45}, at(2,1.05))` → `to("#s2-beam", {rotation:-3, dur:0.45}, at(2,1.55))`
  (basculación **finita**, nunca `repeat`/`yoyo`) · `bar("#s2-splitA", at(2,0.80), 0.45)` +
  `bar("#s2-splitB", at(2,0.80), 0.55)` · reparto al revés en `at(2,1.40)` (`#s2-splitA`→0,55,
  `#s2-splitB`→0,45 y `#s2-knob` se corre).
- **Rótulo en pantalla:** kicker **«EL FENÓMENO»**; chip mono con la consulta. La barra va sin texto.
- **Sonido:** pop 0,18 y 0,34 (fichas) · thud 0,55 (pesa) · tick 1,40 (reparto).
- **Salida:** **objeto que cubre (`.cover`) 0,45 s** — panel `#20202a` que crece desde la balanza y
  despeja la escena oscura.

## B3 · La consecuencia — «El resultado es que ambas se hunden en los resultados de Google.»

- **Qué se ve:** escena oscura. La **escala de posición** (track vertical) con una marca `warn` que
  intenta subir y vuelve a caer; las **dos fichas se hunden** a la vez y la SERP se queda abajo. La
  caída se marca con **↓**, nunca con un número.
- **Elementos:** `#s3-in` · `#s3-kicker` · `#s3-card` (`.card`, panel `#20202a`) · `#s3-ladder`
  (track vertical + etiqueta «POSICIÓN») · `#s3-mark` (marca, `warn`) · `#s3-pos` (indicador `↓`, mono) ·
  `#s3-a`, `#s3-b` (`.pcard`).
- **Receta (rel):** `rise("#s3-card", at(3,0.0))` · `put("#s3-kicker", at(3,0.06),{dur:0.4})` ·
  `put("#s3-ladder", at(3,0.18),{y:30})` · `put("#s3-mark", at(3,0.45),{y:20})` ·
  `put("#s3-a", at(3,0.45))` · `put("#s3-b", at(3,0.60))` ·
  `fromTo("#s3-mark", {y:0}, {y:-56, dur:0.4}, at(3,0.80))` → `to("#s3-mark", {y:0, dur:0.4}, at(3,1.20))`
  (sube y no sube) · `to("#s3-a", {y:26, dur:0.4}, at(3,1.55))` + `to("#s3-b", {y:26, dur:0.4}, at(3,1.70))`
  (las dos se hunden) · `setNum("#s3-pos","↓", at(3,2.10))`.
- **Rótulo en pantalla:** kicker **«LA CONSECUENCIA»**; anotación **«POSICIÓN»**; indicador **↓**.
- **Sonido:** whoosh 0,0 · thud 0,80 y 1,20 (choca, no sube) · buzz 2,10.
- **Salida:** **revelado circular 0,45 s** (`clip-path` sobre `#s4-in` desde la marca; r ≥ 1500).

## B4 · El nombre — «Eso es lo que llaman la canibalización de palabras clave, y sí tiene arreglo.»

- **Qué se ve:** papel claro. Entra el término en grande (**CANIBALIZACIÓN** / DE PALABRAS CLAVE) y,
  debajo, la balanza **empatada** (beam a 0): las dos fichas siguen igualadas. Una pastilla de acento
  anuncia que **sí tiene arreglo** (prepara B10).
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

## B7 · El ejemplo — «Por ejemplo, tu página de servicio y un artículo de tu blog pueden estar compitiendo por lo mismo.»

- **Qué se ve:** **dos ventanas de navegador** una frente a otra —la página de servicio y el artículo
  del blog— y una consulta común encima. Cada dirección se teclea (mono). Es la línea más larga del
  guion (**18 palabras ≈ 4,52 s**): sigue siendo **un solo beat** (texto expreso del dueño), así que la
  animación se reparte a lo largo de ese tiempo en vez de resolverse en el primer segundo.
- **Elementos:** `#s7-in` · `#s7-kicker` · `#s7-card` (`.card`) · `#s7-q` (`.chip` mono) ·
  `#s7-winA` (`.browser`, `.addr` `/servicios/instalacion-de-luz`) · `#s7-winB` (`.browser`, `.addr`
  `/blog/precio-instalacion-de-luz`) · spans `.w` en cada `.addr`.
- **Receta (rel):** `rise("#s7-card", at(7,0.0))` · `put("#s7-kicker", at(7,0.06),{dur:0.4})` ·
  `put("#s7-q", at(7,0.25),{y:-24})` · `put("#s7-winA", at(7,0.60),{y:40})` ·
  `put("#s7-winB", at(7,1.00),{y:40})` · `typeWords("#s7-winA .w", at(7,1.30), 0.05)` ·
  `typeWords("#s7-winB .w", at(7,1.90), 0.05)`.
- **Rótulo en pantalla:** kicker **«EL EJEMPLO»**; las dos direcciones (mono).
- **Sonido:** pop 0,25 · pop 0,60 y 1,00 · tick 1,30.
- **Salida:** **barrido de color (`.sweep`) 0,45 s** — banda de acento sesgada con `x:0` explícito;
  entra el panel oscuro de Search Console (claro → oscuro).

## B8 · Cómo verlo (1/2) — «Para comprobar si te pasa, abre Search Console.»

- **Qué se ve:** escena oscura con el **panel de Search Console** claro: encabezado **Rendimiento**,
  pestañas **Consultas / Páginas** (activa Páginas) y **dos filas iguales** —dos direcciones tuyas—
  unidas por una marca de duplicado.
- **Elementos:** `#s8-in` · `#s8-kicker` · `#s8-panel` (`.panel` › `.phead`, `#s8-tabs` (`.sctabs`),
  `#s8-r1`, `#s8-r2` (`.prow.dup`), `#s8-dup` (corchete que une las dos filas)) · `#s8-sweep`
  (`.sweep`, pieza de transición entrante).
- **Receta (rel):** `rise("#s8-panel", at(8,0.0))` · `put("#s8-kicker", at(8,0.06),{dur:0.4})` ·
  `put("#s8-tabs", at(8,0.18))` · `put("#s8-r1", at(8,0.50),{x:-30})` · `put("#s8-r2", at(8,0.68),{x:-30})` ·
  `put("#s8-dup", at(8,1.15),{scale:0.8})`.
- **Rótulo en pantalla:** kicker **«CÓMO VERLO»**; encabezado **RENDIMIENTO**; pestañas
  **CONSULTAS / PÁGINAS**; las dos direcciones (mono).
- **Sonido:** pop 0,1 · pop 0,50 y 0,68 · ding 1,15.
- **Salida:** **desplazamiento continuo ↑ 0,40 s** (se sigue en oscuro: B9 mantiene el panel).

## B9 · Cómo verlo (2/2) — «Mira para qué consultas apareces y qué página sale en los resultados.»

- **Qué se ve:** el mismo panel de Search Console, ahora con la **consulta** y **dos URLs tuyas** que
  **se alternan** en la tabla: el resalte pasa de una fila a la otra para ver qué página sale en
  cada momento.
- **Elementos:** `#s9-in` · `#s9-kicker` · `#s9-panel` (`.panel`) › `#s9-tabs` (`.sctabs`, activa
  Consultas) · `#s9-q` (`.chip` mono) · `#s9-rA`, `#s9-rB` (`.prow`, dos URLs tuyas) · `#s9-ta`,
  `#s9-tb` (`.tint`).
- **Receta (rel):** `rise("#s9-panel", at(9,0.0))` · `put("#s9-kicker", at(9,0.06),{dur:0.4})` ·
  `put("#s9-tabs", at(9,0.18))` · `put("#s9-q", at(9,0.40),{y:-20})` · `put("#s9-rA", at(9,0.70),{x:-30})` ·
  `put("#s9-rB", at(9,0.95),{x:-30})` · `#s9-ta` arranca en `opacity:1` (CSS) y `#s9-tb` en 0 ·
  `swap("#s9-ta","#s9-tb", at(9,1.50))` → `at(9,2.10)` → `at(9,2.60)` (tres turnos del resalte).
- **Rótulo en pantalla:** kicker **«CONSULTAS Y PÁGINAS»**; pestañas **CONSULTAS / PÁGINAS** (activa
  Consultas); la consulta y las dos URLs (mono).
- **Sonido:** pop 0,1 · pop 0,40 · pop 0,70 y 0,95 · tick 1,50 / 2,10 / 2,60.
- **Salida:** **desplazamiento continuo ↑ 0,40 s** (oscuro → claro; revisar el fotograma medio).

## B10 · El arreglo — «Arréglalo separando bien las dos intenciones o fusionando las dos páginas en una.»

- **Qué se ve:** dos fichas y una **flecha de fusión** que se **dibuja** hacia una **ficha única
  firme** (lo que aportaba el beat eliminado de «la regla», absorbido aquí); la otra se **atenúa**.
  Dos pastillas dan las dos salidas: **separar intenciones** o **fusionar en una**. No se repite la
  frase «NINGUNA GANA» ni la etiqueta «DEJA SOLO UNA» (serían duplicado del cierre retirado).
- **Elementos:** `#s10-in` · `#s10-kicker` · `#s10-card` (`.card`) · `#s10-a`, `#s10-b` (`.pcard`) ·
  `#s10-fuse` (`.fusearw` con `path`) · `#s10-survivor` (`.pcard.ours`, la ficha única firme) ·
  `#s10-optA`, `#s10-optB` (`.pill`).
- **Receta (rel):** `rise("#s10-card", at(10,0.0))` · `put("#s10-kicker", at(10,0.06),{dur:0.4})` ·
  `put("#s10-a", at(10,0.20),{x:-30})` · `put("#s10-b", at(10,0.35),{x:30})` ·
  `draw("#s10-fuse", at(10,0.75), 0.5)` · `to("#s10-b", {opacity:0.42, x:-40, dur:0.5}, at(10,1.35))` ·
  `put("#s10-survivor", at(10,1.45),{scale:0.7})` · `put("#s10-optA", at(10,2.00),{y:20})` ·
  `put("#s10-optB", at(10,2.35),{y:20})`.
- **Rótulo en pantalla:** kicker **«EL ARREGLO»**; pastillas **«SEPARAR INTENCIONES»** y
  **«FUSIONAR EN UNA»**.
- **Sonido:** pop 0,20 y 0,35 · swoosh_up 0,75 (la flecha) · thud 1,35 (se va una) · ding 2,35.
- **Salida:** **desplazamiento continuo ↑ 0,35 s**.

## B11 · CTA — «Guarda esto antes de escribir o de revisar la próxima página de tu web.»

- **Qué se ve:** escena oscura. **Marcador de guardado** grande en acento con **onda** que se dibuja
  alrededor, el rótulo **«Guarda esto»** y, pequeño, el logo de Google. Cierra la pieza.
- **Elementos:** `#s11-in` · `#s11-card` (`.card`, panel `#20202a`) · `#s11-mark` (`.cta-mark`) ·
  `#s11-label` (`.cta-label`) · `#s11-wave` (`.savewave`) · `#s11-logo` (`.tile.google`).
- **Receta (rel):** `rise("#s11-card", at(11,0.0))` · `put("#s11-mark", at(11,0.05),{scale:0.5,dur:0.5})` ·
  `put("#s11-label", at(11,0.60),{scale:0.86,dur:0.5})` · `draw("#s11-wave", at(11,1.00), 0.5)` ·
  `put("#s11-logo", at(11,1.40),{scale:0.6,dur:0.45})`.
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
| **Placa de aviso** (`.warnbadge`) y **flecha de posición** (`.posarrow`) | HTML/CSS/SVG | **Nuevo** |
| **Tinte de resalte** (`.tint`) | HTML/CSS | **Nuevo** |
| **Flecha de fusión** (`.fusearw`) y **onda de guardado** (`.savewave`) | SVG | **Nuevo** |
| Pestañas y fila duplicada de Search Console (`.sctabs`, `.prow.dup`, `#s8-dup`) | HTML/CSS/SVG | **Nuevo** |
| Capas de transición `.cover` y `.sweep`, recorte `clip-path` | HTML/CSS | **Nuevo** (piezas propias) |
| Collage (manos, personas, objetos) | PNG con transparencia | **Descartado**: no hay material |
| Render, vídeo con alfa o 3D | — | No se necesita |

## Ritmo y sonido por beat

| # | Movimiento o lectura | Entrada | Desarrollo | Lectura | Transición | Efectos (rel) |
|---|---|---|---|---|---|---|
| B1 | Movimiento | 0,0-0,3 | 0,3-1,2 | 1,2-fin | 0,35 | whoosh 0,0 · pop 0,45 · thud 1,05 · buzz 1,90 |
| B2 | Movimiento | 0,0-0,4 | 0,4-1,5 | 1,5-fin | 0,45 | pop 0,18 y 0,34 · thud 0,55 · tick 1,40 |
| B3 | Movimiento | 0,0-0,4 | 0,4-1,8 | 1,8-fin | 0,45 | whoosh 0,0 · thud 0,80 y 1,20 · buzz 2,10 |
| B4 | Lectura | 0,0-0,3 | 0,3-1,7 | 1,7-fin | 0,40 | pop 0,3 y 0,9 · ding 1,7 |
| B5 | Movimiento | 0,0-0,5 | 0,5-1,6 | 1,6-fin | 0,35 | pop 0,5 · 0,95 · 1,25 · 1,55 · ding 1,85 |
| B6 | Movimiento | 0,0-0,5 | 0,5-2,0 | 2,0-fin | 0,40 | pop 0,2 y 0,5 y 0,75 · thud 1,3 · pop 1,7 |
| B7 | Lectura | 0,0-0,5 | 0,5-2,5 | 2,5-fin | 0,45 | pop 0,25 · 0,60 y 1,00 · tick 1,30 |
| B8 | Movimiento | 0,0-0,4 | 0,4-1,1 | 1,1-fin | 0,40 | pop 0,1 · pop 0,50 y 0,68 · ding 1,15 |
| B9 | Lectura | 0,0-0,5 | 0,5-2,0 | 2,0-fin | 0,40 | pop 0,1 · 0,40 · 0,70 y 0,95 · tick 1,50 / 2,10 / 2,60 |
| B10 | Movimiento | 0,0-0,4 | 0,4-2,0 | 2,0-fin | 0,35 | pop 0,20 y 0,35 · swoosh_up 0,75 · thud 1,35 · ding 2,35 |
| B11 | Lectura | 0,0-0,5 | 0,5-1,4 | 1,4-fin | — | pop 0,05 · ding 0,7 · swoosh_up 1,0 |

Se alterna movimiento con lectura: B1 mov · B2 mov · B3 mov · B4 lec · B5 mov · B6 mov · B7 lec ·
B8 mov · B9 lec · B10 mov · B11 lec. **Un efecto por aparición**, nunca por palabra.

---

## Ritmo — tiempos estimados por beat

Estimación de planificación: **142 palabras / 3,98 palabras por segundo = 35,68 s** (velocidad de la
voz oficial; los recuentos por línea están en la tabla de `SCRIPT.md`). Las líneas de 14 palabras
≈ 3,52 s; las de 13 ≈ 3,27 s; las de 12 ≈ 3,02 s; la de 8 ≈ 2,01 s; la de 18 (B7) ≈ 4,52 s.
`retime.py` sustituirá estos valores por los reales de `voice_pipeline.py`; el total objetivo es
**~35-36 s**.

| Beat | Pal. | Dur. estimada | Inicio estimado | Fin estimado |
|---|---|---|---|---|
| B1 | 11 | 2,76 | 0,00 | 2,76 |
| B2 | 13 | 3,27 | 2,76 | 6,03 |
| B3 | 12 | 3,02 | 6,03 | 9,05 |
| B4 | 14 | 3,52 | 9,05 | 12,57 |
| B5 | 14 | 3,52 | 12,57 | 16,09 |
| B6 | 13 | 3,27 | 16,09 | 19,36 |
| B7 | 18 | 4,52 | 19,36 | 23,88 |
| B8 | 8 | 2,01 | 23,88 | 25,89 |
| B9 | 12 | 3,02 | 25,89 | 28,91 |
| B10 | 13 | 3,27 | 28,91 | 32,18 |
| B11 | 14 | 3,52 | 32,18 | **35,70** |

**Total estimado: 35,70 s** (dentro de la banda 30-40 s). Ninguna escena baja de 2,0 s (mínimo del
contrato: 1,2 s). La línea 7 es la única que supera los 4,2 s de referencia: **18 palabras, 4,52 s**,
**un solo beat** por texto expreso del dueño; no se parte ni se reparte.

## Reparto de rótulos

| Beat | Kicker (32 px, mayúsculas) | Etiquetas / rótulos en pantalla |
|---|---|---|
| B1 | EL ERROR | placa de aviso `warn` (relleno, tinta encima) · flecha de posición **↓** |
| B2 | EL FENÓMENO | chip de consulta (mono) |
| B3 | LA CONSECUENCIA | anotación **POSICIÓN** + indicador **↓** |
| B4 | EL NOMBRE | término **CANIBALIZACIÓN DE PALABRAS CLAVE** · pastilla **SÍ TIENE ARREGLO** |
| B5 | EL MATIZ | chips de consulta · etiquetas **CONTRATAR** / **INFORMARSE** |
| B6 | LA CAUSA | pastilla de consulta · **MISMA RESPUESTA** |
| B7 | EL EJEMPLO | direcciones (mono): `/servicios/instalacion-de-luz` · `/blog/precio-instalacion-de-luz` |
| B8 | CÓMO VERLO | encabezado **RENDIMIENTO** · pestañas **CONSULTAS / PÁGINAS** · dos direcciones (mono) |
| B9 | CONSULTAS Y PÁGINAS | la consulta y las dos URLs (mono) · resalte alternando |
| B10 | EL ARREGLO | **SEPARAR INTENCIONES** · **FUSIONAR EN UNA** |
| B11 | — (CTA) | **Guarda esto** (96 px) |

Regla: rótulos **nominales en mayúsculas, sin numerar** (decisión de `DIRECCION.md` §10), **nunca
repiten la voz**. La consulta va siempre en JetBrains Mono.

## Revisión antes de dar por bueno el vídeo

Un fotograma de lectura de cada escena · los instantes intermedios de las tres transiciones con
tratamiento especial (`cover` B2→B3, `circle` B3→B4, `sweep` B7→B8) · entradas,
salidas y superposiciones · **luminancia y % de filas con contenido del fotograma 0** (miniatura:
≥ 200/255 y ≈ 100 %) · legibilidad a tamaño móvil · alineación de texto e interfaces · sincronía con
la voz · y el MP4 completo en movimiento.
