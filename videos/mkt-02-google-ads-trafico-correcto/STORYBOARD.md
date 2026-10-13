# STORYBOARD — mkt-02 «El tráfico correcto (Google Job Experiment, 2010)»

Serie **Casos de estudio marketing** · Pieza **mkt-02** · **11 beats · 123 palabras · ≈38,4 s** ·
1080×1920 · faceless · voz en off es-ES (`Pablo`) · subtítulos karaoke. La dirección de arte está en
`DIRECCION.md` y el brief en `DIRECCION-ARTE-BRIEF.md`. Formato calcado de
`mkt-01-responde-con-video/STORYBOARD.md`.

**Todos los tiempos son RELATIVOS al inicio de su beat** (los absolutos los fija la voz con
`retime.py`). Los identificadores son los del `index.html`; el CSS de los elementos nuevos está en
`DIRECCION.md` §8.

**Regla en las 11 escenas:** el escenario (barra de búsqueda / tarjeta / blanco / lista / anuncio /
panel) está visible desde el fotograma 0 y **solo se asienta** (`rise()`); nace en opacidad 0 solo el
contenido. Sin `.from()`, sin `Math.random`, sin `Date.now`, sin contar hacia arriba (`setNum(sel,
txt, t)` fija el número en un salto discreto). Ayudantes: `put`, `rise`, `draw`, `grow`, `bar`,
`typeWords`, `typeChars`, `swap`, `setNum`. Los elementos que se revelan llevan la clase del kit
`.fade-in` (estado inicial en CSS); el resto usa `fromTo`/`.to()`.

**Recurso propio:** **el blanco (la mira) y su barra de búsqueda**, con el anuncio que brota al
teclear un nombre. No se reutiliza la **burbuja de comentario** de `mkt-01`, la **SERP etiquetada** de
V5 ni la **balanza** de V6. **Ejemplo único:** «abogado»/«dentista» (B9), el negocio del espectador.
**La pieza no usa rojo**: no hay pérdida ni error real.

---

## Desviaciones justificadas del contrato

- **Banda segura (`.s-in`).** El contrato §3 fija `padding: 300px 74px 470px`; esta pieza usa
  **`padding: 300px 74px 700px`** (`index.html`), igual que `mkt-01`. Se subió a propósito para que el
  bloque de contenido **no quede bajo la píldora del karaoke** (la píldora va a `bottom:470` y ocupa
  ~y 1230-1450). Es una desviación **solo de margen y más conservadora** que el contrato: no viola la
  banda segura 15-75 % (288-1440).
- **Escenas largas (estimadas).** A **3,2 pal./s** (ritmo real de `Pablo` medido en `mkt-01`), **B3 y
  B9** (14 palabras cada una) dan **≈4,375 s**, por encima del techo de **4,2 s** del contrato §5. **No
  se parten** —la locución la fija `voice_pipeline.py` y el guion es del dueño—: misma situación
  aceptada en `mkt-01` (D39) y en V6 (D38). Si la voz medida deja esos beats por debajo de 4,2 s, la
  excepción desaparece.
- **Beats de más de 10 palabras (del dueño).** Siete de las once líneas superan el beat de 6-10
  palabras del contrato §3: L3 (14) · L4 (13) · L5 (13) · L7 (11) · L9 (14) · L10 (12) · L11 (12),
  todas **≤ 14**. Es texto dictado por el dueño y no se redistribuye; ver `DECISIONS.md` D40.

---

## B1 · Gancho — «¿Cuántos contactos podrías conseguir con 6 euros en Google Ads?»

- **Qué se ve:** papel claro a pantalla completa (**fotograma 0 = miniatura**). Una **barra de
  búsqueda** montada **sobre el blanco** (los anillos de la mira, en contraste bajo): buscar es
  *apuntar*. Colgada de la barra, la cifra **`6 €`** en una placa de acento, y bajo la barra el rótulo
  **«EN GOOGLE ADS»**. La barra, la cifra, el rótulo y el kicker están montados **desde el fotograma
  0** y solo se asientan (`rise()`); la cifra da un **salto discreto** (`scale`, sin tocar opacidad)
  para marcar el gancho: **nada se desvanece ni entra tarde**.
- **Elementos:** `#s1-in` · `#s1-kicker` (`.kicker`) · `#s1-blank` (`.blanco`, fondo) · `#s1-search`
  (`.searchbar`, con `.sicon` y `.shint`) · `#s1-eur` (`.eurmark` «6 €», acento relleno) · `#s1-label`
  (`.chip` «EN GOOGLE ADS», sin acento: el único acento del gancho es la placa «6 €»).
