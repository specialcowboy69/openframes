# V6 — Canibalización de palabras clave

Serie SEO · 1080×1920 · faceless · voz en off es-ES (Fish Audio `Pablo`) · **12 líneas · ~41,5 s**
Ángulo: **dos páginas tuyas compitiendo por la misma búsqueda**.
Tesis: **dos páginas tuyas compitiendo por la misma búsqueda: ninguna gana.**
Estado: **propuesta de guion** (un solo ejemplo; la intención de búsqueda se da por sabida, es de V5).
Pendiente de voz y montaje.

> **Criterio:** el gancho describe el síntoma, no asusta. Primero se explica el fenómeno con palabras
> normales y solo después se le pone el nombre. Un único ejemplo. Nada de cifras, promesas ni
> penalizaciones: todo lo afirmado está en `investigacion/01-fuentes.md`.

## Guion (voz en off)

| # | Texto | Pal. | Beat | Qué se ve |
|---|-------|------|------|-----------|
| 1 | Un día Google muestra una página tuya en los resultados y al siguiente, otra. | 14 | Gancho | Dos tarjetas de resultado tuyas que se turnan en la SERP |
| 2 | Las dos compiten por la misma búsqueda y se acaban quitando fuerza entre ellas. | 14 | El fenómeno | Las dos tarjetas empujándose; una barra que se reparte |
| 3 | Y el resultado es que ninguna de las dos consigue la posición que podría. | 14 | La consecuencia | Marcador de posición que no sube; la SERP se queda abajo |
| 4 | Eso es lo que llaman la canibalización de palabras clave, y sí tiene arreglo. | 14 | El nombre | Rótulo con el término; las dos fichas siguen empatadas |
| 5 | Dos páginas tuyas pueden tratar el mismo tema sin competir, si buscan cosas distintas. | 14 | El matiz | Dos tarjetas separándose, cada una con su etiqueta |
| 6 | Compiten cuando las dos páginas ofrecen la misma respuesta a la misma consulta. | 13 | La causa | Una pastilla de consulta con dos tarjetas solapadas |
| 7 | Tu página de servicio y un artículo tuyo compiten por la misma búsqueda. | 13 | El ejemplo | Dos ventanas de navegador: tu página de servicio y tu artículo |
| 8 | Google alterna entre las dos y ninguna de ellas acaba en la primera posición. | 14 | El resultado | La SERP resalta una y luego la otra; ninguna arriba |
| 9 | En Search Console puedes ver dos páginas tuyas compitiendo por la misma búsqueda. | 13 | Cómo verlo | Search Console → Rendimiento → Páginas, dos filas iguales |
| 10 | Se arregla separando bien las dos intenciones o fusionando las dos páginas en una. | 14 | El arreglo | Flecha de fusión hacia una tarjeta; la otra se atenúa |
| 11 | Dos páginas tuyas compitiendo por lo mismo: ninguna gana, así que deja solo una. | 14 | La regla | Una sola tarjeta firme; rótulo con la regla |
| 12 | Guarda esto antes de escribir o de revisar la próxima página de tu web. | 14 | CTA | Marcador de guardado con onda; rótulo «Guarda esto» |

**Total: 165 palabras.** Objetivo 40-50 s a la velocidad de la voz oficial (**3,98 palabras/s**):
**≈ 41,5 s**. La duración real la fija `voice_pipeline.py`. La banda 30-40 s de la serie queda como
decisión abierta del dueño (ver `BRIEF.md`).

## Jerga que queda definida

| Término | Línea | Cómo se define |
|---|---|---|
| Canibalización de palabras clave | 1-4 | Se explica primero con palabras normales (dos páginas tuyas compitiendo por una búsqueda) y solo en la línea 4 se le pone el nombre |
| Intención | 10 | Vocabulario ya sabido de V5: aquí no se re-explica, se usa |
| Consulta | 6 | La búsqueda concreta que hace una persona (las líneas 2, 7 y 9 dicen «búsqueda») |

No se presenta la taxonomía como doctrina de Google ni se afirma ningún efecto que no esté en las fuentes.

## Lo que NO se repite (continuidad)

- **Con V5:** no se re-explica la intención de búsqueda ni se etiqueta la SERP (guía/comparativa/producto); «una intención, una página» es de V5, no la tesis de V6; nada de «cafetera».
- **Con V1, V2 y V3:** ni las cuatro posiciones, ni «agencias de diseño baratas», ni los modificadores y la URL, ni la autoridad y los enlaces. Aquí Search Console se usa en Rendimiento → Páginas, no en Enlaces (eso fue de V3).
- **Reservadas:** V7 contenido fino, V8 AI Overviews, V9 long-tail, V10 título/H1/URL.

## Alternativas del gancho

1. **En uso:** «Un día Google muestra una página tuya en los resultados y al siguiente, otra.» (14 pal.)
2. **Más directo:** «Dos páginas tuyas se turnan en Google y ninguna de las dos llega arriba.» (14 pal.)
3. **Con el síntoma pegado a ti:** «Esa página que no arranca puede estar peleándose con otra tuya.» (11 pal.)

## Reglas aplicadas

Tratamiento de tú · entrada en frío sin intro · una idea por línea y **≤ 14 palabras** · jerga definida
antes de usarla (el término «canibalización» llega en la línea 4, tras explicar el fenómeno) · **un solo
ejemplo** (página de servicio frente a artículo propio; nada de «cafetera» ni de ejemplos de V1-V3) ·
gancho que describe el síntoma, **sin miedo ni penalizaciones** · **sin cifras inventadas, promesas ni
anglicismos** (Search Console es el nombre del producto) · CTA de guardar · sin avisos de autoría ni
menciones a IA.

## Guion plano (para el pipeline de voz)

Estas son las líneas que lee `voice_pipeline.py` (4 espacios de sangría), en el mismo orden que la tabla.

    Un día Google muestra una página tuya en los resultados y al siguiente, otra.
    Las dos compiten por la misma búsqueda y se acaban quitando fuerza entre ellas.
    Y el resultado es que ninguna de las dos consigue la posición que podría.
    Eso es lo que llaman la canibalización de palabras clave, y sí tiene arreglo.
    Dos páginas tuyas pueden tratar el mismo tema sin competir, si buscan cosas distintas.
    Compiten cuando las dos páginas ofrecen la misma respuesta a la misma consulta.
    Tu página de servicio y un artículo tuyo compiten por la misma búsqueda.
    Google alterna entre las dos y ninguna de ellas acaba en la primera posición.
    En Search Console puedes ver dos páginas tuyas compitiendo por la misma búsqueda.
    Se arregla separando bien las dos intenciones o fusionando las dos páginas en una.
    Dos páginas tuyas compitiendo por lo mismo: ninguna gana, así que deja solo una.
    Guarda esto antes de escribir o de revisar la próxima página de tu web.
