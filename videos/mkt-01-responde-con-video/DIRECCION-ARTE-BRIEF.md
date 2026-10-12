# Brief de dirección de arte — mkt-01 «Responde con vídeo (Old Spice 2010)»

Serie **Casos de estudio marketing** · Pieza **mkt-01** · 9:16 · 1080×1920 · faceless · voz en off es-ES
(`Pablo`) · subtítulos karaoke · barra de progreso. **11 beats · 121 palabras · ≈34,6 s**.
Guion cerrado: `SCRIPT.md` (no se toca). Contrato de producción heredado **tal cual**:
`videos/seo-06-canibalizacion/investigacion/03-contrato.md`. Continuidad de la línea:
`investigacion/02-continuidad.md`. Fuentes del dato: `investigacion/01-fuentes.md`.

> Este fichero fija **qué tiene que conseguir la pieza** (efecto, restricciones, recursos, vetos y lo
> que queda pendiente del dueño). Cómo se resuelve está en `DIRECCION.md`; el desglose por línea, en
> `STORYBOARD.md`.

---

## 1. Efecto buscado en el espectador

Tres cosas, en este orden:

1. **Entender la idea en el primer segundo.** Que quien lo vea entienda «un comentario se puede
   responder con un vídeo». El fotograma 0 es la miniatura del reel (se publica sin portada), así que
   el hilo de comentarios y la burbuja que se abre a clip tienen que estar **montados y encendidos
   desde el segundo cero**, sin desvanecidos ni marco entrando tarde.
2. **Entender la tesis.** Old Spice respondió a sus comentarios con **186 vídeos en dos días y medio**;
   **tú puedes hacer lo mismo, sin comprar anuncios**. El protagonista es una **marca ajena** que
   sirve de **prueba**, no de consejo; el espectador no es el héroe hasta «tu versión» (B6). La fuente
   matiza que el caso tenía **agencia, equipo y guionistas** y que **el mayor coste era producir el
   vídeo** (`01-fuentes.md` §4): la pieza invita a probar sin comprar anuncios, no promete que sea gratis.
3. **Llevarse una acción.** Antes de pensar el próximo vídeo: **empezar por las tres preguntas que más
   se repiten** y responder a la siguiente con un vídeo. Cierra con la CTA de guardar de la serie.

**Tono:** el gancho no usa el mecanismo de «error» de la serie SEO ni una apertura gastada; abre con
**el caso** —un comentario que se convierte en vídeo— y nombra «esta conocida marca» antes de
identificarla como Old Spice (B2). Se cuenta primero qué hizo la marca y solo después se traduce a un
negocio pequeño. Sin cifras que no estén en las fuentes, sin promesas de resultados y con **un solo
ejemplo** (la tienda de ropa, B7-B9).

**Promesa visual:** el vídeo se entiende en mudo por **gráfico + karaoke**, no por texto recargado
(`DESIGN.md` §0). La complejidad sale de coordinar capas, no de acumular recursos.

---

## 2. Restricciones del dueño (duras)

- **Paleta del sistema** (claro de papel / oscuro de carbón) con **un solo acento** (`#c8ff3d`). El
  acento es **siempre relleno con tinta `#0b0b10` encima**; **prohibido como texto o trazo sobre
  claro**. **Panel oscuro nunca por debajo de `#20202a`** (el medidor de montaje cuenta filas con
  luminancia media > 25).
- **El rojo (`warn`) solo para un error real.** Esta pieza **no tiene errores ni pérdidas**: el
  tachado del «presupuesto de anuncio» (B6) marca algo que *no hace falta*, no algo que se pierde, así
  que va en **tinta**, no en rojo. La pieza **no usa `warn` en ningún beat**.
- **El fotograma 0 es la miniatura**: luminancia ≈ **230/255** y **≈ 100 % de filas con contenido**.
  Nada de abrir con pantalla vacía, con desvanecidos ni con el marco entrando tarde.
- **Un escenario visible desde `t=0` en cada escena**, que se asienta con `rise()` (sin animar su
  opacidad). Nacer en `opacity:0` deja los cruces vacíos.
- **Tipografía:** protagonista 110-180 px · frase 70-110 · contexto 38-56 · kicker 32 fijo · CTA
  «Guarda esto» 96 · rótulos menores 22-37 (`DIRECCION.md` §3). **Un solo foco dominante por escena.**
