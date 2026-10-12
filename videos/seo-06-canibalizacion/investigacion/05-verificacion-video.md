# 05 · Verificación adversarial del render — V6 «Canibalización de palabras clave»

Verificador adversarial, sin participación en la construcción de la pieza.
Objeto: `index.html`, `assets/sfx/events.json`, `renders/video.mp4`
(**40,700 s · 1080×1920 · 30 fps · 48 kHz**, según `ffprobe`) y los 11 fotogramas
`renders/frames/s01.png … s11.png`.
Referencias: `STORYBOARD.md`, `DIRECCION.md`, `SCRIPT.md`, `investigacion/03-contrato.md`, `DECISIONS.md`.

**Método** (todo reproducible):
miniatura y cruces medidos sobre el MP4 escalado a 60×107 con `-pix_fmt rgb24 -f rawvideo -`
(luminancia $L=0{,}2126R+0{,}7152G+0{,}0722B$; «fila con contenido» = media de la fila > 25);
barrido completo de los 1221 fotogramas buscando planos (var < 120 y color dominante > 88 %);
audio con `ffmpeg -af volumedetect` / `silencedetect` por tramo;
recuento del `TRANSCRIPT` del karaoke y del guion con Python; `grep` de las reglas duras.
No se ha modificado ningún fichero salvo este informe.

---

## Defectos

### GRAVEDAD ALTA

**Ninguno.** No hay barrido que cubra el cuadro (comprobación 3), ningún corte queda vacío
(comprobación 2), la voz suena en los 11 tramos (comprobación 8) y el fotograma 0 es claro y con
contenido (comprobación 1). Los peores hallazgos son un hueco de voz de 0,40 s y un fotograma de
transition lleno de un solo color; ambos abajo, como MEDIA.

---

### GRAVEDAD MEDIA

**M1 · Escena ≠ clip (relleno de 3 s heredado) → 0,40 s SIN VOZ tras la línea 8.**
- Evidencia: `assets/voice/timing.json` da `scene[3]=3.0` vs `clip[3]=2.972` y **`scene[8]=3.0`
  vs `clip[8]=2.601`**; `08.wav` dura 2,60 s pero `index.html:504` fija
  `#vo-08 data-duration="2.998"`. El contrato lo prohíbe: §5 (`03-contrato.md:87-88`)
  «cada escena dura exactamente su frase, **sin silencio de relleno** (`--min-frame 0`, D23)»;
  `DECISIONS.md:30` (D23).
- Medición: mezcla a **t=29,35–29,70 s = −28,4 dB** (solo música) frente a **−14,3 dB** en
  28,0–28,9 s (con voz). Hueco de voz ≈ **0,40 s**; además la píldora de karaoke no tiene grupo
  visible en 29,60–29,73 s (fin del grupo de L8 a 29,253 s + 0,35 s de buffer).
- Arreglo: `scene[3]=2.972`, `scene[8]=2.601` (recalcular `total`) en
  `videos/seo-06-canibalizacion/assets/voice/timing.json` y rehacer la cadena
  `retime.py --timing assets/voice/timing.json → transiciones.py → check → render`.
  Alternativa: re-lanzar `voice_pipeline.py … --min-frame 0` (contrato §6). Total ≈ **40,27 s**.

**M2 · Duración 40,70 s fuera de la banda 30-40 s, sin excepción registrada.**
- Evidencia: MP4 **40,700 s** (`ffprobe`), `index.html:273` `data-duration="40.692"`,
  `timing.json` `total=40.692`. Contrato §5 (`03-contrato.md:88`): «total **30-40 s**
  (V5 justificó 53 s)». `SCRIPT.md:30` afirma «≈ 35,7 s, **dentro de la banda de 30-40 s**»
  (falso en +5,0 s / +14 %). No hay fila en `DECISIONS.md` que documente la excepción
  (V1 sí la tiene: D04).
- Arreglo (mínimo): añadir fila en `DECISIONS.md` (precedente D04) y corregir `SCRIPT.md:30`.
  Si la banda es no negociable: recortar ~0,7 s con `atempo≈1,017` sobre las 11 voces
  (40,692 → 40,00 s) o podar silencios internos.

