# 04 — Verificación adversarial — mkt-01 «Responde con vídeo (Old Spice 2010)»

Revisión independiente de `SCRIPT.md`, `BRIEF.md`, `STORYBOARD.md`, `DIRECCION.md` y
`DIRECCION-ARTE-BRIEF.md` contra `investigacion/01-fuentes.md`, `investigacion/02-continuidad.md`,
`videos/seo-06-canibalizacion/investigacion/03-contrato.md`, `PROFILE.md` y `DESIGN.md`.
No he participado en la escritura de la pieza. Todo lo que sigue lleva cita y comando cuando aplica.

---

## BLOQUE 1 — Defectos

La severidad se ordena por el daño real: **alta** = rompe una regla dura o miente sobre un dato
heredado; **media** = incoherencia interna o afirmación no soportada; **baja** = imprecisión que no
cambia el resultado.

### ALTA

**1. El guion ordena un contador ascendente, que el contrato prohíbe expresamente.**
- Cita: `SCRIPT.md:20` → `| 4 | En total, 186 vídeos... | 13 | La escala | Contador que sube a 186; la cifra «6 M» creciendo el «día 1» |`.
- Por qué es un problema: el contrato heredado lo prohíbe sin matices — `03-contrato.md:18-19`
  «**Prohibido** `.from()`, `Math.random`, `Date.now`, **contadores que suben** (los números se cambian
  con `tl.set(..., {textContent})`)» — y el propio `STORYBOARD.md:84` dice lo contrario de lo que dice el
  guion: «La cifra aparece de golpe (`setNum`), **nunca contando**». La columna «Qué se ve» de la tabla
  es la fuente de la que se monta la escena, así que si se sigue literalmente se rompe la regla dura.
- Arreglo: reescribir la celda para que describa el salto discreto, p. ej.
  «La cifra 186 aparece de golpe (`setNum`); pastilla «6 M · EL DÍA 1»».

### MEDIA

**2. «Dos días y medio» sin la cautela que la fuente recomienda, y la nota afirma una cautela que el
guion no tiene.**
- Cita: la línea 3 (`SCRIPT.md:73`) dice «…durante **dos días y medio**.»; y `SCRIPT.md:34` dice
  «**en torno a dos días y medio** (línea 3)».
- Por qué es un problema: `01-fuentes.md:31` marca el dato como «**Alta-matizada**: la cobertura en
  directo describe ~2 días de rodaje (13 y 14 de julio); **conviene decir «en torno a dos días y medio»**».
  El guion lo dice sin la cautela y su propia nota lo cita mal, así que presenta como firme un dato que
  la investigación pide matizar.
- Arreglo (cabe en 14 palabras): sustituir la línea 3 por «Un equipo grababa cada respuesta en minutos,
  en torno a dos días y medio.» (14 palabras) — se quita «escribía y» y entra «en torno a».

**3. Se usan tres transiciones de acento donde el contrato heredado admite una o dos.**
- Cita: `DIRECCION.md:168` → «acentos: `cover`, `circle`, `sweep` (**3**)»; frente a
  `03-contrato.md:75` → «Reparto: **una primaria (60-70 %)** + **1-2 acentos**».
- Por qué es un problema: es una regla dura heredada «tal cual» (`02-continuidad.md:3-4`). El plan
  reconoce el desvío («se usan cuatro») pero no lo justifica ni lo anota. (Sí encaja con otra regla del
  sistema, `DESIGN.md` «un mecanismo distinto cada 10-12 s → 30-45 s: 3-4»; el conflicto es entre las
  dos reglas heredadas y el plan lo resuelve en silencio.)
- Arreglo: reducir a dos acentos (p. ej. `B3→B4` de `circle` a `slide`) o anotar la excepción en
  `DECISIONS.md` citando la regla proporcional de variedad.

