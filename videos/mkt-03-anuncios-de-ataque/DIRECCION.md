# DIRECCIÓN DE ARTE — mkt-03 «Anuncios de ataque (Basecamp, 2019)»

Aplica el brief del dueño (`DIRECCION-ARTE-BRIEF.md`) y el contrato de producción heredado
(`videos/seo-06-canibalizacion/investigacion/03-contrato.md`). Serie **Casos de estudio marketing** ·
Pieza **mkt-03** · **11 beats · 119 palabras · ≈37,2 s** · 1080×1920 · voz en off es-ES (`Pablo`) ·
subtítulos karaoke · barra de progreso. Formato y lenguaje visual calcados de
`videos/mkt-02-google-ads-trafico-correcto/DIRECCION.md`.

---

## 1. Dirección elegida: «tu nombre y las vallas de delante»

**Metáfora central.** Tu marca es un **rótulo**: una placa con tu nombre sobre un poste, a la vista de
quien viene a leerla. Delante de ese rótulo se alquilan **vallas** publicitarias: **quien paga se pone
entre tú y quien venía a por tu nombre**. Un **anuncio de ataque** es la **valla de un rival plantada
delante de tu rótulo**; la **defensa** es pagar la valla de delante de **tu propio nombre** para que no
la ocupe otro. La calle (el que llega buscando) es la **búsqueda**; las vallas son los **anuncios**; el
rótulo es **tu resultado**.

La metáfora **reaparece a lo largo de toda la pieza**:

- **B1** la estrena **tapada**: el rótulo de la marca va **censurado** (barras de tinta y un `?`) — «esta
  empresa» sin nombre, intriga pura.
- **B2** la escenifica: una **figura rival clava su valla** delante del rótulo ajeno; los **clientes** que
  iban al rótulo son interceptados por la valla.
- **B5** la mide: al buscar el propio nombre, **cuatro vallas** de competidores **se apilan por delante**
  (arriba) del rótulo propio. Es la imagen central del dato.
- **B7** la lleva al espectador: el montaje **se refleja** sobre **tu** rótulo — a ti pueden hacerte lo
  mismo.
- **B8** la resuelve: **tu valla propia** (en acento) ocupa el sitio de delante; una **puja** paga por él.
- **B9** la cierra con la protesta: Basecamp **usa su propia valla** para protestar.
- **B10** la completa: sin puja, la valla ajena se queda el sitio y **se lleva los clics**.

**Por qué cuenta «ataque y defensa» de un vistazo:** un rótulo con vallas **por delante** dice, sin una
palabra, que **alguien se ha puesto entre tú y tu cliente**; y que ese sitio **se alquila** (se paga)
explica por qué **el que no paga lo pierde**. La metáfora convive con los otros recursos del sistema sin
competir: **demostración** (barra de búsqueda, vallas apiladas, anuncio-protesta) y **animación
tipográfica** (el contador `4`, el año `2019`, el titular del anuncio). **Un foco dominante por escena.**

**Mapeo metáfora ↔ interfaz.** «Por delante» se dibuja **por encima**, porque así aparece en la página
de resultados y porque `SCRIPT.md` lo fija («cuatro anuncios de rivales **arriba**»): la barra de
búsqueda arriba, la **pila de vallas** debajo, y el **rótulo propio** al pie. El rótulo **no es una
tienda física** (Basecamp es software): es el **rótulo de la marca**, un pictograma de señalética, no un
comercio.

**Tres alternativas descartadas (y por qué):**

1. **La subasta de la esquina (la puja como imagen central).** Una pala que puja por el sitio explica
   muy bien el *cómo* (el anuncio es una subasta) pero no el *resultado*: no muestra a nadie **entre tú
   y tu cliente**. Además la línea 10 ya dice «pujar»; hacer de la subasta la metáfora entera reduciría
   la pieza a jerga. **Se conserva como capa secundaria** (`.puja` en B8 y B10), no como imagen central.
2. **La placa de la puerta.** Un nombre en la puerta y un rival pegando su placa encima. Es fuerte en
   «tu nombre» pero **flojo en «clientes»**: no enseña al cliente desviado, que es justo la pérdida
   («robando clientes», «clics que ya eran tuyos»).
3. **La cola de la ventanilla.** Clientes en fila que vienen por tu nombre y un rival que **se cuela**.
   Se entiende «pagar por un sitio», pero una cola dramatiza **esperar**, no **elegir**, y una búsqueda
   es instantánea. Además el que se cuela se lee como **falta de educación**, no como **publicidad**.
4. (descartada también) **El cartel tapado con una lona.** Tapar tu rótulo dice «ataque» pero no dice
   «defensa = paga tu propio nombre»; se queda a medias.

---

## 2. Paleta por escena (hex)

La paleta es la del contrato. **No se introduce ningún token nuevo.** Los dos temas son la variante
clara (papel) y la oscura (carbón); el cambio de tema cae **sobre una transición**, nunca a mitad de
escena.

| token | oscuro | claro | uso |
|---|---|---|---|
| `bg` | `#0a0a0f` | `#f4f1ea` | lienzo |
| `panel` | `#20202a` (**mínimo**) | `#ffffff` | rótulos, vallas, palas, tarjetas |
| `line` | `#26262e` | `#e0dbcf` | bordes 2-5 px y la acera |
| `ink` | `#f5f5f7` | `#14141a` | texto principal, postes, censura |
| `muted` | `#8b8b99` | `#6f6f78` | rótulos, detalle, postes de apoyo |
| `accent` | `#c8ff3d` | `#c8ff3d` | **único acento** (solo relleno) |
| `accent-ink` | `#0b0b10` | `#0b0b10` | tinta sobre el acento |
| `warn` | `#ff5a5a` | `#b3161b` | **solo en B10** (el clic que ya no es tuyo) |

