# 02 — Continuidad de la línea «Casos de estudio marketing» (mkt-01)

Contrato de continuidad para la pieza 1 (campaña Old Spice 2010 → negocio pequeño). Hereda **tal cual**
el contrato de producción vigente de V6 (`videos/seo-06-canibalizacion/investigacion/03-contrato.md`),
que a su vez consolida el sistema de `DESIGN.md`, `WORKFLOW.md` y `PUBLICACION.md`. Este fichero añade
solo lo específico de la línea. Fuentes: `PROFILE.md`, `IDEAS.md`, `DESIGN.md`, `WORKFLOW.md`,
`DECISIONS.md`, `PUBLICACION.md` y los guiones/planes de V1, V2, V3, V5, V6 y GA1.

## 1. Reglas de tono y lenguaje que hereda

- **Longitud de línea ≤ 14 palabras**, frases de 6-10 (`PROFILE.md:31`; `WORKFLOW.md:33`;
  `seo-03/SCRIPT.md:14`; `ga4-01/SCRIPT.md:4`). Si no cabe, no se encoge: **se redistribuye** en varios
  tiempos (`seo-05/DIRECCION.md:63`).
- **Tratamiento de tú**, entrada en frío sin intro (`seo-05/SCRIPT.md:78`; `seo-06/SCRIPT.md:9`).
- **Jerga definida antes de usarla** (`PROFILE.md:32`; `WORKFLOW.md:32`; D03; `IDEAS.md:11`): primero se
  explica con palabras normales y solo después se le pone el nombre (patrón de `seo-06/SCRIPT.md:20`, L4).
- **Un solo ejemplo por pieza** (`seo-05/SCRIPT.md:35`; `seo-06/SCRIPT.md:10`).
- **Sin sujetos elididos ni conclusiones sin premisa** (D17; `seo-03/SCRIPT.md:13`).
- **Nunca cifras inventadas ni afirmaciones sin fuente** (`PROFILE.md:45`; `WORKFLOW.md:34`; D18).
- **Cierre con CTA de guardar** con gesto gráfico (marcador + onda), nunca titular (`DESIGN.md:196`;
  `PROFILE.md:31`), p. ej. «Guarda esto».
- **Rechazado explícitamente:** `@handle` en pantalla, relleno, muletillas, silencios (`PROFILE.md:38`;
  D11); avisos de autoría/IA en vídeo, rótulos o leyenda (`PROFILE.md:38`; D34; `AGENTS.md`);
  anglicismos (D18); promesas de resultado y afirmar una penalización (`seo-05/SCRIPT.md:73-80`); refactor
  sin valor visible (D10); portada en IG/FB (D35).

## 2. Qué NO debe repetir esta pieza

- **Ejemplos ya gastados:** «cafetera» / «cómo limpiar una cafetera» (V5, `seo-05/SCRIPT.md:18`);
  «instalación de luz» / «precio instalación de luz» (V6, `seo-06/STORYBOARD.md:15`); «agencias de diseño
  baratas» (V1, `seo-01/SCRIPT.md:70,77`); «zapatillas baratas [para correr]» (V2,
  `seo-02/SCRIPT.md:31,38`); el 3 vs 118 y Search Console → Enlaces (V3, `videos/seo-03-autoridad`);
  los tres caminos de instalación y el chip `G-XXXXXXXXXX` (GA1, `ga4-01/SCRIPT.md:9-18`).
- **Aperturas de gancho gastadas:** «Este error te hará bajar posiciones en Google. No lo hagas.» (V6,
  `seo-06/SCRIPT.md:17`); «Este es el error que hace que aparezcas cada vez menos en Google…» (V5,
  `seo-05/SCRIPT.md:15`); «Tu web no sube aunque hagas SEO» (V3, `seo-03/SCRIPT.md:1`). La nueva necesita
  un gancho propio: el **caso**, no el error.
- **Vocabulario de cada serie (no reutilizar):** SEO → autoridad, enlaces, modificador, intención,
  canibalización, SERP; GA4 → cuenta, propiedad, flujo, identificador, contenedor, etiqueta
  (`ga4-01/SCRIPT.md:10-15`). La línea nueva define **su** jerga (campaña, comentario, respuesta en vídeo).
- **Recursos visuales ya muy vistos:** la **SERP de Google etiquetada** GUÍA/COMPARATIVA/PRODUCTO (V5) y
  la **balanza de dos platos** (V6, `seo-06/DIRECCION.md:9`). La pieza debe estrenar un recurso propio
  (p. ej. hilo de comentarios → vídeo-respuesta).

