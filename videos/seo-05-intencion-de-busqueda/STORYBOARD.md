# STORYBOARD — V5 «Intención de búsqueda»

**Sustituye al plan anterior**: la dirección de arte está en `DIRECCION.md` y el brief original en
`DIRECCION-ARTE-BRIEF.md`. 12 beats · 188 palabras · ~57-67 s.
**Todos los tiempos son RELATIVOS al inicio de su beat**: los absolutos los fija la voz con `retime.py`.
Las letras A-G remiten a las recetas de animación del brief (§5).

Regla en las 12 escenas: el escenario (fondo + ventana o panel) está visible desde el fotograma 0 y
**solo se asienta** (`rise()`); nace en opacidad 0 solo el contenido. Sin `.from()`, sin contar hacia
arriba, sin `Math.random`.

| # | Idea · objeto · transformación · prepara | Familia | Receta (rel) | Estado inicial → final | Salida |
|---|---|---|---|---|---|
| **B1** | Tu página no responde → desapareces. Página + tres tarjetas de intención + número de posición + aspa. La posición baja 3→12→fuera y el aspa cae. Prepara: una página para varias cosas. | Titular roto | C: página y160→0, rot −7→0, 0,55 power3.out · el aspa escala 0→2,0 en 0,35 · la posición baja en dos saltos | Panel oscuro visible; página pequeña y rotada; aspa oculta → página centrada y cruzada | Desplazamiento continuo (push ↑ 0,45) |
| **B2** | La intención es lo que se quiere conseguir. Ventana + consulta + diana. Se dibuja el trazo consulta→diana. Prepara: la palabra no basta. | Ficha de intención | E: marco y consulta 0,1-0,4 · F: trazo dibujado 0,6-1,3 · B: pastilla «QUIERE CONSEGUIR» 1,4 | Papel claro y ventana visibles; diana oculta; trazo sin dibujar → consulta conectada con la diana | Continuidad por forma (el chip viaja y crece) |
| **B3** | Misma palabra, búsquedas distintas. «cafetera» a 150 px + trazo en V + dos chips. La palabra se abre en dos ramas. Prepara: el ejemplo. | Palabra que ramifica | A: palabra por bloque (yPercent 110→0, 0,4) · F: dos trazos 0,7 y 1,05 · C: chips desde x −40, desfase 0,12 | Papel claro; palabra centrada; trazos sin dibujar → dos ramas abiertas | Continuidad por forma (la palabra ya es el chip) |
| **B4** | «cómo limpiar una cafetera» frente a «comprar una cafetera». Dos consultas completas y su resultado. Cada consulta se escribe y produce su resultado. Prepara: qué quiere cada persona. | Palabra que ramifica | A: dos líneas por palabra (desfase 0,05) · E: dos filas escalonadas 0,10 · F: barras de esqueleto | Papel claro; consulta 1 y su resultado; la segunda oculta → dos parejas completas | Desplazamiento continuo (push ↑ 0,35) |
| **B5** | En una se aprende, en la otra se compra. Dos columnas + libro y carrito + «APRENDER»/«COMPRAR». Las tarjetas se ordenan y los verbos se enfatizan. Prepara: mirar la página de resultados. | Palabra que ramifica | D: dos tarjetas de ±8° → alineadas, desfase 0,12 · B: énfasis de cada verbo 1→1,06→1 | Papel claro; columnas dispersas; verbos ocultos → columnas ordenadas | Barrido de color (0,45) |
| **B6** | Mira los resultados antes de escribir. Ventana + resultados en esqueleto + cursor. El cursor baja y aparece «antes de escribir». Prepara: leer la SERP. | La SERP como examen | E: marco y esqueletos escalonados 0,10 · el cursor baja 0,9-1,9 · B: nota | Ventana clara visible; esqueletos presentes → lista recorrida y nota | Continuidad por forma (misma ventana) |
| **B7** | Guías→entender · comparativas→comparar · producto→comprar. Cuatro resultados con etiqueta y verbos grandes. Tres tiempos, cada uno etiqueta un resultado. Prepara: el caso mezclado. | La SERP como examen | E+B: t1 0,2 (etiqueta + «ENTENDER») · t2 1,1 («COMPARAR») · t3 2,0 («COMPRAR»), pop +0,12 | Ventana clara; cuatro esqueletos → tres etiquetados con su verbo; el cuarto reservado | Continuidad por forma (zoom al cuarto resultado) |
| **B8** | Una palabra puede tener más de una intención. El cuarto resultado a pantalla + tres etiquetas confluyendo + pastilla «MÁS DE UNA INTENCIÓN». Prepara: el error. | La SERP como examen | D: etiquetas convergen, desfase 0,10 · B: pastilla | Papel claro; resultado y etiquetas presentes; pastilla oculta | Objeto que cubre (el resultado crece y tapa) |
| **B9** | Una sola página para todo. Página única + tres intenciones amontonadas + aspa roja. Se amontonan y el aspa cruza. Prepara: la consecuencia. | Titular roto | D: amontonar 0,60/0,75/0,90 · C: aspa 0→2,0 en 0,35 | Panel oscuro visible; página y aspa pequeñas → página cruzada | Revelado circular (clip-path desde el aspa) |
| **B10** | No encuentra → cierra y prueba el siguiente. Resultados claros con el propio atenuado, posición y cursor. El propio se apaga, la posición cae y el cursor vuelve a la barra. Prepara: el arreglo. | La caída | E: el cursor sube (1,1) · atenuado a 0,45 · F: flecha de caída | Resultados visibles; el propio ya atenuado; cursor abajo → cursor en la barra | Barrido de color (0,40) |
| **B11** | Una intención, una página. Cuadrícula 1:1:1 palabra→intención→página→check. Se completan tres filas. Prepara: el CTA. | Cuadrícula de reparto | D: filas 0,30/0,50/0,70, desfase 0,55 · B: checks con `ding` (0,4→1) | Papel claro; fila 1 presente → cuadrícula completa en verde | Corte directo |
| **B12** | Guarda esto antes de escribir. Marcador + «Guarda esto» + logo de Google. Prepara: cierre. | Cuadrícula de reparto | C: marcador 0,05 · A: etiqueta 0,6 · E: logo 1,4 | Panel oscuro visible; contenido oculto → CTA montado | — (fin) |

