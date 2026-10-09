# Backlog de contenido — SEO / marketing digital

Tabla de ideas que **dejamos fuera** de un vídeo para no sobrecargarlo.
Una idea = un vídeo. Antes de montar: definir la jerga en pantalla antes de usarla.

## Convenciones

- **Formato:** 9:16, faceless, voz en off, 30–40 s.
- **Sistema visual:** Kinetic Type + Swiss Grid.
- **CTA:** de guardar (contenido de referencia).
- **Regla de oro:** si un término necesita explicación, o se define en el vídeo o va a otro vídeo.

## En producción

Estado de la **serie SEO**: V1 publicado (voz Kokoro) · V2 publicado (2026-10-08; Facebook dio error de permisos) · V3 publicado (2026-10-08).

| ID | Tema | Ángulo | Formato | Estado |
|----|------|--------|---------|--------|
| GA2 | Cómo saber si GA4 mide de verdad | Los informes tardan y casi nadie lo sabe: parece roto y no lo está | 9:16 · ~30 s · faceless | **En producción** |

## Ideas para próximos vídeos

| ID | Tema | De dónde sale | Por qué se dejó para otro vídeo | Ángulo propuesto | Formato | Estado |
|----|------|---------------|--------------------------------|------------------|---------|--------|
| V2 | Dónde colocar el modificador | Resumen original (e-commerce + lujo) | Asume el concepto de "modificador" que explica V1 | Al final de la URL en alto volumen; nunca en lujo | 9:16 · 29,8 s · 10 frames | **Publicado en Instagram** (2026-10-08; Facebook dio error de permisos). **v7: remontaje** — transiciones, `power3.out`, revelado sincronizado con la voz |
| V3 | Qué es la autoridad y cómo saber la tuya | Implícito en V1 | Es un vídeo base por sí solo; en V1 solo se define de pasada | "Tu web no sube aunque hagas SEO: mira tu autoridad" | 9:16 · 32,0 s · 10 frames | **Hecho v1** — voz `Pablo`; medidor de autoridad, tarjetas de dominio e informe de Enlaces |
| V4 | Modificadores cortos y lectura rápida en Google | Detalle de V2 (la palabra "barato" se procesa de un vistazo) | Es un dato, no una idea completa | Por qué las palabras cortas ganan clics en la SERP | 9:16 · ~25 s (motion-graphics) | Idea |
| V5 | Intención de búsqueda | Extensión natural de V1 | Tema grande; merece su propio vídeo | "Misma palabra, intención distinta, página distinta" | 9:16 · ~40 s | Idea |
| V6 | Canibalización de keywords | Extensión natural | No cabía sin romper el foco de V1 | Dos páginas tuyas compitiendo y ninguna gana | 9:16 · ~40 s | Idea |
| V7 | Contenido fino (thin content) | Extensión natural | Tema aparte | Por qué 500 palabras no posicionan (y 2.000 mal escritas tampoco) | 9:16 · ~40 s | Idea |
| V8 | Aparecer en las respuestas de la IA (AI Overviews) | Enfoque sugerido al inicio | Es un tema actual y potente; pide su propio vídeo | Cómo entra tu marca en la respuesta que ya da Google | 9:16 · ~40 s | Idea |
| V9 | Long-tail vs head terms según autoridad | Derivado de V1/V2 | Detalle de estrategia, no de escritura de títulos | "Si tienes poca autoridad, empieza por lo específico" | 9:16 · ~40 s | Idea |
| V10 | Título, H1 y URL: qué es cada cosa | Jerga usada en V1 | Vídeo 101; solo si el público lo pide | "El título, el encabezado y la URL no son lo mismo" | 9:16 · ~30 s | Idea |

## Serie GA4 — Google Analytics 4

Material completo (briefs, hooks, visuales y listas de referencia) en **`fuentes/ga4-configuracion.md`**.
Aquí solo el plan. **Ocho piezas en tres bloques**; una idea por vídeo, 30-40 s.