## 3. Regla del perfil sobre marcas ajenas y arrobas (literal)

`PROFILE.md:38`:

> | Nada de | `@handle` en pantalla, relleno, muletillas, silencios |

`PROFILE.md:39`:

> | Sí a | El **logo de la marca cuando se la nombra** (Google, Search Console…), en línea sobre tarjeta clara (actualizado 2026-10-11) |

Lectura: **permitido** nombrar la marca y mostrar su **logo en línea sobre tarjeta clara**; **prohibido**
el `@handle`/arroba en pantalla y cualquier adorno de autoría o IA (D11, D34). Antes los logos estaban
prohibidos; se autorizaron el 2026-10-11 (commit `857ba96`).

## 4. Caso de estudio vs. explicador SEO

Estructura de la pieza (dictada): **gancho → el caso → el mecanismo → tu versión → la práctica → cierre**.

- **El dato va en «el caso»** (qué hizo la marca en 2010, con fuente). **La aplicación va en «tu versión»
  y «la práctica»** (cómo lo haría un negocio pequeño: quién responde, con qué, cada cuánto). El
  explicador SEO, en cambio, va definición → ejemplo → regla, con el dato repartido y sin protagonista
  externo.
- **El protagonista es una marca ajena:** sirve de **prueba**, no de consejo; el espectador no es el héroe
  hasta «tu versión». De ahí el puente explícito al negocio pequeño y el **logo de la marca**
  (`PROFILE.md:39`), sin `@handle`.
- **Riesgo:** sin ese puente la pieza parece publicidad de la marca, y el gancho no puede reutilizar el
  mecanismo de «error» de la serie SEO.

## 5. Convenciones de la línea nueva

- **Nombre visible:** «Casos de estudio marketing».
- **Slug/carpeta:** `mkt-01-responde-con-video` — coherente con `seo-05-intencion-de-busqueda` y
  `ga4-01-instalar-sin-duplicar` (`<serie>-<NN>-<tema-kebab>`). Prefijo de serie: **`mkt`**.
- **Segunda pieza:** `mkt-02-<tema>`. El `slug` de publicación es el nombre de la carpeta.
- **Cola de publicación (reutilizar los campos vigentes):** `slug`, `status: needs_review`,
  `outputs.render`, `outputs.cover`, `caption`, `publish_attempt`, `outputs.reel_publish`,
  `reel_status`, `notes`; Release `video-<slug>` con `<slug>.mp4` + `<slug>-cover.png`; **una fila por
  slug en `queue.json` y `video-queue.csv` (LF)**; `platforms: instagram,facebook`,
  `include_cover: false`; `caption` leída de la cola, nunca tecleada (D37; `PUBLICACION.md`).

## 6. Avisos

- **Incoherencias detectadas:** `IDEAS.md:28` (V5) da **186 palabras**, pero `seo-05/STORYBOARD.md:4` da
  **188**; la duración alterna 53,07 s (`IDEAS.md:15`) y 53,041 s (`04-contrato`). `seo-06/BRIEF.md` dice
  **~35,7 s** mientras `SCRIPT.md:3` y D38 dan **40,27 s**: el BRIEF y el contrato quedaron desfasados.
  `README.md` solo lista V1-V2. `PROFILE.md:29` fija 30-40 s, pero V5 (53 s) y V6 (40,27 s) ya la superan.
- **La línea nueva no está en el backlog:** `IDEAS.md` no la recoge; hay que registrar «Casos de estudio
  marketing» y su pieza `mkt-01` para no perder la continuidad.
- **Solapes reservados:** V7 contenido fino, V8 AI Overviews, V9 long-tail, V10 título/H1/URL
  (`IDEAS.md:30-33`) y GA2-GA8 (`IDEAS.md:43-50`). La pieza Old Spice es marketing de redes/contenido,
  no SEO on-page ni GA4: no pisa ninguna. Vigilar que «responder comentarios» no invada V8 (respuestas de
  IA) ni GA7 (UTM/publicación).
- **Riesgo de marca:** `PROFILE.md:39` autoriza el logo de la marca nombrada, pero sus ejemplos son
  plataformas («Google, Search Console»), no una marca de consumo como la de esta pieza. **Confirmar con
  el dueño**; no usar la marca como hashtag ni sugerir afiliación.
