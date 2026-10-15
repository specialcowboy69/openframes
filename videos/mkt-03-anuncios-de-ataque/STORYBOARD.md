# STORYBOARD — mkt-03 «Anuncios de ataque (Basecamp, 2019)»

Serie **Casos de estudio marketing** · Pieza **mkt-03** · **11 beats · 119 palabras · ≈37,2 s** ·
1080×1920 · faceless · voz en off es-ES (`Pablo`) · subtítulos karaoke. La dirección de arte está en
`DIRECCION.md` y el brief en `DIRECCION-ARTE-BRIEF.md`. Formato calcado de
`videos/mkt-02-google-ads-trafico-correcto/STORYBOARD.md`.

**Todos los tiempos son RELATIVOS al inicio de su beat** (los absolutos los fija la voz con
`retime.py`). Los identificadores son los del `index.html`; el CSS de los elementos nuevos está en
`DIRECCION.md` §8.

**Regla en las 11 escenas:** el escenario (calle / rótulo / buscador / pila de vallas / marco del
reflejo / valla-protesta) está visible desde el fotograma 0 y **solo se asienta** (`rise()`); nace en
opacidad 0 el contenido. Sin `.from()`, sin `Math.random`, sin `Date.now`, sin contar hacia arriba
(`setNum(sel, txt, t)` fija el número en un salto discreto). Ayudantes: `put`, `rise`, `draw`, `grow`,
`bar`, `typeWords`, `typeChars`, `swap`, `setNum`. Los elementos que se revelan llevan la clase del kit
`.fade-in` (estado inicial en CSS); el resto usa `fromTo`/`.to()`. **El escenario no se anima en
opacidad.**

**Metáfora:** «tu nombre y las vallas de delante» (`DIRECCION.md` §1). **Recurso propio:** **la valla**
(el anuncio) y **su pila por delante del rótulo** — al buscar una marca, varias vallas de rivales brotan
por encima de su propio resultado. No se reutiliza el blanco de `mkt-02`, la burbuja de `mkt-01`, la
SERP de V5, la balanza de V6 ni la barra de un solo anuncio de `mkt-02`. **Ejemplo único:** el negocio
del espectador. **El rojo se usa una sola vez** (B10, el clic que ya no es tuyo).

---

## Desviaciones justificadas del contrato

- **Banda segura (`.s-in`).** El contrato §3 fija `padding: 300px 74px 470px`; esta pieza usa
  **`padding: 300px 74px 700px`** (`index.html`), igual que `mkt-01` y `mkt-02`. Se subió a propósito
  para que el bloque de contenido **no quede bajo la píldora del karaoke** (la píldora va a `bottom:470`
  y ocupa ~y 1230-1450). Es una desviación **solo de margen y más conservadora** que el contrato: no
  viola la banda segura 15-75 % (288-1440).
- **B1 sin kicker (regla vinculante del dueño).** `SCRIPT.md` fija que el primer beat es un **gancho de
  curiosidad puro**: en el fotograma 0 va **solo el texto del gancho**, **sin rótulo de tema ni de
  serie**. `mkt-01`/`mkt-02` llevaban kicker «GANCHO»; aquí **se omite** para no rotular nada. Queda
  documentado como excepción a la costumbre de la línea.
- **Escenas largas (estimadas).** A **3,2 pal./s**, **B3 (14 palabras) = 4,375 s** y **B11 (14 palabras)
  = 4,375 s** superan el techo de **4,2 s** del contrato §5. **No se parten** —el guion es del dueño y la
  locución la fija `voice_pipeline.py`—: misma excepción aceptada en `mkt-01` (D39), V6 (D38) y `mkt-02`.
  El resto queda por debajo de 4,2 s (máximo: B6 = 4,063 s).
- **Beats de más de 10 palabras (del dueño).** Siete de las once líneas superan el beat de 6-10 palabras
  del contrato §3: L3 (14) · L5 (11) · L6 (13) · L7 (11) · L9 (12) · L10 (12) · L11 (14), todas **≤ 14**.
  Es texto dictado por el dueño y no se redistribuye (ver `mkt-01` D40).

---

## B1 · Gancho — «Esta empresa descubrió algo que no imaginas.»

- **Qué se ve:** papel claro a pantalla completa (**fotograma 0 = miniatura**). La **calle** (acera) y,
  sobre ella, el **rótulo** de una marca con su placa **tapada por barras de censura** y un **`?`**:
  «esta empresa», sin nombre. Un **foco** neutro cae sobre el rótulo. El **texto del gancho** es lo
  **único escrito** en pantalla (titular, 132 px) y está montado **desde el fotograma 0**. **Sin kicker,
  sin rótulo de tema, sin nombre de línea ni de serie.** Todo se asienta con `rise()`; nada se desvanece
  ni entra tarde.
- **Elementos:** `#s1-in` · `#s1-calle` (`.calle`) · `#s1-foco` (`.foco`) · `#s1-rotulo` (`.rotulo` con
  `#s1-redact`, `.redact`) · `#s1-hook` (`.hookline`). *(B1 no lleva `.kicker`.)*
