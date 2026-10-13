# Verificación adversarial — mkt-02 «El tráfico correcto (Google Job Experiment, 2010)»

Rol: verificador adversarial independiente (no he participado en la construcción).
Pieza auditada: `renders/video.mp4` (38,933 s, 1168 fotogramas a 30 fps, 11 escenas).
Fuentes de contraste: `index.html`, `assets/sfx/events.json`, `assets/voice/timing.json`,
`renders/frames/s01.png … s11.png`, `SCRIPT.md`, `STORYBOARD.md`, `DIRECCION.md`,
`investigacion/01-fuentes.md` y `videos/seo-06-canibalizacion/investigacion/03-contrato.md`.

Método: decodificación cruda con
`ffmpeg -i renders/video.mp4 -vf scale=60:107 -pix_fmt rgb24 -f rawvideo -` y análisis en Python.
Medidor de montaje del contrato §2/§6: fila con contenido si su **luminancia media > 25**; fotograma
vacío < ~**4 %** de filas. Acento detectado como verde-lima `#c8ff3d` (r≈200, g≈255, b≈61).

---

## Defectos

### ALTA
Ninguno. No he encontrado ningún incumplimiento de regla dura (sincronía, timeline única, `.from()`/
`Math.random`, hueco de audio, promesa de resultados, afiliación de marca, recurso heredado). Todos
los ítems de la lista de comprobaciones que fallan lo hacen en el margen y se detallan abajo.

### MEDIA

**D1 · El corte B10→B11 deja un tramo casi vacío de 0,10 s justo en el límite.**
Evidencia: fotogramas **1048-1050** (t = **34,933-35,000 s** = **3 fotogramas / 0,100 s**), con
**3,74 % de filas con contenido** (< 4 %, el umbral del contrato) y **luminancia media 14,4/255**
(≈ el lienzo `#0a0a0f`). El fotograma anterior (f1047, t=34,900) estaba a **214/255 con ~99 % de
filas**. Lo que queda en pantalla es solo la píldora de karaoke (fondo `rgba(16,16,22,.86)`) y la barra
de progreso de 6 px: el escenario (el «blanco» de `#s11-blank`) existe pero no registra filas > 25.
`S[11]=34,923` coincide con el fin exacto de `s10` (31,394+3,529 = 34,923), así que es un corte
contiguo sin solape.
Veredicto: **se percibe como un parpadeo / «dead beat» corto, no como un negro prolongado.** Una caída
de ~200/255 mantenida 100 ms (3 fotogramas) en un corte claro→oscuro está en el borde de la percepción;
lo mitiga que el karaoke sigue en pantalla y que la escena entrante es oscura por diseño, pero es el
único tramo del vídeo por debajo del 4 % y conviene eliminarlo.
Arreglo concreto (mínimo y sin romper el corte ni la dirección):
en `index.html`, en el bloque B11, sustituir la entrada con opacidad del marcador por una entrada
**sin opacidad** que ya esté en pantalla en el fotograma 0 de la escena, p. ej.
`grow("#s11-mark", at(11, 0.0), 1, { from: 0.6, dur: 0.18 })` en lugar de
`put("#s11-mark", at(11, 0.05), { scale: 0.5, dur: 0.5 })`.
Así el bloque de acento (`#c8ff3d`, 172 px) aparece en `t=34,923` y las filas suben por encima del 4 %
desde el primer fotograma. Alternativa equivalente: subir el contraste del anillo exterior del blanco
(`--line #26262e` → `--muted #8b8b99`) para que el escenario registre desde el corte.

**D2 · El «barrido» B6→B7 no barre la escena saliente y deja 0,133 s casi a negro antes de la banda.**
Evidencia: el `STORYBOARD` (línea 157) define B6 como «Salida: barrido de color (`.sweep`) 0,45 s», es
decir, la banda debería llevarse la escena del resultado (B6) por delante. En el render, `#s7` (mismo
`z-index:1`, posterior en el DOM) tapa a `#s6` desde 22,292 en el mismo fotograma: medido, la media pasa
de **229,8/255 (f668)** a **14,4/255 (f669)** en un fotograma, sin rastro de contenido claro de B6
durante 22,300-22,742. Además, la banda arranca fuera del encuadre (`xPercent:-130`), por lo que su
primer píxel visible no aparece hasta ~t=22,433:
`f669-672 (22,300-22,400) mean 14,4 · rows 5,6 % · acento 0 %`,
`f673-678 (22,433-22,600) acento 1,4→11,6 %` (pico 11,6 %: la banda se ve, no tapa el cuadro).
Y tras la banda, el escenario sigue teniendo poca materia: `f679-693 (22,633-23,100) rows 5,6-9,3 %`.
Efecto neto: el corte B6→B7 se lee como **corte a negro + banda de acento suelta**, no como el barrido
previsto; y el instante del corte (`S[7]=22,292`, f669) es el segundo más vacío de la pieza
(14,4/255, 5,6 % de filas), por encima del 4 % pero al mismo nivel de negro que D1.
Arreglo concreto: o bien **adelantar el arranque de la banda** para que cruce en el mismo instante del
corte (`xPercent` inicial de −130 → ≈ −60 en el `fromTo` de `#s7-sweep`), o bien **dotar de z-index
superior a la escena saliente** para que la banda realmente barra B6 (como hace `#s2 { z-index:5 }` para
el `cover`), moviendo `#s7-sweep` a `#s6` o subiendo `#s6` por encima de `#s7` durante la transición.