- **Receta (rel):** `rise("#s1-blank", at(1,0.0))` · `rise("#s1-search", at(1,0.0),{y:30})` ·
  `rise("#s1-kicker", at(1,0.0),{y:20})` · `rise("#s1-label", at(1,0.0),{y:20})` ·
  `rise("#s1-eur", at(1,0.0))` ·
  `fromTo("#s1-eur",{scale:1},{scale:1.12,dur:0.12,ease:"power2.out"}, at(1,0.55))` →
  `to("#s1-eur",{scale:1,dur:0.16,ease:"power2.inOut"}, at(1,0.67))` (salto discreto, sin opacidad).
- **Rótulo en pantalla:** kicker **«GANCHO»**; placa **«6 €»**; rótulo **«EN GOOGLE ADS»**.
- **Sonido:** whoosh 0,0 (entra la barra) · tick 0,55 (la cifra) · ding 1,30 · pop 2,40.
- **Salida:** **desplazamiento continuo ↑ 0,35 s**.

## B2 · El caso — «Se lo preguntó Alec Brownstein, publicista, en 2010.»

- **Qué se ve:** papel claro. La **ficha del caso** con el año **2010** (protagonista), el nombre
  **Alec Brownstein** y el rótulo **«PUBLICISTA»**; a la izquierda, un **monograma** (sin foto). Es
  quien se hizo la pregunta, no una marca: el dato y la persona.
- **Elementos:** `#s2-in` · `#s2-kicker` · `#s2-card` (`.card`) · `#s2-mono` (`.monogram` «AB») ·
  `#s2-year` (`.yearbadge` «2010») · `#s2-name` (`.nameplate`) · `#s2-role` (`.chip` «PUBLICISTA») ·
  `#s2-cover` (`.cover`, pieza de transición).
- **Receta (rel):** `rise("#s2-card", at(2,0.0))` · `put("#s2-kicker", at(2,0.06),{dur:0.4})` ·
  `put("#s2-mono", at(2,0.22),{scale:0.7})` · `put("#s2-year", at(2,0.30),{scale:0.8})` ·
  `put("#s2-name", at(2,0.80),{y:20})` · `put("#s2-role", at(2,1.15),{y:16})`.
- **Rótulo en pantalla:** kicker **«EL CASO»**; año **«2010»**; nombre **«Alec Brownstein»**; chip
  **«PUBLICISTA»**.
- **Sonido:** pop 0,22 · tick 0,30 (el año) · pop 0,80 (el nombre) · pop 1,15 · ding 1,55.
- **Salida:** **objeto que cubre (`.cover`) 0,45 s** — el panel `#20202a` crece desde la ficha del caso
  y despeja la escena oscura.

## B3 · El mecanismo — «Su idea fue esta: los directores creativos se buscan a sí mismos en Google.»

- **Qué se ve:** escena oscura. La **marca de la plataforma** (logotipo tipográfico **Google**, tinta
  sobre tarjeta clara) sobre una **barra de búsqueda** en la que se **teclea, carácter a carácter, el
  nombre** de un director creativo (**Scott Vitrone**); al terminar, **brota arriba un anuncio**
  (`.adrow`, acento relleno) — solo aparece al buscar **ese** nombre. Al pie, el rótulo **«SE BUSCAN A
  SÍ MISMOS»**.
- **Elementos:** `#s3-in` · `#s3-kicker` · `#s3-card` (`.card`) · `#s3-brand` (`.brandmark` «Google»,
  tinta sobre `#ffffff`) · `#s3-search` (`.searchbar`) · `#s3-term` (`.sterm`, tecleado con
  `typeChars`) · `#s3-ad` (`.adrow` con `.adlab` «ANUNCIO») · `#s3-note` (`.chip`).
- **Receta (rel):** `rise("#s3-card", at(3,0.0))` · `put("#s3-kicker", at(3,0.06),{dur:0.4})` ·
  `put("#s3-brand", at(3,0.20),{y:16})` · `rise("#s3-search", at(3,0.40),{y:24})` ·
  `typeChars("#s3-term", at(3,0.80),0.05)` (13 caracteres · 0,80-1,45) ·
  `put("#s3-ad", at(3,1.85),{y:-20})` · `put("#s3-note", at(3,2.70),{y:16})`.
