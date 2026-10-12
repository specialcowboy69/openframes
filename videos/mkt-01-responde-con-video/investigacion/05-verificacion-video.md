# 05 · Verificación adversarial del render — MK1 «Responde con vídeo (Old Spice 2010)»

Verificador adversarial, **sin participación** en la construcción de la pieza.
Objeto: `index.html`, `assets/sfx/events.json`, `assets/voice/timing.json`, el MP4
`renders/video.mp4` (**37,533 s · 1080×1920 · 30 fps · 48 kHz**, según `ffprobe`) y los 11
fotogramas `renders/frames/s01.png … s11.png`.
Referencias: `SCRIPT.md`, `STORYBOARD.md`, `DIRECCION.md`, `investigacion/01-fuentes.md`,
`DECISIONS.md` (sección MK1) y `videos/seo-06-canibalizacion/investigacion/03-contrato.md`
(reglas duras heredadas; nota: en este repo es V6).

**Método** (reproducible):
miniatura y cruces medidos sobre el MP4 escalado a 60×107 con `-pix_fmt rgb24 -f rawvideo -`
(luminancia $L=0{,}2126R+0{,}7152G+0{,}0722B$; «fila con contenido» = media de fila > 25);
barrido de los 1126 fotogramas buscando planos (var < 120 y color dominante > 88 %);
texto de pantalla por OCR (`tesseract -l spa`); recuento del `TRANSCRIPT` del karaoke y de
`assets/voice/*.txt` con Python; audio con `ffmpeg -af volumedetect` por tramo; `grep` de las
reglas duras. No se ha modificado ningún fichero salvo este informe.

**Cifras clave:** miniatura (t=0) **L=187,5 · 100 % de filas con contenido · 0 % casi vacías**;
los **10 cruces** con contenido y **sin hueco de audio**; audio voz en los **11 tramos**;
**karake = 121 palabras = voz = guion**; MP4 **37,53 s** (declarado ≈34,6 s).

---

## Defectos

### GRAVEDAD ALTA

**Ninguno.** No hay barrido que cubra el cuadro (comprobación 3: 0 fotogramas planos en los
1126), ningún cruce queda vacío (comprobación 2), la voz suena en los 11 tramos (comprobación 9),
el fotograma 0 es claro y se lee solo (comprobación 1) y el texto de pantalla corresponde al
guion de MK1 sin restos de otra pieza (comprobación 5).

---

### GRAVEDAD MEDIA

**M1 · Dos escenas por encima del máximo de 4,2 s del contrato (§5), y el `STORYBOARD` afirma lo contrario.**
- Evidencia: contrato §5 (`03-contrato.md`): «escenas de **1,2 a 4,2 s**».
  `assets/voice/timing.json` → `clip` **B2 = 4,551 s** y **B4 = 4,690 s**; `index.html:294` y
  `index.html:347` extienden la cola a `data-duration="5.001"` (B2) y **`"5.09"` (B4)**. Aun
  contando solo la frase (no la transición), B2 y B4 superan el techo en **+0,35 s y +0,49 s**.
  El `STORYBOARD.md:279` afirma: «Ninguna escena … **ni sube de 4,00 s** (máximo de referencia:
  4,2 s)» — **falso** en el render. No hay fila en `DECISIONS.md` que documente la excepción
  (el precedente D04/D38 sí documenta las suyas).
- Arreglo: partir la locución de L2 (13 pal.) y L4 (13 pal.) en dos tiempos ≤ 4,2 s cada uno
  (el karaoke admite varios grupos por línea) y rehacer la cadena
  `retime.py → transiciones.py → check → render`; o, si la pieza ya está cerrada, añadir fila en
  `DECISIONS.md` con la excepción y **corregir `STORYBOARD.md:279`**.

---

### GRAVEDAD BAJA

**B1 · Duración declarada («≈34,6 s») desfasada del render (37,53 s).**
- Evidencia: `ffprobe` → MP4 **37,533 s**; animación raíz `#prog-fill` y `timing.json.total`
  = **37,524 s**. Los encabezados de los 5 documentos dicen «**≈34,6 s**»: `BRIEF.md:4`,
  `SCRIPT.md:3`, `STORYBOARD.md:3`, `DIRECCION.md:5`, `DIRECCION-ARTE-BRIEF.md:4` (+2,9 s,
  +8,5 %). Sí está **dentro** de la banda 30-40 s, y `DIRECCION.md:414` ya advierte de que
  «la estimación de ~34,6 s es de palabra/velocidad»; pero el número publicable nunca se corrige.
  Ritmo real: 121/37,53 = **3,22 pal./s** (los docs usan 3,5).
- Arreglo: actualizar los encabezados a **≈37,5 s** y el ritmo a ≈3,2 pal./s.