**M3 · El `cover` B2→B3 deja 0,20 s de fotograma lleno de un solo color.**
- Evidencia: `index.html:700-701` animan `.cover` de `scale 0→1` en `d*0,55` y luego `1→1,3`;
  la escena B2 dura hasta `3.019 + 4.165 = 7.184 s`. Barrido de todo el MP4: los **únicos**
  fotogramas planos (var < 120 y dominante > 88 %) son **t=7,000–7,200 s** (6 fotogramas),
  dominante `(24,24,24)≈#20202a`, `L≈29`, `var≈63`. El medidor de `check` lo aprueba porque la
  luminancia media (29) supera el umbral 25 → «lo da por bueno» sin verlo.
- Impacto: 0,2 s de panel azul-grafito liso entre dos escenas oscuras; el diseño pide «crece desde
  la balanza y **despeja**» (`STORYBOARD.md:59`, `DIRECCION.md:189`), y aquí no despeja: se queda
  lleno hasta que arranca B3.
- Arreglo: en `index.html:700` sustituir las dos líneas por una sola que alcance el lleno justo al
  corte: `tl.fromTo('#s'+n+'-cover',{scale:0},{scale:1,duration:d,ease:'power3.in'},T);`
  → el lleno coincide con el arranque de B3 (≤ 1 fotograma). O acortar la cola de s2.

---

### GRAVEDAD BAJA

**B1 · `.s-in` con 560 px abajo, no los 470 px de la dirección.**
- Evidencia: `index.html:27` `padding: 300px 74px 560px`; `DIRECCION.md:329` y
  `03-contrato.md:57` dicen `300px 74px 470px` («V5 usó 560 abajo»). Efecto: la columna de
  contenido sube 45 px respecto al plan.
- Arreglo: `index.html:27` → `padding: 300px 74px 470px` (comprobar que no choca con la píldora
  karaoke de `bottom:470px`), o actualizar `DIRECCION.md:329` / `03-contrato.md:57` si 560 es lo
  decidido.

**B2 · `#s3-pos` arranca en «↑» y solo pasa a «↓» en t=2,10 s.**
- Evidencia: `index.html:324` `<span class="pos" id="s3-pos">↑</span>`;
  `index.html:592` `setNum("#s3-pos","↓", at(3, 2.10))`. `STORYBOARD.md:68,75` fijan el indicador
  en «↓» (y el contrato §7: «la caída se marca con ↓, nunca con un número»). Durante los 2,10 s
  iniciales de B3 el indicador dice «↑» mientras la voz dice «ambas se hunden».
- Arreglo: `index.html:324` → `↓`, o añadir `setNum("#s3-pos","↓", at(3,0.0))`.

**B3 · Rótulos que repiten literalmente la voz.**
- Evidencia: `STORYBOARD.md:294-295` «rótulos nominales en mayúsculas … **nunca repiten la voz**»,
  pero la propia tabla del storyboard (`STORYBOARD.md:285-291`) prescribe `SÍ TIENE ARREGLO`
  (voz L4: «y sí tiene arreglo»), `MISMA RESPUESTA` (voz L6), `SEPARAR INTENCIONES`/`FUSIONAR EN
  UNA` (voz L10) y `Guarda esto` (voz L11), implementados en `index.html` (`#s4-fix`, `#s6-lab`,
  `#s10-optA/B`, `#s11-label`).
- Arreglo: decidir — aceptar y corregir la regla de `STORYBOARD.md:294`, o cambiar los rótulos por
  nominales no ecoicos (p. ej. `ARREGLO POSIBLE`, `MISMO DESTINO`, `DIVIDIR`/`UNIR`, `PARA LUEGO`).

**B4 · La cadena del contrato no es reproducible: el timing por defecto está desincronizado.**
- Evidencia: `retime.py` usa por defecto `.openhands/tools/voice-timing.json` (contrato §5-§6), que
  contiene **10 entradas y total 37,468 s** (otra pieza), mientras la pieza tiene
  `assets/voice/timing.json` con **11 entradas y total 40,692 s**. Ejecutar el comando documentado
  `python3 .openhands/tools/retime.py --dir videos/seo-06-canibalizacion` aplicaría 10 inicios y
  rompería `S`, la escena 11 y el karaoke.
