# V6 — Canibalización de palabras clave

Serie SEO · 1080×1920 · faceless · voz en off es-ES (Fish Audio `Pablo`) · **11 líneas · ~35,7 s**
Ángulo: **dos páginas tuyas compitiendo por la misma búsqueda**.
Tesis: **dos páginas tuyas compitiendo por la misma búsqueda: ninguna gana.**
Estado: **propuesta de guion** (un solo ejemplo; la intención de búsqueda se da por sabida, es de V5).
Pendiente de voz y montaje.

> **Criterio:** el gancho abre con la consecuencia y con un imperativo (decisión del dueño, 2026-10-11).
> Después se explica el fenómeno con palabras normales y solo entonces se le pone el nombre. Un único
> ejemplo. Nada de cifras inventadas.

## Guion (voz en off)

| # | Texto | Pal. | Beat | Qué se ve |
|---|-------|------|------|-----------|
| 1 | Este error te hará bajar posiciones en Google. No lo hagas. | 11 | Gancho | Aviso grande en pantalla; la flecha de posición girando hacia abajo |
| 2 | Dos páginas de tu sitio web pueden estar compitiendo por la misma búsqueda. | 13 | El fenómeno | Dos tarjetas de resultado tuyas entrando por el mismo hueco |
| 3 | El resultado es que ambas se hunden en los resultados de Google. | 12 | La consecuencia | Las dos tarjetas bajando a la vez; la SERP se queda abajo |
| 4 | Eso es lo que llaman la canibalización de palabras clave, y sí tiene arreglo. | 14 | El nombre | Rótulo con el término; las dos fichas siguen empatadas |
| 5 | Dos páginas tuyas pueden tratar el mismo tema sin competir, si buscan cosas distintas. | 14 | El matiz | Dos tarjetas separándose, cada una con su etiqueta |
| 6 | Compiten cuando las dos páginas ofrecen la misma respuesta a la misma consulta. | 13 | La causa | Una pastilla de consulta con dos tarjetas solapadas |
| 7 | Por ejemplo, tu página de servicio y un artículo de tu blog pueden estar compitiendo por lo mismo. | 18 | El ejemplo | Dos ventanas de navegador: tu página de servicio y tu artículo del blog |
| 8 | Para comprobar si te pasa, abre Search Console. | 8 | Cómo verlo | Search Console → Rendimiento → Páginas, dos filas iguales |
| 9 | Mira para qué consultas apareces y qué página sale en los resultados. | 12 | Cómo verlo | La misma consulta con dos URLs tuyas alternándose en la tabla |
| 10 | Arréglalo separando bien las dos intenciones o fusionando las dos páginas en una. | 13 | El arreglo | Flecha de fusión hacia una tarjeta; la otra se atenúa |
| 11 | Guarda esto antes de escribir o de revisar la próxima página de tu web. | 14 | CTA | Marcador de guardado con onda; rótulo «Guarda esto» |

**Total: 142 palabras.** A la velocidad de la voz oficial (**3,98 palabras/s**): **≈ 35,7 s**, dentro de
la banda de 30-40 s de la serie. La duración real la fija `voice_pipeline.py`.

**Nota de fuentes:** la línea 1 afirma una consecuencia (bajar posiciones) que las fuentes describen como
«ninguna rinde lo que podría», no como una caída garantizada. Decisión del dueño: se mantiene el
imperativo tal cual. Las líneas 2, 3, 5, 6 y 10 están respaldadas por `investigacion/01-fuentes.md`.

## Jerga que queda definida

| Término | Línea | Cómo se define |
|---|---|---|
| Canibalización de palabras clave | 1-4 | Se explica primero con palabras normales (dos páginas tuyas compitiendo por una búsqueda) y solo en la línea 4 se le pone el nombre |
| Intención | 10 | Vocabulario ya sabido de V5: aquí no se re-explica, se usa |
| Consulta | 6 | La búsqueda concreta que hace una persona (las líneas 2, 7 y 9 dicen «búsqueda») |

## Lo que NO se repite (continuidad)

- **Con V5:** no se re-explica la intención de búsqueda ni se etiqueta la SERP (guía/comparativa/producto); «una intención, una página» es de V5, no la tesis de V6; nada de «cafetera».
- **Con V1, V2 y V3:** ni las cuatro posiciones, ni «agencias de diseño baratas», ni los modificadores y la URL, ni la autoridad y los enlaces. Aquí Search Console se usa en Rendimiento → Páginas, no en Enlaces (eso fue de V3).
- **Reservadas:** V7 contenido fino, V8 AI Overviews, V9 long-tail, V10 título/H1/URL.

## Alternativas del gancho

1. **En uso (dictado por el dueño):** «Este error te hará bajar posiciones en Google. No lo hagas.» (11 pal.)
2. **Sin repetir la apertura de V5:** «Hay un error que te está haciendo bajar posiciones en Google.» (11 pal.)
3. **Más concreto:** «Dos páginas tuyas se turnan en Google y ninguna de las dos llega arriba.» (14 pal.)

## Reglas aplicadas

Tratamiento de tú · entrada en frío sin intro · una idea por línea (la línea 7 va a **18 palabras** por
texto expreso del dueño y no se parte; el resto se mantiene en **14 o menos**) · jerga definida
antes de usarla (el término «canibalización» llega en la línea 4, tras explicar el fenómeno) · **un solo
ejemplo** (página de servicio frente a artículo propio; nada de «cafetera» ni de ejemplos de V1-V3) ·
**sin cifras inventadas ni anglicismos** (Search Console es el nombre del producto) · CTA de guardar ·
sin avisos de autoría ni menciones a IA.

## Guion plano (para el pipeline de voz)

Estas son las líneas que lee `voice_pipeline.py` (4 espacios de sangría), en el mismo orden que la tabla.

    Este error te hará bajar posiciones en Google. No lo hagas.
    Dos páginas de tu sitio web pueden estar compitiendo por la misma búsqueda.
    El resultado es que ambas se hunden en los resultados de Google.
    Eso es lo que llaman la canibalización de palabras clave, y sí tiene arreglo.
    Dos páginas tuyas pueden tratar el mismo tema sin competir, si buscan cosas distintas.
    Compiten cuando las dos páginas ofrecen la misma respuesta a la misma consulta.
    Por ejemplo, tu página de servicio y un artículo de tu blog pueden estar compitiendo por lo mismo.
    Para comprobar si te pasa, abre Search Console.
    Mira para qué consultas apareces y qué página sale en los resultados.
    Arréglalo separando bien las dos intenciones o fusionando las dos páginas en una.
    Guarda esto antes de escribir o de revisar la próxima página de tu web.
