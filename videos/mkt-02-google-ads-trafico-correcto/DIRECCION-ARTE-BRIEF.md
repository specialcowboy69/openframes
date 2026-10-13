# Brief de dirección de arte — mkt-02 «El tráfico correcto (Google Job Experiment, 2010)»

Serie **Casos de estudio marketing** · Pieza **mkt-02** · 9:16 · 1080×1920 · faceless · voz en off es-ES
(`Pablo`) · subtítulos karaoke · barra de progreso. **11 beats · 123 palabras · ≈38,4 s**.
Guion cerrado: `SCRIPT.md` (no se toca). Contrato de producción heredado **tal cual**:
`videos/seo-06-canibalizacion/investigacion/03-contrato.md`. Continuidad de la línea:
`videos/mkt-01-responde-con-video/investigacion/02-continuidad.md`. Fuentes del dato:
`investigacion/01-fuentes.md`.

> Este fichero fija **qué tiene que conseguir la pieza** (efecto, restricciones, recursos, vetos y lo
> que queda pendiente). Cómo se resuelve está en `DIRECCION.md`; el desglose por línea, en
> `STORYBOARD.md`. Es la pieza hermana de `mkt-01`, así que imita su formato de entregables.

---

## 1. Efecto buscado en el espectador

Tres cosas, en este orden:

1. **Entender la idea en el primer segundo.** Quien lo vea tiene que entender «estoy preguntando
   cuánto tráfico puedo comprar con 6 euros en Google Ads» y, debajo, la intuición de que **la
   pregunta no es cuánto, sino a quién**. El fotograma 0 es la miniatura del reel (se publica sin
   portada), así que la **barra de búsqueda, la cifra `6 €` y el rótulo «EN GOOGLE ADS»** están
   montados y encendidos **desde el fotograma cero**, sin desvanecidos ni marco entrando tarde.
2. **Entender la tesis.** Alec Brownstein (2010) compró anuncios sobre los **nombres propios de cinco
   directores creativos** con **6 euros**; le llamaron **cuatro** y recibió **dos ofertas**. La
   lección: **en anuncios no gana más tráfico, gana el tráfico correcto**. El protagonista es una
   **persona ajena** que sirve de **prueba**, no de consejo; el espectador no es el héroe hasta
   «Eso mismo vale para tu negocio» (B8). La fuente recuerda que su objetivo era **una audiencia
   diminuta y muy concreta** (`01-fuentes.md` §4): la pieza **invita a probarlo, no promete
   resultados**.
3. **Llevarse una acción.** Antes de pujar por las palabras grandes de su gremio, **pensar qué
   buscaría tu cliente ideal** y quedarse con búsquedas pequeñas pero de altísima intención. Cierra
   con la CTA de guardar de la serie.

**Tono:** el gancho **no** usa el mecanismo de «error» de la serie SEO ni una apertura gastada;
arranca con **una pregunta con la cifra** y **una barra de búsqueda** (territorio propio, distinto del
reloj/mechero de `seo-05`). Se cuenta primero qué hizo Brownstein y solo después se traduce a un
negocio pequeño. Sin cifras fuera de las fuentes, sin promesas de resultados y con **un solo ejemplo**
(«abogado»/«dentista», el negocio del espectador).

**Promesa visual:** el vídeo se entiende en mudo por **gráfico + karaoke**, no por texto recargado
(`DESIGN.md` §0). La complejidad sale de coordinar capas, no de acumular recursos.

---

## 2. Restricciones del dueño (duras)

- **Paleta del sistema** (claro de papel / oscuro de carbón) con **un solo acento** (`#c8ff3d`). El
  acento es **siempre relleno con tinta `#0b0b10` encima**; **prohibido como texto o trazo sobre
  claro**. **Panel oscuro nunca por debajo de `#20202a`** (el medidor de montaje cuenta filas con
  luminancia media > 25).
- **El rojo (`warn`) solo para un error real.** Esta pieza **no tiene errores ni pérdidas
  documentadas**: el tachado de los términos genéricos «abogado»/«dentista» (B9) marca algo que *no
  conviene*, no algo que se pierde, así que va en **tinta**, no en rojo. La pieza **no usa `warn` en
  ningún beat**.
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
- **Helpers** en `index.html`: `put`, `rise`, `draw`, `grow`, `bar`, `typeWords`, `typeChars`,
  `swap`, `setNum`.
- **Kit reutilizado** (CSS/SVG inline, sin banco de imágenes ni generación): `.scene`, `.s-in`,
  `.kicker` (+`.dot`), `.card`, `.chip`, `.pill`, `.tag`, `.tile`, `.rowc`, `.stage`,
  `.cta-mark`/`.cta-label`/`.savewave`, `.progress`/`#prog-fill`.