**Reparto por escena** (`claro` = papel `#f4f1ea`; `oscuro` = degradado `#0a0a0f` con halo de acento):

| Beat | Tema | Colores propios (hex) | Por qué |
|---|---|---|---|
| B1 gancho | **claro** `#f4f1ea` | acera `#e0dbcf` · rótulo censurado `#ffffff`/`#14141a` · foco `#6f6f78` al 18 % · titular `#14141a` | fotograma 0 = miniatura: luminancia medida ≈ 230/255 |
| B2 la emboscada | **oscuro** `#0a0a0f` | rótulos `#20202a`/`#26262e` · figura rival `#8b8b99` · valla ajena `#20202a` · clientes `#f5f5f7` | la emboscada, de noche |
| B3 el mecanismo | **oscuro** | marca `#14141a` sobre `#ffffff` · barra `#20202a`/`#26262e` · valla `#20202a` · chip `#f5f5f7` | la plataforma y el brote de la valla |
| B4 la empresa | **claro** | rótulo `#ffffff`/`#e0dbcf` · marca `#14141a` · año `#14141a` · censura que cae `#14141a` | la marca se desvela sobre papel |
| B5 el dato | **oscuro** | barra `#20202a` · **cuatro vallas `#20202a`/`#26262e`** · rótulo propio `#ffffff` · contador `#20202a`/`#f5f5f7` | la pila de vallas ajenas sobre el carbón |
| B6 por qué | **claro** | rótulos `#20202a`/`#26262e` · cliente `#14141a`/`#6f6f78` · focos `#6f6f78` al 18 % | el cliente eligiendo, sobre papel |
| B7 el reflejo | **oscuro** | marco `#20202a`/`#26262e` · brillo `#26262e` · vallas reflejadas `#20202a` · rótulo «tu negocio» `#ffffff` | el puente al negocio del espectador |
| B8 la defensa | **claro** | rótulo `#ffffff` · pala `#20202a`/`#14141a` · **valla propia `#c8ff3d`/`#0b0b10`** | el único acento: tu valla en el sitio |
| B9 la protesta | **claro** | valla `#20202a`/`#26262e` · titular `#f5f5f7` · **resaltado `#c8ff3d`/`#0b0b10`** · marca `#14141a` sobre `#ffffff` | el anuncio se lee sobre papel |
| B10 la consecuencia | **oscuro** | rótulo `#ffffff` · pala vacía `#8b8b99` (trazo discontinuo) · valla ajena `#20202a` · **clics perdidos `#ff5a5a`** | la pérdida real: único `warn` |
| B11 cierre | **claro** | buscador `#20202a` · vallas ajenas `#20202a` · **valla propia `#c8ff3d`/`#0b0b10`** · «Guarda esto» `#14141a` | cierre: tu nombre, con tu valla delante |

**Contrastes a vigilar** (los valida `check`, WCAG AA): el relleno verde `#c8ff3d` **siempre lleva
`#0b0b10` encima** y **nunca va como texto ni trazo sobre claro** (≈1,3:1). Por eso la marca y el
titular del anuncio son **tinta**, la **valla propia** (B8) y el **resaltado** del anuncio-protesta (B9)
son **relleno de acento con `#0b0b10` encima**, y las **vallas ajenas** son **panel oscuro**. `muted` en
claro = `#6f6f78`; el `warn` de B10 solo se usa en tema oscuro (`#ff5a5a`), nunca en claro.

---

## 3. Tipografía

- **Inter** (400/600/700/800/900) para todo el texto; **JetBrains Mono** (600/800) para lo que
  representa algo que se **escribe o se busca** (el nombre tecleado, el nombre del rival). Las marcas
  (`Basecamp`, `Google`) van como **logotipo tipográfico** en Inter 900.
- **Niveles** (todo tamaño del CSS cae dentro de una banda):
  - **Protagonista 110-180**: el **titular del gancho** (B1, 132 px, `.hookline`), el año **`2019`**
    (B4, 180 px) y el **contador `4`** (B5, 120 px).
  - **Frase principal 70-110**: «Guarda esto» (B11, 96).
  - **Logotipo de marca 44-64**: `.brandmark` de `Basecamp` y `Google` (64 px; 44 en formato `.sm`).
  - **Contexto 38-56**: el **rótulo** (`.rotulo`, 52) · el **titular del anuncio** (`.quote`, 56) ·
    el **nombre tecleado** (`.sterm`, 44) · el **texto de valla** (`.vallatxt`, 40).
  - **Rótulos y mono 22-37**: kicker **32 fijo**, `.vallalab` (26), `.chip` (36), `.pill` (34),
    `.tag` (30); mayúsculas y `letter-spacing:0.28em` en el kicker.
- **Ninguna línea pasa de 14 palabras** (las de 14 son B3 y B11, por texto del dueño, y no se encogen):
  cada una es **un solo beat**, y la animación se reparte a lo largo de su duración en vez de resolverse
  en el primer segundo.
- **Criterio de rótulos:** frases nominales en mayúsculas, **sin numerar** (como V5/V6/mkt-02). Se
  registra como decisión (§10).
- Medir el texto **después de `document.fonts.ready`** (el ancho del logotipo y de los rótulos depende
  de la longitud medida).

---

## 4. Familias de composición (5)

Una familia de composición cada 8-12 s (`DESIGN.md`: «30-45 s: 4-5»): para ~37,2 s tocan **4-5**, y la
pieza usa cinco.

1. **El rótulo (la marca)** — la placa con el nombre sobre su poste, con o sin censura: `.rotulo`
   (+`.redact`) y la **calle**. · **B1, B4, B7, B11**.
   Es la familia de la metáfora: la estrena tapada (B1), la desvela (B4), la refleja en el espectador
   (B7) y la cierra defendida (B11).