**B2 · Líneas de voz fuera del beat de 6-10 palabras (§3).**
- Evidencia: el contrato §3 fija «Un beat = frases de **6-10 palabras**». Recuento de
  `assets/voice/*.txt` (= carrera del karaoke): **L1 12 · L2 13 · L3 14 · L4 13 · L7 14** →
  5 de 11 por encima de 10 (aunque todas ≤ 14, como promete `SCRIPT.md:32`). Está asumido como
  decisión de estilo (`SCRIPT.md:66`, `DIRECCION.md`), pero sin fila en `DECISIONS.md`.
- Arreglo: registrar la excepción en `DECISIONS.md` o redistribuir esas 5 líneas en dos tiempos.

**B3 · Acento verde como trazo sobre escena clara (§2).**
- Evidencia: `.cbubble.hot { border-color:#c8ff3d }` (`index.html:85`), aplicado en la escena
  **B1, clara** (la burbuja destacada «Respóndele con un vídeo»). El contrato §2: «verde sobre
  claro (≈1,3:1) **prohibido como texto/trazo**» (el acento debe ser relleno con `accent-ink`
  encima). El resto de usos del acento en MK1 **sí** cumplen (`.pill.accent`, `.callout`,
  `.vmark`, `.lesstag.accent`, `.cta-mark` = relleno + tinta; `.savewave` = trazo verde pero
  sobre **oscuro**; `.kicker .dot` = punto de color expresamente permitido en §3).
- Arreglo: cambiar el borde de `.hot` por `border-color:var(--line)` o rellenar la burbuja con
  el acento y tinta `accent-ink` encima.

**B4 · Banda segura del `.s-in` distinta del contrato (§3).**
- Evidencia: `index.html:23` → `.s-in { padding:300px 74px 700px }`; el contrato §3 fija
  `padding: 300px 74px 470px`. Es **más conservador** (no viola la banda y la píldora karaoke
  sí usa `bottom:470`, `caption-pill-karaoke.html:26`), pero deja el bloque de contenido ~230 px
  por encima del diseño del contrato. La medida real (t=0): contenido en y **300-1390**, dentro
  de la banda 15-75 % (288-1440). `DIRECCION.md:235` incluso comenta «480 abajo».
- Arreglo: usar 470 (alinear con el contrato) o documentar el 700.

**B5 · Clics de teclado muy tenues (al borde de lo perceptible).**
- Evidencia: `events.json` escena 7 → 14 eventos `key` con `gain: 0.13` (el resto de sfx van a
  0,45-0,85). Medido: `assets/sfx/sfx.wav` en t=24,1-25,5 s (la tecla del comentario) →
  **mean −37,2 dB / max −17,7 dB**, ~16 dB por debajo del sfx más fuerte del stem (max −1,4 dB).
  En la mezcla (bus sfx `data-volume="0.5"`) quedan a ≈−24 dB bajo una voz a ≈−13 dB: dentro del
  beat y **sin tapar la voz** (objetivo), pero difíciles de oír.
- Arreglo: subir el `gain` de los `key` a ~0,25-0,35 (siguen sin enmascarar la voz) o confirmar
  que el susurro de teclado es intencionado en `DECISIONS.md`.

---

## Confirmaciones (con el resultado medido)