- **Receta (rel):** `rise("#s1-calle", at(1,0.0))` · `rise("#s1-foco", at(1,0.0))` ·
  `rise("#s1-rotulo", at(1,0.0),{y:30})` · `rise("#s1-hook", at(1,0.0),{y:20})` ·
  `fromTo("#s1-rotulo",{scale:1},{scale:1.06,dur:0.14,ease:"power2.out"}, at(1,0.55))` →
  `to("#s1-rotulo",{scale:1,dur:0.18,ease:"power2.inOut"}, at(1,0.69))` (latido discreto, sin opacidad).
- **Rótulo en pantalla:** **el texto del gancho** (`SCRIPT.md`: «Solo el texto del gancho»). Sin kicker.
- **Sonido (local: B1 no tiene cues):** whoosh 0,0 (llega la calle) · pop 0,55 (el rótulo late) ·
  ding 1,20 (el foco).
- **Salida:** **objeto que cubre (`.cover`) 0,45 s** — el panel `#20202a` crece desde el rótulo y despeja
  la escena oscura de la emboscada.

## B2 · El caso — «Su competencia le estaba robando clientes anunciándose con su nombre.»

- **Qué se ve:** escena oscura. Dos **rótulos** de marca (A: la víctima, placa clara; B: la competencia,
  placa oscura). Una **figura rival** (`.fig`, SVG 2D) arrastra su **valla** y **la clava delante** del
  rótulo de la víctima; sobre esa valla aparece el **nombre de la víctima** (raído: nadie ha dicho aún
  cuál es). Dos **clientes** (`.gente`) caminan hacia el rótulo A y son **interceptados** por la valla.
- **Elementos:** `#s2-in` · `#s2-calle` (`.calle`) · `#s2-kicker` · `#s2-rotuloA` (`.rotulo.marca`) ·
  `#s2-rotuloB` (`.rotulo.rival`) · `#s2-fig` (`.fig.rival`) · `#s2-valla` (`.valla.rival` con
  `#s2-name`, `.redact`) · `#s2-clientes` (`.gente` ×2).
- **Receta (rel):** `rise("#s2-calle", at(2,0.0))` · `rise("#s2-rotuloA", at(2,0.0))` ·
  `rise("#s2-rotuloB", at(2,0.0))` · `put("#s2-kicker", at(2,0.06),{dur:0.4})` ·
  `put("#s2-fig", cue(2,"competencia"),{y:22,dur:0.26})` ·
  `put("#s2-valla", cue(2,"competencia")+0.06,{y:-20,dur:0.26})` ·
  `put("#s2-clientes .gente", cue(2,"clientes"),{y:16,dur:0.24,stagger:0.06})` ·
  `put("#s2-name", cue(2,"nombre"),{scale:0.86,dur:0.24})`.
- **Rótulo en pantalla:** kicker **«EL CASO»**; `ANUNCIO` sobre la valla ajena (sin marca: la placa va
  raída).
- **Sonido:** pop cue(2,"competencia") · pop cue(2,"clientes") · tick cue(2,"nombre") · ding local 2,50.
- **Salida:** **desplazamiento continuo ↑ 0,40 s**.

## B3 · El mecanismo — «Se conocen como anuncios de ataque: aparecer en Google cuando buscan a tu rival.»

- **Qué se ve:** escena oscura. La **marca de la plataforma** (logotipo tipográfico **Google**, tinta
  sobre tarjeta clara) y una **barra de búsqueda** en la que se **teclea, carácter a carácter, el nombre
  del rival**; al terminar, **brota tu valla** por encima del resultado del rival. Sobre la escena, el
  **término**: chip **«ANUNCIOS DE ATAQUE»**. Es la definición del patrón.
- **Elementos:** `#s3-in` · `#s3-calle` · `#s3-kicker` · `#s3-brand` (`.brandmark` «Google») ·
  `#s3-search` (`.searchbar`) · `#s3-term` (`.sterm`, tecleado) · `#s3-rotuloR` (`.rotulo.rival`) ·
  `#s3-valla` (`.valla.rival`) · `#s3-chip` (`.chip` «ANUNCIOS DE ATAQUE»).
- **Receta (rel):** `rise("#s3-calle", at(3,0.0))` · `put("#s3-kicker", at(3,0.06),{dur:0.4})` ·
  `put("#s3-brand", cue(3,"Google"),{y:16,dur:0.26})` · `rise("#s3-search", at(3,0.40),{y:24})` ·
  `put("#s3-chip", cue(3,"ataque"),{scale:0.86,dur:0.26})` ·
  `typeChars("#s3-term", cue(3,"buscan"),0.045)` ·
  `put("#s3-valla", cue(3,"rival"),{y:-20,dur:0.26})`.
- **Rótulo en pantalla:** kicker **«EL MECANISMO»**; marca **Google**; el **nombre del rival** (mono);
  chip **«ANUNCIOS DE ATAQUE»**.
- **Sonido:** whoosh local 0,40 (la barra) · ding cue(3,"Google") · pop cue(3,"ataque") ·
  key cue(3,"buscan") (tecleo, `offset` por carácter 45 ms) · swoosh_up cue(3,"rival").
- **Salida:** **desplazamiento continuo ↑ 0,40 s** (oscuro → claro).

## B4 · El caso — «Esa empresa era Basecamp, en 2019.»

- **Qué se ve:** papel claro. La **misma placa de B1 se descubre**: la **censura se retira** y aparece el
  **logotipo tipográfico `Basecamp`** (tinta sobre tarjeta clara). Al lado, el **año `2019`** en grande.
  Es la revelación del caso.