- **Rótulo en pantalla:** kicker **«EL MECANISMO»**; marca **«Google»**; el nombre tecleado (mono) ·
  **«ANUNCIO»**; chip **«SE BUSCAN A SÍ MISMOS»**.
- **Sonido:** whoosh 0,40 · tecleo (`key`, 13 clics, loc. 0,80-1,45, **ganancia 0,35**) · swoosh_up
  1,85 (brota el anuncio) · ding 2,70.
- **Salida:** **desplazamiento continuo ↑ 0,45 s** (oscuro → claro).

## B4 · La selección — «Eligió a cinco y compró anuncios que solo aparecían al buscar sus nombres.»

- **Qué se ve:** papel claro. La **lista de cinco nombres** (los cinco directores creativos: Droga,
  Granger, Graf, Reichenthal, Vitrone); cada fila recibe su **casilla marcada** en acento, una a una.
  Al pie, el rótulo **«SOLO ESOS NOMBRES»**.
- **Elementos:** `#s4-in` · `#s4-kicker` · `#s4-card` (`.card`) ·
  `#s4-list` (`.picklist`) · `#s4-p1`…`#s4-p5` (`.pick` con `.pname` + `.pickbox/.pickfill`) ·
  `#s4-k1`…`#s4-k5` (`.pickfill`, acento relleno) · `#s4-note` (`.chip`).
- **Receta (rel):** `rise("#s4-card", at(4,0.0))` ·
  `put("#s4-kicker", at(4,0.06),{dur:0.4})` ·
  `put("#s4-p1", at(4,0.20),{x:-30})` · `put("#s4-p2", at(4,0.42),{x:-30})` ·
  `put("#s4-p3", at(4,0.64),{x:-30})` · `put("#s4-p4", at(4,0.86),{x:-30})` ·
  `put("#s4-p5", at(4,1.08),{x:-30})` ·
  `put("#s4-k1", at(4,1.45),{scale:0.5})` · `put("#s4-k2", at(4,1.68),{scale:0.5})` ·
  `put("#s4-k3", at(4,1.91),{scale:0.5})` · `put("#s4-k4", at(4,2.14),{scale:0.5})` ·
  `put("#s4-k5", at(4,2.37),{scale:0.5})` · `put("#s4-note", at(4,2.80),{y:16})`.
- **Rótulo en pantalla:** kicker **«LA SELECCIÓN»**; los cinco nombres (mono) · chip **«SOLO ESOS
  NOMBRES»**.
- **Sonido:** pop 0,20/0,42/0,64/0,86/1,08 (filas) · tick 1,45/1,68/1,91/2,14/2,37 (casillas) · ding
  2,80.
- **Salida:** **desplazamiento continuo ↑ 0,40 s**.

## B5 · El anuncio — "El anuncio decía: «Buscarte a ti mismo en Google es divertido. Contratarme también»."

- **Qué se ve:** papel claro. La **barra de búsqueda** con el nombre ya escrito, y debajo la **tarjeta
  del anuncio** con la marca **Google** y su texto; la frase clave **«Contratarme también»** se
  **resalta** con una cortina de acento (relleno, con tinta encima). El anuncio que él colocó, leído.
- **Elementos:** `#s5-in` · `#s5-kicker` · `#s5-card` (`.card`) · `#s5-brand` (`.brandmark.sm`) ·
  `#s5-search` (`.searchbar`, término estático) · `#s5-adcard` (`.adcard`) · `#s5-adlab` (`.adlab`
  «ANUNCIO») · `#s5-adtext` (`.adtext` con `<mark class="hl">`) · `#s5-hl` (`.hl`).
- **Receta (rel):** `rise("#s5-card", at(5,0.0))` · `put("#s5-kicker", at(5,0.06),{dur:0.4})` ·
  `put("#s5-brand", at(5,0.18),{y:16})` · `put("#s5-search", at(5,0.40),{y:-16})` ·
  `put("#s5-adcard", at(5,0.80),{y:24})` · `put("#s5-adtext", at(5,1.15),{y:16})` ·
  `fromTo("#s5-hl",{scaleX:0},{scaleX:1,dur:0.3,ease:"power2.out"}, at(5,1.80))` (cortina del
  resaltado; su origen está en CSS, `transform-origin:left center`).
- **Rótulo en pantalla:** kicker **«EL ANUNCIO»**; marca **«Google»**; **«ANUNCIO»**; el texto del
  anuncio con **«Contratarme también»** resaltado.
- **Sonido:** pop 0,18 · pop 0,40 · pop 0,80 · swoosh_up 1,15 · ding 1,80.
- **Salida:** **desplazamiento continuo ↑ 0,35 s**.