| # | Comprobación | Resultado |
|---|---|---|
| 1 | **Miniatura** t=0 | **L media 187,5 · filas con contenido 100 % · filas casi vacías (<4 %) 0 %.** Sin barras negras (celdas <4 %: 0). Tinta oscura (L<120) en y 300-1390, x 74-1072. t=0,5 s: L 187,6 / 100 %. Se lee sola (kicker «GANCHO», teléfono con 3 comentarios y burbuja destacada «Respóndele con un vídeo», clip con ▶). Barra de la casa (300/100 %): **supera** por cobertura. |
| 1b | s01.png vs fotograma 0 | `renders/frames/s01.png` **no** es el fotograma 0: coincide con t≈**1,80 s** (L 177,9). Los 11 PNG son el **fotograma medio** de cada escena (s01→1,80, s02→5,77, s03→10,07, s04→14,33, s05→18,47, s06→21,57, s07→24,90, s08→28,27, s09→30,83, s10→33,23, s11→35,97), no portadas. |
| 2 | **Cruces** (10 cortes) | Sin tramo vacío (0,00 s) y **en el instante de cada corte hay contenido** (L media 178-234, ~100 % de filas > 25 en t=S[k] y S[k]±1 f). Sin huecos de audio: los 11 `<audio id="vo-0N">` van de S[k] a S[k]+dur, encadenados de 0 a 37,524 s sin silencio entre cortes. |
| 3 | **Barridos** | El único `sweep` (`#s8-sweep`, B7→B8) usa `fromTo(..., { x: 0, xPercent: -130, skewX: -12 }, ...)` → `x:0` explícito, sin la trampa `translateX`+`xPercent`. Barrido del MP4 completo: **0 fotogramas planos** (var<120 y dominante>88 %) → ningún cuadro tapado. |
| 4 | **Reglas duras** | `data-start`+`data-duration` en 27 elementos temporales; 11 `<section class="scene clip">`; **una** `gsap.timeline({paused:true})`, registrada en `window.__timelines["main"]` con `tl.seek(0)`; **0** `.from()`, **0** `Math.random`/`Date.now`, **0** contadores (números por `tl.set textContent`), **0** `repeat`/`yoyo` (el único `repeat` es el `grid-template-columns` CSS), **0** `transition`/`@keyframes`; `.s-in` **no** anima opacidad (solo `rise()` con y; el marco nace visible); panel oscuro `#20202a` (≥ mínimo); acento como relleno+tinta salvo el borde de `.hot` (→B3); rojo solo en el tachado (`--warn`); texto en la banda y 300-1390 (288-1440); un foco por escena; fuentes **locales** (`assets/fonts/fonts.css`); **única** petición de red = GSAP CDN (`cdn.jsdelivr.net/.../gsap@3.14.2`), la misma que usa seo-06/V6. |
| 5 | **Texto vs guion MK1** | `TRANSCRIPT` del karaoke = **121 palabras**; por escena `[12,13,14,13,10,8,14,10,9,8,10]` = voz = guion. Texto del karaoke **idéntico** a la concatenación de `assets/voice/*.txt` (comparación exacta: `True`). 11 líneas = 11 escenas. Sin restos de otra pieza (ni «canibalización», ni «keywords»). |
| 6 | **Afirmaciones** | Ni «65 millones» ni ninguna promesa en pantalla ni en voz (`grep 65` solo halla `step=0.065` en `index.html:573` y las notas de exclusión en `SCRIPT.md`). Cifras visibles sostenidas por `01-fuentes.md`: **186 vídeos**, **dos días y medio**, **seis millones el primer día** (L3/L4). |
| 7 | **Marca ajena** | `#s2-brand` = **texto** `Old&nbsp;Spice` (`.brandmark`), **sin arroba y sin `<img>`** (0 `background-image`/`url()`). Se nombra como caso («esta conocida marca», la marca responde a un fan y a un famoso), sin sugerir afiliación. Autorización en `DECISIONS.md` (sección MK1). |
| 8 | **Diferenciación** | Sin la SERP de Google de V5, sin la balanza de V6, sin cafetera ni instalación de luz: `grep -niE "cafeter|instalaci|balanza|serp|google|<img"` → **ninguno**. |
| 9 | **Sincronía y audio** | `S` de `index.html` = `timing.start` de `timing.json` = `[0,3.576,8.127,11.982,16.672,20.248,22.849,26.936,29.583,32.044,34.366]` (11 entradas) y `total=37,524` = raíz; MP4 37,533 s (Δ 9 ms, por el último fotograma). Voz en los 11 tramos (p. ej. tramo 10 32,3-33,9 s: mean −13,4/max −2,3 dB; tramo 11 35,5-37,0 s: mean −13,7/max −2,5 dB). Música (`data-volume 0.18`, track.wav mean −13,9 dB → ≈−28 dB en la mezcla) **por debajo de la voz**. Clics del comentario dentro de su beat (B7, local 1,3-2,6 s) y sin tapar la voz (→B5). |
| 10 | **Retención (11 fotogramas)** | s01 «GANCHO»+marca responde a comentarios · s02 «EL CASO / OLD SPICE / ¿Cuál es tu superpoder?» · s03 «EL MECANISMO / COMENTARIO→GUION→PROMPTER→CÁMARA» · s04 «LA ESCALA / 186 / 6 M·EL DÍA 1» · s05 «LA LECCIÓN / POR SU NOMBRE · RÁPIDO · CON HUMOR» · s06 «TU VERSIÓN / presupuesto tachado» · s07 «EL EJEMPLO / ¿Cómo combino esta chaqueta?» · s08 «LA DOBLE GANANCIA / PARA ELLA» · s09 «LA PRÁCTICA / 3 preguntas + VÍDEO» · s10 «EL CIERRE / 4 preguntas / TUS CLIENTES YA PREGUNTAN» · s11 «Guarda esto» + comentario→clip. En los 11 hay **foco único** y el rótulo es legible sin la voz (OCR completo en los 11). |

---

## Lo que no he podido verificar

- **La escena clara de B2 no se ha visto a resolución completa** más allá del OCR; el juicio de
  «sobra algo» (composición) es de inspección visual de los PNG, no automático.
- **Efecto real del `cover` B2→B3**: medido que la escena pasa de L 213 a L 19 en 0,45 s (t
  8,13-8,57) y que aparece el contenido de B3, y que **no** deja fotograma plano; pero no he
  reconstruido el DOM para confirmar si el `.cover` pinta por encima o por debajo de la escena
  entrante (el resultado observado es correcto en cualquier caso).
- **Sonoridad subjetiva de los clics de teclado** (B5): medido el nivel en el stem, no si el
  oyente los percibe bajo la música.
- **Reproducción en dispositivo real** (TikTok/Reels, canal de audio, tiempos de la UI): no
  verificable aquí; solo geometría y bandas sobre el MP4.

---

_Informe generado por un agente de IA (OpenHands) a partir de la inspección del render; no
sustituye a la revisión humana antes de publicar._