### BAJA

**D3 · B1 usa dos piezas de acento compitiendo.** El contrato §2 exige «un solo acento por escena». B1
(fotograma 0) muestra a la vez la placa `6 €` (`.eurmark`, fondo `#c8ff3d`) y la píldora
`EN GOOGLE ADS` (`.pill.accent`, fondo `#c8ff3d`), además del punto del kicker. Medido: acento
2,51 % del cuadro en f0. Arreglo: dejar en acento solo la placa `6 €` y pasar `EN GOOGLE ADS` a
`.chip` (fondo panel, tinta) —o al revés—.

**D4 · La pista de la barra de progreso está por debajo del panel mínimo.** `index.html:212`
`.progress { background:#1e1e26 }`; el contrato §2 fija «panel oscuro nunca por debajo de `#20202a`»
(`#1e1e26` ≈ luma 30 > 25, así que sigue contando como contenido, de ahí que sea menor). Arreglo:
subir a `#20202a`.

**D5 · La caja de la píldora de karaoke entra 10 px en la zona segura inferior.** Componente
`caption-pill-karaoke.html`: `bottom:470px` y `height:220px` → borde inferior en y=1450, es decir 10 px
por dentro del 25 % inferior (1440 px). Es la posición que **prescribe** el contrato §3
(`bottom:470px`), y el texto queda muy por encima, por lo que es una colisión del propio contrato, no
del montaje. Arreglo: subir la píldora a `bottom:480-500px` si se quiere cumplir §1 al pie de la letra.

**D6 · La ficha de dirección promete más luminancia en la miniatura de la que hay.** `DIRECCION.md`
línea 76: «fotograma 0 = miniatura: luminancia ≈ 230/255». Medido: **221,8/255** (f0) y **221,7/255**
(f15); 100 % de filas con contenido en ambos. La diferencia (~8/255) la produce la píldora oscura del
karaoke en el 25 % inferior. No afecta a la aprobación (sigue muy por encima del 18,7/255 del «gancho
viejo»), pero el número documentado es optimista. Arreglo: corregir la cifra en `DIRECCION.md`.
(Nota: no es un defecto del vídeo; lo anoto por trazabilidad del dossier.)

**D7 · La fila de anuncio de B3 puede leerse como si el texto del anuncio fuera el nombre.**
`index.html:296-298` pinta `<div class="adrow">ANUNCIO · Scott Vitrone</div>`, y justo debajo la barra
de búsqueda con `Scott Vitrone`. Un espectador rápido puede leer «el anuncio dice *Scott Vitrone*»
(el titular real era «Googling yourself is a lot of fun…», que sí aparece correcto en B5). Lo mitigan la
nota `SE BUSCAN A SÍ MISMOS` y que B5 reescribe el texto real. Arreglo: en B3 cambiar el `.adtxt` por
un titular genérico del anuncio (o dejar solo `ANUNCIO` + el nombre en la barra), reservando el texto
literal para B5.

---

## Confirmaciones (medidas)

