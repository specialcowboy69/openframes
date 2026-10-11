# Brief de dirección de arte (especificación del dueño, 2026-10-11)

> Nota de trabajo: el dueño indica **ignorar las menciones a 30 s** que aparecen en el texto
> original. El guion de V5 son 12 líneas, ~57-67 s según la voz.

## 1. Resultado visual

Combinación buscada:

- **Diseño editorial:** palabras grandes, jerarquía clara, composiciones asimétricas, espacio vacío.
- **Collage:** fotografías recortadas, manos, objetos y figuras aisladas que representan conceptos.
- **Profundidad 2,5D:** capas con sombras, diferencias de escala, perspectiva moderada, movimiento relativo.
- **Demostración de producto:** pantallas, tarjetas, cursores, gráficos y estados de una interfaz.
- **Animación tipográfica:** palabras que se revelan, se sustituyen, se agrandan o se convierten en
  parte de una transición.

La complejidad debe salir de la **coordinación** entre elementos. Un foco visual dominante en cada
momento. Una dirección coherente para toda la pieza: **no acumular todos los recursos en cada escena**.

## 2. Sistema gráfico

**Paleta.** Colores de marca si existen; si no, blanco roto + negro carbón + **un único acento
saturado**. Preparar **variante clara y oscura** y cambiar entre ellas en momentos narrativos:
problema, explicación, solución, conclusión.

**Tipografía.** Sans serif con pesos contrastados y, si aporta, una cursiva. Para 1080 × 1920:

- palabra protagonista: **110-180 px**
- frase principal: **70-110 px**
- contexto secundario: **38-56 px**

Ajustar a la longitud del texto y comprobar la lectura en móvil. **No reducir todo el texto para
encajar una frase larga: redistribuir su aparición en el tiempo.**

**Fondos.** Elegir uno o dos tratamientos:

- claro con textura fina de papel;
- oscuro con iluminación suave por degradados;
- retícula de líneas o puntos de baja opacidad;
- halo de color detrás del elemento protagonista.

Grandes formas parcialmente fuera de cuadro solo si equilibran; su contraste debe ser inferior al
del contenido.

## 3. Arquitectura de las escenas

Cada escena es una pequeña acción visual: **(A) aparece la idea → (B) un objeto o sistema la
representa → (C) ocurre una transformación que explica algo → (D) esa transformación prepara el
plano siguiente.**

Capas, en el orden necesario: fondo · textura o retícula · gráficos de apoyo · elemento protagonista ·
texto principal y anotaciones · primer término o transición.

Contenedores separados para: posición y tamaño · movimiento principal · movimiento secundario ·
máscaras y recortes. Así se puede desplazar un objeto mientras una capa interior flota o gira sin que
dos animaciones sobrescriban la misma transformación.

Composiciones variadas: texto dominante con objeto superpuesto · objeto grande con frase breve al
lado · pantalla central con componentes alrededor · palabras que ocupan casi todo el encuadre ·
comparación o transformación de un estado a otro · diagrama que se construye progresivamente.

## 4. Preparación de elementos gráficos

- **HTML/CSS:** tarjetas, etiquetas, botones, contenedores, barras, interfaces, bloques de texto.
- **SVG:** líneas, flechas, diagramas, círculos, máscaras, iconos, gráficos precisos.
- **PNG/WebP con transparencia:** manos, personas recortadas, esculturas, objetos fotográficos.
- **Secuencia renderizada, vídeo con transparencia o 3D:** objetos que deben mostrar varias caras.

Antes de animar: bordes limpios, transparencia correcta, resolución suficiente para el mayor
acercamiento, iluminación y color compatibles, elementos separados cuando deban moverse
independientemente, y **texto importante en HTML/SVG separado de las imágenes**.

Cuando el acabado dependa de un objeto realista, **conseguir o generar ese recurso con las
herramientas disponibles; no sustituirlo silenciosamente por un emoji o un dibujo improvisado.**
Una imagen plana puede trasladarse, escalarse e inclinarse; para un giro que revele otras caras hace
falta un recurso con esa información.