- Arreglo: copiar `assets/voice/timing.json` → `.openhands/tools/voice-timing.json`, o fijar el
  comando del contrato con `--timing videos/<p>/assets/voice/timing.json`.

**B5 · B2 sin el chip de consulta que lista la tabla de rótulos.**
- Evidencia: `STORYBOARD.md:284` («B2 | EL FENÓMENO | chip de consulta (mono)») frente a
  `STORYBOARD.md:41-49` y el §B2 de `index.html`, que **no** incluyen chip; la consulta
  «instalación de luz» no aparece en B2.
- Arreglo: añadir `<span class="chip sm" id="s2-q">instalación de luz</span>` a `#s2-in`, o borrar
  esa celda de la tabla del storyboard.

**B6 · B5 y B7 superan los 4,2 s de referencia del contrato; solo B7 está justificada.**
- Evidencia: `03-contrato.md:88` «escenas de **1,2 a 4,2 s**». Clips reales (timing.json):
  **B5 = 4,505 s**, **B7 = 5,016 s** (> 4,2). `STORYBOARD.md:277` solo justifica la línea 7
  («18 palabras, 4,52 s, un solo beat por texto expreso del dueño»); la 5 no está cubierta.
- Arreglo: registrar la excepción de B5 en `STORYBOARD.md`/`DECISIONS.md`, o subir el ritmo /
  recortar la línea 5.

**B7 · `cover` con origen `50% 40%` en vez de `50% 62%`.**
- Evidencia: `index.html:257` `transform-origin: 50% 40%` frente a `DIRECCION.md:323`
  `transform-origin:50% 62%`.
- Arreglo: `index.html:257` → `50% 62%` (el panel crecería desde la balanza, no desde el centro).

---

## Confirmaciones (una fila por comprobación)