## B6 · El resultado — «Cuatro de los cinco le llamaron y recibió dos ofertas.»

- **Qué se ve:** papel claro. El **marcador**: **`4/5`** con rótulo **«LE LLAMARON»** y **`2`** de
  **«OFERTAS»** (este en placa de acento). Cuatro de los cinco responden. Los números se **fijan en
  salto discreto** (`setNum`), nunca cuentan.
- **Elementos:** `#s6-in` · `#s6-kicker` · `#s6-card` (`.card`) · `#s6-scoreboard` (`.scoreboard`) ·
  `#s6-s1` (`.scorebig` con `#s6-n1` `.scorenum` «4/5» + `#s6-lab1` «LE LLAMARON») · `#s6-s2`
  (`.scorebig.accent` con `#s6-n2` `.scorenum` «2» + `#s6-lab2` «OFERTAS») · `#s6-sweep` (`.sweep`,
  pieza de transición **saliente**: la banda es de B6, que lleva `z-index:5`).
- **Receta (rel):** `rise("#s6-card", at(6,0.0))` ·
  `put("#s6-kicker", at(6,0.06),{dur:0.4})` ·
  `setNum("#s6-n1","4/5", at(6,0.60))` · `put("#s6-lab1", at(6,0.60),{y:12})` ·
  `setNum("#s6-n2","2", at(6,1.50))` · `put("#s6-lab2", at(6,1.50),{y:12})`.
- **Rótulo en pantalla:** kicker **«EL RESULTADO»**; **`4/5` LE LLAMARON** · **`2` OFERTAS** (placa de
  acento).
- **Sonido:** pop 0,60 (el marcador) · ding 0,60 · ding 1,50 ·
  swoosh_up 2,00.
- **Salida:** **barrido de color (`.sweep`) 0,45 s** — la banda de acento cruza la escena **saliente**
  (B6, que lleva `z-index:5` y el `.sweep` es suyo) con **`x:0` explícito**; al desaparecer B6 entra la
  escena oscura del blanco (claro → oscuro).

## B7 · La lección — «No quiso llegar a miles de personas: quería a esas cinco.»

- **Qué se ve:** escena oscura. El **blanco** en grande. Una **multitud de impactos dispersos** se
  llena por todo el lienzo y luego **se apaga**; en el **centro del blanco** quedan encendidas **cinco
  marcas** de acento. El rótulo pasa de **«MILES»** a **«ESAS CINCO»**. Es la imagen de la tesis:
  muchos no valen, cinco sí.
- **Elementos:** `#s7-in` · `#s7-stage` (`.stage`) · `#s7-kicker` · `#s7-blank` (`.blanco`) ·
  `#s7-crowd` (`.crowd` con `.disperso`) · `#s7-five` (`.cinco` con `#s7-m1`…`#s7-m5` `.marca`) ·
  `#s7-labA` (`.crowdlabel` «MILES», visible desde `t=0`) · `#s7-labB` (`.fivelabel.fade-in` «ESAS
  CINCO», nace oculto).
- **Receta (rel):** `rise("#s7-blank", at(7,0.0))` · `put("#s7-kicker", at(7,0.06),{dur:0.4})` ·
  `put("#s7-crowd .disperso", at(7,0.15),{scale:1,dur:0.2,stagger:0.04})` (la multitud se llena) ·
  `to("#s7-crowd",{opacity:0.14,dur:0.5,ease:"power2.out"}, at(7,1.35))` (se apaga) ·
  `swap("#s7-labA","#s7-labB", at(7,1.35))` · `grow("#s7-five", at(7,1.45), 1, {from:0.6,dur:0.4})` ·
  `put("#s7-five .marca", at(7,1.60),{scale:1,dur:0.2,stagger:0.06})`.
- **Rótulo en pantalla:** kicker **«LA LECCIÓN»**; «MILES» (apagado) → **«ESAS CINCO»** (acento relleno).
- **Sonido:** whoosh 0,0 (entra el blanco) · tick 1,60/1,72/1,84/1,96/2,08 (las cinco) · ding 2,60.
- **Salida:** **desplazamiento continuo ↑ 0,40 s** (oscuro → claro; revisar el fotograma medio).

## B8 · Tu versión — «Eso mismo vale para tu negocio.»

- **Qué se ve:** papel claro. Las **cinco marcas** cruzan un **puente** que se dibuja hasta la tarjeta
  **«TU NEGOCIO»**: el mismo gesto que hizo Brownstein sirve para un negocio pequeño. Puente explícito
  del caso al espectador.