## 5. Recetas de animación (puntos de partida)

**A. Revelado tipográfico.** Palabras como spans dentro de contenedores con `overflow:hidden`, con
margen para tildes y descendentes. `yPercent: 110 → 0`, `opacity: 0 → 1`, duración 0,35-0,55 s,
desfase 0,04-0,08 s, `power3.out`. Entradas por palabra o por bloque; letra a letra solo para
énfasis breves.

**B. Énfasis sobre una palabra.** Cambio de peso, tamaño o color, más rectángulo de acento detrás con
`scaleX: 0 → 1` y `transform-origin:left`. Medir el texto tras cargar la fuente. Énfasis puntual:
`scale 1 → 1,06 → 1` en 0,25-0,40 s. Mantener quietas las palabras de contexto.

**C. Entrada de un objeto con peso.** Contenedor de movimiento alrededor del recurso: `y: 160 → 0`,
`scale: 0,88 → 1`, `rotation: -7° → 0°`, `opacity: 0 → 1`, 0,55-0,85 s, `power3.out` o `back.out`
con sobrepaso moderado. Sombra en capa separada (tamaño, desenfoque y opacidad según la proximidad
aparente). Después, movimiento secundario pequeño si encaja (6-12 px o 1-2°), con duración finita y
sin moverlo todo a la vez.

**D. Tarjetas que se ordenan.** Estado inicial disperso (posiciones distintas, rotaciones ~±8°,
escalas y sombras ligeramente distintas) → composición ordenada (convergen, corrigen rotación, se
alinean o encajan en una interfaz, una gana tamaño y las secundarias ceden). Posiciones inicial y
final explícitas con GSAP y desfase 0,08-0,15 s entre tarjetas. La transformación debe expresar una
idea: organización, selección, comparación o simplificación.

**E. Interfaz que se construye.** Separar marco, pantalla, tarjetas, gráficos, etiquetas y cursor.
Secuencia posible: entra el marco con escala e inclinación ligera → aparecen los componentes →
el cursor se desplaza al control relevante → el clic produce respuesta visible → se amplía el
resultado o sale una tarjeta. Animar el contenido dentro de una máscara que respete los bordes del
dispositivo. Con capturas reales, conservar textos y proporciones y usar recortes ampliados para
detalles ilegibles a pantalla completa.

**F. Gráficos y recorridos.** Líneas SVG: calcular longitud, `stroke-dasharray`/`stroke-dashoffset`,
y añadir puntos y etiquetas cuando el trazado los alcanza. Barras: `scaleY` con origen en la base,
valores cerca del final del movimiento. Procesos: un punto recorre una conexión, el nodo de destino
responde, aparece el resultado y el siguiente recorrido parte de ese estado. **Solo datos
proporcionados o ejemplos identificados como ilustrativos.**

**G. Lupa o revelado de claridad.** Lupa con recurso transparente o piezas SVG; detrás, palabra o
dato atenuado; una máscara circular vinculada a la posición de la lente revela una segunda capa
nítida. Ambas capas en el mismo sistema de coordenadas. El movimiento de la lupa debe descubrir
información relevante; **si no se puede mantener la alineación, no añadir la ampliación óptica**.

## 6. Profundidad y movimiento de encuadre

Profundidad con superposición, sombras de contacto, escalas diferentes, perspectiva ligera y
desplazamiento relativo entre capas. Para un desplazamiento global, mover el contenedor de escena y
compensar: fondo poco, contenido intermedio, primer término más. Aproximación suave de escala
1 → 1,04 mientras se completa una idea; los acercamientos intensos, para cambiar de foco. Texto
importante en plano legible; las inclinaciones fuertes, mejor en objetos y tarjetas secundarias.

## 7. Transiciones con construcción definida

Elegir la que mejor conecte cada pareja de escenas:

- **Objeto que cubre el encuadre:** un protagonista crece o atraviesa hasta tapar; revela la
  siguiente escena cuando la cobertura es completa y sigue el movimiento para despejarla.