- **Elementos:** `#s4-in` · `#s4-calle` · `#s4-kicker` · `#s4-rotulo` (`.rotulo`) · `#s4-redact`
  (`.redact`) · `#s4-brand` (`.brandmark` «Basecamp») · `#s4-year` (`.yearbadge` «2019»).
- **Receta (rel):** `rise("#s4-calle", at(4,0.0))` · `rise("#s4-rotulo", at(4,0.0),{y:30})` ·
  `put("#s4-kicker", at(4,0.06),{dur:0.4})` ·
  `to("#s4-redact",{scaleX:0,dur:0.30,ease:"power2.inOut"}, cue(4,"Basecamp"))` ·
  `put("#s4-brand", cue(4,"Basecamp"),{scale:0.9,dur:0.26})` ·
  `put("#s4-year", cue(4,"2019"),{scale:0.8,dur:0.24})`.
- **Rótulo en pantalla:** kicker **«LA EMPRESA»**; marca **Basecamp**; año **2019**.
- **Sonido:** pop cue(4,"Basecamp") (cae la censura) · tick cue(4,"2019") · ding local 1,60.
- **Salida:** **desplazamiento continuo ↑ 0,35 s** (claro → oscuro).

## B5 · El caso (el dato) — «Al buscar su propio nombre, aparecían hasta cuatro anuncios de competidores.»

- **Qué se ve:** escena oscura. La **barra de búsqueda** con **`Basecamp`** tecleado (mono). Debajo, el
  **resultado propio**: el **rótulo** de Basecamp. **Por encima, brotan cuatro vallas** de competidores,
  apiladas, cada una con su etiqueta **`ANUNCIO`**. El **contador `4`** se fija en salto discreto
  (`setNum`, sin contar). Es la imagen central del dato. La **pila** baja ~24 px mientras el rótulo se
  queda (paralaje: el rótulo queda **detrás**).
- **Elementos:** `#s5-in` · `#s5-calle` · `#s5-kicker` · `#s5-search` (`.searchbar`) · `#s5-term`
  (`.sterm`, tecleado) · `#s5-vallas` (`.vallas`) con `#s5-v1`…`#s5-v4` (`.valla.rival`) ·
  `#s5-rotulo` (`.rotulo`) · `#s5-brand` (`.brandmark`) · `#s5-count` (`.contador`) · `#s5-note`
  (`.chip` «DE COMPETIDORES»).
- **Receta (rel):** `rise("#s5-calle", at(5,0.0))` · `rise("#s5-search", at(5,0.0),{y:24})` ·
  `rise("#s5-rotulo", at(5,0.0))` · `put("#s5-kicker", at(5,0.06),{dur:0.4})` ·
  `typeChars("#s5-term", cue(5,"buscar"),0.05)` ·
  `put("#s5-vallas .valla", cue(5,"cuatro"),{y:-20,dur:0.24,stagger:0.07})` ·
  `put("#s5-count", cue(5,"cuatro"),{scale:0.8,dur:0.24})` ·
  `setNum("#s5-count","4", cue(5,"cuatro"))` ·
  `put("#s5-note", cue(5,"competidores"),{y:14,dur:0.26})` ·
  `to("#s5-vallas",{y:24,dur:0.5,ease:"power2.out"}, at(5,2.40))` (paralaje; el rótulo hace 1,04 con
  `grow("#s5-rotulo", at(5,2.40),1,{from:0.96,dur:0.4})`).
- **Rótulo en pantalla:** kicker **«EL DATO»**; **`Basecamp`** tecleado; **`ANUNCIO`** en las cuatro
  vallas; **`4`** (contador); chip **«DE COMPETIDORES»**.
- **Sonido:** key cue(5,"buscar") (tecleo, `offset` por carácter 50 ms) · swoosh_up cue(5,"cuatro") ·
  tick cue(5,"cuatro")+0,10/0,17/0,24/0,31 (las cuatro vallas) · tick cue(5,"cuatro")+0,38 (el contador) ·
  ding cue(5,"competidores").
- **Salida:** **desplazamiento continuo ↑ 0,40 s** (oscuro → claro).

## B6 · El mecanismo — «Funciona porque quien busca una marca está comparando y a punto de elegir.»

- **Qué se ve:** papel claro. La **encrucijada**: un **cliente** (`.gente`, SVG 2D) de pie entre **dos
  rótulos** enfrentados. Al nombrar la voz la comparación, se encienden **dos focos** (uno por opción) y
  el cliente **se inclina** hacia una: está a punto de elegir. Por eso el ataque funciona.
- **Elementos:** `#s6-in` · `#s6-calle` · `#s6-kicker` · `#s6-cliente` (`.gente` con `.sub`) ·
  `#s6-op1` `#s6-op2` (`.rotulo.rival`) · `#s6-foco1` `#s6-foco2` (`.foco`) · `#s6-tag` (`.tag`
  «TU CLIENTE»).
