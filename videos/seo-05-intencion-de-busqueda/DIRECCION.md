# DIRECCIÓN DE ARTE — V5 «Intención de búsqueda»

Aplica el brief del dueño (`DIRECCION-ARTE-BRIEF.md`). Pieza: 12 beats · 188 palabras ·
~57-67 s · 1080×1920 · voz en off es-ES (`Pablo`) · subtítulos karaoke · barra de progreso.

## 1. Dirección elegida: «editorial de papel + demo de Google»

De los cinco recursos del brief se usan **cuatro** y se descarta uno, a propósito:

- **Diseño editorial** — palabras grandes, asimetría, aire, jerarquía por tamaño y color.
- **Profundidad 2,5D** — capas con sombra de contacto, escalas distintas, perspectiva ligera y
  desplazamiento relativo. Nada de 3D ni de giros que revelen caras nuevas.
- **Demostración de producto** — la ventana de Google y la página de resultados *son* el producto:
  pantalla, tarjetas, cursor, estados.
- **Animación tipográfica** — la palabra se revela, ramifica, se sustituye y llega a ser transición.
- **Collage fotográfico: descartado.** Es una decisión, no un olvido: no hay banco de imágenes ni
  generación, el dueño no ha aportado material y el brief prohíbe sustituirlo por un emoji o un
  dibujo improvisado. La fisicidad la asume el chrome de Google, que ya existe y es reconocible.
  Si algún día se quiere collage, hay que aportar los PNG con transparencia.

La complejidad sale de **coordinar** capas, no de acumular recursos. Un foco dominante por escena.

## 2. Paleta (dos variantes de la misma familia)

| token | oscuro | claro | uso |
|---|---|---|---|
| `bg` | `#0a0a0f` | `#f4f1ea` | lienzo |
| `panel` | `#17171e` | `#ffffff` | paneles, ventana, tarjetas |
| `line` | `#26262e` | `#e0dbcf` | bordes 2-5 px |
| `ink` | `#f5f5f7` | `#14141a` | texto principal |
| `muted` | `#8b8b99` | `#6f6f78` | rótulos y anotaciones |
| **`accent`** | `#c8ff3d` | `#c8ff3d` | **único acento**; siempre relleno, con `accent-ink` encima |
| `accent-ink` | `#0b0b10` | `#0b0b10` | tinta sobre el acento |
| `warn` | `#ff5a5a` | `#b3161b` | señal de error (funcional, no decorativa) |

**Cambios de variante en los momentos narrativos:** problema B1 → oscuro · explicación B2-B8 → claro ·
error B9-B10 → oscuro · solución B11 → claro · conclusión B12 → oscuro. Los cuatro cambios caen sobre
transiciones, nunca a mitad de escena.

**Fondos (dos tratamientos):** claro = papel con retícula de puntos a baja opacidad; oscuro =
degradado suave con halo de acento detrás del protagonista.

**Contrastes a vigilar:** el verde sobre claro (≈1,3:1) **prohibido** como texto o trazo; `muted` en
claro debe ser `#6f6f78`; en claro el aviso va en `#b3161b`; el relleno verde siempre lleva tinta
encima. Todo lo valida `check` (WCAG AA).

## 3. Tipografía

- **Inter** 400/600/700/800/900 + **JetBrains Mono** 600/800 para lo que se teclea (consulta, URL).
  Es el par que ya usa la serie.
- **Local, no de red.** El brief pide guardar las fuentes localmente: hay que vendorizar los `woff2`
  de Inter y JetBrains Mono en `assets/fonts/` con `@font-face`. Hoy la serie las carga de Google.
- **Reparto de tamaños del brief:** protagonista 110-180 (palabra, verbos, «una intención, una
  página»); frase principal 70-110 (rótulos grandes); contexto 38-56 (consulta, etiquetas de tipo,
  anotaciones). El kicker se queda en 32: es rótulo fijo del sistema.
- **La línea 7 (24 palabras) no se encoge: se redistribuye.** Tres cláusulas, tres tiempos dentro del
  mismo beat (guías→ENTENDER, comparativas→COMPARAR, producto→COMPRAR); el cuarto resultado se
  reserva para B8.
- Medir el texto **después de `document.fonts.ready`**, porque los trazos y máscaras dependen de la
  longitud medida.

## 4. Familias de composición (6)

1. **Titular roto** — palabra gigante con un objeto o sello que la contradice · B1, B9.
2. **Ficha de intención** — ventana central con la consulta y una tarjeta alrededor · B2.
3. **Palabra que ramifica** — palabra al centro y trazos SVG que la abren en dos destinos · B3-B5.
4. **La SERP como examen** — ventana + resultados con etiquetas que se construyen por pasos · B6-B8.
5. **La caída** — tarjeta única, resultados atenuados y cursor que se va · B10.
6. **Cuadrícula de reparto** — filas 1:1:1 palabra→intención→página→check, y cierre · B11-B12.

## 5. Profundidad y encuadre