2. **La búsqueda apilada** — la barra de búsqueda y la **pila de vallas** por encima del rótulo:
   `.searchbar` + `.vallas`. · **B3, B5**.
   Es la familia del mecanismo y del dato: la valla que brota al buscar un nombre (B3) y **cuatro**
   vallas ajenas sobre el propio (B5).
3. **La emboscada** — la valla ajena **delante** del rótulo y las figuras que la ejecutan o la sufren:
   `.valla.rival` + `.fig`/`.gente`. · **B2, B10**.
   Es la familia del robo: el rival que clava su valla (B2) y los clics que se van con ella (B10).
4. **La encrucijada** — el cliente entre dos opciones: `.gente` + dos `.rotulo` enfrentados. · **B6**.
   Es la familia de «por qué funciona»: quien busca una marca está comparando y a punto de elegir.
5. **La defensa y la protesta** — la puja y la valla propia: `.puja` + `.valla.propia`/`.protesta` +
   `.quote`. · **B8, B9**.
   Es la familia de la aplicación: pagar por tu nombre (B8) y usar tu propia valla para protestar (B9).

**Reparto por beat:** B1(1) · B2(3) · B3(2) · B4(1) · B5(2) · B6(4) · B7(1) · B8(5) · B9(5) ·
B10(3) · B11(1). Cinco familias, ninguna escena con dos familias a la vez.

---

## 5. Profundidad y encuadre

- **Desplazamiento global con compensación por capas** (2,5D): en **B5** la pila de vallas baja ~24 px
  mientras el rótulo propio se queda (aire 0 · vallas +24 · rótulo +48): el rótulo queda **detrás** de
  las vallas, que es exactamente la idea.
- **Aproximación suave 1 → 1,04** al completar la idea: B5 (la cuarta valla se asienta) y B9 (el titular
  se cierra entre comillas).
- **Cambio de foco (acercamiento fuerte):** B1 (el foco cae sobre el rótulo censurado y manda el
  titular), B9 (la valla-protesta con el titular) y B10 (la valla ajena que se lleva los clics).
- **El texto nunca rota y nunca pasa de 1,15×.** Las inclinaciones (≤ 8°) son solo para el **brillo** del
  reflejo (B7, ±18° en una banda plana). Las formas grandes fuera de cuadro solo existen en el barrido,
  con contraste menor que el contenido.
- **Sombras de contacto** en el rótulo (B1, B4, B7-B11), las vallas (B2, B3, B5, B9-B11), la puja (B8,
  B10) y el reflejo (B7).

---

## 6. Transiciones

Las **seis familias** están disponibles (decisión del dueño, `DESIGN.md`). Se usan **cuatro**; `forma` y
`circle` quedan disponibles. `DESIGN.md` fija «un mecanismo distinto cada 10-12 s» (30-45 s: **3-4**): a
~37,2 s la pieza usa **cuatro** (más el corte final). La que necesita **pieza propia** va marcada **(P)**.

| familia | implementación | ¿pieza propia? | dónde |
|---|---|---|---|
| **Desplazamiento continuo** (`slide`) | tween `y` sobre las dos `.s-in`, misma dirección con solape | no | B2→B3, B3→B4, B4→B5, B5→B6, B7→B8, B8→B9 |
| **Continuidad por forma** (`forma`) | tween `y+scale` sobre `.s-in` | no | *(disponible)* |
| **Barrido de color** (`sweep`) | banda de acento 40 % de alto, `skewX(-12deg)`, `z-index:40` | **(P) `.sweep`** | B6→B7 |
| **Objeto que cubre** (`cover`) | panel `#20202a` que crece hasta tapar y despeja | **(P) `.cover`** | B1→B2, B9→B10 |
| **Revelado circular** (`circle`) | `clip-path` sobre `.s-in`, `r ≥ 1500` (cubre esquinas) | no (recorte) | *(disponible)* |
| **Corte directo** (`cut`) | sin cruce | no | B10→B11 |

**Reparto:** primaria `slide` en **6 de 10** cortes (60 %); acentos: `cover` (**2**), `sweep` (**1**),
`cut` (**1**). Duraciones 0,35-0,45 s, ajustadas a la escena.

**Plan de cortes (con duración):**

| Corte | Familia | Dur. | Nota |
|---|---|---|---|
| B1→B2 | **cover** (P) | 0,45 | **claro → oscuro**: el panel `#20202a` crece desde el rótulo censurado |
| B2→B3 | slide ↑ | 0,40 | oscuro → oscuro; entra la búsqueda |
| B3→B4 | slide ↑ | 0,40 | **oscuro → claro**; entra la revelación de la marca |
| B4→B5 | slide ↑ | 0,35 | **claro → oscuro**; entra la pila de vallas |
| B5→B6 | slide ↑ | 0,40 | **oscuro → claro**; entra el cliente |
| B6→B7 | **sweep** (P) | 0,45 | **claro → oscuro**: banda de acento; entra el reflejo |
| B7→B8 | slide ↑ | 0,40 | **oscuro → claro** |
| B8→B9 | slide ↑ | 0,40 | claro → claro |
| B9→B10 | **cover** (P) | 0,45 | **claro → oscuro**: el panel crece desde la valla-protesta |
| B10→B11 | **cut** | 0,00 | **oscuro → claro**; corte directo (sin cruce) |

**Coste de las piezas propias (asumido):**

- **`.cover` (B1→B2 y B9→B10):** DOM nuevo de la escena saliente (`#s1-cover`, `#s9-cover`), `inset:0`,
  `background:#20202a`, `z-index:40`, `transform:scale(0)` con origen en el rótulo/valla; crece
  `scale 0→1` con la duración entera de la transición. Se revisa su **fotograma intermedio**.
