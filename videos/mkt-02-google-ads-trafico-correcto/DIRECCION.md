# DIRECCIÓN DE ARTE — mkt-02 «El tráfico correcto (Google Job Experiment, 2010)»

Aplica el brief del dueño (`DIRECCION-ARTE-BRIEF.md`) y el contrato de producción heredado
(`videos/seo-06-canibalizacion/investigacion/03-contrato.md`). Serie **Casos de estudio marketing** ·
Pieza **mkt-02** · **11 beats · 123 palabras · ≈38,4 s** · 1080×1920 · voz en off es-ES (`Pablo`) ·
subtítulos karaoke · barra de progreso. Formato calcado de `mkt-01-responde-con-video/DIRECCION.md`.

---

## 1. Dirección elegida: «el blanco» (dar en el centro)

**Metáfora central.** La pieza es un **blanco de tiro** (una diana de anillos concéntricos). En
anuncios **no gana quien llena el muro de disparos, gana quien da en el centro**: las **pocas marcas
correctas** viven en el anillo interior y el resto de la pared se queda salpicado de impactos que no
cuentan. El centro del blanco = **los pocos clientes correctos**; el muro = **el tráfico genérico y
masivo** que se dispersa. La metáfora **reaparece a lo largo de toda la pieza**, encadenando el caso
con la aplicación:

- **B1** la estrena: la barra de búsqueda se monta **sobre el blanco** (buscar es *apuntar*), con la
  cifra `6 €` como cebo.
- **B4** la usa como prueba: los **cinco nombres** se marcan uno a uno —la lista de los pocos
  elegidos, frente a los muchos que no se compran—.
- **B6** la mide: el marcador **4/5** y **2** ofertas —cuatro de los cinco responden—.
- **B7** la escenifica: **una multitud de impactos dispersos se apaga** y solo **cinco marcas**
  quedan encendidas en el centro.
- **B9** la aplica: los términos genéricos (los disparos a la pared) se **tachan** y una **lupa**
  amplía **el centro** —«tu cliente ideal»—.
- **B11** la cierra: el **centro del blanco se rellena de acento** con las cinco marcas correctas
  dentro, mientras los impactos de fuera quedan apagados. Esa es la imagen del **tráfico correcto**,
  no del más visitado.

Por qué cuenta «llegar a muy pocos, pero a los correctos» de un vistazo: un blanco es la imagen
universal de **acertar**, no de **disparar mucho**; el contraste entre la pared salpicada (muchos
impactos, ninguno vale) y las cinco marcas del centro (pocas, todas valen) dice, sin una palabra, que
**el valor está en dar, no en llenar**. La metáfora convive con los otros recursos del sistema sin
competir: **demostración** (barra de búsqueda, anuncio, marcador) y **animación tipográfica** (el
`6 €`, el `4/5`, el `2` de ofertas). **Un foco dominante por escena.**

**Tres alternativas descartadas (y por qué):**

1. **El haz de luz / el foco que se cierra.** Una luz que pasa de iluminar a todos a iluminar cinco
   es bonita, pero un haz muestra **concentración**, no acierto: puede alumbrar cualquier grupo. No
   distingue «los correctos» de «los pocos», y sobre escenas de búsqueda se lee como el cliché del
   *searchlight* detrás del buscador.
2. **La criba / el embudo.** Colar el grano para quedarse con el oro describe **volumen filtrado**, y
   eso contradice justo la tesis: aquí no hace falta una montaña de búsquedas para quedarse con unas
   pocas, basta con elegir bien. Además es un proceso pasivo (algo cae y se cuela), no una decisión.
3. **La autopista y la salida.** Es la lectura más literal de «tráfico» (coches) y arrastra un set
   pesado y ajeno a la pieza (asfalto, vehículos), que tira por tierra el lienzo de anuncios de
   búsqueda; y solo dice «tráfico», pierde «correcto».

---

## 2. Paleta por escena (hex)

La paleta es la del contrato. **No se introduce ningún token nuevo.** Los dos temas son la variante
clara (papel) y la oscura (carbón); el cambio de tema cae **sobre una transición**, nunca a mitad de
escena.

| token | oscuro | claro | uso |
|---|---|---|---|
| `bg` | `#0a0a0f` | `#f4f1ea` | lienzo |
| `panel` | `#20202a` (**mínimo**) | `#ffffff` | paneles, tarjetas, barras |
| `line` | `#26262e` | `#e0dbcf` | bordes 2-5 px y anillos del blanco |
| `ink` | `#f5f5f7` | `#14141a` | texto principal y anillo del centro |
| `muted` | `#8b8b99` | `#6f6f78` | rótulos, anotaciones, impactos dispersos |
| `accent` | `#c8ff3d` | `#c8ff3d` | **único acento** (solo relleno) |
| `accent-ink` | `#0b0b10` | `#0b0b10` | tinta sobre el acento |
| `warn` | `#ff5a5a` | `#b3161b` | **sin usar** (la pieza no tiene error real) |

**Reparto por escena** (`claro` = papel `#f4f1ea` con retícula de puntos; `oscuro` = degradado
`#0a0a0f` con halo de acento):