**4. «Las seis familias» pero la tabla solo lista cinco.**
- Cita: `DIRECCION.md:155` → «Las **seis familias** están disponibles…»; la tabla que sigue
  (`DIRECCION.md:162-166`) enumera `slide`, `sweep`, `cover`, `circle`, `cut` (**cinco**).
  El contrato sí tiene seis (`03-contrato.md:66-73`), e incluye «Continuidad por forma (`forma`)».
- Por qué es un problema: se pierde una familia al copiar; el texto dice «seis» y la tabla cinco.
- Arreglo: añadir la fila `forma` a la tabla o cambiar «seis» por «cinco».

**5. Las bandas tipográficas declaradas no cuadran con el CSS que las implementa.**
- Cita: `DIRECCION.md:94-96` declara «Frase principal **70-110**» (metiendo ahí `.lesstag .tx` a
  **54 px**, `DIRECCION.md:323`) y «Contexto **38-56**». Pero en el propio CSS hay textos por debajo
  de 38: `.cmsg .av` 22 (`:253`), `.station .lb` 26 (`:288`), `.cmotif .cbubble` 26 (`:380`),
  `.vmark` 28 (`:366`), `.destcard .dl` 30 (`:355`), `.chatbar .qt` 34 (`:346`), `.bubbles .cbubble`
  34, `.qrow .qt` 36; y `.brandmark` 64 px (`:279`) no cae en ninguna banda.
- Por qué es un problema: el contrato fija «contexto 38-56» y la pieza lo incumple en ocho elementos;
  la frase que lista 54 px bajo «70-110» se contradice a sí misma.
- Arreglo: rehacer la tabla de niveles (p. ej. «rótulos 22-36», «contexto 38-56») o subir los tamaños.

**6. La velocidad de voz declarada contradice el contrato que dicen heredar.**
- Cita: `SCRIPT.md:29`, `BRIEF.md:48` y `STORYBOARD.md:253` usan **3,5 pal./s** «medida en la pieza
  anterior»; el contrato heredado `03-contrato.md:4` declara **3,98 pal./s** para la misma voz `Pablo`.
- Por qué es un problema: el único respaldo de 3,5 es indirecto — `DECISIONS.md:45` (D38): V6 se aceptó
  en **≈40,27 s** con 142 palabras → 142/40,27 ≈ **3,53**. Eso no está citado en mkt-01, así que la
  cifra «medida en la pieza anterior» choca con la única medición que consta en el documento heredado.
- Arreglo: justificar el 3,5 citando D38/40,27 s (o `seo-06/SCRIPT.md:3,31`), o unificar la velocidad
  con el contrato.

**7. «Sin presupuesto de anuncio / solo un móvil» es una afirmación absoluta que las fuentes no
sostienen y que oculta el principal «no se traslada» del caso.**
- Cita: línea 6 (`SCRIPT.md:22`, `SCRIPT.md:76`) y la tesis (`SCRIPT.md:5`, `BRIEF.md:20`).
- Por qué es un problema: `01-fuentes.md:60-61` (§4 «Por qué funcionó allí») dice «Escala y presupuesto:
  agencia global, equipo dedicado, sistema tecnológico propio y guionistas profesionales. El propio caso
  reconoce que **el mayor coste era producir el vídeo**». La pieza no dice en ningún sitio que el caso
  tuviera ese presupuesto; al contrario, tacha el cartel «PRESUPUESTO DE ANUNCIO» (B6). La invitación es
  legítima, pero presentarla como «no necesitas presupuesto» sin el caveat es una promesa de
  transferibilidad que la fuente matiza.
- Arreglo: matizar («para empezar no necesitas comprar anuncios») y/o añadir el caveat de §4; no cerrar
  el caso como si fuera gratis.

**8. «Esa respuesta también ayuda a otros» es un beneficio afirmado sin fuente.**
- Cita: línea 8 (`SCRIPT.md:24`, `SCRIPT.md:78`).
- Por qué es un problema: `01-fuentes.md:54-56` dice que «**no se ha encontrado ningún estudio**
  independiente y sólido que mida el efecto de responder con vídeo a comentarios en un negocio pequeño…
  **La pieza no debe prometer resultados**». Un comentario público «ayuda a otros» es un resultado, no
  un hecho de la mecánica.