| # | Comprobación | Resultado medido |
|---|---|---|
| 1 | Miniatura f0 (60×107, rgb24 crudo) | **luminancia media 221,8/255 · 100 % de filas > 25** · acento 2,5 % |
| 1 | f15 (t=0,5 s) | **221,7/255 · 100 % de filas** |
| 1 | La pregunta del beat 1 se lee sola | Sí: barra «¿A quién buscas?» + placa «6 €» + píldora «EN GOOGLE ADS» + karaoke («¿Cuántos contactos podrías conseguir…»). El karaoke arranca en `start:0,0` |
| 2 | Corte 10→11 | f1048-1050 = **34,933-35,000 s (0,100 s) · 3,74 % filas · media 14,4/255** (ver D1) |
| 3 | Instante de cada corte (media / % filas) | S1 221,8/100 · S2 225,8/100 · S3 226,7/100 · S4 26,8/35,5 · S5 232,2/100 · S6 224,9/100 · **S7 14,4/5,6** · S8 16,6/15,0 · S9 230,6/100 · S10 224,3/100 · **S11 14,4/3,7** |
| 3 | Huecos de audio | `silencedetect=noise=-48dB:d=0.12` → **NONE** |
| 4 | Barrido `#s7-sweep` con `x:0` explícito | Sí (`index.html:694`, `fromTo` con `x:0, xPercent:-130, skewX:-12`) |
| 4 | Barrido no tapa el cuadro | Acento máximo en el barrido **11,6 %** (muy lejos del 72-86 % de la trampa de V5). Pero no barre la saliente: ver D2 |
| 5 | `data-start`/`data-duration` | Raíz, `prog`, karaoke, música, sfx y **vo-01…vo-11**: todos con `data-start`+`data-duration` (y `id`) |
| 5 | `class="clip"` | 11 escenas + `prog` + karaoke + música + sfx + 11 audios de voz |
| 5 | Timeline raíz | `window.__timelines["main"] = tl; tl.seek(0);` — una sola, `gsap.timeline({paused:true})` (el karaoke registra la suya, permitido) |
| 5 | `.from()`/`Math.random`/`Date.now`/contadores/`repeat`/`yoyo` | grep → **NONE** en `index.html` y componentes (`repeat` solo en `grid-template-columns`) |
| 5 | Escenario sin animar opacidad | `rise()` (solo `y`) para `#s1-blank`, `#s2/s3/s4/s5/s6/s7/s8/s9/s10-card`, `#s7-blank`, `#s11-blank`; `opacity` solo en elementos de contenido y en el `#s7-crowd` (multitud, no escenario) |
| 5 | Panel oscuro ≥ `#20202a` | `--panel:#20202a` ✓ (salvo `#1e1e26` de la pista de progreso → D4) |
| 5 | Acento como relleno con tinta encima | `#c8ff3d` siempre con `#0b0b10` (eurmark, pill, adrow, pickfill, fivelabel, hl, idealtag, cta-mark). `savewave` es trazo de acento sobre oscuro (permitido) |
| 5 | Rojo solo para errores | No se usa rojo en la pieza (`#ff5a5a`/`#b3161b` ausentes) |
| 5 | Texto en banda segura (288-1440 px) | Kicker/títulos en `top:300px`; `padding:300 74 700`; karaoke `bottom:470` (contrato §3; ver D5) |
| 5 | Un foco dominante por escena | Sí (ver columna «se lee» abajo) |
| 5 | Fuentes locales | `assets/fonts/fonts.css` + 4 `.woff2` (`@font-face`, sin red). GSAP desde CDN jsdelivr (como la plantilla de la casa) |
| 6 | Karaoke vs guion | **123 entradas = 123 palabras** del guion; 11 líneas. Primer grupo (4 palabras) = «¿Cuántos contactos podrías conseguir…»; último = «…tráfico correcto» (fin 38,837 s) |
| 6 | Restos de otras piezas | grep de cafetera/Old Spice/instalación/balanza/comentario/SERP/canibaliz/mkt-01/seo-/GA4 → **NONE** |
| 7 | Cifras sostenidas | 6 (euros/dólares) ✓, cinco directores ✓, cuatro llamadas ✓, dos ofertas ✓, texto del anuncio ✓ — todas `[documentada]` en `01-fuentes.md` |
| 7 | Nombre propio tecleado en B3 | **«Scott Vitrone» = Vitrone, uno de los cinco documentados** (`01-fuentes.md`: «Droga, Granger, Graf, Reichenthal, Vitrone»; CNN cita a Scott Vitrone). Correcto y sin sugerir afiliación (ver D7 por el encuadre) |
| 7 | Sin promesa de resultados | No hay cifra/promesa de resultados del espectador; la práctica se plantea como invitación |
| 8 | Marca Google | `.brandmark` = texto «Google», **tinta `#14141a` sobre tarjeta blanca `#ffffff`**, sin `@` y sin imagen descargada. Sin «oficial»/afiliación |
| 9 | Diferenciación | Sin burbuja de comentario (MK1), sin SERP de Google (V5), sin balanza (V6); sin ejemplos vetados |
| 10 | `S` vs `timing.json` | `S=[0.0,3.158,6.595,11.1,14.908,19.645,22.292,25.264,26.889,31.394,34.923]` = `start` de `timing.json` (11 entradas) |
| 10 | Duración MP4 | 38,933 s (1168 fotogramas) vs composición 38,917 s → Δ 16 ms (redondeo a fotograma) |
| 10 | Voz en los 11 tramos | 11 ficheros, medias −12,1…−15,2 dB (volumedetect) |
| 10 | Música por debajo | `track.wav` media −13,9 dB a `data-volume="0.18"` (≈ −28,8 dB en mezcla) frente a voz a 1,0; sfx a `0.5` |
| 10 | Clics de teclado B3 | 13 `key` (events.json) en local 0,800-1,450 = **7,395-8,045 s**, dentro del beat (6,595-11,55); `sfx.wav` en esa ventana **media −28,5 dB / máx −11,5 dB**, muy por debajo de la voz |

