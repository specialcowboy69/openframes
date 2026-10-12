# 04 — Verificación adversarial de V6 «Canibalización de palabras clave»

> **Nota de revisión (2026-10-11).** Este informe se ejecutó sobre la **revisión anterior** del guion
> (**12 líneas · 166 palabras · 41,71 s**). El guion vigente es **11 líneas · 142 palabras · 35,68 s**
> (`SCRIPT.md`), así que las referencias `Lx` de abajo (L9, L11, L12…) corresponden a aquella
> revisión. Los defectos del BLOQUE 1 quedaron resueltos en el guion o en el plan visual actuales
> (salvo las incoherencias de repositorio del B9, ajenas a V6).

Verificador sin participación en la escritura. Auditados: `SCRIPT.md`, `BRIEF.md`,
`STORYBOARD.md`, `DIRECCION.md`, `DIRECCION-ARTE-BRIEF.md`.
Referencias: `investigacion/01-fuentes.md`, `02-continuidad.md`, `03-contrato.md`,
`PROFILE.md`, `DESIGN.md`, `IDEAS.md` y los `.wav`/`index.html` de V5 para comprobar helpers.
Toda cita de fichero va con `línea:`; los comandos ejecutados se indican en el BLOQUE 2.

---

## BLOQUE 1 — Defectos

### GRAVEDAD ALTA

**A1. Afirmación absoluta no respaldada: «verás siempre» (L9).**
- Cita: `SCRIPT.md:25` y `SCRIPT.md:76` — «En Search Console **verás siempre** dos páginas tuyas
  compitiendo por la misma búsqueda.»
- Problema: `01-fuentes.md` §3.4 solo dice que es un **patrón a buscar**: «para esa consulta
  aparecen dos o más URLs tuyas con impresiones o clics. **Esa es la pista**». No es una garantía
  ni una condición necesaria. «Siempre» convierte una señal a inspeccionar en un hecho automático,
  y contradice el criterio del propio guion (`SCRIPT.md:10`: «todo lo afirmado está en
  `investigacion/01-fuentes.md`»).
- Arreglo: quitar el absoluto. Propuesto (12 palabras, sigue ≤14):
  «En Search Console puedes ver Dos páginas de tu sitio web compitiendo por la misma búsqueda.»

**A2. Acento usado como trazo sobre fondo claro (regla dura incumplida) en dos elementos.**
- Cita: `DIRECCION.md:278` — `.prow.dup { box-shadow:inset 4px 0 0 var(--accent); }` (B9: panel
  **claro** `#ffffff`, `DIRECCION.md:76` la fila va «sobre claro»). Cita: `DIRECCION.md:270` —
  `.fusearw { display:flex; justify-content:center; color:var(--accent); }` (B10 es escena
  **clara**, `DIRECCION.md:70`).
- Problema: la propia pieza prohíbe el acento como texto/trazo en claro. `DIRECCION.md:61`:
  «verde sobre claro (≈1,3:1) **prohibido** como texto o trazo»; `DIRECCION.md:307` (riesgo 1):
  «El acento solo aparece en rellenos». La flecha de fusión es un trazo (`draw()` sobre `path` →
  `currentColor` = acento) y la fila duplicada es una línea de acento de 4 px sobre blanco:
  contraste ≈1,3:1, `check`/WCAG AA la marcará o será invisible.
- Arreglo: (a) `.prow.dup` → sustituir el trazo de acento por relleno: `background:#dff2b0;` (o
  filo `#4d5a29`); (b) `.fusearw` → trazo en tinta oscura sobre claro (`color:#4d5a29` o
  `#14141a`) o pasar B10 a tema oscuro. Revisar también `.splitbar .seg.l` (acento como relleno
  sobre papel, `DIRECCION.md:264`): usar el tinte `#dff2b0` como en V5 o justificar la excepción.

### GRAVEDAD MEDIA