- **Desplazamiento global con compensación por capas:** B7 (la lista baja ~120 px: fondo 0 ·
  resultados +60 · cursor y etiquetas +120) y B10 (la lista se arrastra mientras el cursor sube).
- **Aproximación suave 1 → 1,04** al completar la idea: B2, B5, B11.
- **Cambio de foco (acercamiento fuerte):** B1 (el aspa a escala 2,0), B7→B8 (el cuarto resultado),
  B8→B9 (el resultado cubre el cuadro).
- **El texto nunca rota y nunca pasa de 1,15×.** Las inclinaciones (±8°) son para tarjetas y objetos.
  Las formas grandes fuera de cuadro solo existen en los barridos, con contraste menor que el contenido.

## 6. Transiciones

Se usan **cinco** mecanismos (el brief sugiere tres para 30-45 s; la pieza es más larga):

| Mecanismo | Dónde | Nota técnica |
|---|---|---|
| **Desplazamiento continuo** | B1→B2, B4→B5 | Hoy el push mueve saliente y entrante en direcciones opuestas; el brief pide la misma dirección con solape: **tween nuevo** |
| **Continuidad por forma** | B2→B3, B3→B4, B6→B7, B7→B8 | Una forma termina coincidiendo con un elemento de la escena siguiente |
| **Barrido de color** | B5→B6, B10→B11 | Barra de acento a lo ancho (0,35-0,65 s); la escena nueva ya está debajo |
| **Objeto que cubre el encuadre** | B8→B9 | El cuarto resultado crece hasta tapar y sigue para despejar |
| **Revelado circular** | B9→B10 | `clip-path` circular desde el aspa; comprobar que el radio cubre las esquinas |
| **Corte directo** | B11→B12 | Sin cruce; la escena de llegada da el foco de inmediato |

Planificar las ventanas de visibilidad para que ninguna escena desaparezca antes de terminar la
transición. La capa que atraviesa el cambio va por encima (z-index 40).

## 7. Implementación

- **Contenedores separados** para no pisar transformaciones: `.slot` (posición y tamaño) → `.move`
  (movimiento principal) → `.sub` (movimiento secundario de 6-12 px o 1-2°) → `.mask` (recorte).
- **z-index:** 0 fondo · 1 retícula/halo · 2 gráficos de apoyo · 3 protagonista · 4 texto y
  anotaciones · 5 primer término · 25 barra de progreso · 30 karaoke · 40 capa de transición.
  (`data-track-index` no controla el orden de pintado: es solo carril del Studio.)
- **Capa de transición:** `.cover` y `.sweep` son DOM de la escena; el envoltorio `.s-in` se sigue
  animando solo con transform, opacidad o filtro. El revelado circular usa `clip-path` sobre `.s-in`.
- **Seek-safe:** estado inicial en CSS, animar con `fromTo`/`.to()`, sin `.from()`, sin contar hacia
  arriba (la posición baja en saltos discretos), sin `Math.random` (los efectos ya usan semilla fija).
- **Karaoke y progreso se mantienen tal cual.** La píldora ya contrasta sobre claro (fondo oscuro
  propio) y la barra usa pista opaca `#1e1e26` con relleno verde.
- **Orden de la cadena tras tocar escenas o línea de tiempo:** `retime.py` → `transiciones.py` →
  `check` → render.

## 8. Ritmo y sonido

Se alterna movimiento con lectura estable: B1 mov · B2 lec · B3 mov · B4 lec · B5 mov · B6 lec ·
B7 mov · B8 mov · B9 mov · B10 mov · B11 lec · B12 lec. Un efecto por aparición, nunca por palabra.
El detalle por beat está en `STORYBOARD.md`.

## 9. Riesgos y mitigación

1. **Verde ilegible sobre claro** → acento solo como relleno con tinta encima; validar con `check`.
2. **B7 se desborda** (24 palabras + 4 resultados + verbos) → repartir en tres tiempos, medir con
   `check`; si aprieta, dejar tres resultados y pasar el mapa a B8.
3. **Cruces negros** si se retima y no se re-aplican las colas → cadena en orden y
   `verificar_montaje.py` (tramo sin contenido ≤ 0,15 s).
4. **Fuentes de red** → vendorizar en `assets/fonts/`; medir tras `document.fonts.ready`.

## 10. Decisiones abiertas para el dueño

1. **Logos de marca:** el perfil antiguo del proyecto los prohíbe, pero su criterio nuevo (y el brief,
   que pide colores de marca) los admite. En esta pieza: logo de Google en tres escenas y chrome real
   de Google como elemento gráfico. ¿Se actualiza el perfil?
2. **Collage:** descartado por falta de material. Si quiere collage, hay que aportar los PNG.
3. **Paleta de marca:** no hay ninguna documentada, así que se mantiene carbón + blanco roto + verde
   ácido y se deriva la variante clara. Si existe una paleta oficial, se cambia.
4. **Sobrepaso:** el brief admite `back.out` moderado; la doctrina previa lo desaconsejaba. Propuesta:
   sobrepaso solo en objetos, texto siempre con `power3.out`.
