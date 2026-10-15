# Brief de dirección de arte — mkt-03 «Anuncios de ataque (Basecamp, 2019)»

Serie **Casos de estudio marketing** · Pieza **mkt-03** · 9:16 · 1080×1920 · faceless · voz en off es-ES
(`Pablo`) · subtítulos karaoke · barra de progreso. **11 beats · 119 palabras · ≈37,2 s**.
Guion cerrado: `SCRIPT.md` (no se toca). Contrato de producción heredado **tal cual**:
`videos/seo-06-canibalizacion/investigacion/03-contrato.md`. Continuidad de la línea:
`videos/mkt-01-responde-con-video/investigacion/02-continuidad.md`. Lenguaje visual vigente y formato:
`videos/mkt-02-google-ads-trafico-correcto/` (`DIRECCION.md`, `DIRECCION-ARTE-BRIEF.md`, `STORYBOARD.md`,
`index.html`).

> Este fichero fija **qué tiene que conseguir la pieza** (efecto, restricciones, recursos, vetos y lo que
> queda pendiente). Cómo se resuelve está en `DIRECCION.md`; el desglose por línea y la tabla de cues,
> en `STORYBOARD.md`. Es la tercera pieza de la línea, así que imita el formato de entregables de
> `mkt-02` y hereda su **lenguaje 2D** (figuras y entornos dibujados con SVG en línea + CSS, planos, dos
> colores más el acento como relleno; aparecen **cuando la voz los nombra**).

---

## 1. Efecto buscado en el espectador

Tres cosas, en este orden:

1. **Picar la curiosidad en el primer segundo.** El **beat 1 es un gancho de curiosidad puro** y es la
   **miniatura del reel** (se publica sin portada): en pantalla va **solo la frase del gancho**, **sin
   rótulo de tema, sin nombre de la línea y sin kicker**. El espectador tiene que quedarse con la intriga
   («algo que no imaginas») y querer saber de qué va; la revelación del tema llega en B2-B4. Es una regla
   **vinculante** del dueño (`BRIEF.md` §«Decisión de dirección»), heredada del guion.
2. **Entender la tesis.** Al buscar el nombre de una marca, **los anuncios que van por encima se pueden
   comprar**: un competidor puede anunciarse con **tu** nombre y llevarse clics que ya eran tuyos. El
   caso es la **prueba**: **Basecamp**, en **2019**, con **hasta cuatro anuncios de competidores** al
   buscar su propio nombre. La lección: **la defensa es pagar por tu propia marca**.
3. **Llevarse una acción.** La micro-acción de cierre: **buscar tu nombre en Google y mirar quién
   aparece antes que tú**. Cierra con la CTA de guardar de la serie.

**Tono:** el gancho **no** usa el mecanismo de «error» de la serie SEO ni la pregunta con cifra de
`mkt-02`; arranca con una **promesa de curiosidad** y **una imagen tapada** (la marca sin desvelar).
Se cuenta primero el hecho (B2-B5) y solo después se traduce al negocio del espectador (B7-B11). Sin
cifras fuera del guion, **sin promesas de resultados** y con **un solo ejemplo**: el negocio del
espectador, con su propio nombre de marca (el caso de Basecamp es prueba, no segundo ejemplo).

**Promesa visual:** el vídeo se entiende en mudo por **gráfico + karaoke**, no por texto recargado
(`DESIGN.md` §0). La complejidad sale de coordinar capas, no de acumular recursos.

---

## 2. Restricciones del dueño (duras)

- **Paleta del sistema** (claro de papel / oscuro de carbón) con **un solo acento** (`#c8ff3d`). El
  acento es **siempre relleno con tinta `#0b0b10` encima**; **prohibido como texto o trazo sobre claro**.
  **Panel oscuro nunca por debajo de `#20202a`** (el medidor de montaje cuenta filas con luminancia
  media > 25).
- **El rojo (`warn`) solo para una pérdida real.** Esta pieza **sí tiene una pérdida**: los clics que
  acaban en el rival (B10, «pagas clics que ya eran tuyos»). Es el **único** uso de `warn` de la pieza
  (contrato §2: «`warn` marca lo que *pierde*… funcional, no decorativo»). En el resto de escenas no
  hay error ni pérdida, así que no se usa rojo.
- **El fotograma 0 es la miniatura**: luminancia ≈ **230/255** y **≈ 100 % de filas con contenido**.
  Nada de abrir con pantalla vacía, con desvanecidos ni con el marco entrando tarde.