- **Receta (rel):** `rise("#s6-calle", at(6,0.0))` · `put("#s6-kicker", at(6,0.06),{dur:0.4})` ·
  `put("#s6-cliente", cue(6,"quien"),{y:20,dur:0.26})` ·
  `put("#s6-tag", cue(6,"quien")+0.10,{y:12,dur:0.24})` ·
  `put("#s6-op1,#s6-op2", cue(6,"marca"),{scale:0.94,dur:0.26,stagger:0.06})` ·
  `to("#s6-foco1,#s6-foco2",{opacity:0.18,dur:0.30}, cue(6,"comparando"))` (estado inicial
  `opacity:0` en CSS) ·
  `to("#s6-cliente .sub",{x:28,rotation:-6,dur:0.40,ease:"power2.out"}, cue(6,"elegir"))`.
- **Rótulo en pantalla:** kicker **«POR QUÉ»**; etiqueta **«TU CLIENTE»**.
- **Sonido:** pop cue(6,"quien") · pop cue(6,"marca") · swoosh_up cue(6,"comparando") · ding
  cue(6,"elegir").
- **Salida:** **barrido de color (`.sweep`) 0,45 s** — la banda de acento cruza la escena **saliente**
  (B6, que lleva `z-index:5` y el `.sweep` es suyo) con **`x:0` explícito**; al desaparecer B6 entra la
  escena oscura del reflejo (claro → oscuro).

## B7 · Tu versión — «El problema es que a ti pueden hacerte exactamente lo mismo.»

- **Qué se ve:** escena oscura. Un **reflejo** (`.reflejo`, marco plano) proyecta el montaje anterior
  (las cuatro vallas) **sobre tu rótulo**, que ahora dice **«TU NEGOCIO»**. El caso ajeno se vuelve el
  tuyo: a ti pueden hacerte lo mismo. Chip **«LO MISMO»**.
- **Elementos:** `#s7-in` · `#s7-calle` · `#s7-kicker` · `#s7-reflejo` (`.reflejo` + `.brillo`) ·
  `#s7-rotulo` (`.rotulo` «TU NEGOCIO») · `#s7-vallas` (`.vallas` con cuatro `.valla.rival`) ·
  `#s7-note` (`.chip` «LO MISMO»).
- **Receta (rel):** `rise("#s7-calle", at(7,0.0))` · `rise("#s7-reflejo", at(7,0.0))` ·
  `put("#s7-kicker", at(7,0.06),{dur:0.4})` · `put("#s7-rotulo", cue(7,"ti"),{y:20,dur:0.26})` ·
  `put("#s7-vallas .valla", cue(7,"mismo"),{y:-16,dur:0.24,stagger:0.06})` ·
  `put("#s7-note", at(7,2.60),{y:14,dur:0.26})`.
- **Rótulo en pantalla:** kicker **«TU VERSIÓN»**; rótulo **«TU NEGOCIO»**; chip **«LO MISMO»**.
- **Sonido:** whoosh local 0,0 (entra el reflejo) · pop cue(7,"ti") ·
  swoosh_down cue(7,"mismo")+0,00/0,06 (las vallas reflejadas) · ding local 2,60.
- **Salida:** **desplazamiento continuo ↑ 0,40 s** (oscuro → claro).

## B8 · La práctica — «Ahí entra la defensa: pagar por tu propio nombre.»

- **Qué se ve:** papel claro. El **rótulo** de Basecamp y, en el **sitio de delante**, una **puja** que
  sube; **tu valla propia** (acento de relleno con tinta encima) **ocupa ese sitio**: la defensa es pagar
  por tu propio nombre. Chip **«DEFENSA»**.
- **Elementos:** `#s8-in` · `#s8-calle` · `#s8-kicker` · `#s8-rotulo` (`.rotulo`) · `#s8-brand`
  (`.brandmark.sm`) · `#s8-puja` (`.puja`) · `#s8-valla` (`.valla.propia`) · `#s8-label` (`.chip`
  «DEFENSA»).
- **Receta (rel):** `rise("#s8-calle", at(8,0.0))` · `rise("#s8-rotulo", at(8,0.0))` ·
  `put("#s8-kicker", at(8,0.06),{dur:0.4})` · `put("#s8-label", cue(8,"defensa"),{scale:0.86,dur:0.26})` ·
  `put("#s8-puja", cue(8,"pagar"),{y:20,dur:0.28})` ·
  `put("#s8-valla", cue(8,"nombre"),{y:-20,dur:0.28})`.
- **Rótulo en pantalla:** kicker **«LA PRÁCTICA»**; marca **Basecamp**; chip **«DEFENSA»**; la valla
  propia (acento) con `ANUNCIO`.
- **Sonido:** pop cue(8,"defensa") · swoosh_up cue(8,"pagar") · ding cue(8,"nombre").
- **Salida:** **desplazamiento continuo ↑ 0,40 s** (claro → claro).

## B9 · El caso (la protesta) — «Basecamp llegó a protestar en el anuncio: «No queremos publicar este anuncio».»

- **Qué se ve:** papel claro. La **valla-protesta** (cartel oscuro) con el logotipo **Basecamp** y la
  etiqueta **`ANUNCIO`**; el **titular entrecomillado** **«No queremos publicar este anuncio»** aparece
  **palabra por palabra** y, al cerrarse las comillas, queda **resaltado** con una cortina de acento
  (relleno, con tinta encima). Basecamp compró su propio nombre y usó el anuncio para protestar.
- **Elementos:** `#s9-in` · `#s9-calle` · `#s9-kicker` · `#s9-valla` (`.valla.protesta`) · `#s9-brand`
  (`.brandmark.sm`) · `#s9-adlab` (`.vallalab` «ANUNCIO») · `#s9-quote` (`.quote` con palabras en
  `span`) · `#s9-hl` (`.hl`) · `#s9-cover` (`.cover`, pieza de transición).