- **Banda segura 15 %-75 % de la altura** (288-1440 px de 1920): texto y marcas dentro de
  `padding: 300px 74px 480px`; nada crítico en el 15 % superior ni el 25 % inferior.
- **Seek-safe:** estado inicial en CSS; animar con `fromTo` / `.to()`. **Prohibido** `.from()`,
  `Math.random`, `Date.now`, contadores que suben (los números se fijan con `setNum(sel, txt, t)`),
  CSS `transition`/`@keyframes` y `repeat`/`yoyo`.
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
  `.kicker` (+`.dot`), `.card`, `.chip`, `.pill`, `.tag`, `.tile`, `.rowc`, `.phone` (nuevo en B1, se
  reusa en B6), `.cta-mark`/`.cta-label`/`.savewave`, `.progress`/`#prog-fill`.
- **Recurso propio de la pieza:** **el comentario que se convierte en vídeo** (burbuja → clip). No se
  reutiliza la **SERP etiquetada** de V5 ni la **balanza de dos platos** de V6.

---

## 4. Qué hay que evitar

- **Ejemplos ya gastados:** nada de «cafetera» (V5), «instalación de luz» (V6), «agencias de diseño
  baratas» (V1), «zapatillas baratas» (V2), el 3 vs 118 y Search Console → Enlaces (V3) ni los caminos
  de instalación y el chip `G-XXXXXXXXXX` (GA1). Aquí el único ejemplo es **la tienda de ropa**.
- **Aperturas gastadas:** el gancho no usa el «error» («Este error te hará bajar posiciones…», V6;
  «el error que hace que aparezcas cada vez menos…», V5; «Tu web no sube aunque hagas SEO», V3).
- **Recursos visuales ya muy vistos:** la **SERP de Google etiquetada** (V5) y la **balanza de dos
  platos** (V6) quedan fuera; la metáfora central es nueva.
- **Vocabulario de otras series:** no se reutiliza el de SEO (autoridad, enlaces, canibalización,
  SERP) ni el de GA4 (cuenta, propiedad, flujo, etiqueta).
- **Marcas:** sin `@handle`/arroba en pantalla y sin ningún adorno de autoría o IA.
- **Cifras inventadas, promesas de resultados, ganchos por miedo, anglicismos innecesarios.**
- **Texto que repita lo que dice la voz** (`DESIGN.md` §0): el peso lo lleva el gráfico.
- **Cualquier cosa aleatoria o no determinista** y **cualquier `.from()` / `repeat` / `yoyo`**.

---

## 5. Uso de la marca ajena

- **El logo de la marca de consumo queda autorizado por el dueño (2026-10-12).** `PROFILE.md:39` autoriza mostrar
  «el logo de la marca cuando se la nombra», pero sus ejemplos son **plataformas** (Google, Search
  Console), no una **marca de consumo** como Old Spice; `investigacion/02-continuidad.md` §6 ya marca
  este riesgo. La marca se representa **solo con su nombre escrito como
  logotipo** (tinta `#14141a` sobre tarjeta clara `#ffffff`), **sin arroba**, **sin descargar ninguna
  imagen de red** y **sin sugerir afiliación** ni usarla como hashtag. Si el dueño confirma el logo
  oficial, se sustituye el logotipo tipográfico por la marca en línea sobre la misma tarjeta.
- **Ninguna otra cosa queda pendiente:** las cifras, el ejemplo único y la duración están resueltos en
  `SCRIPT.md` / `BRIEF.md`.

---

## 6. Barras de calidad (revisión antes de dar el vídeo por bueno)

- `check` sin errores; contraste WCAG AA (texto normal ≥ 4,5:1; grande ≥ 3:1).
- **Fotograma 0** (B1): luminancia ≥ 200/255 y ≈ 100 % de filas con contenido, medido con
  `verificar_montaje.py`.
- **Cruces sin tramo vacío** ≤ 0,15 s por fotograma a 30 fps (umbral fijo 25): revisar los instantes
  intermedios de `cover` (B2→B3) y `sweep` (B7→B8); B10→B11 es corte directo.
- **Audio sin huecos** > 0,12 s por debajo de −48 dBFS.
- Un fotograma de lectura por escena · alineación de texto e interfaces · sincronía con la voz · el MP4
  completo en movimiento.