- Arreglo: reformular a alcance visible, que sí se sigue de la mecánica: «Respondes con un vídeo corto
  y otros también lo ven.» (12 palabras).

### BAJA

**9. `.prompter` baja del suelo de panel oscuro.**
- Cita: `DIRECCION.md:296` (y `:70`) → `.prompter { background:#0e0e14; ... }`, frente a
  `DIRECCION-ARTE-BRIEF.md:44` «**Panel oscuro nunca por debajo de `#20202a`**».
- Por qué es un problema: `#0e0e14` (media ≈ 16) está por debajo del umbral 25 que usa el medidor de
  montaje; una fila dominada por el teleprompter puede contarse como vacía.
- Arreglo: subir a `#20202a` o declarar el teleprompter como `field` (token `#0e0e14` del contrato).

**10. La tabla de ritmo redondea mal los arranques/fines (0,01 s).**
- Cita: `STORYBOARD.md:264-269`: B4 fin **14,86** (11,14+3,71 = 14,85), B6 fin **20,29** (17,71+2,57 =
  20,28), B7 24,29 (20,29+4,00 = 24,29 según su propio arrastre), B9 30,29 (27,71+2,57 = 30,28).
- Por qué es un problema: el total final (35,43) sí cuadra, pero los acumulados internos no son la suma
  de sus duraciones; con 2 decimales el error es de un céntimo.
- Arreglo: recalcular con más decimales o anotar que son valores redondeados.

**11. `DIRECCION.md:409` afirma que el callout está visible desde `t=0`, pero la receta lo entra a 0,10 s.**
- Cita: `DIRECCION.md:409` → «el hilo, la burbuja, el kicker **y el callout** están visibles desde `t=0`»;
  `STORYBOARD.md:36` → `put("#s1-label", at(1,0.10),{x:-20})`.
- Por qué es un problema: la afirmación literal es falsa; afecta a la miniatura del fotograma 0 (el
  rótulo «ESTA MARCA» no está en el primer fotograma).
- Arreglo: mover `#s1-label` a `at(1,0.0)` o corregir la afirmación.

**12. Inclinaciones de B10: ±4° en la dirección, ±2° en las recetas.**
- Cita: `DIRECCION.md:145-146` «Las inclinaciones (≤ 8°) … (B10, **±4°**)»; `STORYBOARD.md:185-186`
  `rot:-2` / `rot:2`.
- Arreglo: unificar en un solo valor.

**13. «Se alterna movimiento con lectura» no describe la secuencia real.**
- Cita: `STORYBOARD.md:246` → «Se alterna movimiento con lectura: B1 mov · B2 mov · B3 mov · B4 mov ·
  B5 lec · …».
- Por qué es un problema: hay cuatro «mov» seguidos y luego tres; no alterna.
- Arreglo: decir «Combina movimiento y lectura» o corregir el reparto.

**14. «Nunca dos acentos en la misma escena» choca con las propias recetas.**
- Cita: `DIRECCION.md:211`; pero B4 combina `.minifocus` (relleno de acento) **y** `.pill.accent`
  «6 M · EL DÍA 1»; B1 suma callout de acento, `.play` de acento y el filo `.cbubble.hot`; B9 usa tres
  `.vmark` de acento.
- Por qué es un problema: la regla, leída literal, se incumple. (El contrato en realidad prohíbe «dos
  acentos **compitiendo**», es decir dos *colores* de acento: `03-contrato.md:41-42`.)
- Arreglo: precisar «un solo *color* de acento por escena, nunca dos compitiendo».

**15. Color no listado en la paleta: `#a9c65f`.**
- Cita: `DIRECCION.md:314` → `.minifocus { … border:5px solid #a9c65f; … }`, que no aparece en la tabla
  de tokens ni en el reparto por escena de `DIRECCION.md:52-78`, pese a que `DIRECCION.md:48` dice «No
  se introduce ningún token nuevo».