| Beat | Tema | Colores propios (hex) | Por qué |
|---|---|---|---|
| B1 gancho | **claro** `#f4f1ea` | barra `#20202a`/`#26262e` · lupa `#6f6f78` · placa `6 €` `#c8ff3d`/`#0b0b10` · anillos `#e0dbcf` | fotograma 0 = miniatura: luminancia medida ≈ 222/255 |
| B2 el caso | **claro** | tarjeta `#ffffff`/`#e0dbcf` · año `#14141a` · nombre `#14141a` · chip `#20202a`/`#26262e` | la cifra y el nombre se leen sobre papel |
| B3 el mecanismo | **oscuro** `#0a0a0f` | marca `#14141a` sobre tarjeta `#ffffff` · barra `#20202a`/`#26262e` · anuncio `#c8ff3d`/`#0b0b10` | la marca y el anuncio brotan sobre carbón |
| B4 la selección | **claro** | filas `#20202a`/`#26262e` · casilla vacía `#6f6f78` · casilla marcada `#c8ff3d`/`#0b0b10` | la lista de nombres se lee mejor sobre papel |
| B5 el anuncio | **claro** | tarjeta anuncio `#ffffff`/`#e0dbcf` · resaltado `#c8ff3d`/`#0b0b10` · barra `#20202a` | el anuncio, sobre claro como en un buscador |
| B6 el resultado | **claro** | cifra `#14141a` · placa ofertas `#c8ff3d`/`#0b0b10` · rótulo `#6f6f78` | el marcador de aciertos |
| B7 la lección | **oscuro** | anillos `#26262e` · centro `#f5f5f7` · cinco marcas `#c8ff3d` · dispersos `#8b8b99` | la multitud se apaga y quedan las cinco |
| B8 tu versión | **claro** | cinco `#c8ff3d` · puente `#6f6f78` · tarjeta «tu negocio» `#20202a`/`#26262e` | el puente al negocio del espectador |
| B9 la práctica | **claro** | filas `#20202a`/`#26262e` · tachado `#14141a` · lupa `#14141a` · ideal `#c8ff3d`/`#0b0b10` | términos y lupa sobre papel |
| B10 la práctica | **claro** | pista `#e0dbcf` · barras `#c8ff3d` · etiqueta `#6f6f78` | la gráfica corta sobre papel |
| B11 cierre | **oscuro** `#0a0a0f` | centro `#c8ff3d`/`#0b0b10` · cinco marcas `#0b0b10` · dispersos `#8b8b99` · marcador `#c8ff3d` | cierre de serie: el blanco encendido |

**Contrastes a vigilar** (los valida `check`, WCAG AA): el relleno verde `#c8ff3d` **siempre lleva
`#0b0b10` encima** y **nunca va como texto ni trazo sobre claro** (≈1,3:1); por eso el logotipo de
Google y el **tachado** de los términos genéricos son **tinta**, y las **marcas correctas** del blanco
son **puntos rellenos** de acento (relleno, no trazo), como el `.dot` del kicker. `muted` en claro =
`#6f6f78`. **La pieza no usa `warn`.**

---

## 3. Tipografía

- **Inter** (400/600/700/800/900) + **JetBrains Mono** (600/800) para lo que representa algo que se
  **escribe o se busca** (la consulta tecleada, los nombres, los términos genéricos). Es el par del
  sistema.
- **Niveles** (todo tamaño del CSS cae dentro de una banda; el carril «rótulos» recoge el texto
  pequeño):
  - **Protagonista 110-180**: la cifra **`6 €`** (B1, 150 px), el año **`2010`** (B2, 180 px) y el
    marcador **`4/5`** (B6, 170 px).
  - **Frase principal 70-110**: «Guarda esto» (B11, 96).
  - **Logotipo de marca 57-69**: la marca tipográfica `Google` (B3/B5, 64 px, `.brandmark`).
  - **Contexto 38-56**: `.adtext` (48), `.genterm`/`.pname` (44-46), `.bl` de «tu negocio» (52),
    `.idealtag` (46), `.scorelab`/`.blab` (32-38).
  - **Rótulos y mono 22-37**: kicker **32 fijo**, `.adlab` (26-28), `.chip` (36), `.pick .pname`
    (44 → en la banda de contexto), `.statlab` (38), anotaciones del blanco (24-30), mayúsculas y
    `letter-spacing:0.28em` en el kicker.
- **Frase larga no se encoge: se redistribuye.** Ninguna línea pasa de **14 palabras** (las de 14 son
  B3 y B9, por texto del dueño, y no se encogen): cada una es **un solo beat**, y la animación se
  reparte a lo largo de su duración en vez de resolverse en el primer segundo.
- **Criterio de rótulos:** frases nominales en mayúsculas, **sin numerar** (como V5/V6), porque el
  contenido no es una secuencia de pasos. Se registra como decisión (§10).
- Medir el texto **después de `document.fonts.ready`** (el ancho del logotipo y de las etiquetas
  depende de la longitud medida).

---

## 4. Familias de composición (5)

Una familia de composición cada 8-12 s (`DESIGN.md`: «30-45 s: 4-5»): para ~38,4 s tocan **4-5**, y
la pieza usa cinco.

1. **El blanco (la mira)** — el retículo de anillos con las marcas: `.blanco` + `.marca`/`.disperso`.
   · **B1, B7, B11**.
   Es la familia de la metáfora: la estrena (B1, la búsqueda sobre el blanco), la lleva al clímax
   (B7, la multitud que se reduce a cinco) y la cierra encendida (B11, el centro correcto).
2. **La búsqueda y el anuncio** — la barra de búsqueda y el anuncio que brota: `.searchbar` +
   `.adrow`/`.adcard`. · **B3, B5**.
   Es la familia del mecanismo: el anuncio aparece **solo** al buscar el nombre correcto (B3) y luego
   se lee su texto (B5).
3. **La ficha del caso** — la tarjeta con dato + rótulo: `.card` + `.yearbadge`/`.nameplate` (B2) y
   `.bizcard` (B8). · **B2, B8**.
   Es la familia que fija el dato (quién y cuándo) y la que lo traslada al negocio del espectador.
4. **La lista de la selección** — filas alineadas con una marca: `.picklist` (B4) y `.scoreboard`
   (B6). · **B4, B6**.
   Es la familia de «cuáles» y «cuántos»: los cinco nombres elegidos y el recuento del resultado.
5. **La práctica dirigida** — dos términos y una herramienta que apunta: `.genrow` + `.lupa` (B9) y
   `.barchart` (B10). · **B9, B10**.
   Es la familia de la aplicación: dónde no disparar (B9) y qué poco pero qué bueno (B10).

**Reparto por beat:** B1(1) · B2(3) · B3(2) · B4(4) · B5(2) · B6(4) · B7(1) · B8(3) · B9(5) ·
B10(5) · B11(1). Cinco familias, ninguna escena con dos familias a la vez.

---

## 5. Profundidad y encuadre

- **Desplazamiento global con compensación por capas** (2,5D): en B7 el blanco baja ~30 px mientras
  las cinco marcas se quedan (fondo 0 · anillos +30 · marcas +60).
- **Aproximación suave 1 → 1,04** al completar la idea: B4 (la última casilla marcada) y B10 (la
  última barra se asienta).