### Retención fotograma a fotograma (¿se lee el mensaje de su línea sin la voz?)

| Frame | Línea (guion) | Qué hay en pantalla | ¿Se lee? |
|---|---|---|---|
| s01 | «¿Cuántos contactos… con 6 euros en Google Ads?» | Barra «¿A quién buscas?» + «6 €» + «EN GOOGLE ADS» | **Sí** |
| s02 | «Se lo preguntó Alec Brownstein, publicista, en 2010» | «2010» + «Alec Brownstein» + «PUBLICISTA» | **Sí** |
| s03 | «los directores creativos se buscan a sí mismos» | «Google» + «ANUNCIO/Scott Vitrone» + barra + «SE BUSCAN A SÍ MISMOS» | **Sí** (depende de la nota; ver D7) |
| s04 | «Eligió a cinco y compró anuncios…» | 5 nombres (Droga, Granger, Graf, Reichenthal, Vitrone) + casillas marcadas + «SOLO ESOS NOMBRES» | **Sí** |
| s05 | «El anuncio decía: …» | «Google» + barra + tarjeta con el texto resaltado | **Sí** |
| s06 | «Cuatro de los cinco le llamaron y recibió dos ofertas» | «4/5 LE LLAMARON» · «2 OFERTAS» | **Sí** |
| s07 | «…quería a esas cinco» | multitud apagada → «ESAS CINCO» sobre el blanco | **Sí** |
| s08 | «Eso mismo vale para tu negocio» | cinco → puente → «TU NEGOCIO» + «EL MISMO GESTO» | **Sí** |
| s09 | «…piensa qué buscaría tu cliente ideal» | «abogado»/«dentista» tachados + lupa + «TU CLIENTE IDEAL» | **Sí** |
| s10 | «…sean tus mejores clientes» | barras cortas + «BÚSQUEDAS AL MES» + «TUS MEJORES CLIENTES» | **Sí** |
| s11 | «Guarda esto… el tráfico correcto» | marcador + «Guarda esto» + «EL TRÁFICO CORRECTO» + blanco | **Sí** |

---

## Lo que no he podido verificar

- **Nada he visto con mis ojos «reales»**: los 11 PNG y el MP4 se han medido por muestreo de píxeles
  (luminancia, filas con contenido, cobertura de acento, coincidencia fotograma↔PNG por luminancia).
  No he hecho OCR ni he inspeccionado la composición gráfica fina (alineaciones, pesos, recortes de
  texto dentro de las tarjetas) ni el encuadre subjetivo.
- **La coincidencia PNG↔fotograma** se estimó por luminancia media, que es ambigua entre las escenas
  claras (varias dan ~225-232). Las tres oscuras (s03, s07, s11) sí casan sin ambigüedad.
- **Si el corte B10→B11 se percibe o no** es un juicio: mi veredicto de “parpadeo corto” se apoya en la
  medida (único tramo < 4 %, caída de ~200/255 mantenida 0,10 s), no en una proyección a pantalla.
- **Separación voz/música en la mezcla final**: he medido los niveles de los activos por separado y los
  `data-volume` del HTML (música 0,18); no he podido aislar la música de la voz dentro del MP4.
- **`check`/`npm run check`**: no lo he ejecutado (no he reproducido la cadena de herramientas); las
  reglas duras las he comprobado por lectura del HTML y medida del render.
- **Las fuentes originales** (CNN, NPR, D&AD, blogspot…) no se han reabierto: he contrastado contra
  `investigacion/01-fuentes.md`, que es lo único afirmable según el encargo.
