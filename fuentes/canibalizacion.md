# V6 — Canibalización de keywords: fuentes y hallazgos

Pieza 9:16 (~40-50 s) para pequeños negocios y autónomos que hacen SEO por su cuenta.
Cada afirmación va marcada como **[documentada]** (respaldada por documentación de Google o
fuente SEO de referencia) o **[opinión]** (criterio de industria). No hay cifras de impacto
porque no existen datos verificables en las fuentes consultadas.

## 1. Definición precisa

- **[documentada]** Canibalización de keywords: dos o más páginas **del mismo sitio** compiten
  por la misma consulta, de modo que Google alterna cuál muestra y ninguna rinde lo que podría.
  La causa no es tener «el mismo tema», sino disputarse la **misma consulta con la misma
  intención**.
- **[documentada]** Dos páginas pueden tratar el mismo asunto y **no** canibalizar si atienden
  intenciones distintas (guía informativa frente a página de compra).
- **Qué NO es:**
  - No es «tener dos páginas del mismo tema». **[documentada]**
  - No es «contenido duplicado»: eso es un problema técnico (mismo contenido en varias URLs) y se
    resuelve con canónica o redirección. Google dice que algo de contenido duplicado es normal y
    no viola sus políticas. **[documentada]**
  - No es que Google «se confunda»: sabe qué hay en cada página. **[opinión]**

## 2. Cómo se manifiesta (señales sin herramientas de pago)

- **[documentada]** La posición de una consulta «baila»: un día aparece una URL tuya y otro día
  la otra.
- **[documentada]** Dos URLs tuyas reciben impresiones por la misma consulta.
- **[documentada]** Aparece la página que no quieres (la antigua o la más floja), no la que te
  interesa.
- **[documentada]** Muchas impresiones y pocos clics: el resultado mostrado no convence.
- **[opinión]** El tráfico se estanca aunque sigas publicando, y los enlaces internos y externos
  se reparten entre dos páginas del mismo tema.

## 3. Cómo se detecta (Search Console)

1. **[documentada]** Search Console → **Rendimiento**. Periodo: últimos 3 meses (hay hasta 16
   meses de histórico).
2. **[documentada]** Pestaña **Consultas**; ordena por impresiones y localiza la consulta que
   importa.
3. **[documentada]** Haz clic en esa fila (queda como filtro) y baja a la pestaña **Páginas**.
   Alternativa: **Añadir filtro → Consultas → «contiene»** → escribe la consulta → Aplicar.
4. **[documentada]** Patrón a buscar: para esa consulta aparecen **dos o más URLs tuyas** con
   impresiones o clics. Esa es la pista.
5. **[documentada]** Confirma a mano: si las dos dan la misma respuesta a la misma intención, es
   canibalización real; si cubren intenciones distintas, no lo es.
6. **[opinión]** Cambia la granularidad a diaria o semanal: si la URL que se lleva los clics
   cambia de una a otra, es la firma «misma consulta, dos URLs alternándose».

Otros métodos: **[documentada]** matriz consulta–URL en una hoja de cálculo buscando consultas
repetidas; **[documentada]** `site:tudominio.com "tema"` como pista rápida, aunque devuelve
coincidencias vagas.

## 4. Cómo se arregla: salidas y cuándo usar cada una

- **A) Diferenciar la intención de cada página.** Cuándo: las intenciones son distintas o cada
  página cubre un subtema. Coste/riesgo: **bajo** (reescribir título, encabezados y enlaces).
  **[documentada]**
- **B) Fusionar y redirigir (301) a una sola.** Cuándo: las dos responden a la **misma
  intención** y una cabe dentro de la otra. Coste/riesgo: **medio-alto**; es la salida más
  eficaz porque une enlaces y señales, pero exige reescribir y actualizar enlaces internos.
  **[documentada]**
- **C) Canónica (`rel="canonical"`).** Cuándo: son **casi idénticas** (duplicado real).
  Coste/riesgo: **bajo**, pero Google la trata como pista y **no arregla** páginas con contenido
  distinto. **[documentada]**
- **D) Dejar de enlazar la débil.** Cuándo: hay una ganadora clara y la otra aporta poco. No hace
  falta borrarla. Coste/riesgo: **bajo**. **[opinión]**

Regla rápida: **distinta intención** → A o D · **misma intención** → B · **duplicado técnico** → C.

## 5. Qué NO hay que hacer

- **[documentada]** **Borrar sin más**: se pierden posiciones de cola larga y enlaces.
- **[documentada]** **Redirigir a la que no corresponde**: enviar a otra intención confunde al
  usuario y a Google.
- **[documentada]** **Poner noindex**: saca la página del índice y pierde **todo** su tráfico, no
  solo esa consulta.
- **[documentada]** **Creer que es «contenido duplicado»**: son problemas distintos y se arreglan
  distinto.
- **[documentada]** **«Desoptimizar»** quitando la keyword: no se puede desoptimizar para una sola
  consulta sin tocar las demás.
- **[documentada]** **Canonicalizar dos páginas distintas**: no funciona si no son duplicado.

## 6. Dos ejemplos dibujables

**Ejemplo 1 (cotidiano).** Una web de café tiene la guía alojada en el blog y la categoría de
producto. Las dos salen para la misma consulta; Google alterna y ninguna acaba primera. Dibujo:
dos fichas en el podio con «empate: no gana ninguna». Arreglo: categoría para comprar, guía para
*cómo elegir*; o fusionar si dicen lo mismo. **Ojo:** V5 ya usó «cafetera», así que en V6 este
ejemplo solo vale como referencia interna, no para pantalla.

**Ejemplo 2 (autónomo).** La página de servicio (instalación de luz) y un artículo del blog con
precios compiten por la misma consulta. Dibujo: dos cajas con la misma etiqueta de consulta y una
flecha de fusión hacia la superviviente. Arreglo: la de servicio para contratar; el artículo para
informar y enlazar al servicio; o fusionar en la de servicio si el artículo no aporta nada único.

## 7. Fuentes (consulta: 2026-10-11)

Documentación de Google:
- Search Central — URL canónica: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Search Central — Canonicalización: https://developers.google.com/search/docs/crawling-indexing/canonicalization
- Search Central — Redirecciones 301: https://developers.google.com/search/docs/crawling-indexing/301-redirects
- Search Central — Meta robots / noindex: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
- Search Console — Informe «Rendimiento»: https://support.google.com/webmasters/answer/7576553?hl=es
- Search Console — Filtrado avanzado: https://support.google.com/webmasters/answer/17011165?hl=es

Fuentes SEO de referencia:
- Moz — Keyword Cannibalization: https://moz.com/blog/keyword-cannibalization
- Ahrefs — Keyword cannibalization: https://ahrefs.com/blog/keyword-cannibalization/
- Search Engine Journal — Keyword Cannibalization: https://www.searchenginejournal.com/keyword-cannibalization/
- Search Engine Land — «What people get wrong about keyword cannibalization» (Patrick Stox):
  https://searchengineland.com/what-people-get-wrong-about-keyword-cannibalization-292148 —
  **[no verificada]** (bloqueó el acceso automatizado; se cita solo a través de Ahrefs)

**Límites declarados:** Google no usa el término «canibalización» en su documentación (es
terminología de industria) y no se han encontrado cifras de impacto verificables, así que no se
incluye ningún número.