- **Cambio de foco (acercamiento fuerte):** B1 (la cifra `6 €` entra de golpe y manda), B3 (el
  anuncio brota sobre la barra) y B9 (la lupa se corre hasta el centro del blanco).
- **El texto nunca rota y nunca pasa de 1,15×.** Las inclinaciones (≤ 8°) son solo para los impactos
  dispersos de B7 (±3°). Las formas grandes fuera de cuadro solo existen en el barrido, con contraste
  menor que el contenido.
- **Sombras de contacto** en la barra de búsqueda (B1, B3), la tarjeta del caso (B2), el anuncio
  (B5), la lista (B4) y la CTA (B11).

---

## 6. Transiciones

Las **seis familias** están disponibles (decisión del dueño, `DESIGN.md`). Se usan **cuatro**; `forma`
y `circle` quedan disponibles. `DESIGN.md` fija «un mecanismo distinto cada 10-12 s» (30-45 s:
**3-4**): a ~38,4 s la pieza usa **cuatro** (más el corte final). La que necesita **pieza propia**
está marcada con **(P)**.

| familia | implementación | ¿pieza propia? | dónde |
|---|---|---|---|
| **Desplazamiento continuo** (`slide`) | tween `y` sobre las dos `.s-in`, misma dirección con solape | no | B1→B2, B3→B4, B4→B5, B5→B6, B7→B8, B8→B9, B9→B10 |
| **Continuidad por forma** (`forma`) | tween `y+scale` sobre `.s-in` | no | *(disponible)* |
| **Barrido de color** (`sweep`) | banda de acento 40 % de alto, `skewX(-12deg)`, `z-index:40` | **(P) `.sweep`** | B6→B7 |
| **Objeto que cubre** (`cover`) | panel `#20202a` que crece hasta tapar y despeja | **(P) `.cover`** | B2→B3 |
| **Revelado circular** (`circle`) | `clip-path` sobre `.s-in`, `r ≥ 1500` (cubre esquinas) | no (recorte) | *(disponible)* |
| **Corte directo** (`cut`) | sin cruce | no | B10→B11 |

**Reparto:** primaria `slide` en **7 de 10** cortes (70 %); acentos: `cover`, `sweep` (**2**), cada
uno en una bisagra de cambio de tema; el corte final (B10→B11) es directo. Duraciones 0,35-0,45 s,
ajustadas a la escena.

**Plan de cortes (con duración):**

| Corte | Familia | Dur. | Nota |
|---|---|---|---|
| B1→B2 | slide ↑ | 0,35 | mismo tema claro; entra la tarjeta del caso |
| B2→B3 | **cover** (P) | 0,45 | **claro → oscuro**: el panel `#20202a` crece desde la tarjeta del caso |
| B3→B4 | slide ↑ | 0,45 | **oscuro → claro**; `slide` sustituye al recorte circular (acentos a 2) |
| B4→B5 | slide ↑ | 0,40 | — |
| B5→B6 | slide ↑ | 0,35 | — |
| B6→B7 | **sweep** (P) | 0,45 | **claro → oscuro**: banda de acento; entra la escena del blanco |
| B7→B8 | slide ↑ | 0,40 | **oscuro → claro**; revisar el fotograma medio |
| B8→B9 | slide ↑ | 0,40 | — |
| B9→B10 | slide ↑ | 0,40 | — |
| B10→B11 | **cut** | 0,00 | **claro → oscuro**; corte directo (sin cruce) |

**Coste de las piezas propias (asumido):**

- **`.cover` (B2→B3):** DOM nuevo de la escena B2 (`#s2-cover`), `inset:0`, `background:#20202a`,
  `z-index:40`, `transform:scale(0)` con origen en la tarjeta del caso; crece `scale 0→1` (tween
  escrito a mano, con la duración entera de la transición). Se revisa su **fotograma intermedio**.
- **`.sweep` (B6→B7):** DOM nuevo de la escena **saliente** B6 (`#s6-sweep`), banda de 40 % de alto,
  `z-index:40`. **Trampa medida en V5:** el CSS arranca con `translateX(-130%)`, así que GSAP lo lee
  como `x`; hay que poner **`x: 0` explícito en el `fromTo`** o `xPercent` solo llega a
  `translateX(0)` y **la banda tapa el cuadro entero**. Un barrido es **una banda, nunca `inset:0`**.

`transiciones.py` extiende las colas (`data-duration += d`) y acepta cualquier nombre de tipo en `TR`;
ningún `<audio>` se toca.

---

## 7. Reglas de la pieza

1. **El escenario nace visible.** La barra / tarjeta / blanco / lista / anuncio / panel de cada escena
   existe desde `t=0` y solo se asienta con `rise()`; **nunca** se anima la opacidad del escenario.
2. **Un foco dominante por escena.** Nada compite con el objeto que explica la línea (el blanco es
   fondo salvo en B7 y B11, donde es el protagonista).
3. **El acento es relleno**, con `accent-ink` encima; **nunca como texto ni trazo sobre fondo claro**.
   **La pieza no usa rojo** (`warn`): no hay pérdida ni error real, así que el tachado de los términos
   genéricos (B9) va en **tinta**. Nunca dos acentos compitiendo.
4. **Los números no suben.** El `6 €` (B1), el `4/5` (B6) y el `2` de ofertas (B6) se fijan con
   `setNum(sel, txt, t)` en un salto discreto; prohibido contar hacia arriba.
5. **Seek-safe.** Estado inicial en CSS; animar con `fromTo` / `.to()`. Sin `.from()`, `Math.random`,
   `Date.now`, `repeat` ni `yoyo`.
6. **La animación no dura más que su escena** y cierra antes del corte.
7. **La transición ES la salida**: no se anima nada «hacia fuera» salvo el último fotograma.
8. **Ningún texto repite la voz**; los rótulos son nominales y cortos.
9. **Nada de la lista de vetos** (§4 del brief): ni «cafetera», ni «instalación de luz», ni la SERP
   etiquetada de V5, ni la balanza de V6, ni la burbuja de `mkt-01`, ni las aperturas gastadas.
10. **Todo elemento nuevo trae su CSS** (clase, medidas, colores) en §8, para que se implemente sin
    interpretar nada.

---

## 8. Elementos nuevos (CSS)