- **Elementos:** `#s8-in` · `#s8-kicker` · `#s8-card` (`.card`) · `#s8-five` (`.cinco` con `.marca`) ·
  `#s8-bridge` (`.bridge`, SVG, se dibuja con `draw`) · `#s8-biz` (`.bizcard` con `.bizic` + `.bl`
  «TU NEGOCIO») · `#s8-note` (`.chip` «EL MISMO GESTO»).
- **Receta (rel):** `rise("#s8-card", at(8,0.0))` · `put("#s8-kicker", at(8,0.06),{dur:0.4})` ·
  `put("#s8-five", at(8,0.20),{x:-24})` · `draw("#s8-bridge", at(8,0.55),0.4)` ·
  `put("#s8-biz", at(8,0.95),{x:24})` · `put("#s8-note", at(8,1.30),{y:16})`.
- **Rótulo en pantalla:** kicker **«TU VERSIÓN»**; tarjeta **«TU NEGOCIO»** · chip **«EL MISMO GESTO»**.
- **Sonido:** pop 0,20 · swoosh_up 0,55 (el puente) · pop 0,95 · ding 1,30.
- **Salida:** **desplazamiento continuo ↑ 0,40 s**.

## B9 · La práctica — "En vez de pelear por «abogado» o «dentista», piensa qué buscaría tu cliente ideal."

- **Qué se ve:** papel claro. Dos términos genéricos **«abogado»** y **«dentista»** (mono) se **tachan
  en tinta** (no en rojo: marcan lo que *no conviene*, no una pérdida); una **lupa** recorre la lista
  hasta el centro y allí aparece la etiqueta **«TU CLIENTE IDEAL»** en placa de acento. Dónde no
  disparar y dónde apuntar.
- **Elementos:** `#s9-in` · `#s9-kicker` · `#s9-card` (`.card`) ·
  `#s9-gen1` (`.genrow` con `.genterm` «abogado» + `#s9-s1` `.strike`) · `#s9-gen2` (`.genrow` con
  `.genterm` «dentista» + `#s9-s2` `.strike`) · `#s9-lupa` (`.lupa`, SVG) · `#s9-ideal` (`.idealtag`
  «TU CLIENTE IDEAL»).
- **Receta (rel):** `rise("#s9-card", at(9,0.0))` ·
  `put("#s9-kicker", at(9,0.06),{dur:0.4})` · `put("#s9-gen1", at(9,0.20),{x:-30})` ·
  `draw("#s9-s1", at(9,0.55),0.3)` · `put("#s9-gen2", at(9,0.80),{x:-30})` ·
  `draw("#s9-s2", at(9,1.15),0.3)` · `put("#s9-lupa", at(9,1.60),{x:-40})` ·
  `put("#s9-ideal", at(9,2.15),{scale:0.86})`.
- **Rótulo en pantalla:** kicker **«LA PRÁCTICA»**; **«abogado»** · **«dentista»** (tachados en tinta) ·
  **«TU CLIENTE IDEAL»** (acento relleno).
- **Sonido:** pop 0,20 · swoosh_down 0,55 · pop 0,80 · swoosh_down 1,15 · swoosh_up 1,60 (la lupa) ·
  ding 2,15.
- **Salida:** **desplazamiento continuo ↑ 0,40 s**.

## B10 · La práctica — «Puede que tenga pocas búsquedas al mes, pero sean tus mejores clientes.»

- **Qué se ve:** papel claro. Una **gráfica de barras corta** (tres barras horizontales, todas
  pequeñas) con la etiqueta **«búsquedas al mes»**; bajo ella, la placa **«TUS MEJORES CLIENTES»**. La
  paradoja visual: barras cortas (pocas búsquedas) pero las mejores. Las barras se llenan con `bar`.
- **Elementos:** `#s10-in` · `#s10-kicker` · `#s10-card` (`.card`) · `#s10-chart` (`.barchart`) ·
  `#s10-r1`…`#s10-r3` (`.brow` con `#s10-f1`…`#s10-f3` `.bfill`) · `#s10-axis` (`.blab` «BÚSQUEDAS AL
  MES») · `#s10-best` (`.pill.accent` «TUS MEJORES CLIENTES»).
