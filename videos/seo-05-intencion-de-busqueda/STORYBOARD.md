# STORYBOARD — V5 «Intención de búsqueda»

**Guion v2: 13 beats.** El mapa de escenas y los tiempos se recalculan cuando se grabe la voz
(`retime.py`). Cambios previstos: la SERP se reparte en dos escenas (la regla y la lectura de los
cuatro tipos, cada uno con lo que quiere la persona), el error se separa de la consecuencia, y la
escena de la consecuencia muestra el gesto concreto (el cursor cierra la pestaña y baja al
siguiente resultado).

10 escenas · 1080×1920 · Kinetic Type + Swiss Grid · subtítulos karaoke + barra de progreso.
Duración total provisional **≈ 40 s**. Los tiempos reales salen de la voz con `retime.py`;
el eje propuesto es `S = [0 · 4.0 · 8.0 · 11.7 · 15.7 · 19.7 · 24.0 · 28.0 · 32.7 · 37.0]`,
calculado a 3,0 palabras/s sobre las 123 palabras del guion (ninguna escena baja de 2,8 ni sube de 3,1
palabras/s; la duración real la fija la voz con `retime.py`).

**Regla de masa clara:** el escenario (`.pg` a `#26262e`, o `.card` a `#20202a`, o el cuerpo
claro `.serpbody` `#eef1f5`) está presente **desde t=0** y solo se asienta con `rise()`.
El acento verde va como relleno con tinta oscura encima, o como texto solo sobre fondo oscuro.

**Mapa de transiciones** (animan `#sN-in`, nunca el clip; la cola de la escena saliente se
extiende con `transiciones.py`):

| Corte | Tipo | Dur. | Por qué |
|---|---|---|---|
| F1→F2 | push ↑ | 0,45 | paso primario: la definición |
| F2→F3 | push ↑ | 0,40 | definición → la palabra no cambia (mantiene el push como transición primaria) |
| F3→F4 | push ↑ | 0,40 | punto nuevo: primer ejemplo |
| F4→F5 | push ↑ | 0,35 | encadena ejemplos |
| F5→F6 | push ↑ | 0,35 | encadena ejemplos |
| F6→F7 | **zoom-through** | 0,50 | clímax: el truco, la SERP |
| F7→F8 | blur-crossfade | 0,50 | contención: el error |
| F8→F9 | push ↓ | 0,30 | la caída → el arreglo (corte corto) |
| F9→F10 | crossfade | 0,50 | outro |

---

## F1 · Hook · 4,3 s
**Ids:** cada elemento animado lleva un id único con el prefijo de su escena (`#sN-<elemento>`:
`#s1-x`, `#s4-w1`, `#s7-cursor`…), de modo que no se repiten entre escenas.

**Elementos:** `.pg` oscuro · `.kicker` con `.tile.sm` (**logo Google**) · `.chip.big` con la
lupa y la palabra **cafetera** · tres `.tile.stroke` **sin rótulo** (serán guía, comparativa y ficha: se etiquetan desde F4) · `.tile.stroke`
de una sola página · `.xover` (aspa roja grande) encima.
**Animación:** `rise(#s1-pg)` → kicker → chip (escala 0,82) → los tres iconos **escalonados**
(1,00 / 1,25 / 1,50 s, suben 44 px) → la página única (escala 0,72) → **aspa a escala 2,0** con
golpe de sonido.
**Texto mínimo:** kicker «LA PALABRA» + «cafetera» (el término «intención de búsqueda» no se rotula
hasta F2, y las etiquetas de tipo no aparecen hasta F4: la jerga se define antes de usarla).

## F2 · Definir la intención · 3,8 s
**Elementos:** `.pg` · `.kicker` «LA INTENCIÓN» · `.tile.lg.stroke` persona+lupa → `.wire.on`
→ `.tile.lg.stroke` diana · `.pill.ok` «QUIERE CONSEGUIR».
**Animación:** `rise` → kicker → cabeza (0,72) → **trazo que se dibuja** (0,95 s) → diana →
pastilla, con un «ding».
**Texto mínimo:** kicker + «QUIERE CONSEGUIR».

## F3 · La palabra no cambia · 3,4 s
**Elementos:** `.pg` · `.kicker` «LA PALABRA NO CAMBIA» · `.chip.accent` **cafetera** fija ·
dos `.wire.on` que salen de ella · dos `.tile.stroke` (escobilla → limpiar; carrito → comprar).
**Animación:** `rise` → kicker → chip → los dos **trazos dibujados** (0,70 y 1,05 s) → los dos
iconos entran desde la izquierda (-40 px).
**Texto mínimo:** «cafetera» + «limpiar» / «comprar».

## F4 · Ejemplo cafetera · 4,6 s
**Elementos:** `.pg` · kicker «EJEMPLO» con logo Google · `.chip` «cafetera» · dos filas `.node`:
(icono → trazo → `.tile.lg` guía) y (icono → trazo → `.tile.lg` ficha) · dos `.pill.ok`.
**Animación:** `rise` → kicker → chip → fila 1 (icono 0,50 · trazo 0,80 · guía 1,00 con escala 0,7)
→ fila 2 (icono 1,70 · trazo 2,00 · ficha 2,20) → pastillas.
**Texto mínimo:** «cafetera» + «guía» / «ficha».

## F5 · Ejemplo alojamiento web · 3,4 s
**Elementos:** `.pg` · kicker «EJEMPLO» · `.chip` «alojamiento web» · una tarjeta de
**comparativa** con tres filas y sus barras · `.pill.ok` «comparativa».
**Animación:** `rise` → kicker → chip (escala 0,8) → la tarjeta sube 40 px → **las tres barras
se llenan** (0,82 / 0,55 / 0,30 a 1,05, 1,25 y 1,45 s) → pastilla.
**Texto mínimo:** «alojamiento web» + «comparativa».