Todo es CSS + SVG inline (sin imágenes externas). Reutilizados del kit: `.scene`, `.s-in`, `.kicker`
(+`.dot`), `.card`, `.chip`, `.pill`, `.rowc`, `.rowline`, `.stage`, `.cta-mark`/`.cta-label`/
`.savewave`, `.progress`/`#prog-fill`. **Nuevos:**

```css
/* ---- base de la pieza: panel nunca por debajo de #20202a ---- */
:root { --panel:#20202a; --accent:#c8ff3d; --accent-ink:#0b0b10; }
/* banda segura 15%-75% de 1920 (288-1440): 300 arriba, 700 abajo (contrato 470; mismo margen
   más conservador que mkt-01, para no quedar bajo la píldora del karaoke — ver STORYBOARD) */
.s-in { position:absolute; inset:0; display:flex; flex-direction:column; justify-content:center;
        align-items:stretch; gap:24px; padding:300px 74px 700px; }

/* ===================== EL BLANCO (la metáfora) =====================
   Anillos concéntricos. El centro se marca con el anillo de tinta; en el cierre, el centro
   se RELLENA de acento (zona correcta). El acento nunca va como trazo: el centro es relleno. */
.blanco { position:absolute; left:50%; top:50%; width:860px; height:860px;
          margin:-430px 0 0 -430px; z-index:1; pointer-events:none; }
.blanco svg { width:100%; height:100%; display:block; }
.blanco .ring       { fill:none; stroke:var(--line);   stroke-width:3; }
.blanco .ring.inner { fill:none; stroke:var(--muted);  stroke-width:3; }
.blanco .core       { fill:none; stroke:var(--ink);    stroke-width:6;
                      transform-box:fill-box; transform-origin:center; }
.blanco.correct .core { fill:var(--accent); stroke:none; }
.blanco .cross      { stroke:var(--line); stroke-width:2; }     /* retícula de la mira */

/* las pocas marcas correctas (acento = «lo correcto») y los muchos impactos dispersos (apagados).
   Nacen a escala 0 y se encienden con `put(...,{scale:1,stagger:...})`: estado inicial en CSS. */
.marca    { width:40px; height:40px; border-radius:50%; background:var(--accent);
            transform:scale(0); transform-origin:center; }
.blanco.correct .marca { background:var(--accent-ink); }         /* tinta sobre el centro de acento */
.disperso { width:20px; height:20px; border-radius:50%;
            background:var(--muted); opacity:0.5; transform:scale(0); transform-origin:center; }
/* rejillas deterministas (sin aleatoriedad): la multitud y las cinco marcas */
.crowd  { display:grid; grid-template-columns:repeat(8, 46px); gap:22px;
          justify-content:center; width:100%; }
.crowd .disperso { justify-self:center; }
.cinco  { display:grid; grid-template-columns:repeat(3, 56px); gap:22px;
          justify-content:center; width:100%; }
.cinco .marca { justify-self:center; }

/* ---- B1/B3/B5: la barra de búsqueda (recurso propio de la pieza) ---- */
.searchbar { position:relative; display:flex; align-items:center; gap:18px;
             width:100%; max-width:840px; margin:0 auto; padding:24px 28px;
             border-radius:20px; background:var(--panel); border:3px solid var(--line);
             box-shadow:0 24px 60px rgba(0,0,0,0.28); }
.searchbar .sicon { flex:0 0 auto; width:46px; height:46px; color:var(--muted); }
.searchbar .sicon svg { width:100%; height:100%; display:block; }
.searchbar .sterm { flex:1; font-family:"JetBrains Mono",monospace; font-size:44px;
             font-weight:600; color:var(--ink); white-space:pre; }
.searchbar .scaret { flex:0 0 auto; width:4px; height:56px; background:var(--ink); }
.searchbar .shint  { font-family:"Inter",sans-serif; font-size:40px; color:var(--muted); }

/* la cifra-cifra del gancho: acento de relleno con tinta encima */
.eurmark { display:inline-flex; align-items:center; padding:14px 40px; border-radius:26px;
           background:var(--accent); color:var(--accent-ink);
           font-size:150px; font-weight:900; letter-spacing:-0.03em; line-height:1; }

/* ---- B2: la ficha del caso (año + nombre) ---- */
.yearbadge { font-family:"Inter",sans-serif; font-size:180px; font-weight:900;
             letter-spacing:-0.04em; line-height:1; color:var(--ink); }
.nameplate { font-family:"Inter",sans-serif; font-size:56px; font-weight:800;
             letter-spacing:-0.01em; line-height:1.1; color:var(--ink); }
.monogram  { width:132px; height:132px; border-radius:50%; background:var(--panel);
             border:3px solid var(--line); display:flex; align-items:center; justify-content:center;
             font-size:52px; font-weight:900; letter-spacing:0.04em; color:var(--ink); }

/* ---- marca de la plataforma: logotipo TIPOGRÁFICO, tinta sobre tarjeta clara (sin @, sin red) --- */
.brandmark { display:inline-flex; align-items:center; padding:18px 34px; border-radius:14px;
             background:#ffffff; border:3px solid var(--line);
             font-family:"Inter",sans-serif; font-size:64px; font-weight:900; letter-spacing:0.01em;
             color:#14141a; }
.brandmark.sm { font-size:44px; padding:12px 24px; }

/* ---- B3: el anuncio que brota sobre la barra ---- */
.adrow { position:relative; display:flex; align-items:center; gap:18px;
         width:100%; max-width:840px; margin:0 auto; padding:20px 26px; border-radius:16px;
         background:var(--accent); color:var(--accent-ink); }
.adrow .adlab { font-size:28px; font-weight:800; letter-spacing:0.18em; text-transform:uppercase; }
.adrow .adtxt { font-size:38px; font-weight:700; }

/* ---- B4: la lista de los cinco nombres que se marcan ---- */
.picklist { display:flex; flex-direction:column; gap:16px; width:100%; }
.pick { position:relative; display:flex; align-items:center; justify-content:space-between;
        gap:20px; padding:20px 26px; border-radius:16px; background:var(--panel);
        border:3px solid var(--line); }
.pick .pname { font-family:"JetBrains Mono",monospace; font-size:44px; font-weight:600; color:var(--ink); }
.pickbox { position:relative; flex:0 0 auto; width:58px; height:58px; border-radius:14px;
        border:3px solid var(--muted); }
.pickfill { position:absolute; inset:-3px; border-radius:14px; background:var(--accent);
        display:flex; align-items:center; justify-content:center; }        /* acento relleno */
.pickfill svg { width:38px; height:38px; color:var(--accent-ink); }

/* ---- B5: la tarjeta del anuncio y el texto resaltado ---- */
.adcard { position:relative; width:100%; padding:28px 30px; border-radius:20px;
          background:#ffffff; border:3px solid var(--line); display:flex;
          flex-direction:column; gap:16px; box-shadow:0 24px 60px rgba(0,0,0,0.22); }
.adcard .adlab { font-size:26px; font-weight:800; letter-spacing:0.18em; text-transform:uppercase;
          color:var(--muted); }
.adcard .adtext { font-size:48px; font-weight:800; line-height:1.22; color:#14141a; }
.hl { background:var(--accent); color:var(--accent-ink); padding:0 12px; border-radius:10px;
      display:inline-block; transform-origin:left center; }   /* resaltado: acento relleno + tinta */

/* ---- B6: el marcador del resultado ---- */
.scoreboard { display:flex; align-items:flex-end; justify-content:center; gap:64px; }
.scorebig { display:flex; flex-direction:column; align-items:center; gap:14px; }
.scorenum { font-size:170px; font-weight:900; letter-spacing:-0.04em; line-height:1; color:var(--ink); }
.scorebig.accent .scorenum { background:var(--accent); color:var(--accent-ink);
          border-radius:26px; padding:0 30px; display:inline-block; }     /* acento relleno + tinta */
.scorelab { font-size:32px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase;
          color:var(--muted); }

/* ---- B7/B11: el rótulo de la multitud y el de las cinco ---- */
.crowdlabel { font-size:30px; font-weight:700; letter-spacing:0.24em; text-transform:uppercase;
          color:var(--muted); text-align:center; }
.fivelabel { display:inline-flex; align-items:center; padding:12px 26px; border-radius:999px;
          background:var(--accent); color:var(--accent-ink); font-size:34px; font-weight:900;
          letter-spacing:0.06em; }                                        /* acento relleno + tinta */

/* ---- B8: el puente y la tarjeta «tu negocio» ---- */
.bridge { width:100%; height:150px; color:var(--muted); }
.bridge svg { width:100%; height:100%; display:block; }
.bridge svg path { fill:none; stroke:currentColor; stroke-width:6; stroke-linecap:round; }
.bizcard { width:420px; padding:28px 30px; border-radius:24px; background:var(--panel);
          border:3px solid var(--line); display:flex; flex-direction:column; align-items:center;
          gap:16px; }
.bizcard .bizic { width:92px; height:92px; color:var(--ink); }
.bizcard .bl { font-size:52px; font-weight:900; letter-spacing:-0.01em; color:var(--ink); }

/* ---- B9: los términos genéricos, el tachado y la lupa ---- */
.genrow { position:relative; display:flex; align-items:center; justify-content:space-between;
          gap:20px; padding:18px 26px; border-radius:16px; background:var(--panel);
          border:3px solid var(--line); }
.genterm { font-family:"JetBrains Mono",monospace; font-size:46px; font-weight:600; color:var(--ink); }
.strike { position:absolute; inset:0; color:var(--ink); }      /* tachado en tinta, NO rojo */
.strike svg { width:100%; height:100%; display:block; }
.strike svg path { fill:none; stroke:currentColor; stroke-width:8; stroke-linecap:round; }
.lupa { position:relative; width:240px; height:240px; color:var(--ink); }
.lupa svg { width:100%; height:100%; display:block; }
.lupa svg circle { fill:none; stroke:currentColor; stroke-width:8; }
.lupa svg path { fill:none; stroke:currentColor; stroke-width:12; stroke-linecap:round; }
.idealtag { display:inline-flex; align-items:center; padding:16px 32px; border-radius:999px;
          background:var(--accent); color:var(--accent-ink); font-size:46px; font-weight:900;
          letter-spacing:-0.01em; }                                       /* acento relleno + tinta */

/* ---- B10: la gráfica de barras corta (relleno con `bar`, escalaX) ---- */
.barchart { display:flex; flex-direction:column; gap:24px; width:100%; }
.brow { position:relative; height:58px; border-radius:12px; background:var(--line); overflow:hidden; }
.bfill { height:100%; border-radius:12px; background:var(--accent);
         transform:scaleX(0); transform-origin:left center; }             /* barras en acento */
.blab { font-size:28px; font-weight:700; letter-spacing:0.14em; text-transform:uppercase;
         color:var(--muted); }

/* ---- piezas propias de transición ---- */
.cover { position:absolute; inset:0; z-index:40; background:#20202a; transform:scale(0);
         transform-origin:50% 62%; pointer-events:none; }
.sweep { position:absolute; left:0; right:0; top:30%; height:40%; z-index:40;
         background:var(--accent); transform:translateX(-130%) skewX(-12deg); pointer-events:none; }

/* ---- estados iniciales (seek-safe) ---- */
.fade-in { opacity:0; }        /* contenido que nace oculto y se revela con put()/grow()/typeWords() */
```