**M1. `DIRECCION.md` se contradice sobre la balanza y sobre «una familia por escena».**
- Cita: `DIRECCION.md:13` — «La balanza **reaparece tres veces**» (B2, B4, B11 según
  `DIRECCION.md:15-19`). Frente a `DIRECCION.md:112` — familia 1 «· **B1, B2, B3, B4, B11**».
  Y `DIRECCION.md:125` — «Cinco familias, **ninguna escena con dos familias a la vez**», frente a
  `DIRECCION.md:124` — «**B1(1,2)**».
- Problema: `STORYBOARD.md` B1 (líneas 24-40) **no contiene `.scale`**: es la SERP con el
  distintivo «TURNO» (familia 2). Y B3 (líneas 63-78) es una escala vertical de posición
  (`#s3-ladder`), no la balanza. Por tanto B1 no puede ser familia 1, y B1(1,2) contradice la
  propia frase «ninguna escena con dos familias a la vez».
- Arreglo: familia 1 → «B2, B4, B11»; reparto por beat → «B1(2)»; si B3 cuenta como familia 1,
  definir su `.scale` en `STORYBOARD.md` (hoy no existe) o sacarlo de la familia.

**M2. Elementos nuevos sin CSS, contra la regla 10 de la propia dirección.**
- Cita: `DIRECCION.md:216` — «Todo elemento nuevo trae su CSS (clase, medidas, colores) en §8».
  Faltan: `#s9-dup` («marca de duplicado», `STORYBOARD.md:162`; declarado **Nuevo** en
  `STORYBOARD.md:233`) y `#s3-ladder`/`#s3-mark`/`#s3-pos` (`STORYBOARD.md:67-68`, con el número
  de posición). No aparecen en `DIRECCION.md` §8 (líneas 220-300) ni en la tabla de reutilizados.
- Arreglo: añadir a §8 `.ladder`, `.ladder .mark`, `#s9-dup` (con medidas, colores, `warn`/tinte y
  `transform-origin`), o reclasificarlos como reutilizados del kit y citar de dónde salen.

**M3. Colisión de medidas: `.pcard` 340 px dentro de `.seat` 300 px (B2).**
- Cita: `DIRECCION.md:234` — `.pcard { width:340px; … }`; `DIRECCION.md:253` —
  `.scale .seat { position:relative; width:300px; … }`; `STORYBOARD.md:47-49` coloca `#s2-a`,
  `#s2-b` (`.pcard`) en `#s2-seatL`/`#s2-seatR` (`.seat`).
- Problema: la ficha (340 px) no cabe en el plato (300 px) → desborde de 40 px o solape entre
  platos (`.scale` solo mide 680 px, `DIRECCION.md:247`, y dos platos de 300 dejan 80 px).
- Arreglo: unificar a `width:340px` en `.seat` (y subir `.scale` a `760px`), o bajar `.pcard` a
  `260px` dentro del plato, o `transform:scale()` de las fichas del plato.

**M4. Tabla de jerga con líneas equivocadas en `SCRIPT.md`.**
- Cita: `SCRIPT.md:38` — «**Intención** | `5-6, 10`»; `SCRIPT.md:39` — «**Consulta** | `6, 9`».
- Problema (comprobado con `grep` sobre el guion plano): la palabra «intención» aparece **solo en
  L10**; L5-L6 expresan la idea pero no usan el término. La palabra «consulta» aparece **solo en
  L6**; **L9 dice «búsqueda»**, no «consulta». Los rangos citados no corresponden al uso real.
- Arreglo: «Intención | 10»; «Consulta | 6» (y anotar que L9, 2 y 7 dicen «búsqueda»).

**M5. B1: la descripción del fotograma 0 no la respalda la receta (riesgo para la miniatura).**
- Cita: `STORYBOARD.md:28` — «Nada de pantalla vacía: **en el fotograma 0 ya están la ventana, la
  consulta y las dos fichas**.» Frente a `STORYBOARD.md:33-34` — `put("#s1-q", at(1,0.15))`,
  `put("#s1-oa", at(1,0.20))`, `put("#s1-ob", at(1,0.50))`.
