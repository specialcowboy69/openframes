# V5 — Intención de búsqueda

Serie SEO · 1080×1920 · faceless · voz en off es-ES (Fish Audio `Pablo`) · **12 líneas · ~60 s**
Ángulo: **misma palabra, intención distinta, página distinta**.
Estado: **guion v5** (un ejemplo; la intención la fija la búsqueda completa). Pendiente de voz y montaje.

> **Criterio de esta revisión (2026-10-11, pedido del dueño):** primero que se entienda; la duración
> es lo de menos. La palabra suelta no decide la intención: la decide la **búsqueda completa**, y una
> palabra corta puede mezclar varias. Un solo ejemplo.

## Guion (voz en off)

| # | Texto | Pal. | Beat |
|---|-------|------|------|
| 1 | Este es el error que hace que aparezcas cada vez menos en Google. Y casi nadie te lo cuenta. | 19 | Gancho |
| 2 | La intención de búsqueda es lo que alguien quiere conseguir cuando escribe una palabra en Google. | 16 | Definir |
| 3 | La misma palabra sirve para búsquedas distintas: lo que cambia es qué quiere cada persona. | 15 | La palabra no basta |
| 4 | «Cafetera» no es lo mismo que «cómo limpiar una cafetera» o «comprar una cafetera». | 14 | El ejemplo |
| 5 | En una quieres aprender y en la otra quieres comprar; y Google enseña páginas distintas para cada una. | 18 | Qué cambia |
| 6 | El truco es mirar los resultados que ya salen en Google antes de escribir la tuya. | 16 | La regla |
| 7 | Si los primeros resultados son guías, la gente quiere entender. Si son comparativas, quiere comparar. Si son páginas de producto, quiere comprar. | 22 | Leer la SERP |
| 8 | Y si ves varias de esas mezcladas, esa palabra tiene más de una intención. | 14 | Caso mezclado |
| 9 | El error es darle una sola página para todo eso. | 10 | El error |
| 10 | Quien busca no encuentra lo que quería: cierra la pestaña de tu web y hace clic en el siguiente resultado. | 20 | La consecuencia |
| 11 | Una intención, una página. Decide qué página merece cada búsqueda antes de escribir. | 13 | El arreglo |
| 12 | Guarda este vídeo antes de escribir tu próxima página. | 9 | CTA |

**Total: 186 palabras.** **Voz generada y medida** (12 líneas, Fish Audio `Pablo`, 2026-10-11): total **53,041 s**, clips de 2,467 a 7,941 s.
Los tiempos por línea están en `assets/voice/timing.json` y la tabla de escenas en `STORYBOARD.md`.

## Lo que corrige esta versión

| Punto | Antes | Ahora | Por qué |
|---|---|---|---|
| Ejemplo único | Tres ejemplos (cafetera, alojamiento web, seguro de coche) | **Solo «cafetera»** | Petición del dueño: un ejemplo basta. |
| Qué fija la intención | «Quien busca «alojamiento web» espera una comparativa…» | ««Cafetera» no es lo mismo que «cómo limpiar una cafetera» o «comprar una cafetera»» | La palabra suelta **no** determina la intención: la determina la búsqueda completa. El dueño lo señaló y tenía razón. |
| Palabra corta ambigua | No se contemplaba | Línea 8: «si ves varias de esas mezcladas, esa palabra tiene más de una intención» | «Alojamiento web» puede querer decir comparar o contratar según quién busque. Es el caso real. |
| La regla final | «Una palabra, una intención, una página» | **«Una intención, una página»** | Si una palabra mezcla intenciones, necesita más de una página. Así la regla aguanta el caso mezclado. |

## Sobre la palabra «penaliza» (decisión del dueño, 2026-10-11)

El gancho describe el efecto real: si tu página no responde a lo que pide la búsqueda, **pierdes
relevancia de forma progresiva y acabas dejando de aparecer**. En la documentación de Google,
«penalización» se usa para acciones manuales por spam, así que el guion cuenta la consecuencia en
lugar de afirmar una penalización formal. Si se prefiere la palabra, la opción 4 la usa en coloquial.

### Alternativas del gancho

1. **En uso:** «Este es el error que hace que aparezcas cada vez menos en Google. Y casi nadie te lo cuenta.» (18 pal.)
2. **Sin la palabra «error»:** «Si tu página no responde a lo que la gente busca, aparecerás cada vez menos en Google. Y nadie te lo cuenta.» (22 pal.)
3. **Más seco, con el mecanismo:** «Misma palabra, intenciones distintas, una sola página: por eso vas perdiendo posiciones en Google.» (15 pal.)
4. **Con «penaliza», en coloquial:** «Google te va penalizando poco a poco: primero apareces menos y acabas desapareciendo de esas búsquedas.» (16 pal.)

## Jerga que queda definida en pantalla

| Término | Línea | Cómo se define |
|---|---|---|
| Intención de búsqueda | 2 | «lo que alguien quiere conseguir cuando escribe una palabra en Google» |
| Búsqueda completa | 4-5 | Se ve con el ejemplo: la misma palabra, dos búsquedas, dos resultados |
| Guía | 7 | Con su uso: si aparecen guías, la gente quiere entender |
| Comparativa | 7 | Con su uso: si aparecen comparativas, quiere comparar |
| Página de producto | 7 | Con su uso: si aparecen páginas de producto, quiere comprar |

Nunca se presenta la taxonomía como doctrina de Google: es convención de industria. Y no se dice
que una palabra tenga una única intención: eso es justo lo que el vídeo corrige.

## Lo que NO se repite (ya está en V1–V3)

- V1: qué es un modificador, las cuatro posiciones de la palabra clave, escribir según autoridad.
- V2: dónde va el modificador en la URL y la excepción de lujo.
- V3: qué es la autoridad, que la dan los enlaces, Search Console → Enlaces.

Y no se deriva a los vídeos vecinos: nada de canibalización (V6), long-tail (V9), modificadores
cortos (V4) ni AI Overviews (V8).

## Reglas aplicadas

Tratamiento de tú · entrada en frío sin intro · **la claridad manda sobre la brevedad** · sin
muletillas · sin cifras ni promesas · sin afirmaciones sin fuente · sin anglicismos · jerga definida
antes de usarla · CTA de guardar · sin avisos de autoría ni menciones a IA.

## Guion plano (para el pipeline de voz)

Estas son las líneas que lee `voice_pipeline.py` (4 espacios de sangría). Las comillas
de cita se quitan en la locución; en pantalla se muestran como citas.

    Este es el error que hace que aparezcas cada vez menos en Google. Y casi nadie te lo cuenta.
    La intención de búsqueda es lo que alguien quiere conseguir cuando escribe una palabra en Google.
    La misma palabra sirve para búsquedas distintas: lo que cambia es qué quiere cada persona.
    Cafetera no es lo mismo que cómo limpiar una cafetera o comprar una cafetera.
    En una quieres aprender y en la otra quieres comprar; y Google enseña páginas distintas para cada una.
    El truco es mirar los resultados que ya salen en Google antes de escribir la tuya.
    Si los primeros resultados son guías, la gente quiere entender. Si son comparativas, quiere comparar. Si son páginas de producto, quiere comprar.
    Y si ves varias de esas mezcladas, esa palabra tiene más de una intención.
    El error es darle una sola página para todo eso.
    Quien busca no encuentra lo que quería: cierra la pestaña de tu web y hace clic en el siguiente resultado.
    Una intención, una página. Decide qué página merece cada búsqueda antes de escribir.
    Guarda este vídeo antes de escribir tu próxima página.