# Backlog de contenido — SEO / marketing digital

Tabla de ideas que **dejamos fuera** de un vídeo para no sobrecargarlo.
Una idea = un vídeo. Antes de montar: definir la jerga en pantalla antes de usarla.

## Convenciones

- **Formato:** 9:16, faceless, voz en off, 30–40 s.
- **Sistema visual:** Kinetic Type + Swiss Grid.
- **CTA:** de guardar (contenido de referencia).
- **Regla de oro:** si un término necesita explicación, o se define en el vídeo o va a otro vídeo.

## Idea en producción

| ID | Tema | Ángulo | Formato | Estado |
|----|------|--------|---------|--------|
| V1 | Por qué copiar el título del nº1 no funciona | La autoridad decide cómo de rígido escribes (poca = literal / mucha = libre) | 9:16 · 42,5 s · 11 frames de 3-5 s | Renderizado (v2) — pendiente de revisar |

## Ideas para próximos vídeos

| ID | Tema | De dónde sale | Por qué se dejó para otro vídeo | Ángulo propuesto | Formato | Estado |
|----|------|---------------|--------------------------------|------------------|---------|--------|
| V2 | Dónde colocar el modificador | Resumen original (e-commerce + lujo) | Asume el concepto de "modificador" que explica V1 | Al final de la URL en alto volumen; nunca en lujo | 9:16 · 29,8 s · 10 frames | Guion reescrito + voz oficial Fish Audio `Pablo` + rediseño gráfico (ventana de navegador, cursor) y efectos de sonido |
| V3 | Qué es la autoridad y cómo saber la tuya | Implícito en V1 | Es un vídeo base por sí solo; en V1 solo se define de pasada | "Tu web no sube aunque hagas SEO: mira tu autoridad" | 9:16 · ~40 s | Idea |
| V4 | Modificadores cortos y lectura rápida en Google | Detalle de V2 (la palabra "barato" se procesa de un vistazo) | Es un dato, no una idea completa | Por qué las palabras cortas ganan clics en la SERP | 9:16 · ~25 s (motion-graphics) | Idea |
| V5 | Intención de búsqueda | Extensión natural de V1 | Tema grande; merece su propio vídeo | "Misma palabra, intención distinta, página distinta" | 9:16 · ~40 s | Idea |
| V6 | Canibalización de keywords | Extensión natural | No cabía sin romper el foco de V1 | Dos páginas tuyas compitiendo y ninguna gana | 9:16 · ~40 s | Idea |
| V7 | Contenido fino (thin content) | Extensión natural | Tema aparte | Por qué 500 palabras no posicionan (y 2.000 mal escritas tampoco) | 9:16 · ~40 s | Idea |
| V8 | Aparecer en las respuestas de la IA (AI Overviews) | Enfoque sugerido al inicio | Es un tema actual y potente; pide su propio vídeo | Cómo entra tu marca en la respuesta que ya da Google | 9:16 · ~40 s | Idea |
| V9 | Long-tail vs head terms según autoridad | Derivado de V1/V2 | Detalle de estrategia, no de escritura de títulos | "Si tienes poca autoridad, empieza por lo específico" | 9:16 · ~40 s | Idea |
| V10 | Título, H1 y URL: qué es cada cosa | Jerga usada en V1 | Vídeo 101; solo si el público lo pide | "El título, el encabezado y la URL no son lo mismo" | 9:16 · ~30 s | Idea |

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
