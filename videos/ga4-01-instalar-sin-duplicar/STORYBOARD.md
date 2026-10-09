# STORYBOARD — GA1: Instalar GA4 sin duplicar las visitas

1080×1920 · 30 fps · 10 escenas (escena = clip de voz, sin silencios) · **37,47 s** · voz oficial
`Pablo` (Fish Audio). Serie GA4, bloque 1.

**Verificado sin ojos:** `check` 0 errores · contraste **40/40** WCAG AA · **ningún cruce sin
contenido** (peor tramo 0,00 s; barra ≤ 0,15 s) · **0 huecos** de silencio en el audio.
Montaje: 3 `push-slide` + `zoom-through` + `blur-crossfade` + 3 `crossfade`, sobre la capa
interna `.s-in` (el clip nunca se anima) y con la cola de la escena saliente extendida.

| # | t (s) | Voz | En pantalla |
|---|-------|-----|-------------|
| F1 | 0,00-4,23 | "Instalar Google Analytics es el paso fácil. El error es hacerlo dos veces." | Kicker **GOOGLE ANALYTICS 4**; tarjeta con dos filas: **1 método** (pill ok) y **2 métodos** (pill x2) |
| F2 | 4,23-9,47 | "Todo cuelga de una estructura: cuenta, propiedad, flujo de datos y un identificador." | Kicker **LA ESTRUCTURA**; árbol A Cuenta → B Propiedad → C Flujo de datos → D Identificador con chip `G-XXXXXXXXXX` (entra en el segundo tiempo) |
| F3 | 9,47-13,30 | "Ese identificador empieza por G y es el que conecta tu web con Analytics." | Kicker **EL IDENTIFICADOR**; chip grande `G-XXXXXXXXXX` y la nota "conecta tu web con Analytics" |
| F4 | 13,30-17,52 | "El primer camino es tu gestor de contenidos: pegas el identificador y ya está." | Kicker **1 · TU GESTOR DE CONTENIDOS**; WordPress, Shopify y Wix, y el chip con la pill "pegar" |
| F5 | 17,52-21,35 | "El segundo es la etiqueta de Google, en la cabecera de todas las páginas." | Kicker **2 · LA ETIQUETA**; bloque de código con el `<script>` de gtag en la cabecera |
| F6 | 21,35-24,77 | "Funciona, pero cada cambio posterior te obliga a tocar código." | Kicker **OJO CON LA ETIQUETA**; tarjeta: "la etiqueta vive dentro del código" y la pill de aviso |
| F7 | 24,77-29,38 | "El tercero es Tag Manager: creas un contenedor, pones la etiqueta y publicas." | Kicker **3 · TAG MANAGER**; pasos 1 Contenedor, 2 Etiqueta, 3 Publicar + pill "activado en todas las páginas" |
| F8 | 29,38-31,65 | "El error es instalar por dos caminos a la vez." | Kicker **EL ERROR**; las dos vías (gestor y Tag Manager) y la pill "las dos a la vez = x2" |
| F9 | 31,65-34,84 | "Si los dos envían la etiqueta, cada visita se cuenta dos veces." | Kicker **LA CONSECUENCIA**; dos filas "Analytics 1" y el total en rojo "Total 2 visitas" |
| F10 | 34,84-37,47 | "Elige un método y comprueba que solo hay una etiqueta." | CTA: marca de guardar + **Guarda esto** + pill "solo una etiqueta" |

## Notas de montaje

- **El escenario nunca se oculta:** las tarjetas y el bloque de código nacen visibles y solo se
  asientan con `rise()` (mueve en Y, no toca la opacidad). Antes se animaban con `put()` desde
  opacidad 0 y los cruces se quedaban sin contenido (peor tramo 0,40 s).
- Los paneles suben a `#20202a` (por encima del umbral de luminancia que usa el verificador) y el
  tipo crece: es lo que da masa clara en pantalla durante los empujes.
- F2 es la escena larga (5,24 s) y por eso va en **dos tiempos**: el árbol, y luego el identificador.
- Estado inicial de todo lo animado: `opacity: 0` en CSS (`.pop`, `.fade-up`, `.fade-in`) + `fromTo`
  explícito en GSAP. Nada de `.from()`, contadores, `Date.now()` ni `Math.random()`.

## v2 — feedback del dueño (2026-10-09)

Petición: "hay demasiado texto, necesito menos texto y más elementos gráficos y más
animaciones, y si cuando nombres Google o Analytics pudiera aparecer su logo".

- **Logos en pantalla**, cada uno sobre una tarjeta clara: Google y Google Analytics 4 (logo
  oficial), Tag Manager, WordPress, Shopify y Wix (marcas de simple-icons). Van **en línea**
  (SVG incrustado), así el render no depende de la red.
- **Fuera casi todo el texto**: el que queda son cuatro palabras del diagrama (Cuenta,
  Propiedad, Flujo, ID), una línea de código, el chip `G-XXXXXXXXXX` y el CTA. Las escenas
  de los tres caminos ya no llevan rótulos: hablan los logos.
- **Más animación**: 3 trazos que se dibujan (el árbol, la conexión con la web y los pasos
  de Tag Manager), entradas escalonadas de logos, sellos `x2` que caen y un pulso de aviso.
- **Escenas rehechas**: F1 y F8/F9 pasan a página + etiquetas + sello `x2`; F2 es un diagrama
  con iconos; F3 conecta el logo con la web; F4 son los tres gestores; F7 son tres iconos
  (contenedor → etiqueta → publicar) con la marca verde final.
- Verificado igual que la v1: `check` 0 errores, contraste 23/23 y **0,00 s de tramo vacío**
  en los 9 cruces (mínimos de 43,8 % a 48,5 %).