- **Receta (rel):** `rise("#s9-calle", at(9,0.0))` · `rise("#s9-valla", at(9,0.0))` ·
  `put("#s9-kicker", at(9,0.06),{dur:0.4})` · `put("#s9-brand", cue(9,"Basecamp"),{scale:0.9,dur:0.24})` ·
  `put("#s9-quote", cue(9,"protestar"),{y:16,dur:0.26})` ·
  `put("#s9-adlab", cue(9,"anuncio"),{y:12,dur:0.24})` ·
  `typeWords("#s9-quote span", cue(9,"No"),0.16)` ·
  `fromTo("#s9-hl",{scaleX:0},{scaleX:1,dur:0.30,ease:"power2.out"}, cue(9,"anuncio",2))` (origen
  `transform-origin:left center` en CSS).
- **Rótulo en pantalla:** kicker **«LA PROTESTA»**; marca **Basecamp**; **`ANUNCIO`**; el titular
  entrecomillado resaltado.
- **Sonido:** pop cue(9,"protestar") · swoosh_up cue(9,"anuncio") ·
  tick cue(9,"No") (offset por palabra 160 ms, ganancia baja) · ding cue(9,"anuncio",2).
- **Salida:** **objeto que cubre (`.cover`) 0,45 s** — el panel `#20202a` crece desde la valla-protesta y
  despeja la escena oscura de la consecuencia (claro → oscuro).

## B10 · La práctica — «Si nadie puja por tu marca, pagas clics que ya eran tuyos.»

- **Qué se ve:** escena oscura. El **rótulo** de Basecamp con el sitio de delante **sin dueño**: una
  **puja vacía** (trazo discontinuo, «sin postor»), chip **«SIN PUJA»**. Los **clics** llegan a buscar tu
  nombre y, al no haber puja, **se desvían hacia la valla ajena** que ocupa el sitio: pierdes clics que
  ya eran tuyos. Los clics desviados **se marcan en rojo** (único uso de `warn`: una pérdida real).
- **Elementos:** `#s10-in` · `#s10-calle` · `#s10-kicker` · `#s10-rotulo` (`.rotulo`) · `#s10-brand`
  (`.brandmark.sm`) · `#s10-puja` (`.puja.vacia`) · `#s10-note` (`.chip` «SIN PUJA») · `#s10-valla`
  (`.valla.rival`) · `#s10-clics` (`.clics` con `#s10-c1`…`#s10-c3` `.clic`).
- **Receta (rel):** `rise("#s10-calle", at(10,0.0))` · `rise("#s10-rotulo", at(10,0.0))` ·
  `rise("#s10-valla", at(10,0.0))` · `put("#s10-kicker", at(10,0.06),{dur:0.4})` ·
  `put("#s10-puja", cue(10,"puja"),{y:20,dur:0.28})` ·
  `put("#s10-note", cue(10,"puja")+0.10,{scale:0.86,dur:0.24})` ·
  `put("#s10-clics .clic", cue(10,"clics"),{scale:0.6,dur:0.22,stagger:0.08})` ·
  `to("#s10-clics",{x:132,y:-168,dur:0.50,ease:"power2.inOut"}, cue(10,"tuyos"))` (los clics se van con
  la valla ajena) · `to("#s10-clics .clic",{color:"#ff5a5a",dur:0.30}, cue(10,"tuyos"))` (rojo
  funcional: la pérdida).
- **Rótulo en pantalla:** kicker **«LA CONSECUENCIA»**; marca **Basecamp**; chip **«SIN PUJA»**; `ANUNCIO`
  en la valla ajena.
- **Sonido:** pop cue(10,"puja") · tick cue(10,"clics")+0,00/0,08/0,16 (las fichas) ·
  swoosh_down cue(10,"tuyos") (se las lleva la valla ajena).
- **Salida:** **corte directo** (oscuro → claro).

## B11 · Cierre — «Guarda esto: busca tu nombre en Google y mira quién aparece antes que tú.»

- **Qué se ve:** papel claro. El **marcador de guardado** con la **onda** que se dibuja y el rótulo
  **«Guarda esto»**. Debajo, la **barra de búsqueda** con tu nombre y, **por encima**, las **vallas
  ajenas** que aparecen *antes que tú*; tu **rótulo** con tu **valla propia** (acento) delante. Cierra
  enlazando la CTA con la micro-acción: **busca tu nombre y mira quién aparece antes que tú**.
- **Elementos:** `#s11-in` · `#s11-calle` · `#s11-mark` (`.cta-mark`) · `#s11-label` (`.cta-label`
  «Guarda esto») · `#s11-wave` (`.savewave`) · `#s11-search` (`.searchbar`) · `#s11-term` (`.sterm`,
  tecleado) · `#s11-vallas` (`.vallas` con `.valla.rival` ×2-3) · `#s11-rotulo` (`.rotulo`) ·
  `#s11-brand` (`.brandmark.sm`) · `#s11-valla` (`.valla.propia`).