- **Receta (rel):** `rise("#s10-card", at(10,0.0))` · `put("#s10-kicker", at(10,0.06),{dur:0.4})` ·
  `put("#s10-chart", at(10,0.20),{y:20})` ·
  `bar("#s10-f1", at(10,0.45),0.30)` · `bar("#s10-f2", at(10,0.65),0.42)` · `bar("#s10-f3", at(10,0.85),0.24)` ·
  `put("#s10-best", at(10,1.30),{scale:0.86})`.
- **Rótulo en pantalla:** kicker **«LA PRÁCTICA»**; etiqueta **«búsquedas al mes»** · pastilla
  **«TUS MEJORES CLIENTES»**.
- **Sonido:** pop 0,20 · tick 0,45/0,65/0,85 (las barras) · ding 1,30.
- **Salida:** **corte directo** (claro → oscuro).

## B11 · Cierre — «Guarda esto: en anuncios no gana más tráfico, gana el tráfico correcto.»

- **Qué se ve:** escena oscura. El **marcador de guardado** con la **onda** que se dibuja y el rótulo
  **«Guarda esto»**. Detrás, **el blanco encendido**: el **centro relleno de acento** con **cinco
  marcas en tinta** dentro, y los impactos dispersos apagados por fuera. Cierra enlazando la CTA con la
  imagen del **tráfico correcto**: pocos, pero en el centro. Al pie, la pastilla **«EL TRÁFICO
  CORRECTO»**.
- **Elementos:** `#s11-in` · `#s11-blank` (`.blanco.correct`) · `#s11-core`
  (`.core`, relleno de acento) · `#s11-five` (`.cinco` con `#s11-m1`…`#s11-m5` `.marca`, tinta sobre
  el centro) · `#s11-mark` (`.cta-mark`) · `#s11-label` (`.cta-label` «Guarda esto») · `#s11-wave`
  (`.savewave`) · `#s11-note` (`.pill.accent` «EL TRÁFICO CORRECTO»).
- **Receta (rel):** `rise("#s11-blank", at(11,0.0))` ·
  `put("#s11-mark", at(11,0.05),{scale:0.5,dur:0.5})` ·
  `put("#s11-label", at(11,0.55),{scale:0.86,dur:0.5})` · `draw("#s11-wave", at(11,0.95),0.5)` ·
  `grow("#s11-core", at(11,1.30), 1, {from:0.3,dur:0.4})` (se enciende el centro) ·
  `put("#s11-five .marca", at(11,1.60),{scale:1,dur:0.2,stagger:0.08})` (las cinco marcas, en tinta) ·
  `put("#s11-note", at(11,2.30),{y:16})`.
- **Rótulo en pantalla:** **«Guarda esto»** (96 px); pastilla **«EL TRÁFICO CORRECTO»**. Sin kicker.
- **Sonido:** pop 0,05 · ding 0,55 · swoosh_up 0,95 · pop 1,30 · ding 2,30.
- **Salida:** — (fin).

---

## Recursos

| Recurso | Tipo | Origen |
|---|---|---|
| Fuentes, voz `Pablo`, música, efectos, karaoke, barra de progreso | — | Reutilizado (kit) |
| `.scene`, `.s-in`, `.kicker` (+`.dot`), `.card`, `.chip`, `.pill`, `.stage` | HTML/CSS | Reutilizado (kit) |
| Marcador de guardado + onda (`.cta-mark`, `.cta-label`, `.savewave`) | HTML/SVG | Reutilizado (kit / GA4) |
| **El blanco / la mira** (`.blanco`, `.ring`, `.core`, `.crowd`, `.cinco`, `.marca`, `.disperso`) | HTML/CSS/SVG | **Nuevo** (la metáfora) |
| **Barra de búsqueda** (`.searchbar`, `.sicon`, `.sterm`, `.scaret`, `.shint`) | HTML/CSS/SVG | **Nuevo** |
| **Cifra-cifra del gancho** (`.eurmark`) | HTML/CSS | **Nuevo** |
| **Ficha del caso** (`.yearbadge`, `.nameplate`, `.monogram`) | HTML/CSS | **Nuevo** |
| **Marca de la plataforma** (`.brandmark`, tinta sobre tarjeta clara) | HTML/CSS | **Nuevo** (sin `@handle`, sin red) |
| **Anuncio** (`.adrow`, `.adcard`, `.adlab`, `.adtext`, `.hl`) | HTML/CSS | **Nuevo** |
| **Lista de selección** (`.picklist`, `.pick`, `.pname`, `.pickbox`, `.pickfill`) | HTML/CSS/SVG | **Nuevo** |
| **Marcador del resultado** (`.scoreboard`, `.scorebig`, `.scorenum`, `.scorelab`) | HTML/CSS | **Nuevo** |
| **Rótulos del blanco** (`.crowdlabel`, `.fivelabel`) | HTML/CSS | **Nuevo** |
| **Puente y «tu negocio»** (`.bridge`, `.bizcard`, `.bizic`) | HTML/CSS/SVG | **Nuevo** |
| **Términos, tachado y lupa** (`.genrow`, `.genterm`, `.strike`, `.lupa`, `.idealtag`) | HTML/CSS/SVG | **Nuevo** |
| **Gráfica corta** (`.barchart`, `.brow`, `.bfill`, `.blab`) | HTML/CSS | **Nuevo** |
| Capas de transición `.cover` y `.sweep`, recorte `clip-path` | HTML/CSS | **Nuevo** (piezas propias) |
| Collage (manos, personas, objetos) o imágenes de red | PNG | **Descartado**: no hay material y la marca va como logotipo tipográfico |
| Render, vídeo con alfa o 3D | — | No se necesita |