- Arreglo: documentar el color en la tabla o sustituirlo por un token del contrato.

**16. «Los comentarios de sus fans» omite a los famosos.**
- Cita: línea 2 (`SCRIPT.md:72`); `01-fuentes.md:16-17` → «respuestas de vídeo personalizadas a
  comentarios **de fans y de famosos**».
- Arreglo (cabe en 14): «En 2010, Old Spice respondió con vídeos a comentarios de fans y famosos.» (13 palabras).

**17. La tabla de jerga define términos que el guion no usa.**
- Cita: `SCRIPT.md:47` → «Campaña / caso | 2-4», pero ni «campaña» ni «caso» aparecen en las 11 líneas
  habladas (verificado con el regex del pipeline); y «Reproducciones | 4» se usa y se define en la misma
  línea 4.
- Arreglo: alinear la tabla con el texto hablado (o retirar las filas que no aplican).

**18. `STORYBOARD.md` no recoge la cautela «pendiente de confirmación del dueño».**
- Cita: `grep -rn "pendiente de confirmación"` solo aparece en `DIRECCION.md:279,413,432` y
  `DIRECCION-ARTE-BRIEF.md:106`; en `STORYBOARD.md` (que es quien monta B2 y lista `.brandmark` como
  elemento nuevo) no está.
- Arreglo: añadir la nota en B2 o en la tabla de Recursos de `STORYBOARD.md`.

---

## BLOQUE 2 — Confirmaciones