- **`.sweep` (B6→B7):** DOM nuevo de la escena **saliente** B6 (`#s6-sweep`), banda de 40 % de alto,
  `z-index:40`. **Trampa medida en V5:** el CSS arranca con `translateX(-130%)`, así que GSAP lo lee
  como `x`; hay que poner **`x: 0` explícito en el `fromTo`** o `xPercent` solo llega a
  `translateX(0)` y **la banda tapa el cuadro entero**. Un barrido es **una banda, nunca `inset:0`**.

`transiciones.py` extiende las colas (`data-duration += d`) y acepta cualquier nombre de tipo en `TR`;
ningún `<audio>` se toca.

---

## 7. Reglas de la pieza

1. **El escenario nace visible.** La calle, el rótulo, la barra, la pila de vallas y el marco de cada
   escena existen desde `t=0` y solo se asientan con `rise()`; **nunca** se anima la opacidad del
   escenario.
2. **Un foco dominante por escena.** Nada compite con el objeto que explica la línea.
3. **El acento es relleno**, con `accent-ink` encima; **nunca como texto ni trazo sobre fondo claro**.
   **Nunca dos acentos compitiendo.** El **rojo** aparece **solo en B10** (el clic que ya no es tuyo).
4. **Los números no suben.** El contador `4` (B5) y el año `2019` (B4) se fijan con `setNum` en un salto
   discreto; prohibido contar hacia arriba.
5. **Seek-safe.** Estado inicial en CSS; animar con `fromTo` / `.to()`. Sin `.from()`, `Math.random`,
   `Date.now`, `repeat` ni `yoyo`.
6. **La animación no dura más que su escena** y cierra antes del corte.
7. **La transición ES la salida**: no se anima nada «hacia fuera» salvo el último fotograma.
8. **Cada elemento que la voz nombra entra en su cue** (`cue()`), **≤ 0,3 s**; ningún texto repite la
   voz salvo el gancho (B1) y el titular citado del anuncio (B9).
9. **Nada de la lista de vetos** (§4 del brief): ni «cafetera», ni «instalación de luz», ni la tienda de
   ropa, ni la SERP etiquetada de V5, ni la balanza de V6, ni la burbuja de `mkt-01`, ni el blanco de
   `mkt-02`, ni la barra de un solo anuncio de `mkt-02`, ni las aperturas gastadas.
10. **Todo elemento nuevo trae su CSS** (clase, medidas en píxeles, hex, posición, z-index) en §8.

---

## 8. Elementos nuevos (CSS)

Todo es CSS + SVG inline (sin imágenes externas). Reutilizados del kit: `.scene`, `.s-in`, `.kicker`
(+`.dot`), `.card`, `.chip`, `.pill`, `.tag`, `.stage`, `.searchbar` (+`.sicon`/`.sterm`/`.scaret`),
`.brandmark`, `.yearbadge`, `.hl`, `.cta-mark`/`.cta-label`/`.savewave`, `.progress`/`#prog-fill`,
`.gente`/`.fig` (figuras 2D del lenguaje de la casa). **Nuevos:**