- **Receta (rel):** `rise("#s11-calle", at(11,0.0))` · `rise("#s11-rotulo", at(11,0.0))` ·
  `rise("#s11-search", at(11,0.0),{y:24})` · `grow("#s11-mark", at(11,0.0),1,{from:0.6,dur:0.18})` (el
  marcador nace visible en el fotograma 0: el corte B10→B11 no debe dejar tramo vacío) ·
  `put("#s11-label", cue(11,"Guarda"),{scale:0.86,dur:0.5})` ·
  `draw("#s11-wave", cue(11,"Guarda")+0.40,0.5)` ·
  `typeChars("#s11-term", cue(11,"busca"),0.05)` ·
  `put("#s11-vallas .valla", cue(11,"antes"),{y:-16,dur:0.24,stagger:0.06})` ·
  `put("#s11-valla", at(11,0.0))` · `put("#s11-note", at(11,3.60),{y:14,dur:0.26})`.
- **Rótulo en pantalla:** **«Guarda esto»** (96 px); sin kicker; chip **«TU NOMBRE, DEFENDIDO»**.
- **Sonido:** pop local 0,0 (el marcador) · ding cue(11,"Guarda")+0,45 (la onda) ·
  swoosh_up cue(11,"busca") · tick cue(11,"antes")+0,00/0,07 (las vallas) · ding local 3,60 (cierre).
- **Salida:** — (fin).

---

## Recursos

| Recurso | Tipo | Origen |
|---|---|---|
| Fuentes, voz `Pablo`, música, efectos, karaoke, barra de progreso | — | Reutilizado (kit) |
| `.scene`, `.s-in`, `.kicker` (+`.dot`), `.card`, `.chip`, `.pill`, `.tag`, `.stage` | HTML/CSS | Reutilizado (kit) |
| Marcador de guardado + onda (`.cta-mark`, `.cta-label`, `.savewave`) | HTML/SVG | Reutilizado (kit / GA4) |
| **Barra de búsqueda** (`.searchbar`, `.sicon`, `.sterm`, `.scaret`) | HTML/CSS/SVG | Reutilizado (kit `mkt-02`), aquí **con pila de vallas** |
| **Logotipo tipográfico** (`.brandmark`) y **año** (`.yearbadge`), **resaltado** (`.hl`) | HTML/CSS | Reutilizado (kit `mkt-01`/`mkt-02`) |
| **Figuras 2D** (`.gente`, `.fig`) | HTML/SVG | Reutilizado (lenguaje de la casa) |
| **La calle** (`.calle`, `.aire`, `.acera`, `.borde`) | HTML/CSS | **Nuevo** (entorno) |
| **El rótulo** (`.rotulo`, `.placa`, `.poste`, `.redact`) | HTML/CSS | **Nuevo** (la marca) |
| **La valla** (`.valla`, `.tablon`, `.poste`, `.vallalab`, `.vallatxt`, `.vallas` + `.rival`/`.propia`/`.protesta`) | HTML/CSS | **Nuevo** (el recurso propio) |
| **La puja** (`.puja`, `.palo`, `.placa`, `.vacia`) | HTML/SVG | **Nuevo** |
| **El clic** (`.clics`, `.clic`, `.perdido`) | HTML/SVG | **Nuevo** |
| **El reflejo** (`.reflejo`, `.brillo`) | HTML/CSS | **Nuevo** |
| **El foco** (`.foco`, `.haz`) | HTML/SVG | **Nuevo** |
| **Titulares nuevos** (`.hookline`, `.contador`, `.quote`) | HTML/CSS | **Nuevo** |
| Capas de transición `.cover` y `.sweep` | HTML/CSS | **Nuevo** (piezas propias) |
| Collage (manos, personas, objetos) o imágenes de red | PNG | **Descartado**: no hay material y la marca va como logotipo tipográfico |
| Render, vídeo con alfa o 3D | — | No se necesita |

## Ritmo y sonido por beat

> **Nota (sonido anclado al cue).** Un efecto que acompaña a un elemento entra **en el instante de su
> cue** (imagen y voz no se separan), no en el arranque de la escena: el detalle y la regla están en
> `DIRECCION.md` §12 «Sonido» y en `assets/sfx/events.json` (`"cue"` + `"offset"`). Solo B1 (sin cues:
> todo montado en el fotograma 0) y los `whoosh` de transición se anclan distinto: los efectos de B1 con
> `"local"` y los `whoosh` al **instante visual del corte** (medido, no nominal).

