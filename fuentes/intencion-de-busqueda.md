# Intención de búsqueda — material de referencia (V5)

Recopilado el 2026-10-11 para el guion de V5. Separa lo que es **doctrina de Google** de lo que
es **convención de la industria**, porque el vídeo no debe atribuir a Google una taxonomía que
no publica.

## 1. La taxonomía de tipos de intención

- El núcleo **informacional / navegacional / transaccional** nace en la **academia**:
  Andrei Broder, *A Taxonomy of Web Search*, ACM SIGIR Forum (2002) —
  `https://dl.acm.org/doi/10.1145/792550.792552` (el sitio bloquea el acceso automatizado;
  corroborado en `https://en.wikipedia.org/wiki/Web_search_query`).
- La cuarta, **comercial** (*commercial investigation*), la añadió la **industria**:
  `https://moz.com/learn/seo/search-intent` · `https://roborank.io/glossary/commercial-investigation/`
- **Google no publica ni adopta esa taxonomía de cuatro tipos.** Verificado: no aparece en
  `https://www.google.com/search/howsearchworks/how-search-works/ranking-results/` ni en
  `https://blog.google/products/search/search-language-understanding-bert/`.
  → En el vídeo: hablar de **tipos de página que posicionan**, no de etiquetas oficiales.

## 2. Lo que sí dice Google (fuentes oficiales abiertas y confirmadas)

- Interpreta la intención de la consulta para ordenar resultados: «establecer qué estás buscando
  — la intención detrás de tu consulta» —
  `https://www.google.com/search/howsearchworks/how-search-works/ranking-results/`
- Esa interpretación se apoya en modelos de lenguaje (BERT) para «entender la intención detrás
  de las consultas» — `https://blog.google/products/search/search-language-understanding-bert/`
- El peso de cada factor **varía según la naturaleza de la consulta** (misma URL que la primera).
- Google adapta el tipo de resultado: recetas, imágenes, resultados locales, etc.
  (misma URL).
- **Contenido útil para personas**: hecho para personas y no para manipular rankings; incluye la
  pregunta «¿es el tipo de página que guardarías o recomendarías?» —
  `https://developers.google.com/search/docs/fundamentals/creating-helpful-content`
  (de ahí sale el CTA de guardar: es literalmente el criterio que Google pone por escrito.)
- Guía oficial de evaluación: *Search Quality Rater Guidelines* (PDF oficial, existe; no se citó
  su redacción literal porque es binario y no se pudo extraer texto) —
  `https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf`

## 3. Cómo se detecta la intención (lectura de la SERP)

- Señales oficiales de tipo de resultado: fragmentos destacados y «People Also Ask» —
  `https://developers.google.com/search/docs/appearance/featured-snippets`
- Los resultados de imagen y vídeo son más probables en consultas *image-seeking* / *video-seeking*;
  los rich results (estrellas, recetas) los activan los datos estructurados —
  `https://developers.google.com/search/docs/appearance/visual-elements-gallery`
- Lectura práctica (**convención de industria**): fragmento destacado o knowledge graph →
  informacional/navegacional; tabla comparativa → comercial; anuncios, fichas y shopping →
  transaccional — `https://moz.com/blog/understanding-fulfilling-search-intent`
- Una SERP **no** suele tener un único tipo de intención; mezcla varios
  (**convención de industria**, misma URL de Moz).

## 4. Ejemplos (misma palabra, páginas distintas)

| Palabra | Intención | Página que le corresponde |
|---|---|---|
| cafetera | limpiarla (informacional) | guía / tutorial |
| cafetera | comprarla (transaccional) | ficha de producto |
| alojamiento web | comparar (comercial) | comparativa, no la home de una marca |
| seguro de coche | qué cubre (informacional) | guía de coberturas |
| seguro de coche | contratar (transaccional) | simulador |

## 5. El error de una sola página

- Si el contenido no encaja con la intención, el usuario vuelve a Google y el ranking cae
  (*pogo-sticking*) — **convención de industria**:
  `https://moz.com/blog/search-intent-and-seo-a-quick-guide`
- Nota honesta: **no** se encontró una página oficial de Google que formule literalmente este
  error. Google solo dice que prioriza el contenido útil para personas (URL de la sección 2).

## 6. Las ideas más «guardables» (para el CTA y los rótulos)

1. La SERP es el examen: mira quién posiciona (guía, comparativa, ficha, mapa) y esa lectura te
   dice la intención **antes** de escribir.
2. Una SERP puede mezclar intenciones: por eso a veces la misma palabra necesita **más de una
   página**.
3. El usuario decide en segundos: si tu página no le da lo que esperaba, vuelve a Google.
4. Google lo dice por escrito: ¿es el tipo de página que **guardarías** o recomendarías?