| # | Comprobación | Resultado real |
|---|---|---|
| 1 | Afirmaciones contra `01-fuentes.md` | **Parcial.** Soportadas: L2 (2010, vídeos a comentarios), L4 (186 y ~5,9 M el día 1), L5 (§3). No soportadas/matizables: L3 pierde el hedge de `01-fuentes.md:31` (defecto 2); L6 y L8 son absolutas/beneficios sin fuente (defectos 7 y 8). |
| 2 | Cifra «65 millones» | **OK, ausente.** Solo aparece en notas/vetos (`SCRIPT.md:11,35,63`; `BRIEF.md:44`; `01-fuentes.md:34,42`), nunca en las líneas habladas. |
| 3 | Promesas de resultados | **Casi.** No hay cifras-promesa; quedan dos formulaciones blandas (L6, L8) señaladas en defectos 7 y 8. |
| 4 | Líneas >14 palabras | **OK.** Máximo real = 14 (L3 y L7). Regex sobre las 11 líneas del `## Guion plano`: ninguna supera 14. |
| 5 | Un solo ejemplo | **OK.** Único ejemplo: la tienda de ropa (B7-B9). |
| 6 | Vetos de ejemplos | **OK.** Sin «cafetera», «instalación de luz», «agencias de diseño baratas», «zapatillas», 3 vs 118, Search Console, `G-XXXXXXXXXX` en guion/plan (solo en las listas de vetos). |
| 7 | Anglicismos | **OK en lo visible.** Cero anglicismos en las 11 líneas habladas ni en los rótulos (todos en español); los términos ingleses (`.clip`, `thread`, `kicker`) son solo CSS/producción. |
| 8 | Tratamiento de tú | **OK.** L1, L6, L7, L9, L10, L11. |
| 9 | CTA de guardar al cierre | **OK.** L11 «Guarda esto y…»; rótulo «Guarda esto» 96 px (B11). |
| 10 | Avisos de autoría/IA | **OK.** Ninguno en guion, rótulos ni plan. |
| 11 | Tabla == `## Guion plano` | **OK exacto.** Las 11 cadenas coinciden carácter a carácter y en el mismo orden (script de comparación). |
| 12 | Recuentos y suma | **OK.** Palabras reales = 12,13,14,13,10,9,14,12,9,8,10 = **124**; la suma declarada es 124. |
| 13 | Regex del pipeline | **OK.** `re.finditer(r"^    (\S.*)$", text, re.M)` devuelve **exactamente 11 líneas**, las del `## Guion plano`. |
| 14 | 124/3,5 y banda | **OK.** 124/3,5 = **35,43 s ≈ 35,4 s**, dentro de 30-40 s (`PROFILE.md:29`). Razonamiento: ver defecto 6 (la velocidad 3,5 no está conciliada con el contrato). |
| 15 | Vetos de continuidad (ejemplos, aperturas, recursos) | **OK.** Gancho por «el caso», no por error; sin SERP de V5 ni balanza de V6; sin vocabulario SEO/GA4. |
| 16 | Marca ajena (regla del perfil) | **OK con matiz.** `PROFILE.md:39` («logo de la marca… en línea sobre tarjeta clara») se reproduce en `02-continuidad.md:53`; el plan usa logotipo tipográfico sobre tarjeta clara, sin `@handle`/afiliación, y marca el pendiente en `DIRECCION-ARTE-BRIEF.md:106` y `DIRECCION.md:413,432`. `SCRIPT.md:57` y `:18` afirman «muestra su logo» sin el matiz (defecto 18/nota). |
| 17 | Fotograma 0 = miniatura | **Casi OK.** El escenario y la burbuja existen desde `t=0` con `rise()` sin opacidad; pero el callout entra a 0,10 s (defecto 11). |
| 18 | Un foco dominante por escena | **Declarado** en `DIRECCION.md:29-30,207`. No hay dos protagonistas evidentes en las recetas (juicio de diseño, no medible sin render). |
| 19 | Niveles de texto en bandas | **No cumple** (defecto 5). |
| 20 | Banda segura 15 %-75 % | **OK.** `.s-in { padding:300px 74px 480px }` (`DIRECCION.md:236-238`) → 300-1440 px de 1920 = 15,6 %-75 %. |
| 21 | Estado inicial en CSS + `fromTo`/`.to()` | **OK.** `STORYBOARD.md:16-17` (`.fade-in`) y recetas con `fromTo`/`.to()`; sin `.from()`. |
| 22 | Sin contadores / aleatoriedad | **Falla en el guion** (defecto 1): `SCRIPT.md:20` pide «contador que sube». El plan visual sí usa `setNum` (`STORYBOARD.md:84,92`); sin `Math.random`/`Date.now`. |
| 23 | Escenario visible desde `t=0` | **OK.** `STORYBOARD.md:12-13`; todas las escenas envuelven su marco y usan `rise()`. |
| 24 | Panel oscuro ≥ `#20202a` | **Casi OK.** Todos los paneles lo respetan salvo `.prompter` `#0e0e14` (defecto 9). |
| 25 | Acento solo como relleno con tinta encima | **Casi OK.** Callout/play/pill/vmark/lesstag.accent/minifocus usan relleno + `#0b0b10`; excepción de color `#a9c65f` en el borde del `.minifocus` (defecto 15). |
| 26 | Rojo solo para errores reales | **OK.** `warn` no se usa; el tachado del presupuesto va en tinta (`DIRECCION.md:210-212`, `STORYBOARD.md:119-120`). |
| 27 | `x:0` explícito en el barrido | **OK.** `DIRECCION.md:193-195` y `STORYBOARD.md:145`. |
| 28 | Coherencia entre los 3 documentos visuales (ids, recetas, transiciones, tiempos) | **Casi OK.** Las 11 salidas de `STORYBOARD.md` (`Salida:`) coinciden con el plan de cortes de `DIRECCION.md:174-185` en familia y duración (0,35-0,45 s), y con la tabla de transiciones de `STORYBOARD.md:55-65`. Fallos: «seis vs cinco familias» (defecto 4), ±4° vs ±2° (defecto 12), callout `t=0` (defecto 11). |
| 29 | Todo elemento nuevo trae su CSS completo | **OK.** Verificado con script: todas las clases marcadas «Nuevo» en `STORYBOARD.md:36-47` (`.phone`, `.cthread`, `.cmsg`, `.cbubble`, `.replyclip`, `.callout`, `.brandmark`, `.yearbadge`, `.chain`, `.station`, `.chainarrow`, `.sheet`, `.prompter`, `.clipgrid`, `.mini`, `.minifocus`, `.bignum`, `.statlab`, `.lesstag`, `.tripod`, `.sign`, `.strike`, `.store`, `.hanger`, `.chatbar`, `.fork`, `.destcard`, `.avatars`, `.qlist`, `.qrow`, `.vmark`, `.bubbles`, `.cmotif`, `.cover`, `.sweep`) tienen definición CSS con medidas/colores/posición en `DIRECCION.md:233-389`. |
| 30 | Ritmo: tabla ↔ 11 líneas y 3,5 pal./s | **OK** (con el redondeo del defecto 10). Cada duración = palabras/3,5 (14→4,00; 13→3,71; 12→3,43; 10→2,86; 9→2,57; 8→2,29); total 35,43. |
| 31 | Ningún beat con más animación que duración | **OK, con salvedad.** El último evento de cada beat (p. ej. B4 `put("#s4-plabel", at(4,2.70))`, B6 1,60, B10 1,00) cierra antes de la duración menor (B10 = 2,29 s). No se puede cerrar del todo sin el `dur` por defecto de `put()` (ver Bloque 3). |
| 32 | Transiciones coherentes con los cortes | **OK.** 7 `slide` + 3 acentos en las bisagras de cambio de tema; `cover` B2→B3, `circle` B3→B4, `sweep` B7→B8 (ver defecto 3 para el recuento de acentos). |