| # | Movimiento o lectura | Entrada | Desarrollo | Lectura | Transición | Efectos (anclados al cue) |
|---|---|---|---|---|---|---|
| B1 | Movimiento | 0,0-0,4 | 0,4-1,3 | 1,3-fin | 0,45 | whoosh local 0,0 · pop local 0,55 · ding local 1,20 |
| B2 | Movimiento | 0,0-0,4 | 0,4-2,4 | 2,4-fin | 0,40 | pop @competencia · pop @clientes · tick @nombre · ding local 2,50 |
| B3 | Movimiento | 0,0-0,5 | 0,5-2,8 | 2,8-fin | 0,40 | whoosh local 0,40 · ding @Google · pop @ataque · key @buscan · swoosh_up @rival |
| B4 | Movimiento | 0,0-0,4 | 0,4-1,5 | 1,5-fin | 0,35 | pop @Basecamp · tick @2019 · ding local 1,60 |
| B5 | Movimiento | 0,0-0,5 | 0,5-3,2 | 3,2-fin | 0,40 | key @buscar · swoosh_up @cuatro · tick @cuatro (×4) · tick @cuatro+0,38 (contador) · ding @competidores |
| B6 | Lectura | 0,0-0,5 | 0,5-2,4 | 2,4-fin | 0,45 | pop @quien · pop @marca · swoosh_up @comparando · ding @elegir |
| B7 | Movimiento | 0,0-0,4 | 0,4-2,5 | 2,5-fin | 0,40 | whoosh local 0,0 · pop @ti · swoosh_down @mismo (×2) · ding local 2,60 |
| B8 | Movimiento | 0,0-0,4 | 0,4-1,4 | 1,4-fin | 0,40 | pop @defensa · swoosh_up @pagar · ding @nombre |
| B9 | Lectura | 0,0-0,5 | 0,5-3,3 | 3,3-fin | 0,45 | pop @protestar · swoosh_up @anuncio(1) · tick @No (×palabras) · ding @anuncio(2) |
| B10 | Movimiento | 0,0-0,4 | 0,4-3,2 | 3,2-fin | 0,00 | pop @puja · tick @clics (×3) · swoosh_down @tuyos |
| B11 | Lectura | 0,0-0,5 | 0,5-3,4 | 3,4-fin | — | pop local 0,0 · ding @Guarda+0,45 · swoosh_up @busca · tick @antes (×2) · ding local 3,60 |

Se alterna movimiento con lectura: B1 mov · B2 mov · B3 mov · B4 mov · B5 mov · B6 lec · B7 mov ·
B8 mov · B9 lec · B10 mov · B11 lec. **Un efecto por aparición**, nunca por palabra.

## Ritmo — tabla calculada a 3,2 palabras/segundo

Total del guion: **119 palabras**. A **3,2 palabras/s** (el ritmo real de la voz `Pablo` medido en
`mkt-01`: 121 pal. / 37,52 s ≈ 3,22 pal./s), **119 ÷ 3,2 ≈ 37,2 s**. Los tiempos definitivos los fija
`voice_pipeline.py` y los aplica `retime.py`; toda la animación está en tiempos **relativos** al inicio
de su beat. La tabla es **estimada** y cuadra palabra a palabra con `SCRIPT.md`.

| Beat | Pal. | Dur. (s) | Inicio (s) | Fin (s) |
|---|---|---|---|---|
| B1 | 7 | 2,188 | 0,000 | 2,188 |
| B2 | 10 | 3,125 | 2,188 | 5,313 |
| B3 | 14 | **4,375** | 5,313 | 9,688 |
| B4 | 6 | 1,875 | 9,688 | 11,563 |
| B5 | 11 | 3,438 | 11,563 | 15,000 |
| B6 | 13 | 4,063 | 15,000 | 19,063 |
| B7 | 11 | 3,438 | 19,063 | 22,500 |
| B8 | 9 | 2,813 | 22,500 | 25,313 |
| B9 | 12 | 3,750 | 25,313 | 29,063 |
| B10 | 12 | 3,750 | 29,063 | 32,813 |
| B11 | 14 | **4,375** | 32,813 | **37,188** |

**Total: 119 palabras · 37,188 s ≈ 37,2 s** (dentro de la banda 30-40 s). **Cuadre:** la suma de
palabras de la tabla es 7+10+14+6+11+13+11+9+12+12+14 = **119** = `SCRIPT.md` = carrera del karaoke =
`assets/voice/*.txt`.

**Excepciones de duración (estimadas).** La escena más corta es **1,875 s** (B4; el mínimo del contrato
es 1,2 s) y **dos escenas superan el techo de 4,2 s** del contrato §5: **B3 = 4,375 s** y **B11 =
4,375 s**, por la longitud de la frase (14 palabras cada una) al ritmo de `Pablo`. **No se parten** —el
guion es del dueño y la locución la fija `voice_pipeline.py`—: misma excepción aceptada en `mkt-01`
(D39), V6 (D38) y `mkt-02`. El resto queda por debajo de 4,2 s (máximo: B6 = 4,063 s).

## Tabla de cues (qué elemento entra con qué palabra)

El instante se calcula con `cue(línea, palabra, [ocurrencia])`, el **mismo reparto por longitud** que el
karaoke: `S[n-1] + clip[n]·Σlen(palabras anteriores)/Σlen(línea)`. Los **instantes** de la columna son
**estimados** a 3,2 pal./s (los reales los fija `retime.py`); el **elemento entra ≤ 0,3 s después**. La
ocurrencia se indica entre corchetes cuando la palabra se repite.

