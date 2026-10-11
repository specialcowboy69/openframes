# 02 — Continuidad de la serie SEO para V6 (canibalización de keywords)

Contrato de continuidad. Fuentes: `IDEAS.md`, `PROFILE.md`, `DESIGN.md`, `WORKFLOW.md`,
`DECISIONS.md`, `MEMORY.md` y los guiones/planes de V1, V2, V3, V5 y GA1.
V6 = «dos páginas tuyas compitiendo y ninguna gana» (`IDEAS.md:29`).

## 1. Qué ha cubierto cada pieza

| ID | Tema | Tesis (una frase) | Se ve en pantalla |
|----|------|-------------------|-------------------|
| **V1** | Copiar el título del nº1 | La autoridad decide cómo escribes el título, no la fórmula del que está arriba (`seo-01/BRIEF.md:5`) | Mini-SERP, barra de búsqueda, las 4 posiciones (Título/URL/Encabezado/Párrafo 1) con check, candado, puntos de posición |
| **V2** | Dónde va el modificador / lujo | Dónde colocar el modificador depende del tipo de tienda; en lujo nunca se usa (`seo-02/BRIEF.md:5`) | Ventana de navegador (`tutienda.com/zapatillas-baratas`), marcador `+`, barras, gema + «barato» tachado, SERP con scroll y cursor |
| **V3** | Autoridad | Tu web no sube por el contenido: sube por los enlaces que otros te dan (`seo-03/BRIEF.md:5`) | Medidor (22→58→83/100), tarjetas de dominio, artículo con check tachado, Search Console → Enlaces, barras 3 vs 118 |
| **V5** | Intención de búsqueda | «Una intención, una página» (`seo-05/BRIEF.md:19`) | Aspa roja sobre la página única, trazo consulta→diana, «cafetera» que ramifica, SERP con etiquetas GUÍA/COMPARATIVA/PRODUCTO, cuadrícula 1:1:1 |
| **GA1** | Instalar GA4 sin duplicar | Tres formas de conectar la web: hay que elegir una; dos vías a la vez duplican (`ga4-01/BRIEF.md:4-5`) | Logos (Google, Analytics, Tag Manager, WordPress, Shopify, Wix), árbol cuenta→propiedad→flujo→ID, chip `G-XXXXXXXXXX`, sellos `x2` |

## 2. Reglas de tono y lenguaje (deducidas)

- **Jerga definida antes de usarla.** `DECISIONS.md:10` (D03); `WORKFLOW.md:32`; `PROFILE.md:32`;
  `seo-03/SCRIPT.md:13`; `seo-05/SCRIPT.md:79`; `ga4-01/SCRIPT.md:4`; `IDEAS.md:11`.
- **Sin sujetos/verbos elididos; cada conclusión con su premisa.** `DECISIONS.md:24` (D17);
  `seo-03/SCRIPT.md:13`; `MEMORY.md` («conclusiones sin premisa: "Exacto."»).
- **Línea ≤ 14 palabras** (`seo-03/SCRIPT.md:14`; `ga4-01/SCRIPT.md:4`); frases de 6-10 (`WORKFLOW.md:33`).
  Si no cabe, **se redistribuye en el tiempo, no se encoge** (`seo-05/DIRECCION.md:63`).
- **Un solo ejemplo por pieza:** V5 pasó de tres a solo «cafetera» (`seo-05/SCRIPT.md:35`).
- **Nada de ganchos por miedo ni de afirmar penalización:** V5 retiró la negación de la penalización y
  cuenta la consecuencia (`seo-05/SCRIPT.md:40-45`; commit `e4b1bbd`).
- **Sin anglicismos, cifras inventadas, promesas ni afirmaciones sin fuente.**
  `seo-05/SCRIPT.md:79`; `PROFILE.md:45`; `WORKFLOW.md:34`; `DECISIONS.md:25` (D18).
- **Sin muletillas, relleno, `@handle` ni avisos de IA.** `PROFILE.md:38`; `DECISIONS.md:18,41`.
- **Tú, entrada en frío sin intro, CTA de guardar con gesto gráfico.** `seo-05/SCRIPT.md:78`;
  `WORKFLOW.md:30`; `DESIGN.md:196`.

## 3. Qué puede heredar V6

- **Ecos y continuidad.** V5 cierra con «una intención, una página» (`seo-05/SCRIPT.md:25`); V6 es su
  reverso: la **misma** intención repartida en dos páginas propias que compiten. Hereda la lógica
  1:1:1 y el mapa de la SERP; el conflicto es entre páginas tuyas, no entre intenciones.
- **Vocabulario ya sabido (no redefinir):** autoridad y enlaces (V3), modificador/URL (V1-V2), intención
  de búsqueda, búsqueda completa, SERP, guía/comparativa/ficha/página de producto (V5), posición.
- **Objetos del kit reutilizables:** ventana de navegador, tarjeta de resultado, SERP con scroll y
  cursor, barras comparadas, aspa roja, cuadrícula 1:1:1, diana, marcador de guardado (`DESIGN.md` §3).
- **Cierre/CTA de serie:** guardar con marcador + onda; rótulo **Guarda esto** (`DESIGN.md:196`;
  `seo-05/BRIEF.md:33-34`). Cierre tipo V5: «Guarda este vídeo antes de escribir tu próxima página».