### Comandos usados (extracto)

```bash
# 1) regex del pipeline sobre SCRIPT.md (11 líneas, 124 palabras)
python3 -c 'import re;t=open("videos/mkt-01-responde-con-video/SCRIPT.md").read();
print(len(re.findall(r"^    (\S.*)$",t,re.M)))'

# 2) tabla vs guion plano (coincidencia exacta y suma)
#    (script de comparación: 11 filas, 0 discrepancias, suma 124)

# 3) vetos y cifras
grep -rniE "cafetera|instalaci.n de luz|balanza|SERP|65|warn|#ff5a5a" videos/mkt-01-responde-con-video/

# 4) cobertura CSS de los elementos nuevos (0 clases nuevas sin CSS)
#    (script que compara .clases referenciadas vs definidas en el bloque ```css)

# 5) velocidades declaradas
grep -rn "3,98\|3,5 palab" videos/ DESIGN.md
```

---

## BLOQUE 3 — Lo que no he podido verificar

1. **No existe `index.html` en la carpeta** (solo los 7 documentos). No se puede medir la luminancia
   real del fotograma 0 (los «≈ 230/255» de `DIRECCION.md:68` y `DIRECCION-ARTE-BRIEF.md:49` frente al
   umbral «≥ 200» de `DIRECCION-ARTE-BRIEF.md:121`), ni el % de filas con contenido, ni el contraste
   WCAG, ni los tramos vacíos en los cruces, ni comprobar en código la ausencia de `.from()`/contadores.
2. **Duración final.** El 35,4 s es una proyección (124/3,5); la fija `voice_pipeline.py`. No hay
   `voice-timing.json` ni render de mkt-01 para confirmarla.
3. **La velocidad 3,5.** No se puede medir directamente sin el timing real de V6; solo se infiere de
   `DECISIONS.md:45` (40,27 s / 142 palabras ≈ 3,53).
4. **`dur` por defecto de `put()`** no está documentado en estos ficheros, así que la comprobación 31
   («ninguna animación excede su beat») no es del todo concluyente, aunque los eventos de sonido sí caben.
5. **Dibujo real de los SVG** (percha, trípode, horquilla, tachado, onda del CTA, cámara, iconos de las
   etiquetas): solo se aporta el CSS del contenedor; los `<path>` no están especificados.
6. **Logotipo de marca.** El `.brandmark` (CSS en `DIRECCION.md:276-279`) es un logotipo tipográfico;
   no hay arte ni confirmación del dueño, así que no se puede validar su representación final.