## Recursos

| Recurso | Tipo | Origen |
|---|---|---|
| Paneles, tarjetas, tiles, chips, pastillas, nodes, trazos, sellos, aspa, badge, CTA, barra de progreso, kicker, cursor, ventana de Google, página de resultados, scroll, resultado propio | HTML/CSS | Reutilizado del vídeo de referencia |
| Logo de Google (cuatro trazos), Google Maps, Search Console | SVG en línea | Reutilizado |
| Iconos lupa, documento, carrito, barras, check, aspa, marcador, candado, flecha | SVG | Reutilizado |
| Escobilla, diana, libro, tabla de comparativa, pin de mapa, flecha de posición | SVG nuevo | Nuevo |
| Tarjeta de intención, etiqueta de tipo (GUÍA / COMPARATIVA / PRODUCTO / MAPA), chip de consulta mono, verbo grande, rama en V, cuadrícula de reparto, número de posición, barrido, cobertor | HTML/CSS/SVG | Nuevo |
| Máscara del revelado circular | `clip-path` | Nuevo |
| Collage (manos, objetos) | PNG con transparencia | **Descartado**: no hay material |
| Render, vídeo con alfa o 3D | — | No se necesita |

## Ritmo y sonido por beat

| # | Movimiento o lectura | Entrada | Desarrollo | Lectura | Transición | Efectos (rel) |
|---|---|---|---|---|---|---|
| B1 | Movimiento | 0,0-0,6 | 0,6-1,6 | 1,6-2,2 | 0,45 | whoosh 0,0 · tick 0,5 y 1,0 · thud 1,6 |
| B2 | Lectura | 0,0-0,4 | 0,4-1,4 | 1,4-fin | 0,40 | pop 0,1 y 0,6 · ding 1,4 |
| B3 | Movimiento | 0,0-0,4 | 0,4-1,4 | 1,4-2,0 | 0,40 | pop 0,1 · swoosh 0,7 y 1,05 |
| B4 | Lectura | 0,0-0,5 | 0,5-2,0 | 2,0-fin | 0,35 | tick 0,5 y 1,2 · pop 1,0 |
| B5 | Movimiento | 0,0-0,5 | 0,5-1,8 | 1,8-2,4 | 0,45 | pop 0,2 · ding 0,9 y 1,5 |
| B6 | Lectura | 0,0-0,6 | 0,6-1,9 | 1,9-fin | 0,50 | whoosh 0,0 · tick 0,9 |
| B7 | Movimiento (clímax) | 0,0-0,4 | 0,4-2,8 | 2,8-fin | 0,50 | tick y ding en 0,2/1,1/2,0 |
| B8 | Movimiento | 0,0-0,4 | 0,4-1,6 | 1,6-fin | 0,45 | pop 0,3 · buzz 1,4 |
| B9 | Movimiento | 0,0-0,5 | 0,5-1,5 | 1,5-2,0 | 0,45 | thud 0,6 · buzz 1,5 |
| B10 | Movimiento | 0,0-0,5 | 0,5-2,0 | 2,0-fin | 0,40 | swoosh 0,6 · click 1,7 |
| B11 | Lectura | 0,0-0,4 | 0,4-1,8 | 1,8-fin | corte | ding 0,95 / 1,5 / 2,05 |
| B12 | Lectura | 0,0-0,5 | 0,5-1,2 | 1,2-fin | — | pop 0,05 · ding 1,3 |

## Revisión antes de dar por bueno el vídeo (brief §10)

Un fotograma de lectura de cada escena · los instantes intermedios de las cinco transiciones ·
entradas, salidas y superposiciones · legibilidad a tamaño móvil · alineación de texto e interfaces ·
sincronía con la voz · y el MP4 completo en movimiento.