- **Longitud real de la serie:** V5 mide **53,041 s** (`seo-05/STORYBOARD.md`), no los ~40 s del backlog.
- **Aviso:** V5 promete **no** derivar a V6 (`seo-05/SCRIPT.md:73`); V6 abre con pregunta propia sin
  repetir el mecanismo de V5.

## 4. Qué NO debe repetir V6 (solapamientos concretos)

1. **Con V5:** no re-explicar la intención ni la lectura de la SERP con etiquetas
   GUÍA/COMPARATIVA/PRODUCTO; no reusar «cafetera» («cómo limpiar una cafetera» / «comprar una
   cafetera», `seo-05/SCRIPT.md:18`) ni «alojamiento web» / «seguro de coche»
   (`fuentes/intencion-de-busqueda.md:53-59`); **«una intención, una página» es de V5**, no la tesis de V6.
2. **Con V1:** no repetir las 4 posiciones ni «agencias de diseño baratas» / «el nº1 escribe: las
   agencias de diseño más baratas» (`seo-01/SCRIPT.md:56,70,77`).
3. **Con V2:** no reusar «zapatillas baratas» / «zapatillas baratas para correr», ni la excepción de
   lujo, ni la colocación del modificador en la URL (`seo-02/SCRIPT.md:31,38,59`).
4. **Con V3:** no re-explicar autoridad/enlaces, ni Search Console → Enlaces, ni 3 vs 118, ni
   `medio.com`/`otratienda.com` (`seo-03/STORYBOARD.md:51,63,89`).
5. **Reservadas:** V7 contenido fino, V8 AI Overviews, V9 long-tail vs head, V10 título/H1/URL
   (`IDEAS.md:30-33`). No pisarlas.
6. **Ganchos ajenos:** «aparece cada vez menos» (`seo-05/SCRIPT.md:15`) y «tu web no sube aunque hagas
   SEO» (`seo-03/SCRIPT.md:23`). V6 necesita uno propio.

## 5. Convenciones de pantalla e idioma

- **Kicker:** 28-32 px, 700, **mayúsculas**, `letter-spacing: 0.28em`, `muted` con punto de color
  (`DESIGN.md:59`; `seo-05/DIRECCION.md:57,61`).
- **Rótulos de sección:** mayúsculas, frase nominal («EL IDENTIFICADOR», «LA CONSECUENCIA», «EL ERROR»)
  y **numerados** «1 · », «2 · », «3 · » (`ga4-01/STORYBOARD.md:13-20`).
- **Pastillas/etiquetas:** mayúsculas («QUIERE CONSEGUIR», «MÁS DE UNA INTENCIÓN»,
  «ENTENDER/COMPARAR/COMPRAR»; `seo-05/STORYBOARD.md`).
- **CTA:** «Guarda esto», 96 px, con marcador + onda (`seo-05/DIRECCION.md:60`).
- **Palabras por beat:** mínimo; guion ≤ 14 palabras, pero V5 **reparte** una línea de 22-24 en 2-3
  tiempos dentro del beat (`seo-05/DIRECCION.md:63`). Nada de texto que repita la voz (`DESIGN.md:27`).
- **Tipografía:** Inter + JetBrains Mono para lo tecleado; protagonista 110-180 px, frase 70-110,
  contexto 38-56 (`DESIGN.md` §2; `seo-05/DIRECCION.md` §3).
- **Montaje:** escena = clip sin silencios; escenario visible desde t=0, solo `rise()`; karaoke abajo;
  barra de progreso arriba (`DESIGN.md:83,100-105`; `ga4-01/STORYBOARD.md:26-28`).
- **Cierre:** siempre CTA de guardar con gesto gráfico, nunca titular (`DESIGN.md:194-197`).

## 6. Incoherencias detectadas

- **`IDEAS.md:28` (fila V5) desactualizada:** dice «10 escenas · 123 palabras ≈ 41 s. Pendiente: voz y
  montaje». Real: **12 escenas · 188 palabras · 53,041 s**, voz y montaje hechos (`seo-05/BRIEF.md:4`;
  `SCRIPT.md:28`; `MEMORY.md`).
- **`IDEAS.md:15` (estado de la serie SEO):** solo lista V1-V3 publicados; **no menciona V5** ni V6.
- **Duración de V5 contradictoria:** `seo-05/SCRIPT.md:3` dice «12 líneas · ~60 s» frente a **53,041 s**;
  y 186 palabras en `SCRIPT.md:28` frente a **188** en `seo-05/STORYBOARD.md:4` (`seo-05/BRIEF.md:4`
  solo declara la duración, no el recuento).
- **Gancho de V5 contado dos veces:** `seo-05/SCRIPT.md:15` da 19 palabras y `SCRIPT.md:49`, 18.
- **V2 desfasado:** `seo-02/SCRIPT.md:6` dice **34,09 s**, pero `seo-02/STORYBOARD.md:3` e
  `IDEAS.md:25` dicen **29,8 s** (residuo v4→v5).
- **V6 en backlog dice «~40 s»** (`IDEAS.md:29`), lejos de la deriva real (~53 s en V5); decidir antes de montar.

---
Creado 2026-10-11 como contrato de continuidad para V6. Fuera de este fichero no se ha tocado nada.