```css
/* ---- base de la pieza: panel nunca por debajo de #20202a ---- */
:root { --panel:#20202a; --accent:#c8ff3d; --accent-ink:#0b0b10; --warn:#ff5a5a; }
/* banda segura 15%-75% de 1920 (288-1440): 300 arriba, 700 abajo (contrato 470; mismo margen
   más conservador que mkt-01/mkt-02, para no quedar bajo la píldora del karaoke — ver STORYBOARD) */
.s-in { position:absolute; inset:0; display:flex; flex-direction:column; justify-content:center;
        align-items:stretch; gap:24px; padding:300px 74px 700px; }

/* ===================== LA CALLE (entorno) =====================
   La acera y el aire. La calle es el «camino» del que llega buscando: plana, de dos colores,
   sin degradados ni texturas. Nunca es un bloque oscuro en tema claro. */
.calle { position:absolute; left:0; right:0; bottom:0; height:560px; z-index:0; pointer-events:none; }
.calle .aire  { position:absolute; left:0; right:0; bottom:170px; top:0; background:transparent; }
.calle .acera { position:absolute; left:0; right:0; bottom:0; height:170px; background:var(--line); }
.calle .borde { position:absolute; left:0; right:0; bottom:170px; height:4px; background:var(--muted); }

/* ===================== EL RÓTULO (la marca) =====================
   Una placa con el nombre sobre un poste. Es el resultado propio de la marca: pictograma de
   señalética, NO una tienda. La marca nombrada va como logotipo tipográfico: tinta #14141a
   sobre tarjeta clara #ffffff, en línea, sin @handle y sin red. */
.rotulo { position:relative; display:inline-flex; flex-direction:column; align-items:center; z-index:3; }
.rotulo .placa { display:inline-flex; align-items:center; justify-content:center; padding:16px 30px;
        border-radius:12px; background:#ffffff; border:3px solid var(--line);
        box-shadow:0 18px 40px rgba(0,0,0,0.24); font-family:"Inter",sans-serif; font-size:52px;
        font-weight:900; letter-spacing:0.01em; color:#14141a; }
.rotulo .poste { width:14px; height:120px; background:var(--muted); }
.rotulo.rival .placa { background:var(--panel); border-color:var(--line); color:var(--ink); } /* marca ajena, anónima */
.rotulo .sub { font-family:"Inter",sans-serif; font-size:30px; font-weight:700; letter-spacing:0.02em;
        color:var(--muted); }

/* La marca del gancho va CENSURADA: barras de tinta y un «?» (nadie sabe qué empresa es). */
.redact { position:absolute; inset:0; display:flex; align-items:center; justify-content:center; gap:16px;
        background:#ffffff; border-radius:12px; transform-origin:left center; z-index:4; }
.redact b { display:block; width:96px; height:28px; border-radius:7px; background:var(--ink); }
.redact b.c { width:56px; }
.redact .q { font-family:"Inter",sans-serif; font-size:56px; font-weight:900; color:var(--ink); }

/* ===================== LA VALLA (el anuncio; recurso propio de la pieza) =====================
   Un cartel rectangular sobre dos postes. Es distinta del rótulo (más ancha y sobre dos postes).
   Varias vallas se apilan «por delante» (arriba) del rótulo propio: el mecanismo del caso. */
.valla { position:relative; width:660px; height:190px; z-index:3; }
.valla .tablon { position:absolute; left:0; right:0; top:0; height:148px; border-radius:14px;
        background:var(--panel); border:3px solid var(--line); box-shadow:0 20px 48px rgba(0,0,0,0.30);
        display:flex; flex-direction:column; justify-content:center; gap:8px; padding:0 28px; }
.valla .poste { position:absolute; bottom:0; width:14px; height:42px; background:var(--muted); }
.valla .poste.l { left:70px; } .valla .poste.r { right:70px; }
.valla .vallalab { font-family:"Inter",sans-serif; font-size:26px; font-weight:800; letter-spacing:0.20em;
        text-transform:uppercase; color:var(--muted); }
.valla .vallatxt { font-family:"JetBrains Mono",monospace; font-size:40px; font-weight:700; color:var(--ink); }
/* tu marca: acento de relleno con accent-ink encima (nunca el acento como texto/trazo suelto) */
.valla.propia .tablon { background:var(--accent); border-color:var(--accent); }
.valla.propia .vallalab, .valla.propia .vallatxt { color:var(--accent-ink); }
/* la protesta: cartel oscuro con el titular citado y su resaltado de acento dentro */
.valla.protesta .tablon { height:210px; }
.valla .quote { font-family:"Inter",sans-serif; font-size:56px; font-weight:800; line-height:1.22;
        color:var(--ink); }

/* La pila de vallas (varias, apiladas por delante del rótulo propio) — B5, B7, B11 */
.vallas { display:flex; flex-direction:column; gap:18px; width:100%; align-items:center; z-index:3; }

/* ===================== LA PUJA (el sitio se alquila) =====================
   La pala del que compra el sitio de delante. `.vacia` = sin postor (trazo discontinuo). */
.puja { position:relative; width:132px; height:186px; z-index:4; }
.puja svg { width:100%; height:100%; display:block; }
.puja .palo  { fill:var(--muted); }
.puja .placa { fill:var(--panel); stroke:var(--ink); stroke-width:5; }
.puja.vacia .placa { fill:none; stroke:var(--muted); stroke-dasharray:16 12; }

/* ===================== EL CLIC (la ficha que venía a por tu nombre) =====================
   Un puntero-cursor. Cuando el sitio lo ocupa la valla ajena, el clic se va con ella y se marca
   en rojo: es el ÚNICO uso de `warn` de la pieza (una pérdida real, B10). */
.clics { display:flex; gap:22px; justify-content:center; z-index:4; }
.clic { width:52px; height:52px; color:var(--ink); }
.clic svg { width:100%; height:100%; display:block; }
.clic svg path { fill:currentColor; }
.clic.perdido { color:var(--warn); }

/* ===================== EL REFLEJO (el puente al negocio del espectador) =====================
   Marco plano que refleja la pila de vallas sobre TU rótulo. Banda de brillo plana (sin degradado). */
.reflejo { position:relative; width:760px; height:520px; border-radius:22px; background:var(--panel);
        border:3px solid var(--line); overflow:hidden; box-shadow:0 24px 60px rgba(0,0,0,0.32); z-index:2; }
.reflejo .brillo { position:absolute; left:-14%; top:-40%; width:56%; height:180%; background:var(--line);
        opacity:0.35; transform:skewX(-18deg); }

/* ===================== EL FOCO (cono de luz plano) =====================
   Neutro (muted), nunca acento: el acento no es luz. Ilumina el rótulo del gancho. */
.foco { position:absolute; width:560px; height:640px; pointer-events:none; z-index:1; }
.foco svg { width:100%; height:100%; display:block; }
.foco .haz { fill:var(--muted); opacity:0.18; }

/* ===================== TITULARES NUEVOS ===================== */
/* El texto del gancho (B1). Única vez que se imprime la voz: lo pide SCRIPT.md y es la miniatura. */
.hookline { font-family:"Inter",sans-serif; font-size:132px; font-weight:900; letter-spacing:-0.02em;
        line-height:1.04; color:var(--ink); text-align:center; z-index:5; }
/* El contador del dato (B5): se FIJA con setNum, nunca cuenta hacia arriba. */
.contador { display:inline-flex; align-items:center; justify-content:center; min-width:150px;
        padding:8px 26px; border-radius:20px; background:var(--panel); border:3px solid var(--line);
        font-family:"Inter",sans-serif; font-size:120px; font-weight:900; letter-spacing:-0.04em;
        line-height:1; color:var(--ink); z-index:4; }

/* ===================== PIEZAS PROPIAS DE TRANSICIÓN ===================== */
.cover { position:absolute; inset:0; z-index:40; background:#20202a; transform:scale(0);
        transform-origin:50% 62%; pointer-events:none; }
.sweep { position:absolute; left:0; right:0; top:30%; height:40%; z-index:40; background:var(--accent);
        transform:translateX(-130%) skewX(-12deg); pointer-events:none; }

/* ---- estados iniciales (seek-safe) ---- */
.fade-in { opacity:0; }   /* contenido que nace oculto y se revela con put()/grow()/typeWords() */
```

**Posiciones (ids, absolutas dentro de `.stage`; medidas en px sobre el lienzo 1080×1920):**