| ID | Carpeta prevista | Idea | Bloque | Formato | Estado |
|----|------------------|------|--------|---------|--------|
| GA1 | `videos/ga4-01-instalar-sin-duplicar` | Instalar GA4 sin duplicar las visitas (3 métodos, elige uno) | 1 · instalar | 37,5 s | **Hecho v2 y publicado** (2026-10-09): 10 escenas con logos, poco texto y más animación; `check` 0 errores, 0 cruces vacíos, 0 huecos. Reel en Instagram y Facebook sin portada (job `reel-ga4-01-instalar-sin-duplicar-37944250517`, n8n `ok:true created:1`). Estado comprobado: Instagram **published**, Facebook **error** (job `partial_error`). Es el token/permisos de la Página en n8n, igual que en V2, no el vídeo: hay que reautorizar la credencial de Facebook en el flujo `programacion de reels`. TikTok y YouTube: descartado que sea el webhook (el mismo los admite); n8n responde 400 "YouTube/TikTok require a direct URL on an approved media host" — hace falta alojar el MP4 en un host directo aprobado (GitHub Releases sirve por redirección y no vale para esos dos). **YouTube y TikTok: publicados** (job `reel-ga4-01-instalar-sin-duplicar-tiktok-youtube-37988371777`, pending con media_status staging tras el arreglo de n8n del 2026-10-09; entrada de cola propia). Facebook: 3 publicadas y 5 con error; todas por la misma ruta sin portada y **el corte está en la fecha** (22/28/29-09 publicadas, 30-09 y siguientes con error) → no es `/video_reels` vs `/videos`, sino algo roto desde el 30-09 (probable caducidad del token de Página) |
| GA2 | `videos/ga4-02-comprobar-si-mide` | Cómo saber si GA4 mide de verdad (los informes tardan: no está roto) | 1 · instalar | ~30 s | **En producción** |
| GA3 | `videos/ga4-03-que-mide-solo` | Lo que GA4 ya mide por ti (automáticos + medición mejorada, y qué revisar) | 2 · eventos | ~35 s | Idea |
| GA4 | `videos/ga4-04-eventos-recomendados` | No inventes nombres: usa los recomendados (`generate_lead`, `purchase`…) | 2 · eventos | ~35 s | Idea |
| GA5 | `videos/ga4-05-eventos-clave` | El evento que vale dinero: eventos clave y medir la confirmación real | 2 · eventos | ~35 s | Idea |
| GA6 | `videos/ga4-06-ajustes-que-se-olvidan` | Los ajustes que casi nadie hace (14 meses, tráfico interno, Search Console, Consent Mode) | 3 · ajustar | ~40 s | Idea |
| GA7 | `videos/ga4-07-utm-campanas` | Saber qué publicación trae clientes (UTM; nunca en enlaces internos) | 3 · ajustar | ~35 s | Idea |
| GA8 | `videos/ga4-08-informes-que-importan` | Los siete informes que sí importan | 3 · ajustar | ~40 s | Idea |

Los IDs `GA*` son de esta serie; los `V*` siguen siendo la serie SEO.

## Historial

- **V1** — guion aprobado (3ª iteración, más explicativo, jerga definida). Montado en
  `content/videos/seo-01-copiar-titulo/` con voz local Kokoro `ef_dora`, 7 frames,
  42,3 s, 1080×1920, renderizado a `renders/video.mp4`.
- **V1 (montaje)** — de la línea 3 se quitó "Ese añadido es el modificador." para
  acercar el vídeo a 40 s. Sin música todavía (voz + texto).
- **V1 v2** — reescrito a **11 frames de 3-5 s** (antes 7, con cuatro de 6-8 s) para
  más dinamismo. Se añadieron micro-elementos: mini-SERP de Google, barra de búsqueda,
  iconos de enlaces/historial/tamaño, candado, puntos de posición y barra de progreso.
  Frase confusa "no hay margen. Literal" → "no puedes improvisar. Hay que ser literal".
- **V2** — montado y renderizado: `content/videos/seo-02-modificador-lujo/`, 10 frames,
  34,5 s, 1080×1920, mismo sistema visual y karaoke. Tema: dónde va el modificador
  (e-commerce → final de la URL) y la excepción de lujo. Publicar después de V1.