- Problema: en el kit, `put()` es un `fromTo` con `opacity:0→1` (`videos/seo-05-intencion-de-busqueda/index.html:598-602`),
  así que la consulta y **las dos fichas nacen invisibles** y aparecen a 0,15/0,20/0,50 s. El
  fotograma 0 solo tiene la ventana (con `rise()`) y los esqueletos; la afirmación «ya están …
  la consulta y las dos fichas» es falsa y compromete el requisito de miniatura
  (`DIRECCION-ARTE-BRIEF.md:41`: «≈ 100 % de filas con contenido», «nada de … desvanecidos»).
- Arreglo: subir la ventana y las dos fichas con `rise()` (visibles a 0) y dejar el turno (`swap`)
  como animación, o corregir la descripción. Medir el fotograma 0 antes de aprobar.

**M6. «Consulta única» del encabezado contra dos consultas en B5.**
- Cita: `STORYBOARD.md:17` — «**Consulta única del vídeo (mono): «instalación de luz».**» Frente a
  `STORYBOARD.md:96-97` — B5 «cada una con **su propia consulta** (una de contratar, otra de
  informarse)»; `STORYBOARD.md:105` — «dos chips de consulta».
- Problema: si B5 muestra dos consultas distintas, la pieza no tiene «consulta única».
- Arreglo: redactar el encabezado como «consulta de **ejemplo** única: «instalación de luz» (B2,
  B6, B7, B9)» y fijar en B5 los dos textos de chip (p. ej. «instalación de luz» vs «precio
  instalación de luz»), o renombrar B5 para no apoyarse en consultas distintas.

**M7. Tamaños de `.title` (150/130 px) sin CSS; riesgo de desborde del término.**
- Cita: `DIRECCION.md:89-90` — «CANIBALIZACIÓN (B4, **150 px**)», «NINGUNA GANA (B11, **130 px**)».
  El kit redefine `.title` a **110 px** (`videos/seo-05-intencion-de-busqueda/index.html:135`) y
  `DIRECCION.md` §8 no da override. Banda útil = 1080−2·74 = **932 px** (`DIRECCION.md:299-300`).
- Problema: «CANIBALIZACIÓN» (14 glifos, mayúsculas, peso 900) a 150 px supera con holgura los
  932 px y no puede partirse (una sola palabra). Queda por resolver el encaje.
- Arreglo: fijar el tamaño real en §8 tras medir («Medir el texto tras `document.fonts.ready`»,
  `DIRECCION.md:98`) y bajar a un valor que quepa (≈110 px con `letter-spacing:-0.03em`) o partir
  el término en dos líneas.

**M8. Opinión presentada como hecho en L3 («la posición que merece»).**
- Cita: `SCRIPT.md:21` y `SCRIPT.md:70` — «ninguna de las dos consigue **la posición que
  merece**».
- Problema: `01-fuentes.md` §1 dice «ninguna **rinde lo que podría**» (rendimiento), y §6 habla de
  «ninguna acaba primera». «Merece» es un juicio de valor que la fuente no sostiene y suena a
  promesa/opinión.
- Arreglo (13 palabras, ≤14): «Y el resultado es que ninguna de las dos consigue la posición que
  podría.»

**M9. Afirmación absoluta en L6 («solo cuando»).**
- Cita: `SCRIPT.md:22` y `SCRIPT.md:73` — «Compiten **solo cuando** las dos páginas ofrecen la
  misma respuesta a la misma consulta.»
- Problema: `01-fuentes.md` §1 dice que la causa **no es** el mismo tema sino disputar «la misma
  consulta con la misma intención»; no afirma que sea la única causa posible. «Solo cuando» es una
  condición necesaria y suficiente no respaldada.
- Arreglo: «Compiten cuando las dos páginas ofrecen la misma respuesta a la misma consulta.»
  (11 palabras).