```css
/* B1: el rótulo censurado sobre la acera (escena sin tarjeta) */
#s1-calle   { position:absolute; left:0; right:0; bottom:0; top:0; }
#s1-rotulo  { position:absolute; left:50%; top:38%; margin-left:-210px; z-index:3; }
#s1-foco    { position:absolute; left:50%; top:26%; margin-left:-280px; z-index:1; }
#s1-hook    { position:relative; z-index:5; }
/* B4: la marca desvelada, sobre la acera */
#s4-rotulo  { position:relative; z-index:3; }
#s4-year    { position:absolute; right:60px; top:-30px; z-index:4; }
/* B5: la pila de vallas por encima del rótulo propio (escena sin tarjeta) */
#s5-search  { position:relative; z-index:4; }
#s5-vallas  { position:relative; z-index:3; }
#s5-rotulo  { position:relative; z-index:2; }
#s5-count   { position:absolute; right:64px; top:38%; z-index:5; }
/* B7: el reflejo, centrado (escena sin tarjeta) */
#s7-reflejo { position:absolute; left:50%; top:44%; margin:-260px 0 0 -380px; z-index:2; }
#s7-rotulo  { position:absolute; left:50%; top:70%; margin-left:-200px; z-index:3; }
#s7-vallas  { position:absolute; left:50%; top:30%; width:520px; margin-left:-260px; z-index:3; opacity:0.7; }
/* B8: la puja junto al rótulo */
#s8-puja    { position:absolute; right:56px; top:40%; z-index:5; }
/* B9: la valla-protesta y su titular */
#s9-valla   { position:relative; z-index:3; }
/* B10: la puja vacía y los clics (escena sin tarjeta) */
#s10-puja   { position:absolute; right:56px; top:36%; z-index:5; }
#s10-clics  { position:relative; z-index:4; }
/* B11: el buscador, la pila de vallas y el rótulo propio (escena sin tarjeta) */
#s11-in     { align-items:center; }
#s11-mark   { position:relative; z-index:5; }
#s11-search { position:relative; z-index:4; }
#s11-vallas { position:relative; z-index:3; }
#s11-rotulo { position:relative; z-index:2; }
```

**z-index:** 0 fondo · 1 foco (`.foco`) · 2 marco/reflejo (`.reflejo`) · 3 protagonista (rótulo, valla,
pila, buscador, anuncio) · 4 texto y controles (contador, puja, clics, chip) · 5 primer término
(titular del gancho, marcador de guardado) · 25 barra de progreso · 30 karaoke · 40 capa de transición
(`.cover`/`.sweep`). Las escenas de B1 y B9 llevan `z-index:5` para que su pieza de transición
(`.cover`) quede por encima de la escena siguiente durante el cruce.

---

## 9. Riesgos y mitigación

1. **El gancho sin rótulo.** B1 no lleva kicker ni etiqueta de tema/línea/serie: **solo** el titular del
   gancho y el rótulo censurado. Verificar que el fotograma 0 **se lee solo** (intriga) y que su
   luminancia (≥ 200/255) y % de filas con contenido (≈ 100 %) pasan `verificar_montaje.py`.
2. **Verde ilegible sobre claro** → el acento nunca como texto/trazo en claro; el logotipo tipográfico y
   el titular del anuncio van en tinta; la **valla propia** (B8) y el **resaltado** del protesta (B9)
   usan **relleno de acento con `#0b0b10` encima**; validar con `check`.
3. **El rojo (`warn`).** Solo aparece en **B10** para el clic que ya no es tuyo (una pérdida real,
   contrato §2). No se usa en claro (`#b3161b` queda disponible pero no se necesita). Si el dueño
   prefiere una pieza sin rojo, se sustituye por el clic **apagado** (muted) sin tocar el texto.
4. **La pila de vallas (B5) contra la «SERP etiquetada» de V5.** Nuestra pila **no** tiene resultados
   con título/URL ni etiquetas GUÍA/COMPARATIVA/PRODUCTO: son **cuatro vallas de panel** con la
   etiqueta `ANUNCIO` y, debajo, el **rótulo propio** con el logotipo de Basecamp. Es una escena de
   metáfora, no una captura de resultados.
5. **La barra de búsqueda de `mkt-02`.** Se reutiliza el componente, pero **aquí apila varias vallas**
   por encima (B3 una, B5 cuatro, B11 varias): es el recurso propio de la pieza, no la barra de un solo
   anuncio.
6. **Cruces claros/oscuros (B1→B2, B3→B4, B4→B5, B5→B6, B6→B7, B7→B8, B9→B10, B10→B11)** → cada
   escena tiene escenario visible desde `t=0`; B1→B2 y B9→B10 cubren con panel `#20202a`; B6→B7 lleva la
   banda con **`x:0` explícito**; B10→B11 es un corte directo. Revisar los fotogramas medios con
   `verificar_montaje.py` (tramo sin contenido ≤ 0,15 s).
7. **El logotipo de las marcas** → **logotipo tipográfico** (tinta `#14141a` sobre tarjeta clara
   `#ffffff`), sin arroba, sin imagen de red y sin sugerir afiliación (§5 del brief).
8. **Duraciones reales ≠ estimadas** → la tabla de ritmo va calculada a **3,2 pal./s** (`mkt-01`); los
   tiempos definitivos los fija `voice_pipeline.py` y los aplica `retime.py`. Toda la animación está en
   tiempos **relativos** al inicio de su beat y los cues se recalculan con `cue()`.
9. **Fuentes de red** → las `woff2` ya están vendorizadas; medir tras `document.fonts.ready`.

---

## 10. Decisiones

1. **Metáfora (resuelto):** «tu nombre y las vallas de delante». Descartadas la subasta como imagen
   central (queda como capa), la placa de la puerta, la cola de la ventanilla y el cartel tapado (§1).
2. **Metáfora distinta de las series anteriores (resuelto):** no se reutiliza el blanco de `mkt-02`, la
   burbuja de `mkt-01`, la SERP etiquetada de V5 ni la balanza de V6; el recurso propio es **la valla y
   su pila por delante del rótulo**.