- **Música** — ambos vídeos llevan una cama electrónica discreta generada en local con
  MusicGen, por debajo de la voz (data-volume 0.18). Pista en `assets/music/track.wav`.
- **V1 v3** — añadidos **subtítulos karaoke** (`caption-pill-karaoke`) en píldora inferior,
  con la palabra activa en verde acento. Timings por palabra aproximados (sin transcripción).
  La barra de progreso se movió arriba (y=300) para no chocar con la píldora.
- **V2 v2 (guion)** — reescritura de claridad tras el feedback ("críptico y poco claro"):
  el hook ancla "modificador" a **"URL"** (el espectador puede no haber visto V1); el giro
  L6→L7 se conecta ("…no lo deberías usar nunca." → "En el lujo, el comprador ve barato
  como mala calidad."); "zapatillas barato" → **"zapatillas baratas"**; "e-commerce" →
  **"comercio electrónico"**; fuera el "Y" inicial y el verbo comodín "va". 10 líneas.
- **V2 v3 (voz + montaje)** — voz clonada de **Fish Audio** ("Consultor Digital",
  `reference_id 694223d3f7ff42979a320307b1254a00`) en lugar de Kokoro; colas de silencio
  recortadas a 0,18 s; composición **re-timada a 37,81 s** (frames 3,0–4,97 s) desde las
  duraciones reales de los clips; karaoke con timings **anclados a las pausas reales**;
  música extendida con crossfade. Rótulos en pantalla actualizados (kicker "COMERCIO
  ELECTRÓNICO", slugs `-baratas`, F6 "donde no lo deberías usar nunca.", F9 "EL MISMO
  MODIFICADOR").
- **V2 v4 (voz definitiva)** — el clon propio ("Consultor Digital") se **descarta**: el
  audio con el que se entrenó venía marcado `quality_passed: false` (*multi speaker*).
  Se adopta la voz **oficial** de Fish Audio **`Pablo`**
  (`1bd666ea8ada44c789e0fec21cf78f33`, masculina, es-ES, *brisk*, `state: trained`).
  Regenerado todo el montaje: **34,09 s**, frames 3,0–4,18 s, karaoke y música re-timados
  (los timings del clon ya no aplicaban).
- **V2 v5 (gráficos + sonido, enfoque definitivo)** — petición del usuario: quitar los
  silencios entre frases, poner efectos de sonido al aparecer cada elemento y **sustituir
  texto por gráficos**. Cambios: escena = clip (voz continua, **29,78 s**); ventana de
  navegador con barra de direcciones en F1–F4; F8 pasa a ser un SERP que se desplaza con
  el cursor pasando de largo (sin una palabra); iconos SVG en lugar de rótulos; fuera los
  textos que repetían la voz. Capa de audio nueva: `assets/sfx/sfx.wav` (34 efectos de 9
  tipos, sintetizados con `tools/sfx.py`).
- **V2 v6 (publicación)** — subido a **Instagram y Facebook** el 2026-10-08. Alojado como
  Release pública `video-seo-02-modificador-lujo` en `openframes` (MP4 + portada) y encolado
  en `hypervideo` (`status: needs_review`). El primer intento, con portada, fue **rechazado
  por n8n** (`jobs: []`); la Action de estado confirmó `not_found`, se **reconcilió la
  reserva** y el reintento **sin portada** fue aceptado (`ok: true, created: 1`, job
  `reel-seo-02-modificador-lujo-37786555312`). La portada queda guardada en la cola.
- **V2 v7 (remontaje: nivel de montaje)** — petición del usuario: subir el nivel de montaje.
  Tres capas, según la doctrina del framework:
  1. **Transiciones** en los 9 cortes (`push-slide` primaria; `zoom-through` en el giro;
     `blur-crossfade` en el lujo; `crossfade` en continuidad y outro). Animan una **capa
     interna** nueva (`#sN-in`) y **extienden la cola** de la escena saliente; los `<audio>`
     no se tocan → **cero silencios**.
  2. **Doctrina de movimiento**: fuera el rebote (`back.out(2)` → **`power3.out`**) y entradas
     con `fromTo` explícito.
  3. **Revelado sincronizado con la voz**: cada elemento aparece cuando el karaoke dice su
     palabra, y el **escenario (el marco) entra con la escena** en lugar de a los 0,3-0,4 s.
  Verificado sin ojos: cobertura del lienzo ≥ 8 % en todos los cruces (antes caía al 3,1 % con
  la escena entrando vacía), perfil de bandas confirmando el desplazamiento, `check` en verde
  y **0 huecos** de silencio en el audio.
- **V3 v1 (autoridad: el vídeo que faltaba)** — primer vídeo construido **enteramente con el
  sistema nuevo** (V2 lo estrenó a posteriori). Guion de 114 palabras con las reglas de claridad
  (jerga definida antes de usarla, sin sujetos elididos, ninguna línea > 14 palabras): autoridad
  = cuánto se fía Google de tu dominio, y se mide por los enlaces que otras webs te dan.
  Voz Fish Audio `Pablo`, **32,05 s · 10 frames**. Kit nuevo: medidor de autoridad, tarjetas de
  dominio, artículo tachado, flujo de enlaces, informe tipo Search Console, barras comparadas
  (3 vs 118). Escena 7 (Enlaces) es el dato accionable del vídeo.
  Verificado: `check` 0 errores · contraste 41/41 · **ningún cruce sin contenido más de 0,13 s**
  · **0 huecos** de silencio.
- **Serie GA4 (planificación)** — el resumen de Google Analytics 4 que trajo el dueño (2026-10-09)
  queda guardado como **fuente** en `fuentes/ga4-configuracion.md`: material completo, brief por
  pieza, hooks, visuales sugeridos y las listas de referencia (eventos recomendados, parámetros,
  UTM, informes, ajustes), para no tener que releer nada de la web. De ahí salen **8 piezas en 3
  bloques**: instalar (GA1-GA2), eventos y conversiones (GA3-GA5) y leer y ajustar (GA6-GA8). Su
  intuición de "tres vídeos" se mantiene como **bloques**; en el formato de 30-40 s cada bloque son
  2-3 piezas, porque aquí **una idea = un vídeo**. Se empieza por **GA1** (instalar sin duplicar
  visitas), que además planta la tesis de la serie: tener Analytics instalado no es tenerlo bien
  configurado. Los `V*` siguen siendo la serie SEO.
- **GA1 v1 (Instalar GA4 sin duplicar las visitas)** — primer vídeo de la serie GA4, montado con
  la cadena completa. 10 escenas, **37,47 s**, voz `Pablo`. Verificado sin ojos: `check` 0 errores,
  contraste 40/40, **0,00 s de tramo vacío** en los 9 cruces y **0 huecos** de audio. Dos lecciones
  de montaje: (1) **el escenario no se anima con opacidad** — si nace en `opacity: 0`, los cruces se
  quedan sin contenido (el peor tramo llegó a 0,40 s); ahora nace visible y solo se asienta con
  `rise()`, que mueve en Y; (2) el verificador mide **píxeles claros**, así que los paneles suben a
  `#20202a` y el tipo crece. La escena 2 (5,24 s) va en dos tiempos. Render en `renders/video.mp4`.
- **GA1 v2 (menos texto, logos y más animación)** — feedback del dueño tras ver la v1. Los tres
  caminos pasan a **logos** (Google, Analytics 4, Tag Manager, WordPress, Shopify y Wix, SVG en
  línea sobre tarjeta clara), se retira casi todo el rótulo (quedan 4 palabras del diagrama, una
  línea de código, el chip y el CTA) y se añade montaje: **trazos que se dibujan**, entradas
  escalonadas, sellos `x2` y un pulso de aviso. **Aviso de proceso:** al reconstruir la región de
  escenas se pierden las colas que añade `transiciones.py`, la escena saliente desaparece al
  empezar el cruce y el lienzo queda negro — hay que rehacer `retime.py` → `transiciones.py`
  antes de renderizar. Verificado: `check` 0 errores, contraste 23/23, 0,00 s de tramo vacío.