**Posiciones (ids, absolutas dentro de `.stage`):**

```css
/* B1: la búsqueda sobre el blanco (escena sin tarjeta) */
#s1-blank  { position:absolute; left:50%; top:44%; margin:-430px 0 0 -430px; }
#s1-search { position:relative; z-index:3; }
#s1-eur    { position:absolute; right:64px; top:-70px; z-index:5; }  /* la cifra, colgada de la barra */
#s1-label  { position:relative; z-index:4; }
/* B7: el blanco con la multitud y las cinco marcas (escena sin tarjeta) */
#s7-blank  { position:absolute; left:50%; top:50%; margin:-430px 0 0 -430px; }
#s7-crowd  { position:absolute; left:50%; top:32%; width:760px; margin-left:-380px; z-index:2; }
#s7-five   { position:absolute; left:50%; top:50%; width:360px; margin:-110px 0 0 -180px; z-index:3; }
#s7-labA   { position:absolute; left:0; right:0; top:72%; z-index:4; }
#s7-labB   { position:absolute; left:0; right:0; top:72%; z-index:4; }
/* B9: la lupa, centrada en la tarjeta (sin retícula de fondo) */
#s9-lupa   { position:absolute; left:50%; top:56%; margin:-120px 0 0 -120px; z-index:5; }
/* B11: el blanco encendido, detrás de la CTA (escena sin tarjeta) */
#s11-in    { align-items:center; }
#s11-blank { position:absolute; left:50%; top:50%; margin:-430px 0 0 -430px; z-index:1; }
#s11-five  { position:absolute; left:50%; top:50%; width:360px; margin:-110px 0 0 -180px; z-index:2; }
#s11-note  { position:relative; z-index:4; }
```