| # | Comprobación | Medida (evidencia) | Resultado |
|---|---|---|---|
| 1 | Miniatura: fotograma 0 y primeros 0,5 s | `L` media **210,8 → 210,9**; filas con contenido **100,0 %** en los 15 fotogramas (0–0,467 s) | **CUMPLE** (≥ 200/255 y ≈ 100 %) |
| 2 | Cruces: contenido en el *instante* del corte | F1→F2 **100 %** · F2→F3 100 % · F3→F4 **35,5 %** · F4→F5 100 % · F5→F6 100 % · F6→F7 100 % · F7→F8 **25,2 %** · F8→F9 27,1 % · F9→F10 34,6 % · F10→F11 100 % (0 huecos de audio) | **CUMPLE** — ningún corte vacío |
| 3 | Barridos: `translateX(...)` inicial + `xPercent` sin `x:0` | Único caso: `.sweep` (`index.html:259`, `translateX(-130%)`); su `fromTo` lleva **`x:0` explícito** (`index.html:697-698`). `.slide-x` (`translateX(-120px)`) **no se usa**. Ningún fotograma con barrido cubriendo | **CUMPLE** — no cubre el cuadro |
| 4a | `data-start` + duración en cada elemento temporal | 27/27 etiquetas con `data-start` tienen `data-duration` (11 escenas, 11 voces, música, sfx, `prog`, karaoke, raíz) | **CUMPLE** |
| 4b | `class="clip"` en cada elemento temporal | 26/27; la única sin `clip` es `#root` (no exigido) | **CUMPLE** |
| 4c | Una sola timeline raíz, pausada | `index.html:511` `gsap.timeline({paused:true})` = `"main"`; el componente karaoke registra la suya (`"caption-pill-karaoke"`), como prevé el contrato §7 | **CUMPLE** |
| 4d | Ausencia de `.from()` / `Math.random` / `Date.now` / contadores / `repeat` / `yoyo` / `transition:` / `@keyframes` | 0 ocurrencias de cada uno; `gsap.timeline` = 1 en `index.html` | **CUMPLE** |
| 4e | Escenario sin animar su opacidad | El escenario usa `rise()` (`index.html:521-525`), que solo mueve `y`; nunca toca `opacity` | **CUMPLE** |
| 4f | Panel oscuro ≥ `#20202a` | `--panel:#20202a` (`index.html:14`); `#20202a` en `.card`/`.splitbar`/`.cover`. El único por debajo es la pista de progreso `#1e1e26` (`index.html:251`), exenta por `DIRECCION.md` §8 | **CUMPLE** |
| 4g | Acento solo como relleno con tinta encima | `.chip.accent`/`.pill.accent`/`.tag`/`.fav`/`.cta-mark` = relleno acento + `accent-ink`; **sin acento como trazo sobre claro** (los defectos A2 de `04-verificacion.md` —`.prow.dup`, `.fusearw`— quedaron en `#4d5a29`). `.savewave` es trazo acento en escena **oscura** (sancionado, `DIRECCION.md` §8) | **CUMPLE** |
| 4h | Texto dentro de la banda segura (15 %-75 % = y 288-1440) | Tinta más baja detectada en escenas claras: **y = 1417 < 1440**; en escenas oscuras, contenido en y 1440-1920 = **0,0 %** | **CUMPLE** |
| 4i | Un solo foco dominante por escena | foco claro en B1-B9/B11; **B10** es el más cargado (7 objetos), ver retención | **CUMPLE con reserva** |
| 5 | Rótulos y subtítulos = guion de V6 (11 líneas, 142 palabras) | `TRANSCRIPT` del karaoke = **142 entradas / 142 palabras**, reparto por línea **[11,13,12,14,14,13,18,8,12,13,14]** = guion línea a línea (coincidencia exacta tras normalizar puntuación); 48 eventos sfx coinciden 1:1 con las 11 recetas de `STORYBOARD.md:235-245` | **CUMPLE** |
| 5b | Sin restos de la pieza anterior | 0 coincidencias de `cafetera`, `GUÍA`, `COMPARATIVA`, `PRODUCTO`, `DEJA SOLO UNA`, `autoridad`, `modificador` en `index.html` y en el karaoke | **CUMPLE** |
| 6 | Inicios de escena de `S` vs `timing.json` | `S = [0,0, 3,019, 6,734, 9,734, 13,542, 18,047, 21,716, 26,732, 29,732, 33,122, 37,116]` **idéntico** a `timing.json.start` (11 entradas) | **CUMPLE** |
| 6b | Duración del MP4 | MP4 **40,700 s** vs `data-duration` **40,692 s** → Δ 8 ms = redondeo a 30 fps | **CUMPLE** |
| 8 | Voz en los 11 tramos | media por tramo: **−14,5 / −15,2 / −14,0 / −14,8 / −15,8 / −15,8 / −14,9 / −16,2 / −15,0 / −14,3 / −14,4 dB** (todos con voz) | **CUMPLE** |
| 8b | La música no tapa la voz | `track.wav` −13,9 dB a plena, pero a `data-volume="0.18"` ≈ **−29 dB** en la mezcla; la voz (`01.wav` −13,2 dB) queda ≈ **16 dB por encima** | **CUMPLE** |
| 8c | Huecos de audio | `silencedetect -48 dB / 0,12 s` → 0 eventos; sin embargo la **voz** deja 0,40 s tras L8 (ver M1) | **CUMPLE** (audio), con la salvedad de M1 |

---

## Retención · fotograma de lectura por escena (1-11)

`L` y «contenido» medidos sobre `renders/frames/sNN.png` (escala 60×107). La valoración de
legibilidad se apoya en el código (qué texto aparece) y en la luminancia medida; **no** en ver la
imagen (ver «Lo que no he podido verificar»).

