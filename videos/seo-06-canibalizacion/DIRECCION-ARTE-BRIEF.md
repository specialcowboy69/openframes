# Brief de dirección de arte — V6 «Canibalización de palabras clave»

Pieza: **11 beats · 137 palabras · ~34,4 s** · 9:16 · 1080×1920 · faceless · voz en off es-ES
(`Pablo`) · subtítulos karaoke · barra de progreso. Guion cerrado: `SCRIPT.md` (no se toca).
Contrato de producción: `investigacion/03-contrato.md`. Continuidad: `investigacion/02-continuidad.md`.

> Este fichero fija **qué tiene que conseguir la pieza** (efecto, restricciones, recursos, vetos).
> Cómo se resuelve está en `DIRECCION.md`; el desglose por línea, en `STORYBOARD.md`.

---

## 1. Efecto buscado en el espectador

Tres cosas, en este orden:

1. **Reconocer el error en el primer segundo.** Que quien lo vea entienda «esto me está costando
   posiciones y no debo hacerlo». El fotograma 0 es la miniatura del reel (se publica sin portada),
   así que el aviso —contenido desde el fotograma cero, sin desvanecidos— tiene que estar montado y
   encendido desde el segundo cero.
2. **Entender la tesis.** Dos páginas tuyas compitiendo por **la misma** búsqueda: **ninguna gana**.
   No es «tener dos páginas del mismo tema» ni «contenido duplicado»; es disputarse la misma
   consulta con la misma intención (`investigacion/01-fuentes.md`).
3. **Llevarse una acción.** Antes de escribir o revisar la próxima página: **separar las
   intenciones o fusionar las dos en una**. Cierra con la CTA de guardar de la serie.

**Tono:** el gancho abre con la **consecuencia y un imperativo** («Este error te hará bajar posiciones
en Google. No lo hagas.»), no con el síntoma. Después se explica el fenómeno con palabras normales
(dos páginas compitiendo por la misma búsqueda) y solo entonces el nombre —*canibalización*— llega en
la línea 4. Sin cifras, sin promesas de resultados y sin hablar de penalizaciones. Un solo ejemplo
(página de servicio frente a artículo propio).

**Promesa visual:** el vídeo se entiende en mudo, pero por **gráfico + karaoke**, no por texto
recargado (`DESIGN.md` §0). La complejidad sale de coordinar capas, no de acumular recursos.

---

## 2. Restricciones del dueño (duras)

- **Paleta del sistema** (claro de papel / oscuro de carbón) con **un solo acento** (`#c8ff3d`).
  El acento es **siempre relleno con tinta `#0b0b10` encima**; prohibido como texto o trazo sobre
  claro. El **rojo** (`warn`) solo marca un **error real** (aquí: lo que *pierde*), nunca decoración.
  **Panel oscuro nunca por debajo de `#20202a`** (el medidor de montaje cuenta filas con luminancia
  media > 25 y `#17171e` se queda fuera).
- **El fotograma 0 es la miniatura**: luminancia ≈ **200+ / 255** y **≈ 100 % de filas con
  contenido**. Nada de abrir con pantalla vacía, con desvanecidos ni con el marco entrando tarde.
- **Un escenario visible desde `t=0` en cada escena**, que se asienta con `rise()` (sin animar su
  opacidad). Nacer en `opacity:0` deja los cruces vacíos.
- **Tipografía:** protagonista 110-180 px · frase 70-110 · contexto 38-56 · kicker 32 fijo ·
  CTA «Guarda esto» 96. Todo dentro de la **banda segura** `padding: 300px 74px 470px`
  (nada crítico en el 15 % superior ni el 25 % inferior). **Un solo foco dominante por escena.**
- **Seek-safe:** estado inicial en CSS; animar con `fromTo` / `.to()`. **Prohibido** `.from()`,
  `Math.random`, `Date.now`, contadores que suben (los números cambian con `tl.set(..., {textContent})`),
  CSS `transition`/`@keyframes` y `repeat`/`yoyo`.
- **Seis familias de transición disponibles**, incluidas las que necesitan **pieza propia de escena**
  (`.cover`, `.sweep`) o **recorte** (`clip-path`). Esas se pagan con código propio en la línea de
  tiempo y con **revisión del fotograma intermedio** con el medidor de montaje.
- **Cadena obligatoria:** `retime.py` → `transiciones.py` → `check` → render. Nunca a mano.
- **`check` con 0 errores** y contraste WCAG AA; cruces sin tramo vacío ≤ 0,15 s; audio sin huecos
  > 0,12 s.

---

## 3. Recursos disponibles

- **Fuentes** `Inter` (400/600/700/800/900) + `JetBrains Mono` (600/800), vendorizadas en
  `assets/fonts/` (`@font-face`, sin red en el render). Medir texto tras `document.fonts.ready`.
- **Voz** Fish Audio **`Pablo`** (`reference_id 1bd666ea8ada44c789e0fec21cf78f33`), cola 0,08 s.
- **Música** `assets/music/track.wav` (vol. 0,18) y **efectos** `assets/sfx/sfx.wav` (vol. 0,5),
  sintetizados de forma determinista (9 tipos: `whoosh, pop, tick, click, swoosh_up, swoosh_down,
  ding, thud, buzz`).
- **Karaoke** `caption-pill-karaoke` + `TRANSCRIPT` con tiempos absolutos.
- **Kit de componentes** (todo CSS/SVG inline, sin banco de imágenes ni generación):
  ventana de navegador, tarjeta de resultado / SERP, tarjetas, pastillas, chips, etiquetas, tiles,
  barras comparadas, cursor, panel de datos, CTA de guardar, barra de progreso.
- **Helpers** en `index.html`: `put`, `rise`, `draw`, `grow`, `bar`, `typeWords`, `swap`, `setNum`.

---

## 4. Qué hay que evitar

- **Repetir V5**: no re-explicar la intención de búsqueda; no usar las etiquetas
  GUÍA / COMPARATIVA / PRODUCTO; nada de «cafetera», «alojamiento web» ni «seguro de coche»; «una
  intención, una página» **es de V5**, no la tesis de V6. Y, sobre todo, **la metáfora central no
  puede ser la caída en los resultados ni la SERP como examen** (eso ya es de V5).
- **Repetir V1 / V2 / V3**: ni las cuatro posiciones del título ni «agencias de diseño baratas» (V1);
  ni el modificador, la URL ni la excepción de lujo ni «zapatillas» (V2); ni la autoridad, los
  enlaces, el 3-vs-118 ni `medio.com`/`otratienda.com` (V3). Aquí **Search Console se usa en
  Rendimiento → Páginas**, no en Enlaces.
- **Pisar lo reservado**: V7 contenido fino, V8 AI Overviews, V9 long-tail vs head, V10 título/H1/URL.
- **Anglicismos, cifras inventadas, promesas, afirmaciones sin fuente, ganchos por miedo.**
- **Texto que repita lo que dice la voz** (`DESIGN.md` §0): el peso lo lleva el gráfico.
- **Cualquier cosa aleatoria o no determinista** y **cualquier `.from()` / `repeat` / `yoyo`**.