**z-index:** 0 fondo · 1 retícula/blanco de fondo (`.blanco`) · 2 gráficos de apoyo (multitud, cinco,
puente, gráfica) · 3 protagonista (barra, anuncio, tarjeta, lista, marcador, lupa) · 4 texto y
anotaciones · 5 primer término (la cifra `6 €`, la lupa) · 25 barra de progreso · 30 karaoke · 40
capa de transición (`.cover`/`.sweep`). Las escenas de B2 y B6 llevan `z-index:5` para que su pieza de
transición (`.cover` en B2, `.sweep` en B6) quede por encima de la escena siguiente durante el cruce.

---

## 9. Riesgos y mitigación

1. **Verde ilegible sobre claro** → el acento nunca como texto/trazo en claro; el logotipo de Google y
   el tachado van en tinta; la cifra `6 €`, el resaltado, el marcador de resultado, la etiqueta
   «ideal» y las marcas del blanco usan **relleno de acento con `#0b0b10` encima**; validar con
   `check`.
2. **El blanco contra el contenido** → en **B1** el retículo es **fondo** (z-index 1, contraste bajo,
   anillos en `--line`); en **B7 y B11** el blanco es protagonista y el contenido se reduce a las
   marcas. Solo aparece en escenas **sin tarjeta opaca** (una `.card` taparía el retículo): nunca
   compite con la barra ni con la lista.
3. **Cruces claros/oscuros (B2→B3, B3→B4, B6→B7, B7→B8, B10→B11)** → cada escena tiene escenario
   visible desde `t=0`; B2→B3 cubre con panel `#20202a`; B3→B4 entra con `slide`; B6→B7 lleva la banda
   con **`x:0` explícito**; B10→B11 es un corte directo. Revisar los fotogramas medios con
   `verificar_montaje.py` (tramo sin contenido ≤ 0,15 s).
4. **El fotograma 0 (B1) es la miniatura** → la barra, la cifra `6 €`, el rótulo «EN GOOGLE ADS» y el
   kicker están visibles desde `t=0`, sin desvanecidos; solo se asientan con `rise()`. Medir
   luminancia y % de filas con contenido (≥ 200/255 y ≈ 100 %).
5. **El logotipo de Google** → es un **logotipo tipográfico** (tinta `#14141a` sobre tarjeta clara
   `#ffffff`), sin arroba, sin imagen de red y sin sugerir afiliación (§5 del brief).
6. **Duraciones reales ≠ estimadas** → la tabla de ritmo va calculada a **3,2 pal./s** (`mkt-01`);
   los tiempos definitivos los fija `voice_pipeline.py` y los aplica `retime.py`. Toda la animación
   está en tiempos **relativos** al inicio de su beat.
7. **Fuentes de red** → las `woff2` ya están vendorizadas; medir tras `document.fonts.ready`.

---

## 10. Decisiones

1. **Metáfora (resuelto):** el blanco (dar en el centro). Descartados el haz de luz, la criba y la
   autopista (§1).
2. **Metáfora distinta de las series anteriores (resuelto):** no se reutiliza la burbuja de `mkt-01`,
   la SERP etiquetada de V5 ni la balanza de V6; el recurso propio es **el blanco** con sus marcas.
3. **El rojo no se usa (resuelto):** la pieza no tiene pérdida ni error real; el tachado de
   «abogado»/«dentista» (B9) marca algo que *no conviene*, y va en tinta. `warn` queda sin usar.
4. **El foco se cierra en cinco, no en uno (resuelto):** la pieza defiende *pocos pero correctos*
   (cinco personas), así que el centro del blanco acumula **cinco** marcas, no una.
5. **La marca se representa como logotipo tipográfico (resuelto):** tinta `#14141a` sobre tarjeta
   clara `#ffffff`, sin arroba ni imagen de red (§5 del brief).
6. **Rótulos nominales, sin numerar (resuelto):** los kickers siguen los nombres de beat de
   `SCRIPT.md` (GANCHO, EL CASO, EL MECANISMO, LA SELECCIÓN, EL ANUNCIO, EL RESULTADO, LA LECCIÓN,
   TU VERSIÓN, LA PRÁCTICA, LA PRÁCTICA; B11 no lleva kicker).
7. **Transiciones (resuelto):** primaria `slide` (7/10, 70 %) + `cover`, `sweep` como acentos (**2**);
   el corte final B10→B11 es directo; `forma` y `circle` disponibles.
8. **Ejemplo único (resuelto):** «abogado»/«dentista» (B9), de `SCRIPT.md`; no repite «cafetera» (V5)
   ni «instalación de luz» (V6) ni los demás ejemplos gastados.
9. **El blanco se rellena de acento solo en el cierre (resuelto):** en B1 y B7 el centro es un anillo
   de tinta; en **B11** el centro se rellena de acento con las cinco marcas en tinta, para que la
   última imagen diga «aquí está lo correcto» sin una palabra.
10. **El lenguaje 2D entra cuando la voz nombra (resuelto):** personajes y entornos se dibujan con
   **SVG en línea** (plano, dos colores + acento) y aparecen en el instante que fija `cue()` —el mismo
   reparto por longitud que el karaoke—, con entradas ≤0,3 s; se prefieren figuras a rótulos y cajas
   (§12). El mapeo palabra→elemento está declarado en §12.