**M10. Estado del guion desactualizado respecto a los ficheros que ya existen.**
- Cita: `SCRIPT.md:7` — «Pendiente de voz, storyboard y montaje.»
- Problema: `STORYBOARD.md`, `DIRECCION.md` y `DIRECCION-ARTE-BRIEF.md` ya están escritos (este
  mismo entregable los audita). El estado induce a error sobre qué falta.
- Arreglo: «Pendiente de voz y montaje» (o el estado real).

**M11. Objetivo de duración incoherente con el repositorio.**
- Cita: `BRIEF.md:4` y `SCRIPT.md:30` — «objetivo **40-50 s**». Frente a `PROFILE.md:29` — «Objetivo
  **30-40 s**» — y `03-contrato.md:5`/§5 — «total **30-40 s**».
- Problema: la pieza se planifica a 41,7 s, fuera del objetivo declarado en `PROFILE.md` y en el
  contrato. `IDEAS.md:29` decía «~40 s».
- Arreglo: decidir y alinear las tres cifras (o registrar la excepción como se hizo con V5). Si se
  acepta 40-50, anotarlo en `DECISIONS.md` y corregir `PROFILE.md`/`03-contrato.md`.

### GRAVEDAD BAJA

**B1. Cifra inventada en pantalla (B3).** `STORYBOARD.md:74` fija la posición en `"8"` y
`STORYBOARD.md:68` «número **8**». `01-fuentes.md` dice que no hay cifras verificables y el brief
prohíbe cifras (`DIRECCION-ARTE-BRIEF.md:88`). Es ilustrativa, pero conviene una marca no numérica
(p. ej. «↓ varias posiciones») o etiquetarla como ejemplo.

**B2. Referencia a una clase inexistente: `.pumark`.** `DIRECCION.md:307` la menciona como relleno
de acento; no está definida en §8 ni en el kit. Eliminarla o definirla.

**B3. `.splitbar` por debajo del mínimo de panel.** `DIRECCION.md:262` usa `background:#1e1e26`,
inferior a `#20202a` (el contrato prohíbe «panel oscuro por debajo de `#20202a`»,
`03-contrato.md:45-47`). La pista de progreso ya usa `#1e1e26` en la serie, así que probablemente
sea admisible, pero unificar a `#20202a` elimina la duda.

**B4. Riesgo de token `--panel`.** `DIRECCION.md:234` usa `var(--panel)` en `.pcard`; el token base
del sistema es `#14141a` (`DESIGN.md:48`), por debajo del mínimo. Hay que asegurar que este
`index.html` define `--panel:#20202a` (como la variante clara/oscura de `DESIGN.md`, líneas
199-210) o usar el hex directo.

**B5. Firma de `setNum` divergente del contrato.** `03-contrato.md:266` (lista de helpers) declara
`setNum(txt,t)`; `DIRECCION.md:207` y `STORYBOARD.md:13` usan `setNum(sel,txt,t)`. La decisión está
justificada (`DIRECCION.md:330`), pero el contrato no se actualizó.

**B6. Opacidad de la ficha atenuada incoherente.** `DIRECCION.md:239` define
`.pcard.faded{opacity:0.42}` pero la receta de B10 anima a `opacity:0.35`
(`STORYBOARD.md:139`). Igualar a un solo valor.

**B7. L11 «deja solo una» puede leerse como «borra la otra».** `SCRIPT.md:27` y `SCRIPT.md:78`.
`01-fuentes.md` §5 documenta que **no** hay que borrar sin más; conviene precisar
«deja solo una con vida» / «quítale el peso a la otra». Baja, pero evita contradecir §5.

**B8. Cinco mecanismos de transición para ~42 s.** `DIRECCION.md:159` usa cinco familias
(`slide, forma, cover, circle, sweep`), cuando `DESIGN.md` fija «un mecanismo distinto cada 10-12 s
→ 30-45 s: **3-4**». No es una violación dura, pero excede la regla proporcional; justificar o
reducir a cuatro.

**B9. Incoherencias del repositorio confirmadas (ítem 8).** Todas reales:
- `IDEAS.md:29` (fila V6): «9:16 · ~40 s | **Idea**» — pero V6 ya tiene guion, brief, storyboard y
  dirección. Actualizar a ~41,7 s y estado.