- **Un escenario visible desde `t=0` en cada escena**, que se asienta con `rise()` (sin animar su
  opacidad). Nacer en `opacity:0` deja los cruces vacíos.
- **Tipografía:** protagonista 110-180 px · frase 70-110 · contexto 38-56 · kicker 32 fijo · CTA
  «Guarda esto» 96 · rótulos menores 22-37 (`DIRECCION.md` §3). **Un solo foco dominante por escena.**
- **Banda segura 15 %-75 % de la altura** (288-1440 px de 1920): texto y marcas dentro de
  `padding: 300px 74px 700px`; nada crítico en el 15 % superior ni el 25 % inferior.
- **Seek-safe:** estado inicial en CSS; animar con `fromTo` / `.to()`. **Prohibido** `.from()`,
  `Math.random`, `Date.now`, contadores que suben (los números se fijan con `setNum(sel, txt, t)`),
  CSS `transition`/`@keyframes` y `repeat`/`yoyo`. En los **barridos**, `x: 0` explícito.
- **Cada elemento que la voz nombra entra cuando se dice la palabra**, con el reparto por palabra del
  helper `cue(línea, palabra, [ocurrencia])` (el mismo que el karaoke); entrada **≤ 0,3 s**.
- **Cadena obligatoria:** `retime.py` → `transiciones.py` → `check` → render. Nunca a mano.
- **`check` con 0 errores** y contraste WCAG AA; cruces sin tramo vacío ≤ 0,15 s; audio sin huecos
  > 0,12 s.
- **Nada de red, nada de aleatoriedad**, ningún aviso de autoría ni mención a IA.

---

## 3. Recursos disponibles

- **Fuentes** `Inter` (400/600/700/800/900) + `JetBrains Mono` (600/800), vendorizadas en
  `assets/fonts/` (`@font-face`, sin red en el render). Medir el texto tras `document.fonts.ready`.
- **Voz** Fish Audio **`Pablo`** (`reference_id 1bd666ea8ada44c789e0fec21cf78f33`), cola 0,08 s.
- **Música** `assets/music/track.wav` (vol. 0,18) y **efectos** `assets/sfx/sfx.wav` (vol. 0,5),
  sintetizados de forma determinista (9 tipos: `whoosh, pop, tick, click, swoosh_up, swoosh_down,
  ding, thud, buzz`).
- **Karaoke** `caption-pill-karaoke` + `TRANSCRIPT` con tiempos absolutos.
- **Helpers** en `index.html`: `put`, `rise`, `draw`, `grow`, `bar`, `typeWords`, `typeChars`, `swap`,
  `setNum`, y `cue(línea, palabra, occ)` que reparte por longitud de palabra.
- **Kit reutilizado** (CSS/SVG inline, sin banco de imágenes ni generación): `.scene`, `.s-in`,
  `.kicker` (+`.dot`), `.card`, `.chip`, `.pill`, `.tag`, `.stage`, `.cta-mark`/`.cta-label`/`.savewave`,
  `.progress`/`#prog-fill`, la **barra de búsqueda** `.searchbar`, el **logotipo tipográfico**
  `.brandmark` (tinta sobre tarjeta clara), el **año** `.yearbadge` y el **resaltado** `.hl`.
- **Recurso propio de la pieza:** **la valla** (el anuncio) y **su pila por delante del rótulo** — al
  buscar una marca, **varias vallas de rivales brotan por encima** de su propio resultado. Es distinto
  del anuncio único de `mkt-02` y del blanco, la burbuja, la SERP y la balanza. Piezas propias de
  transición: `.cover` (B1→B2 y B9→B10) y `.sweep` (B6→B7).

**Lenguaje 2D (heredado de `mkt-02`, detalle en `DIRECCION.md` §12).** Personajes y entornos se
**dibujan en la propia composición** con **SVG en línea + CSS**: plano, geométrico, de **dos colores**
(`ink` + `muted`) más el acento **solo como relleno**, legible a tamaño pequeño. Aparecen **cuando la
voz los nombra**: el instante sale de `cue(línea, palabra)`, y la figura entra **≤0,3 s** después con
`put()`. Aquí las **figuras** son: el **cliente** que busca y elige (B6, B11), los **clientes
interceptados** (B2) y la **figura rival** que clava su valla (B2). Los **entornos** son la **calle**
y el **rótulo** de cada marca (B1, B4, B5, B7-B11). Nada de red, nada de bitmap.

---