## Ritmo y sonido por beat

| # | Movimiento o lectura | Entrada | Desarrollo | Lectura | Transición | Efectos (rel) |
|---|---|---|---|---|---|---|
| B1 | Movimiento | 0,0-0,4 | 0,4-1,5 | 1,5-fin | 0,35 | whoosh 0,0 · tick 0,55 · ding 1,30 · pop 2,40 |
| B2 | Movimiento | 0,0-0,4 | 0,4-1,4 | 1,4-fin | 0,45 | pop 0,22 · tick 0,30 · pop 0,80 · pop 1,15 · ding 1,55 |
| B3 | Movimiento | 0,0-0,5 | 0,5-2,7 | 2,7-fin | 0,45 | whoosh 0,40 · key 0,80-1,45 · swoosh_up 1,85 · ding 2,70 |
| B4 | Movimiento | 0,0-0,4 | 0,4-2,8 | 2,8-fin | 0,40 | pop 0,20/0,42/0,64/0,86/1,08 · tick 1,45/1,68/1,91/2,14/2,37 · ding 2,80 |
| B5 | Lectura | 0,0-0,5 | 0,5-2,0 | 2,0-fin | 0,35 | pop 0,18 · pop 0,40 · pop 0,80 · swoosh_up 1,15 · ding 1,80 |
| B6 | Movimiento | 0,0-0,4 | 0,4-1,5 | 1,5-fin | 0,45 | pop 0,60 · ding 0,60 · ding 1,50 · swoosh_up 2,00 |
| B7 | Movimiento | 0,0-0,4 | 0,4-2,6 | 2,6-fin | 0,40 | whoosh 0,0 · tick 1,60/1,72/1,84/1,96/2,08 · ding 2,60 |
| B8 | Movimiento | 0,0-0,3 | 0,3-1,3 | 1,3-fin | 0,40 | pop 0,20 · swoosh_up 0,55 · pop 0,95 · ding 1,30 |
| B9 | Lectura | 0,0-0,5 | 0,5-2,1 | 2,1-fin | 0,40 | pop 0,20 · swoosh_down 0,55 · pop 0,80 · swoosh_down 1,15 · swoosh_up 1,60 · ding 2,15 |
| B10 | Movimiento | 0,0-0,4 | 0,4-1,3 | 1,3-fin | 0,00 | pop 0,20 · tick 0,45/0,65/0,85 · ding 1,30 |
| B11 | Lectura | 0,0-0,5 | 0,5-1,6 | 1,6-fin | — | pop 0,05 · ding 0,55 · swoosh_up 0,95 · pop 1,30 · ding 2,30 |

Se alterna movimiento con lectura: B1 mov · B2 mov · B3 mov · B4 mov · B5 lec · B6 mov · B7 mov ·
B8 mov · B9 lec · B10 mov · B11 lec. **Un efecto por aparición**, nunca por palabra.

---

## Ritmo — tabla calculada a 3,2 palabras/segundo

Total del guion: **123 palabras**. A **3,2 palabras/s** (el ritmo real de la voz `Pablo` medido en
`mkt-01`: 121 pal. / 37,52 s ≈ 3,22 pal./s), **123 ÷ 3,2 ≈ 38,4 s**. Los tiempos definitivos los
fija `voice_pipeline.py` y los aplica `retime.py`; toda la animación está en tiempos **relativos** al
inicio de su beat. La tabla es **estimada** y cuadra palabra a palabra con `SCRIPT.md`.