11. **B4 nombra a las personas por su nombre de pila (resuelto):** la lista de los cinco directores
   creativos se rotula con **David, Tony, Gerry, Ian, Scott** en lugar de sus apellidos (Droga,
   Granger, Graf, Reichenthal, Vitrone). El motivo es de **lectura en español**: «Droga» se lee como
   la palabra que ya se sabe y distrae; el apellido no aporta y sí estorba. El **nombre de pila**
   conserva que son **personas reales** sin esa mala lectura. Son los nombres de pila reales de los
   cinco directores creativos (David Droga, Tony Granger, Gerry Graf, Ian Reichenthal y Scott
   Vitrone). **No cambia** el nombre tecleado de B3 ni el de la búsqueda de B5 («Scott Vitrone»),
   porque ahí el mecanismo es buscar el nombre y apellido de una persona.
12. **El sonido cuelga del cue del elemento, no del arranque de escena (resuelto):** un efecto que
   acompaña a un elemento entra **en el mismo instante** que ese elemento (su cue), no al empezar su
   escena. Los efectos se declaran en `assets/sfx/events.json` con `"cue": ["palabra", ocurrencia]`
   (+ `"offset"` opcional para el desfase propio del elemento, p. ej. el carácter *i* de un tecleo o
   una línea que se dibuja 0,3 s después); el tecleo de B3 también cuelga del cue de la palabra que
   se teclea («buscan»), con un `offset` por carácter. Solo los elementos que **no** se movieron al
   rehacerse la pieza (los colocados con `at(n, local)`) siguen anclados con `"local"`. El
   modo cues de `.openhands/tools/sfx.py` es **retrocompatible**: solo se activa si el evento declara
   `"cue"`, de modo que V6 y MK1 (que usan `"local"`) no cambian. Así, **si un cue se mueve, su sonido
   se mueve con él**: reapuntar la pieza o retimar la voz no vuelve a desincronizar el sonido.
   Si un efecto necesita sonar unas milésimas antes por el ataque del sonido, nunca supera **40 ms**;
   el valor por defecto es coincidencia exacta (offset 0).

---

## 11. Implementación y orden de la cadena

- **Contenedores separados** para no pisar transformaciones: `.pos` (posición y tamaño) → `.move`
  (movimiento principal) → `.sub` (movimiento secundario, 6-12 px o 1-2°) → `.mask` (recorte). El
  nombre `.slot` ya existe en la serie y es otra cosa; no se reutiliza.
- **Las transiciones animan `.s-in`**, nunca el clip; `.cover`/`.sweep` son DOM nuevo de la escena y
  van a `z-index:40`.
- **Karaoke y progreso** se mantienen tal cual (barra con pista oscura y relleno de acento).
- **Orden obligatorio tras tocar escenas o línea de tiempo:**
  `retime.py` → `transiciones.py` → `check` → render. Después, `verificar_montaje.py`.
- **Revisión final** (checklist en `STORYBOARD.md`): un fotograma de lectura por escena, los instantes
  intermedios de `cover` y `sweep`, entradas y salidas, alineación, sincronía con la voz y el
  MP4 completo en movimiento.

---

## 12. Lenguaje 2D — personajes y entornos (heredable)

**Regla de la línea:** cuando la voz **nombra** a alguien o algo, entra en pantalla **una figura o una
escena dibujada**, no un rótulo. La pieza prefiere **generación de personajes y entornos** antes que
cajas, cartelas y letras sueltas; el texto en pantalla queda solo para lo que la voz **no** dice
(la cifra `6 €`, la marca, el año) o para fijar una frase clave.

### Cómo se dibujan

- **HTML `<svg>` en línea + CSS**. Nada de imagen de red, nada de bitmap, nada de banco de assets:
  todo determinista y compatible con el avance fotograma a fotograma.
- **Plano y geométrico**, sin degradados ni texturas, **legible a tamaño pequeño** y con **un solo
  foco** por escena. Todas las figuras usan `fill="currentColor"` y heredan el color de su contenedor;
  `aria-hidden="true"` y sin texto dentro (el rótulo, si hace falta, va fuera).
- **Dos colores + acento.** El cuerpo va en `ink` (tinta clara sobre oscuro, tinta oscura sobre
  claro); el detalle (corbata, cuello, respaldo de silla, cruces del retículo) en `muted`. El acento
  **nunca es la figura entera salvo dentro de una zona de acento**: las cinco personas del cierre
  (B7/B8/B11) van en `--accent` como **relleno** cuando están sobre el núcleo del blanco, con
  `--accent-ink` encima (`.blanco.correct .gente { color: var(--accent-ink) }` cuando el núcleo es de
  acento; el relleno va por `fill: currentColor`). Nunca hay texto sobre estas figuras.

### Piezas y medidas

| pieza | viewBox | uso / tamaño | color |
|---|---|---|---|
| `.gente` (persona, cabeza + torso) | `0 0 64 64` — `circle r12 cy20` + `path` de hombros | cinco correctos (B7/B8/B11) y respondedores (B6), a **52 px** | `ink`/`muted`; `accent-ink` dentro del núcleo |
| `.fig` (figura de cuerpo entero) | `0 0 120 200` — **5 variantes** distintas por atributo (gafas + corbata, pelo, moño + gafas, chistera, cuello) | 5 directores (B3) a **100 px**; filas (B4) a **54 px**; cliente (B9) a **60 px** | `ink` + `muted` |
| `.fig.al` (Alec, `--fig-w` propio) | `0 0 140 210` | protagonista dentro de la redacción (B2), a **150 px** | `ink` + `muted` |
| `.office` / `.officebg` (redacción de agencia) | `0 0 900 460` — ventana con skyline, escritorio, silla, lámpara | fondo de la tarjeta del caso (B2), a ancho completo de la tarjeta (alto 460 px) | skyline `muted`, mobiliario `ink`/`line` |
| `.crowd .disperso` (impacto) | `0 0 64 64` | multitud de la pared (B7) | `muted` (se apaga a 0,14) |

Todas las figuras de una escena se alinean a la misma línea de suelo y comparten escala; ninguna
sobresale de la tarjeta ni pisa la banda de karaoke (el contenido de `.s-in` termina en
`padding-bottom:700px`, y la píldora vive a `bottom:470`).

### Cuándo entran (regla de cues)

Cada elemento **nombrado por la voz** se ancla con el helper `cue(línea, palabra, [ocurrencia])`:

```
cue(n, word, occ) = S[n-1] + (clip[n] · Σlen(palabras anteriores) / Σlen(línea))
```