## 4. Qué hay que evitar

- **Ejemplos ya gastados:** nada de «cafetera» (V5), «instalación de luz» (V6), «agencias de diseño
  baratas» (V1), «zapatillas baratas» (V2), el 3 vs 118 y Search Console → Enlaces (V3), los caminos de
  instalación y el chip `G-XXXXXXXXXX` (GA1), la **tienda de ropa** (mkt-01) ni los términos
  «abogado»/«dentista» (mkt-02). Aquí el único ejemplo es **el negocio del espectador** con su propio
  nombre de marca.
- **Aperturas gastadas:** el gancho no usa el «error» («Este error te hará bajar posiciones…», V6;
  «Este es el error…», V5; «Tu web no sube…», V3) ni la pregunta con cifra de `mkt-02` («¿Cuántos
  contactos…?») ni el arranque de `mkt-01` («La estrategia que usó esta conocida marca…»).
- **Recursos visuales ya muy vistos:** el **blanco/mira** de `mkt-02`, la **burbuja de comentario** de
  `mkt-01`, la **SERP etiquetada** de V5 y la **balanza de dos platos** de V6 quedan fuera; **la
  metáfora central es nueva** (§ `DIRECCION.md` §1). Tampoco se reutiliza **la barra de búsqueda de un
  solo anuncio** de `mkt-02`: la de esta pieza **apila varias vallas**.
- **Vocabulario de otras series:** no se reutiliza el de SEO (autoridad, enlaces, canibalización, SERP)
  ni el de GA4 (cuenta, propiedad, flujo, etiqueta, contenedor).
- **Marcas:** sin `@handle`/arroba en pantalla y sin ningún adorno de autoría o IA; sin sugerir
  afiliación ni usar la marca como hashtag.
- **Cifras inventadas, promesas de resultados, ganchos por miedo, anglicismos innecesarios.**
- **Texto que repita lo que dice la voz** (`DESIGN.md` §0): el peso lo lleva el gráfico. **Única
  excepción:** el **texto del gancho** en B1 (lo pide `SCRIPT.md`: «Solo el texto del gancho») y la
  **frase entrecomillada del anuncio** en B9 (el anuncio es un objeto citado, como el texto del anuncio
  de `mkt-02`).
- **Cualquier cosa aleatoria o no determinista** y **cualquier `.from()` / `repeat` / `yoyo`**.

---

## 5. Uso de la marca ajena (Basecamp y Google)

- **La marca se representa con su nombre escrito como logotipo tipográfico**: **tinta `#14141a` sobre
  tarjeta clara `#ffffff`**, **en línea**. `Basecamp` (la marca del caso, B4, B5, B8-B11) y `Google` (la
  plataforma, B3, B11). **Sin arroba**, **sin descargar ninguna imagen de red** (nada de logos de color
  ni capturas) y **sin sugerir afiliación**. Es la misma solución autorizada para `mkt-01` y `mkt-02`
  (`PROFILE.md:39`, «el logo de la marca cuando se la nombra, en línea sobre tarjeta clara»).
- **Nada más queda pendiente del dueño:** las cifras, el ejemplo único y la duración están resueltos en
  `SCRIPT.md` / `BRIEF.md` (sin pasada de fuentes, por decisión expresa del dueño).

---

## 6. Barras de calidad (revisión antes de dar el vídeo por bueno)

- `check` sin errores; contraste WCAG AA (texto normal ≥ 4,5:1; grande ≥ 3:1).
- **Fotograma 0** (B1): luminancia ≥ 200/255 y ≈ 100 % de filas con contenido, medido con
  `verificar_montaje.py`.
- **Cruces sin tramo vacío** ≤ 0,15 s por fotograma a 30 fps (umbral fijo 25): revisar los instantes
  intermedios de `cover` (B1→B2 y B9→B10) y `sweep` (B6→B7); B10→B11 es corte directo.
- **Audio sin huecos** > 0,12 s por debajo de −48 dBFS.
- **Sincronía de sonido medida sobre el render** (`.openhands/tools/medir_sync.py`): cortes
  |audio−imagen| ≤ 0,04 s y cues por zona ≤ 0,06 s; los efectos de elemento se atan a su **cue** y los
  `whoosh` de transición al **instante visual del corte** (`DIRECCION.md` §12 «Sonido» y «Regla de
  sonido»).
- Un fotograma de lectura por escena · alineación de texto e interfaces · sincronía con la voz · el MP4
  completo en movimiento.