| F | Escena | Texto/objetos en pantalla (`index.html`) | Foco | `L` / contenido | ¿Se lee el mensaje sin voz? | Riesgo |
|---|---|---|---|---|---|---|
| s01 | B1 | kicker EL ERROR · placa **AVISO** (relleno rojo + tinta) · flecha ↓ | la placa | 207,4 / 100 % | **Sí**: «error / aviso / posición abajo» | ninguno; nada sobra |
| s02 | B2 | kicker EL FENÓMENO · balanza (2 fichas «Tu página», `/servicios/…` vs `/blog/…`) · barra que se reparte | la balanza | 223,9 / 100 % | **Sí**: dos páginas compitiendo | falta la consulta que pide el storyboard (B5 del informe) |
| s03 | B3 | kicker LA CONSECUENCIA · escala **POSICIÓN** + marca + indicador · 2 fichas hundiéndose | marca + fichas | 19,3 / 38,3 % (oscuro) | **Sí** | el indicador arranca «↑» (B2 del informe) |
| s04 | B4 | kicker EL NOMBRE · título **CANIBALIZACIÓN / DE PALABRAS CLAVE** (110/78 px) · balanza mini · pastilla SÍ TIENE ARREGLO | el término | 221,4 / 100 % | **Sí**, el más claro | ninguno |
| s05 | B5 | kicker EL MATIZ · 2 fichas + 2 chips (consultas) + 2 etiquetas CONTRATAR/INFORMARSE | las 2 fichas | 229,8 / 100 % | **Sí** | 7 objetos; el par chip+etiqueta por columna puede fundirse en uno |
| s06 | B6 | kicker LA CAUSA · chip (consulta) · 2 fichas solapadas + corchete · MISMA RESPUESTA | el solape | 227,1 / 100 % | **Sí** | 6 objetos; aceptable |
| s07 | B7 | kicker EL EJEMPLO · chip · 2 ventanas con URLs largas (mono 27 px) | las 2 ventanas | 227,6 / 100 % | **Sí** (URLs algo pequeñas en móvil) | riesgo bajo |
| s08 | B8 | kicker CÓMO VERLO · panel Rendimiento→Páginas · 2 filas iguales + corchete | las 2 filas | 49,1 / 27,1 % (oscuro) | **Sí**, el beat más explícito | ninguno |
| s09 | B9 | kicker CONSULTAS Y PÁGINAS · panel Consultas · chip · 2 filas + tinte alternando | la fila resaltada | 59,4 / 32,7 % (oscuro) | **Sí** | ninguno |
| s10 | B10 | kicker EL ARREGLO · 2 fichas + flecha de fusión + ficha firme + pastillas SEPARAR INTENCIONES / FUSIONAR EN UNA | (difuso) | 226,9 / 100 % | **Sí, con esfuerzo** | **7 objetos: el más cargado**; flecha + 3 fichas + 2 pastillas compiten |
| s11 | B11 | ficha centrada · marcador (acento) + onda · **Guarda esto** (96 px) · logo Google | marcador + rótulo | 25,4 / 39,3 % (oscuro) | **Sí** | ninguno |

Beats que conviene revisar por sobrecarga: **B10** (7 objetos) y, en menor medida, **B5** y **B6**.

---

## Lo que no he podido verificar

- **Percepción visual directa** de los fotogramas y del MP4: no disponible en este entorno (la
  lectura de imágenes no me devuelve contenido perceptible). La valoración de retención se apoya en
  el código (qué texto/objetos aparecen), en la luminancia y % de contenido medidos y en los
  contrastes deducidos del CSS, **no** en ver la imagen.
- **Escucha del audio**: verifico por `volumedetect` y por duración de fichero, no por escucha.
- **Forma de onda de `sfx.wav`/`track.wav`**: solo comprobé que `events.json` (48 eventos, ganancias
  0,45–0,85, tipos válidos) coincide 1:1 con el plan y que los niveles son coherentes; no el
  contenido de la señal.
- **`npm run check` / `hyperframes`**: no re-ejecutados (no debía tocar nada); me baso en la
  medición del MP4 renderizado.
- **Legibilidad real a tamaño móvil y contraste WCAG exacto**: no medidos píxel a píxel sobre el
  render.
- **Columnas/medidas internas de tipografías** (anchura de URLs de B7, encaje del panel de B8/B9 en
  el ancho móvil): deducidas del CSS, no medidas sobre la captura.