- **Continuidad por forma:** una forma termina en posición y tamaño que coinciden con un elemento de
  la escena siguiente.
- **Barrido de color:** una forma grande de la paleta cruza el encuadre; la escena nueva ya está
  preparada debajo. 0,35-0,65 s.
- **Revelado circular:** `clip-path` circular desde el punto de interés hasta cubrir el cuadro;
  comprobar que el radio final cubre las esquinas.
- **Desplazamiento continuo:** saliente y entrante se mueven en la misma dirección con tiempos
  parcialmente solapados; aceleración al salir, desaceleración al llegar.
- **Corte directo:** para cambios contundentes; la composición de llegada debe dar el nuevo foco de
  inmediato.

Planificar las ventanas de visibilidad para que las escenas no desaparezcan antes de terminar la
transición. Reservar una capa superior para los elementos que atraviesen el cambio.

## 8. Ritmo y sonido

Dividir el guion **por ideas**, no por frases de longitud uniforme. Orientación: entrada 0,3-0,7 s ·
desarrollo o transformación 0,8-2 s · lectura del resultado, lo que pida el texto · transición
0,2-0,6 s. Pueden solaparse; la duración real la manda la locución. Alternar escenas de mucho
movimiento con escenas de lectura estable.

Con voz: usar el guion aprobado **literalmente**, alinear palabras importantes y transformaciones con
sus tiempos reales y verificar el audio antes del render. Con música y efectos: voz inteligible,
efectos en acciones concretas (clic, impacto, encaje, desplazamiento, aparición) y una familia
sonora pequeña y coherente.

## 9. Implementación en HyperFrames

Consultar el contrato de la versión instalada antes de escribir la composición. Definir dimensiones y
duración finita. Declarar los tiempos de los clips con los atributos compatibles. Crear las timelines
con `gsap.timeline({ paused: true })` y registrarlas en `window.__timelines` con el
`data-composition-id` correspondiente. Posiciones temporales explícitas y estados inicial y final
claros. Separar el tiempo global del local de las subcomposiciones. Dejar que HyperFrames gestione
reproducción y visibilidad de clips; controlar el orden visual con `z-index`. Usar wrappers para
animar medios y combinar transformaciones. Mantener todas las animaciones vinculadas al tiempo de
render. **Precalcular cualquier variación aleatoria con semilla fija.** Comprobar los efectos al
saltar a un instante y al retroceder. Guardar imágenes, fuentes y audio localmente cuando se pueda y
cargar las fuentes antes de medir texto o construir máscaras dependientes de su tamaño.

## 10. Producción y revisión

Preparar primero: dirección gráfica de la pieza · desglose temporal de escenas · lista de recursos ·
estado inicial, transformación y estado final de cada escena · transiciones previstas. Después,
implementar y renderizar.

En piezas de 30-45 s, orientación de **cuatro familias de composición y tres mecanismos de
transición**; ajustar la variedad al guion. Revisar: un fotograma de lectura de cada escena · los
instantes intermedios de las transiciones · entradas, salidas y superposiciones · legibilidad a
tamaño móvil · alineación de texto e interfaces · sincronía con la voz · el MP4 completo en
movimiento.

## Notas de compatibilidad con el proyecto (a decidir)

1. **Collage fotográfico:** hace falta material con transparencia (manos, objetos, personas). En este
   entorno no hay generación ni banco de imágenes, y no puedo ver imágenes para validarlas. Si el
   dueño no aporta esos recursos, la dirección coherente es SVG/HTML/tipografía, sin collage.
2. **Sobrepaso:** el brief admite `back.out` moderado en objetos; la doctrina previa del proyecto
   desaconsejaba rebotes. Propuesta: sobrepaso solo en objetos, texto siempre `power3.out`.
3. **Fuentes:** el brief pide sans con pesos contrastados y cursiva opcional. Hay que confirmar qué
   familia se puede empaquetar localmente para el render.
4. **Paleta:** si no hay colores de marca documentados, se mantiene carbón + blanco roto + un único
   acento (el verde actual) y se deriva la variante clara.