3. **El primer beat es un gancho de curiosidad puro (resuelto, regla vinculante):** B1 lleva **solo el
   titular del gancho** (`SCRIPT.md`: «Solo el texto del gancho») y el rótulo censurado; **sin kicker**,
   sin tema, sin nombre de línea ni de serie. Se registra la excepción al «no repetir la voz».
4. **El rojo se usa una sola vez (resuelto):** en **B10** (la pérdida real: clics que ya no son tuyos).
   En el resto de escenas no hay error ni pérdida y no se usa `warn` (§2/§9).
5. **El rótulo no es una tienda (resuelto):** es un pictograma de **señalética** (placa + poste), para no
   sugerir que Basecamp (software) tiene un comercio. Evita además el eco de la «tienda de ropa» de
   `mkt-01` (§1).
6. **La marca se representa como logotipo tipográfico (resuelto):** tinta `#14141a` sobre tarjeta clara
   `#ffffff`, sin arroba ni imagen de red (§5 del brief).
7. **Rótulos nominales, sin numerar (resuelto):** kickers: B1 **(sin kicker)**, B2 `EL CASO`,
   B3 `EL MECANISMO`, B4 `LA EMPRESA`, B5 `EL DATO`, B6 `POR QUÉ`, B7 `TU VERSIÓN`, B8 `LA PRÁCTICA`,
   B9 `LA PROTESTA`, B10 `LA CONSECUENCIA`, B11 **(sin kicker, CTA)**.
8. **Transiciones (resuelto):** primaria `slide` (6/10, 60 %) + `cover` (B1→B2, B9→B10), `sweep`
   (B6→B7) y `cut` (B10→B11); `forma` y `circle` disponibles (§6).
9. **Ejemplo único (resuelto):** el negocio del espectador, con su propio nombre de marca. El caso
   Basecamp es **prueba**, no segundo ejemplo; no repite «cafetera» (V5), «instalación de luz» (V6), la
   tienda de ropa (`mkt-01`) ni «abogado»/«dentista» (`mkt-02`).
10. **El lenguaje 2D entra cuando la voz nombra (resuelto):** personajes y entornos se dibujan con
    **SVG en línea** (plano, dos colores + acento) y aparecen en el instante que fija `cue()` —el mismo
    reparto por longitud que el karaoke—, con entradas ≤0,3 s. El mapeo palabra→elemento está en §12 y
    la tabla de cues en `STORYBOARD.md`.
11. **El sonido cuelga del cue del elemento (resuelto):** un efecto que acompaña a un elemento entra en
    el **mismo instante** que ese elemento (su cue), declarado en `assets/sfx/events.json` con
    `"cue": ["palabra", ocurrencia]` (+ `"offset"` opcional). Los `whoosh` de transición se atan al
    **instante visual del corte**. Solo los elementos que no se anclan a una palabra usan `"local"`.
12. **La pila se dibuja «por encima» (resuelto):** «por delante» de la metáfora se resuelve **arriba**
    en el encuadre, que es lo que fija `SCRIPT.md` («cuatro anuncios de rivales arriba») y lo que
    conviene a la composición vertical 9:16 (§1).

---

## 11. Implementación y orden de la cadena

- **Contenedores separados** para no pisar transformaciones: `.pos` (posición y tamaño) → `.move`
  (movimiento principal) → `.sub` (movimiento secundario, 6-12 px o 1-2°) → `.mask` (recorte). El nombre
  `.slot` ya existe en la serie y es otra cosa; no se reutiliza.
- **Las transiciones animan `.s-in`**, nunca el clip; `.cover`/`.sweep` son DOM nuevo de la escena y van
  a `z-index:40`.
- **Karaoke y progreso** se mantienen tal cual (barra con pista oscura y relleno de acento).
- **Orden obligatorio tras tocar escenas o línea de tiempo:**
  `retime.py` → `transiciones.py` → `check` → render. Después, `verificar_montaje.py` y `medir_sync.py`.
- **Revisión final** (checklist en `STORYBOARD.md`): un fotograma de lectura por escena, los instantes
  intermedios de `cover` y `sweep`, entradas y salidas, alineación, sincronía con la voz y el MP4
  completo en movimiento.

---

## 12. Lenguaje 2D — personajes y entornos (con la tabla de cues)

**Regla de la línea:** cuando la voz **nombra** a alguien o algo, entra en pantalla **una figura o una
escena dibujada**, no un rótulo. Aquí las figuras son el **cliente** (`.gente`), los **clientes
interceptados** (`.gente`) y la **figura rival** (`.fig`); los entornos son la **calle** (`.calle`), el
**rótulo** (`.rotulo`) y la **valla** (`.valla`). Se dibujan con **HTML `<svg>` en línea + CSS**, planos,
de **dos colores + acento como relleno**, legibles a tamaño pequeño, con `fill="currentColor"` y
`aria-hidden="true"`. Nada de red, nada de bitmap.

### Cuándo entran (regla de cues)

Cada elemento **nombrado por la voz** se ancla con el helper `cue(línea, palabra, [ocurrencia])`:

```
cue(n, word, occ) = S[n-1] + (clip[n] · Σlen(palabras anteriores) / Σlen(línea))
```

Es el **mismo reparto proporcional por longitud que usa el karaoke**. El elemento entra **≤0,3 s**
después de ese instante, con `put()`, de modo que **la voz lo trae**. La **tabla completa de cues**
(palabra → elemento, con su instante estimado) está en `STORYBOARD.md` §«Tabla de cues». Resumen de
anclas declaradas:

| línea | palabra (occ) | elemento que entra |
|---|---|---|
| L2 | «competencia» | la **figura rival** y **su valla** (la emboscada) |
| L2 | «clientes» | los **clientes** interceptados |
| L2 | «nombre» | el **nombre copiado** en la valla ajena |
| L3 | «Google» | el **logotipo** de la plataforma |
| L3 | «ataque» | el término **«ANUNCIOS DE ATAQUE»** |
| L3 | «buscan» | el **nombre del rival** tecleado en el buscador |
| L3 | «rival» | **tu valla** que brota por encima |
| L4 | «Basecamp» | la **marca** (cae la censura) |
| L4 | «2019» | el **año** |
| L5 | «buscar» | el **nombre propio** tecleado |
| L5 | «cuatro» | las **cuatro vallas** de rivales + el **contador `4`** |
| L5 | «competidores» | el rótulo **«DE COMPETIDORES»** |
| L6 | «quien» | el **cliente** que busca |
| L6 | «marca» | las **dos opciones** (dos rótulos) |
| L6 | «comparando» | el **foco doble** (comparación) |
| L6 | «elegir» | el **sesgo del cliente** hacia una opción |
| L7 | «ti» | **tu rótulo** («TU NEGOCIO») |
| L7 | «mismo» | las **cuatro vallas reflejadas** |
| L8 | «defensa» | la etiqueta **«DEFENSA»** |
| L8 | «pagar» | la **puja** |
| L8 | «nombre» | **tu valla propia** (acento) |
| L9 | «Basecamp» | la **marca** en la valla-protesta |
| L9 | «protestar» | la **valla-protesta** |
| L9 | «anuncio» (1) | la etiqueta **«ANUNCIO»** |
| L9 | «No» | el **titular entrecomillado** (palabra a palabra) |
| L9 | «anuncio» (2) | el **resaltado** del titular |
| L10 | «puja» | la **puja vacía** + chip **«SIN PUJA»** |
| L10 | «clics» | las **fichas de clic** |
| L10 | «tuyos» | los clics **se van** con la valla ajena (rojo) |
| L11 | «Guarda» | el **marcador de guardado** + su **onda** |
| L11 | «busca» | el **buscador** con tu nombre |
| L11 | «antes» | las **vallas ajenas** que aparecen antes que tú |

### Sonido (misma regla que la imagen)

**Un efecto que acompaña a un elemento se ata al cue de ese elemento, no al arranque de su escena.** El
sonido entra **en el mismo instante** que la figura; nunca antes. En `assets/sfx/events.json` se declara
con `"cue": ["palabra", ocurrencia]` (+ `"offset"` para el desfase propio del elemento: el carácter de un
tecleo, la palabra de un titular o la línea que se dibuja 0,3 s después). Los **`whoosh` de transición**
se atan al **instante visual del corte** (medido, no nominal). **B1 no tiene cues** (todo está montado en
el fotograma 0), así que sus efectos usan `"local"` —el único caso—. Criterio de ajuste: coincidencia
exacta por defecto; nunca más de 40 ms de adelanto. La tabla de efectos por beat está en `STORYBOARD.md`.

### Choques con el contrato y cómo se resuelven

- **«Un solo acento por escena» (contrato §2).** En B5 las cuatro vallas son **panel** (no acento); en
  B8 el único acento es **tu valla propia**; en B9 el único acento es el **resaltado** del titular. Los
  rótulos y figuras se dibujan en `ink`/`muted`.
- **«El acento siempre relleno con `accent-ink` encima» / verde prohibido como trazo.** La valla propia y
  el resaltado son **relleno puro con `#0b0b10` encima**; nunca hay texto o trazo verde sobre claro. El
  detalle va en `muted` (`#6f6f78` en claro).
- **Panel oscuro mínimo (contrato §2).** La calle es `--line` (claro) o `#26262e` (oscuro) y el lienzo
  `#0a0a0f`; ningún bloque baja de `#20202a`.
- No hay más contradicciones: el estado inicial sigue en CSS (`transform:scale(0)` estático, sin
  `transition`/`@keyframes`), las entradas usan `put()`/`fromTo`, el escenario nace visible con `rise()`
  y no se toca `.from()`, `Math.random`, `Date.now` ni `repeat`/`yoyo`.

## Regla de sonido (2026-10-14)

Los efectos que acompañan a un elemento se atan al cue de ese elemento, no al arranque de la escena: si
el cue se mueve, el sonido se mueve con él. Los whoosh de transición se atan al instante visual del corte
(medido, no nominal). Y el criterio de aceptación se mide sobre el render final, nunca sobre la
composición: se comprueba con la herramienta de la casa `medir_sync.py`, que detecta los ataques de sonido
en `sfx.wav` y los cambios reales de imagen en el MP4. Objetivos: cortes |audio−imagen| ≤ 0,04 s y cues
por zona ≤ 0,06 s. Esta pieza declara **10 cortes** y **32 cues** (ver `STORYBOARD.md`).

**Lección (2026-10-15, mkt-03): el whoosh de cada corte necesita su ajuste, medido sobre el render.** El
instante visual real de la transición no coincide exactamente con el teórico de la tabla `TR`: medido el
render, los `slide` de esta pieza entraban **~80 ms pronto** con el whoosh puesto en su `TR` nominal (y B9
~67 ms tarde). No hay regla fija que lo arregle: **se mide cada whoosh contra su corte y se ajusta su
`local`/`offset` en `events.json`**, del orden de **una a tres centésimas de segundo** por corte. Con ese
ajuste por corte, los desfases `a−i` medidos quedaron: B2 +0,000 · B3 −0,007 · B4 +0,000 · B5 −0,023 ·
B6 +0,007 · B7 −0,033 · B8 −0,023 · B9 −0,003 · B10 −0,023 · B11 +0,037 (10/10 ≤ 0,04 s). Nunca más de
40 ms de adelanto. Los latidos `local` que caen dentro de la transición de entrada de su escena no son
medibles (cambio global): se atan igual al instante visual medido y se dejan como «no fiables».