- `IDEAS.md:28` (fila V5): «10 escenas · 123 palabras ≈ 41 s. Pendiente: voz `Pablo` y montaje» —
  real: **12 escenas · 188 palabras · 53,041 s**, voz y montaje hechos (`seo-05/BRIEF.md:4`,
  `seo-05/STORYBOARD.md:4`). Merece corregirse.
- `IDEAS.md:15`: estado de la serie SEO solo lista V1-V3; no cita V5 ni V6. Corregir.
- V5 `SCRIPT.md:3` «~60 s» frente a **53,041 s**; `SCRIPT.md:28` «186 palabras» frente a **188**
  (`seo-05/STORYBOARD.md:4`). Corregir.
- V5 gancho contado dos veces: `seo-05/SCRIPT.md:15` da **19** y `SCRIPT.md:49`, **18**. Corregir.
- V2 `seo-02-modificador-lujo/SCRIPT.md:6` «Duración real (index.html): **34,09 s**» frente a
  `STORYBOARD.md` (`duration: 29.8s`) e `IDEAS.md:25` (**29,8 s**). Corregir.
- Prioridad de arreglo: la fila V5 de `IDEAS.md` y el estado de la serie (afectan a la
  continuidad); V2 34,09 vs 29,8 (afecta a duraciones); el resto, cosmético.

**B10. Cita imprecisa en el contrato de continuidad.** `02-continuidad.md` §6 afirma «**188** en
`BRIEF.md:4`/`STORYBOARD.md`», pero `seo-05/BRIEF.md:4` no contiene el número de palabras (solo
`STORYBOARD.md:4`). Corregir la cita.

**B11. Afirmación causal en L2 (matiz).** «se acaban quitando fuerza entre ellas»
(`SCRIPT.md:20`) es una paráfrasis de «ninguna rinde lo que podría» (`01-fuentes.md` §1); es
aceptable, pero es la única formulación causal no literal del guion. Si se quiere ser estricto,
alinearla con la fuente.

---

## BLOQUE 2 — Confirmaciones