- **Recurso propio de la pieza:** **el blanco (la mira) y la barra de búsqueda que se monta sobre
  él**. La metáfora central es **el blanco** (B1 lo estrena; B7 y B11 lo protagonizan) y la barra de
  búsqueda —con el anuncio que brota al teclear un nombre— la acompaña (B1, B3, B5). Piezas propias
  de transición: `.cover` (B2→B3) y `.sweep` (B6→B7). No se reutiliza el hilo de comentarios → vídeo
  de `mkt-01`, ni la **SERP etiquetada** de V5, ni la **balanza de dos platos** de V6.

**Lenguaje 2D (nuevo, heredable — detalle en `DIRECCION.md` §12).** Los personajes y entornos se
**dibujan en la propia composición** con **SVG en línea + CSS**: plano, geométrico, de **dos colores**
(`ink` + `muted`) más el acento **solo como relleno**, legible a tamaño pequeño. Aparecen **cuando la
voz los nombra**: el instante sale del helper `cue(línea, palabra)` = inicio de línea + posición
proporcional **ponderada por longitud de palabra** (el mismo reparto que el karaoke), y la figura entra
**≤0,3 s** después con `put()`, para que **la voz la traiga**. Se prefieren figuras a cartelas: Alec
(persona genérica) y la redacción con skyline (B2), los **cinco directores creativos** distintos (B3),
una figura por fila (B4), los cuatro que responden (B6), las **cinco personas** del cierre (B7/B8/B11)
y el cliente ideal (B9). Nada de red, nada de bitmap.

---

## 4. Qué hay que evitar

- **Ejemplos ya gastados:** nada de «cafetera» (V5), «instalación de luz» (V6), «agencias de diseño
  baratas» (V1), «zapatillas baratas» (V2), el 3 vs 118 y Search Console → Enlaces (V3) ni los
  caminos de instalación y el chip `G-XXXXXXXXXX` (GA1). Aquí el único ejemplo es **el negocio del
  espectador** con sus términos propios (**«abogado»**, **«dentista»**).
- **Aperturas gastadas:** el gancho no usa el «error» («Este error te hará bajar posiciones…», V6;
  «el error que hace que aparezcas cada vez menos…», V5; «Tu web no sube aunque hagas SEO», V3) ni el
  arranque de `mkt-01` («esta conocida marca…»).
- **Recursos visuales ya muy vistos:** la **SERP de Google etiquetada** (V5), la **balanza de dos
  platos** (V6) y la **burbuja de comentario** de `mkt-01` quedan fuera; **la metáfora central es
  nueva** (§ `DIRECCION.md` §1).
- **Vocabulario de otras series:** no se reutiliza el de SEO (autoridad, enlaces, canibalización,
  SERP) ni el de GA4 (cuenta, propiedad, flujo, etiqueta, contenedor).
- **Marcas:** sin `@handle`/arroba en pantalla y sin ningún adorno de autoría o IA.
- **Cifras inventadas, promesas de resultados, ganchos por miedo, anglicismos innecesarios.**
- **Texto que repita lo que dice la voz** (`DESIGN.md` §0): el peso lo lleva el gráfico.
- **Cualquier cosa aleatoria o no determinista** y **cualquier `.from()` / `repeat` / `yoyo`**.

---

## 5. Uso de la marca ajena (Google)

- **La plataforma se representa solo con su nombre escrito como logotipo**: la palabra `Google` como
  marca tipográfica, **tinta `#14141a` sobre tarjeta clara `#ffffff`**, **en línea** (B3, B5).
  **Sin arroba**, **sin descargar ninguna imagen de red** (nada de rombos de color ni capturas) y
  **sin sugerir afiliación** ni usarla como hashtag. Es la misma solución autorizada para `mkt-01`
  (`PROFILE.md:39`, «el logo de la marca cuando se la nombra, en línea sobre tarjeta clara»).
- **Nada más queda pendiente del dueño:** las cifras, el ejemplo único, la divisa (6 euros por
  decisión del dueño) y la duración están resueltos en `SCRIPT.md` / `BRIEF.md` / `01-fuentes.md`.

---

## 6. Barras de calidad (revisión antes de dar el vídeo por bueno)

- `check` sin errores; contraste WCAG AA (texto normal ≥ 4,5:1; grande ≥ 3:1).
- **Fotograma 0** (B1): luminancia ≥ 200/255 y ≈ 100 % de filas con contenido, medido con
  `verificar_montaje.py`.
- **Cruces sin tramo vacío** ≤ 0,15 s por fotograma a 30 fps (umbral fijo 25): revisar los instantes
  intermedios de `cover` (B2→B3) y `sweep` (B6→B7); B10→B11 es corte directo.
- **Audio sin huecos** > 0,12 s por debajo de −48 dBFS.
- Un fotograma de lectura por escena · alineación de texto e interfaces · sincronía con la voz · el
  MP4 completo en movimiento.