Es el **mismo reparto proporcional por longitud que usa el karaoke**
(`caption-pill-karaoke.html`): el instante local de una palabra pesa por su longitud sobre el total de
la línea. El elemento entra **≤0,3 s** después de ese instante, con `put()` (`fromTo` de opacidad/`y`/
`scale`), de modo que **la voz lo trae**: primero se oye la palabra, en seguida llega la figura. La
segunda ocurrencia de una palabra repetida (p. ej. «tráfico» en B11) se pide con `occ=2`.

**Anclas declaradas** (instante absoluto = inicio de línea + posición ponderada de la palabra):

| línea | palabra que la voz dice | elemento que entra | instante |
|---|---|---|---|
| L2 | «Alec» | personaje de Alec + oficina | 4,075 s |
| L2 | «Brownstein» | nombre en pantalla | 4,380 s |
| L2 | «publicista» | tarjeta «PUBLICISTA» | 5,220 s |
| L2 | «2010» | año | 6,213 s |
| L3 | «directores» | los cinco directores | 7,830 s |
| L3 | «buscan» | se teclea el nombre | 9,356 s |
| L3 | «mismos» | brota el anuncio | 10,010 s |
| L4 | «cinco» | primera fila de la lista | 11,530 s |
| L4 | «nombres» | nota «SOLO ESOS NOMBRES» | 14,417 s |
| L5 | «anuncio» | tarjeta del anuncio | 15,040 s |
| L5 | «Contratarme» | resaltado | 18,329 s |
| L6 | «llamaron» | 4 respondedores + marcador 4/5 | 20,704 s |
| L6 | «dos» | marcador «2 ofertas» | 21,645 s |
| L7 | «esas» | cinco personas encendidas | 24,632 s |
| L7 | «cinco» | rótulo «ESAS CINCO» | 24,885 s |
| L8 | «mismo» | las cinco cruzan | 25,451 s |
| L8 | «vale» | puente | 25,764 s |
| L8 | «negocio» | tarjeta «TU NEGOCIO» | 26,389 s |
| L9 | «abogado» / «dentista» | término + tachado | 27,934 / 28,587 s |
| L9 | «piensa» | lupa | 29,305 s |
| L9 | «cliente» | cliente ideal + etiqueta | 30,545 s |
| L10 | «mejores» | «TUS MEJORES CLIENTES» | 33,982 s |
| L11 | «tráfico» (2.ª) | cinco personas sobre el núcleo | 37,852 s |
| L11 | «correcto» | nota «EL TRÁFICO CORRECTO» | 38,318 s |

### Sonido (misma regla que la imagen)

**Un efecto que acompaña a un elemento se ata al cue de ese elemento, no al arranque de su escena.**
El sonido entra **en el mismo instante** que la figura; nunca antes. Si el cue se mueve (reapuntado de
la pieza, retimado de la voz), **su sonido se mueve con él**.

En `assets/sfx/events.json` se declara con `"cue": ["palabra", ocurrencia]`; el instante se calcula con
el **mismo reparto por longitud** que `cue()` (`S[n-1] + clip[n]·Σlen_previas/Σlen_línea`), así que
imagen y sonido no pueden desincronizarse. El tecleo carácter a carácter de B3 se ata al cue de la
palabra que se escribe («buscan»), con un `offset` por carácter (paso de 45 ms); los efectos que
acompañan a elementos que **no** se movieron al rehacerse la pieza (los colocados con `at(n, local)`)
siguen anclados con `"local"` (segundos desde el inicio de escena). El campo opcional `"offset"` añade
el desfase propio del elemento dentro de su cue (p. ej. el carácter *i* de un tecleo con paso de 45 ms,
o la línea de tachado que se dibuja 0,3 s después de oír el término).

Criterio de ajuste: **coincidencia exacta** por defecto; un efecto puede ir unas milésimas antes por el
ataque del sonido, pero **nunca más de 40 ms**. Esto se apoya en el modo cues **retrocompatible** de
`.openhands/tools/sfx.py`: solo se activa cuando el evento declara `"cue"`, de modo que las piezas que
usan `"local"` (p. ej. V6, MK1) no cambian.

### Choques con el contrato y cómo se resuelven

- **«Un solo acento por escena» (contrato §2).** Los cinco de B7/B8/B11 y las casillas de B4 usan el
  acento que **ya tenía** la escena (las marcas del blanco, las casillas): no añaden un segundo
  acento. Los cuatro respondedores de **B6** se dibujan en **`ink`/`muted`**, no en acento, para no
  competir con el marcador «2 OFERTAS» (el único acento de esa escena).
- **«El acento siempre relleno con `accent-ink` encima» / verde prohibido como trazo (contrato §2).**
  Las figuras de acento son **relleno puro sin texto** (igual que las `.marca` que ya existían); en
  ningún caso hay texto o trazo verde sobre claro. El detalle va en `muted` (`#6f6f78` en claro),
  nunca en acento.
- **Panel oscuro mínimo (contrato §2).** La ventana de la redacción (B2) es **claro sobre claro**
  (`--panel`/`--bg`), nunca un bloque oscuro; el cielo no baja de `--bg` (`#f4f1ea`).
- No hay más contradicciones: el estado inicial sigue en CSS (`transform:scale(0)` estático, sin
  `transition`/`@keyframes`), las entradas usan `put()`/`fromTo`, el escenario nace visible con
  `rise()` y no se toca `.from()`, `Math.random`, `Date.now` ni `repeat`/`yoyo`.

## Regla de sonido (2026-10-14)

Los efectos que acompanan a un elemento se atan al cue de ese elemento, no al arranque de la escena: si el
cue se mueve, el sonido se mueve con el. Los whoosh de transicion se atan al instante visual del corte
(medido, no nominal). Y el criterio de aceptacion se mide sobre el render final, nunca sobre la composicion:
se comprueba con la herramienta de la casa medir_sync.py, que detecta los ataques de sonido en sfx.wav y los
cambios reales de imagen en el MP4. Objetivos: cortes |audio-imagen| <= 0,04 s y cues por zona <= 0,06 s.
Medido en esta pieza: 10 cortes de 10 y 21 cues de 21 dentro de objetivo.