| Beat | Palabra (occ) | Inst. est. (s) | Elemento que entra |
|---|---|---|---|
| B2 | competencia | 2,292 | figura rival (`.fig.rival`) **y** su valla (`.valla.rival`) |
| B2 | clientes | 3,646 | los clientes interceptados (`.gente` ×2) |
| B2 | nombre | 4,948 | el nombre de la víctima en la valla ajena (`#s2-name`, raído) |
| B3 | Google | 7,924 | el logotipo de la plataforma (`.brandmark` «Google») |
| B3 | ataque | 6,814 | el término (`.chip` «ANUNCIOS DE ATAQUE») |
| B3 | buscan | 8,708 | el nombre del rival tecleado (`typeChars`) |
| B3 | rival | 9,296 | tu valla que brota por encima (`.valla.rival`) |
| B4 | Basecamp | 10,528 | la marca (`.brandmark`; cae la censura) |
| B4 | 2019 | 11,239 | el año (`.yearbadge`) |
| B5 | buscar | 11,667 | el nombre propio tecleado (`typeChars` «Basecamp») |
| B5 | cuatro | 13,490 | las **cuatro** vallas ajenas (`.vallas`, stagger) **y** el contador `4` (`setNum`) |
| B5 | competidores | 14,323 | el chip «DE COMPETIDORES» |
| B6 | quien | 15,917 | el cliente que busca (`.gente`) **y** la etiqueta «TU CLIENTE» |
| B6 | marca | 16,769 | las dos opciones (dos `.rotulo.rival`) |
| B6 | comparando | 17,359 | el foco doble (`.foco` ×2, comparación) |
| B6 | elegir | 18,604 | el sesgo del cliente hacia una opción (`.sub`) |
| B7 | ti | 20,163 | tu rótulo «TU NEGOCIO» (`.rotulo`) |
| B7 | mismo | 22,087 | las cuatro vallas reflejadas (`#s7-vallas`) |
| B8 | defensa | 23,186 | la etiqueta «DEFENSA» (`.chip`) |
| B8 | pagar | 23,735 | la puja (`.puja`) |
| B8 | nombre | 24,832 | tu valla propia (`.valla.propia`, acento) |
| B9 | Basecamp | 25,313 | la marca en la valla-protesta (`.brandmark.sm`) |
| B9 | protestar | 26,096 | el titular entrecomillado, contenedor (`.quote`) |
| B9 | anuncio [1] | 26,824 | la etiqueta `ANUNCIO` (`.vallalab`) |
| B9 | No | 27,271 | el titular, palabra a palabra (`typeWords`) |
| B9 | anuncio [2] | 28,559 | el resaltado del titular (`.hl`, cortina de acento) |
| B10 | puja | 29,621 | la puja vacía (`.puja.vacia`) **y** el chip «SIN PUJA» |
| B10 | clics | 31,217 | las fichas de clic (`.clic` ×3) |
| B10 | tuyos | 32,334 | los clics **se van** con la valla ajena (`.to` + rojo `#ff5a5a`) |
| B11 | Guarda | 32,813 | el marcador de guardado **y** su onda (`draw`) |
| B11 | busca | 33,615 | el buscador con tu nombre (`typeChars`) |
| B11 | antes | 36,385 | las vallas ajenas que aparecen antes que tú (`#s11-vallas`) |

**32 cues** declarados (B1 no tiene cues: todo va montado en el fotograma 0).

## Reparto de rótulos

| Beat | Kicker (32 px, mayúsculas) | Etiquetas / rótulos en pantalla |
|---|---|---|
| B1 | **— (sin kicker, regla vinculante)** | el **texto del gancho** (132 px) · rótulo **raído** con `?` |
| B2 | EL CASO | `ANUNCIO` (valla ajena) · nombre **raído** de la víctima |
| B3 | EL MECANISMO | marca **Google** · nombre del rival (mono) · chip **ANUNCIOS DE ATAQUE** |
| B4 | LA EMPRESA | marca **Basecamp** · año **2019** |
| B5 | EL DATO | **Basecamp** (mono, tecleado) · `ANUNCIO` ×4 · contador **4** · chip **DE COMPETIDORES** |
| B6 | POR QUÉ | etiqueta **TU CLIENTE** |
| B7 | TU VERSIÓN | rótulo **TU NEGOCIO** · chip **LO MISMO** |
| B8 | LA PRÁCTICA | marca **Basecamp** · chip **DEFENSA** · `ANUNCIO` (valla propia) |
| B9 | LA PROTESTA | marca **Basecamp** · `ANUNCIO` · titular **«No queremos publicar este anuncio»** resaltado |
| B10 | LA CONSECUENCIA | marca **Basecamp** · chip **SIN PUJA** · `ANUNCIO` (valla ajena) |
| B11 | **— (CTA)** | **Guarda esto** (96 px) · chip **TU NOMBRE, DEFENDIDO** |

Regla: rótulos **nominales en mayúsculas, sin numerar** (decisión de `DIRECCION.md` §10), **nunca
repiten la voz** —salvo el **texto del gancho** (B1, lo pide `SCRIPT.md`) y el **titular citado** del
anuncio-protesta (B9, object citado). Lo que alguien **escribe o busca** (el nombre tecleado, el nombre
del rival) va en JetBrains Mono.

## Revisión antes de dar por bueno el vídeo

**11 beats** en orden, cada uno con su línea exacta de `SCRIPT.md`; **B1 sin rótulo de tema** (solo el
texto del gancho). Un fotograma de lectura de cada escena · los instantes intermedios de las
transiciones con tratamiento especial (`cover` B1→B2 y B9→B10; `sweep` B6→B7; el corte final B10→B11 es
directo) · entradas, salidas y superposiciones · **luminancia y % de filas con contenido del fotograma
0** (miniatura: ≥ 200/255 y ≈ 100 %) · legibilidad a tamaño móvil · alineación de texto e interfaces ·
**sincronía con la voz medida sobre el render** con `.openhands/tools/medir_sync.py` (10 cortes
|audio−imagen| ≤ 0,04 s y 32 cues por zona ≤ 0,06 s) · y el MP4 completo en movimiento.