| Beat | Pal. | Dur. (s) | Inicio (s) | Fin (s) |
|---|---|---|---|---|
| B1 | 10 | 3,125 | 0,000 | 3,125 |
| B2 | 8 | 2,500 | 3,125 | 5,625 |
| B3 | 14 | **4,375** | 5,625 | 10,000 |
| B4 | 13 | 4,063 | 10,000 | 14,063 |
| B5 | 13 | 4,063 | 14,063 | 18,126 |
| B6 | 10 | 3,125 | 18,126 | 21,251 |
| B7 | 11 | 3,438 | 21,251 | 24,689 |
| B8 | 6 | 1,875 | 24,689 | 26,564 |
| B9 | 14 | **4,375** | 26,564 | 30,939 |
| B10 | 12 | 3,750 | 30,939 | 34,689 |
| B11 | 12 | 3,750 | 34,689 | **38,439** |

**Total: 123 palabras · 38,439 s ≈ 38,4 s** (dentro de la banda 30-40 s). **Cuadre:** la suma de
palabras de la tabla es 10+8+14+13+13+10+11+6+14+12+12 = **123** = `SCRIPT.md` = carrera del karaoke
= `assets/voice/*.txt`.

**Excepciones de duración (estimadas).** La escena más corta es **1,875 s** (B8; el mínimo del
contrato es 1,2 s) y **dos escenas superan el techo de 4,2 s** del contrato §5: **B3 = 4,375 s** y
**B9 = 4,375 s**, por la longitud de la frase (14 palabras cada una) al ritmo de `Pablo`. **No se
parten** —el guion es del dueño y la locución la fija `voice_pipeline.py`—: misma excepción aceptada
en `mkt-01` (D39) y V6 (D38). El resto queda por debajo de 4,2 s (máximo: B4/B5 = 4,063 s).

**Excepción del beat (del dueño).** Siete de las once líneas superan el beat de **6-10 palabras** del
contrato §3: L3 = 14 · L4 = 13 · L5 = 13 · L7 = 11 · L9 = 14 · L10 = 12 · L11 = 12 (todas ≤ 14). Es
texto dictado por el dueño y no se redistribuye; ver `DECISIONS.md` D40.

## Reparto de rótulos

| Beat | Kicker (32 px, mayúsculas) | Etiquetas / rótulos en pantalla |
|---|---|---|
| B1 | GANCHO | placa **6 €** · rótulo **EN GOOGLE ADS** |
| B2 | EL CASO | año **2010** · nombre **Alec Brownstein** · chip **PUBLICISTA** |
| B3 | EL MECANISMO | marca **Google** · nombre tecleado (mono) · **ANUNCIO** · chip **SE BUSCAN A SÍ MISMOS** |
| B4 | LA SELECCIÓN | los cinco nombres (mono) · chip **SOLO ESOS NOMBRES** |
| B5 | EL ANUNCIO | marca **Google** · **ANUNCIO** · texto del anuncio con **Contratarme también** resaltado |
| B6 | EL RESULTADO | **4/5 LE LLAMARON** · **2 OFERTAS** (placa de acento) |
| B7 | LA LECCIÓN | «MILES» (apagado) → **ESAS CINCO** (acento) |
| B8 | TU VERSIÓN | tarjeta **TU NEGOCIO** · chip **EL MISMO GESTO** |
| B9 | LA PRÁCTICA | **abogado / dentista** (tachados en tinta) · **TU CLIENTE IDEAL** |
| B10 | LA PRÁCTICA | **búsquedas al mes** · pastilla **TUS MEJORES CLIENTES** |
| B11 | — (CTA) | **Guarda esto** (96 px) · pastilla **EL TRÁFICO CORRECTO** |

Regla: rótulos **nominales en mayúsculas, sin numerar** (decisión de `DIRECCION.md` §10), **nunca
repiten la voz**. Lo que alguien *escribe o busca* (el nombre tecleado, los cinco nombres, «abogado» y
«dentista») va en JetBrains Mono.

## Revisión antes de dar por bueno el vídeo

Un fotograma de lectura de cada escena · los instantes intermedios de las transiciones con
tratamiento especial (`cover` B2→B3 y `sweep` B6→B7; el corte final B10→B11 es directo) · entradas,
salidas y superposiciones · **luminancia y % de filas con contenido del fotograma 0** (miniatura:
≥ 200/255 y ≈ 100 %) · legibilidad a tamaño móvil · alineación de texto e interfaces · sincronía con
la voz · y el MP4 completo en movimiento.