| # | Comprobación | Resultado |
|---|---|---|
| 1 | Afirmaciones contra `01-fuentes.md` | L1, L2, L4-L8, L10-L12 respaldadas (definición §1, señales §2, detección §3, arreglo §4, ejemplo §6). **No** respaldadas: L9 «siempre» (A1), L3 «merece» (M8), L6 «solo» (M9). |
| 2 | Líneas >14 palabras | **NINGUNA** (`python3 -c "import re;… "`: 12 líneas, todas ≤14). |
| 2b | Jerga antes de explicar | Correcto: «canibalización» solo aparece en L4, tras explicar el fenómeno. «intención» se da por sabida de V5 (autorizado por `BRIEF.md`, público «puede no haber visto V5»). |
| 2c | Gancho por miedo / penalización | No. L1 describe el síntoma; ninguna línea afirma penalización. |
| 2d | Más de un ejemplo | No: un único ejemplo (página de servicio vs artículo, B7); B1/B5/B6/B8/B11 son genéricos. |
| 2e | Anglicismos | No en la voz: solo «Search Console» (nombre de producto, autorizado) y «SEO» en el encabezado. |
| 2f | Cierre de guardar | Sí: L12 CTA + rótulo «Guarda esto» (96 px), `STORYBOARD.md:201`. |
| 3 | Tabla vs `## Guion plano` | **Idénticos**, mismo orden y mismas palabras (comparación programática = `True`). |
| 3b | Recuentos y suma de la tabla | Coinciden con el conteo real: 14/14/14/14/14/14/13/14/13/14/14/14. Suma tabla = **166** = suma guion plano. |
| 3c | Regex del pipeline | `python3 -c "import re;print(re.findall(r'^    (\S.*)$', open('videos/seo-06-canibalizacion/SCRIPT.md',encoding='utf-8').read(), re.M))"` → **12 líneas**, exactamente las del guion plano, sin extras. |
| 3d | 166/3,98 ∈ [40,50] s | **41,71 s** ✅ (dentro de 40-50). |
| 4 | Solapamientos con piezas previas | **Ninguno real.** «cafetera», GUÍA/COMPARATIVA/PRODUCTO, cuatro posiciones de V1, «zapatillas»/lujo/URL (V2), autoridad/3-vs-118/`medio.com`/`otratienda.com`/Enlaces (V3) aparecen **solo en listas de veto**, nunca como contenido. Search Console se usa en Rendimiento→Páginas. |
| 5 | Contrato de producción (plan visual) | Cumple: primer fotograma claro (B1 `#f4f1ea`); un foco dominante (`DIRECCION.md:187`); niveles de texto dentro de banda (`DIRECCION.md:87-95`); banda `300/74/470` (`DIRECCION.md:299`); estado inicial en CSS + `fromTo`/`.to()`; **sin `.from()`/contadores/random**; `rise()` sin opacidad para el escenario; `.cover` `#20202a`; rojo solo en B3 (pérdida); trampa `xPercent` del barrido documentada con `x:0` explícito. **Incumple:** acento como trazo sobre claro (A2) y `#1e1e26` (B3). |
| 6 | Coherencia entre los 3 documentos visuales | IDs/recetas/transiciones/tiempos coinciden entre `STORYBOARD`↔`DIRECCION` (p. ej. las 11 salidas y sus duraciones). **Falla:** `#s9-dup` y `#s3-ladder`/`#s3-mark`/`#s3-pos` sin CSS (M2), `.title` 150/130 sin override (M7), balanza familia 1 (M1). |
| 7 | Ritmo (tabla de tiempos) | Cuadra con 12 beats; cada dur. = palabras/3,98 (14→3,52; 13→3,27); arranques/fin acumulados correctos; total 41,71. Ninguna animación supera su escena (último evento ≤2,6 s < 3,27 s mínimo); B7 y B9 (3,27 s) son los más justos. |
| 8 | Incoherencias del repositorio | Confirmadas todas (ver BLOQUE 1, B9). Merecen corrección: fila V5 de `IDEAS.md`, estado de la serie (`IDEAS.md:15`), 186↔188 y 60↔53,041 (V5), 34,09↔29,8 (V2). |
| 9 | «3,98 pal./s» | Estimación de producción, no una afirmación del guion; no requiere fuente. |

---

## BLOQUE 3 — Lo que no he podido verificar

1. **Implementación real (`index.html`, render, `check`, `verificar_montaje.py`).** No existen
   todavía para V6; todos los juicios sobre contraste, `--panel` y desbordes son sobre el CSS/plan
   descritos, no medidos. Las cifras de luminancia del fotograma 0 (B1) son estimaciones del
   documento («≈230/255»), no medidas.
2. **Encaje real del término «CANIBALIZACIÓN» a 150 px** (M7): depende de las métricas exactas de
   Inter tras `document.fonts.ready`; solo puedo señalar el riesgo, no el tamaño que cabe.
3. **Duración real de la voz.** El 41,71 s es la proyección 166/3,98; la fija `voice_pipeline.py`
   y la aplica `retime.py`, aún no ejecutados.
4. **Cumplimiento final de contraste WCAG AA.** El `check` no se ha corrido; A2 se deduce de los
   hex (§2 y §8), no de una medición.
5. **API real de `swap()` y del karaoke de V6.** Verifiqué `put/rise/draw/grow/typeWords/swap/setNum`
   en V5 (`index.html:598-634`); V6 introduce `setNum(sel,…)` y aún no tiene `index.html` propio
   donde confirmarlo.
6. **Interpretación de «consulta única» (M6).** Depende de la intención de los autores; señalo la
   contradicción textual, no el contenido final de los chips.
7. **Cifras de `IDEAS.md` sobre V5** (53,041 s / 188 palabras): confirmadas contra
   `seo-05/BRIEF.md` y `STORYBOARD.md`, pero no contra el render final.