## F6 · Ejemplo seguro de coche · 4,6 s
**Elementos:** `.pg` · kicker «EJEMPLO» · `.chip` «seguro de coche» · dos filas: (escudo →
trazo → guía) y (calculadora → trazo → **mini-formulario** del simulador con su barra).
**Animación:** `rise` → kicker → chip → fila 1 (0,50 / 0,80 / 1,00) → fila 2 (1,80 / 2,10 / 2,30)
→ la **barra del simulador** se llena (2,70 s).
**Texto mínimo:** «seguro de coche» + «guía» / «simulador».

## F7 · El truco: la SERP · 4,8 s  ← clímax
**Elementos:** `.browser` con barra de direcciones y candado (escenario, desde t=0) · kicker con
**logo Google** · `.chip` con la consulta · `.serpbody` con **cuatro resultados**, cada uno con su
favicon y su **etiqueta de tipo**: GUÍA · COMPARATIVA · FICHA · **MAPA** (el cuarto con
mini-mapa y pin) · un `.cursor` que baja por los resultados.
**Animación:** `rise` al navegador → kicker → chip de la consulta → los resultados **escalonados**
(0,75 / 1,25 / 1,75 s, suben 36 px) con su etiqueta +0,20 s → el resultado con mapa (2,30) →
el **cursor recorre** la lista en 1,4 s.
**Texto mínimo:** la consulta + las cuatro etiquetas (es el único fotograma con varias palabras:
es el mapa mental de la intención).

## F8 · El error · 4,6 s
**Elementos:** `.pg` oscuro · kicker «EL ERROR» con punto rojo · `.tile.lg` de una sola página ·
tres `.tile.sm` (intenciones) amontonadas encima · `.xover` roja · `.serpbody` claro con el
resultado propio atenuado y una flecha de caída · `.cursor` que sube de vuelta a la barra.
**Animación:** `rise` → kicker → la página (0,70) → los tres iconos **amontonados** (0,60/0,75/0,90)
→ el **aspa** a escala 2,0 → la SERP clara entra (2,05) → el resultado propio se **atenúa**
(opacidad 0,45) → **flecha de caída** (escala 1,4) → el cursor **vuelve arriba** en 1,1 s.
**Texto mínimo:** «EL ERROR» + la posición, si acaso.

## F9 · El arreglo · 3,8 s
**Elementos:** `.pg` · kicker «EL ARREGLO» · tres filas **1:1:1**: `.chip` (palabra) →
`.tile.sm` (intención) → `.tile.stroke` (página) → `.badge-ok` (check verde).
**Animación:** fila 1 a 0,30 / 0,50 / 0,70 con el check a 0,95 (escala 0,4, «ding»); fila 2 +0,55;
fila 3 +1,10.
**Texto mínimo:** la palabra una vez + tres checks.

## F10 · CTA · 2,6 s
**Elementos:** `.pg` visible desde t=0 (escenario) · `.cta-mark` (marcador) · `.cta-label` «Guarda esto» · `.tile.sm` con el logo Google.
**Animación:** `rise(#s10-pg)` → marcador (escala 0,5) → etiqueta (0,85) → logo (0,6).
**Texto mínimo:** «Guarda esto».

---

## Assets

**Logos (SVG en línea, sobre `.tile` claro):** Google «G» (los `<path>` ya incrustados en
`videos/ga4-01-instalar-sin-duplicar/index.html`) · Google Search Console y Google Maps
(`simple-icons`, para la SERP y el resultado con mapa). Reutilizables ya: lupa, documento,
carrito, barras, check, aspa, cursor, marcador, candado.

**Iconos propios nuevos (trazo, `currentColor`):** escobilla (limpiar), diana (intención),
escudo (qué cubre), calculadora (simulador), pin (mapa).

## Los cinco momentos que hacen recordar el vídeo

1. **F1** — el **aspa roja** cae sobre la única página: la tesis en una imagen.
2. **F4/F6** — el **trazo que se dibuja** desde la palabra y se abre en dos páginas distintas.
3. **F7** — la **SERP completa con los cuatro tipos etiquetados** y el cursor bajando: el fotograma
   capturable y el corazón del truco.
4. **F8** — la página amontonada se cruza, el resultado propio se apaga y el **cursor vuelve solo
   a Google**: el castigo visual del error.
5. **F9** — la **cuadrícula verde 1:1:1** con los tres «ding» antes del CTA.

## Riesgos a vigilar en el montaje

- **F6:** el chip «seguro de coche» (14 caracteres) se sale a tamaño grande: bajarlo a chip normal
  o partirlo en dos líneas.
- **F7:** cuatro resultados + cuatro etiquetas + mapa compiten en altura con kicker y barra:
  medir con `check` y, si aprieta, dejar tres resultados + mapa.
- **F4/F6:** dos filas con tarjeta `.lg` de 260 px + chip + kicker queda justo: bajar a 200 px.
- **Contraste:** el verde de acento sobre claro no pasa AA; usarlo como relleno con tinta oscura.
  Revisar también el rojo de las etiquetas sobre la SERP clara.
- **Masa clara escasa:** F2, F3, F9 y F10 son las más desnudas; el panel oscuro y las tarjetas
  claras deben estar desde el primer fotograma para no dejar tramos vacíos en los cruces.
- **Orden obligatorio de herramientas** después de tocar escenas o la línea de tiempo:
  `retime.py` → `transiciones.py` → `check` → render. Si se reconstruyen las escenas y se salta
  `transiciones.py`, se pierden las colas de transición y los cruces salen negros.
