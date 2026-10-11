# DIRECCIÓN DE ARTE — V6 «Canibalización de palabras clave»

Aplica el brief del dueño (`DIRECCION-ARTE-BRIEF.md`) y el contrato (`investigacion/03-contrato.md`).
Pieza: **12 beats · 165 palabras · ~41,5 s** · 1080×1920 · voz en off es-ES (`Pablo`) · subtítulos
karaoke · barra de progreso. Formato calcado del de V5 (`seo-05-intencion-de-busqueda/DIRECCION.md`).

---

## 1. Dirección elegida: «la balanza de dos platos (el empate que no se resuelve)»

**Metáfora central.** Una **balanza de dos platos** en la que van tus dos páginas. Google pone el
peso en un plato y luego en el otro; **el fiel oscila, el empate no se resuelve y ninguna de las dos
gana**. La balanza reaparece tres veces y da unidad a la pieza:

- **B2** la presenta: las dos fichas caen en los platos y se empujan (el fenómeno).
- **B4** la deja **empatada** justo cuando llega el nombre del problema.
- **B11** la **vacía**: un plato se queda sin ficha (la regla, «deja solo una»).

Por qué cuenta «**se turnan y ninguna gana**» de un vistazo: dos platos = dos páginas; un fiel que
nunca se queda quieto = **alternancia**; el fiel inclinado = **nadie se queda arriba**; vaciar un
plato = **deja solo una**. Y como *balanza*, añade la lectura de que Google **pesa / compara** tus
dos páginas —justo el matiz de «empate» que pide la línea 4 («siguen empatadas»).

La metáfora se combina con los otros recursos del sistema, sin competir con ella:
**demostración de producto** (ventana, SERP, panel de Search Console) y **animación tipográfica**
(el término gigante al final del gancho). **Un foco dominante por escena.**

**Dos alternativas descartadas (y por qué):**

1. **El balancín / columpio de dos (sube y baja).** Da la misma oscilación, pero se lee como juego,
   no como juicio, y pierde la connotación de **comparar/empatar**; la balanza dice además «Google
   pesa tus dos páginas». Nos quedamos con la balanza.
2. **El partido de ping-pong (la bola va y vuelve sin marcador) o la carrera de relevos.** Se
   descartan por dos motivos: meten objetos ajenos al kit (bola, palas, pista, testigo) y, sobre
   todo, **una carrera o un partido sugieren que existe una meta y un ganador**, que es exactamente
   lo contrario de la tesis. La alternancia se leería como deporte, no como búsqueda.

---

## 2. Paleta (variantes por escena, hex)

La paleta es la del contrato. **No se introduce ningún token nuevo.** Los dos temas son la variante
clara (papel) y la oscura (carbón); el cambio de tema cae siempre **sobre una transición**, nunca a
mitad de escena.

| token | oscuro | claro | uso |
|---|---|---|---|
| `bg` | `#0a0a0f` | `#f4f1ea` | lienzo |
| `panel` | `#20202a` (**mínimo**) | `#ffffff` | paneles, ventanas, tarjetas |
| `line` | `#26262e` | `#e0dbcf` | bordes 2-5 px |
| `ink` | `#f5f5f7` | `#14141a` | texto principal |
| `muted` | `#8b8b99` | `#6f6f78` | rótulos y anotaciones |
| `accent` | `#c8ff3d` | `#c8ff3d` | **único acento** (solo relleno) |
| `accent-ink` | `#0b0b10` | `#0b0b10` | tinta sobre el acento |
| `warn` | `#ff5a5a` | `#b3161b` | solo lo que **pierde** (error real) |
| `chrome` / `field` | `#1c1c24` / `#0e0e14` | `#ffffff` / `#ffffff` | ventana de navegador |
| SERP (claro) | — | `#eef1f5` / `#16181c` | cuerpo de resultados |

**Reparto por escena** (`claro` = papel con retícula de puntos; `oscuro` = degradado con halo de
acento):

| Beat | Tema | Por qué |
|---|---|---|
| B1 gancho | **claro** `#f4f1ea` | fotograma 0 = miniatura: luminancia ≈ 230/255 |
| B2 fenómeno | claro | la balanza se ve sobre papel |
| B3 consecuencia | **oscuro** `#0a0a0f`, panel `#20202a` | la pérdida de posición pesa más en oscuro |
| B4 nombre | claro | el término entra sobre papel limpio |
| B5 matiz | claro | — |
| B6 causa | claro | — |
| B7 ejemplo | claro | las dos ventanas sobre papel |
| B8 resultado | claro | la SERP es un bloque claro por naturaleza |
| B9 cómo verlo | **oscuro** + panel claro `#ffffff` | el panel de Search Console destaca sobre oscuro |
| B10 arreglo | claro | — |
| B11 regla | claro | cierre luminoso antes del CTA |
| B12 CTA | **oscuro** `#0a0a0f` | cierre de serie (marcador en acento) |

**Contrastes a vigilar** (los valida `check`, WCAG AA): verde sobre claro (≈1,3:1) **prohibido** como
texto o trazo → el «tus páginas» de la SERP usa el **relleno tintado `#dff2b0`** con tinta
`#14141a` (como ya hace V5), no el acento puro; `muted` en claro = `#6f6f78`; aviso en claro =
`#b3161b`; **el relleno verde siempre lleva `#0b0b10` encima**.

---

## 3. Tipografía

- **Inter** (400/600/700/800/900) + **JetBrains Mono** (600/800) para lo que representa consulta,
  URL o identificador. Es el par del sistema.
- **Niveles:**
  - **Protagonista 110-180**: el término «CANIBALIZACIÓN» (B4) y la regla «NINGUNA GANA» (B11), ambos
    a **110 px** con `letter-spacing:-0.03em` —el ancho real se fija midiendo tras `document.fonts.ready`,
    con el override `.title` de §8 (la banda útil es 932 px y el término no puede partirse).
  - **Frase principal 70-110**: «DE PALABRAS CLAVE» (B4, 78), «DEJA SOLO UNA» (B11, 96),
    «Guarda esto» (B12, 96).
  - **Contexto 38-56**: títulos de ficha (38), consulta en mono (42), etiquetas y pastillas (44),
    anotaciones (44).
  - **Kicker 32 fijo** (rótulo del sistema), mayúsculas, `letter-spacing: 0.28em`, `muted` con punto.
- **Frase larga no se encoge: se redistribuye.** Ninguna línea de V6 pasa de 14 palabras, así que no
  hace falta partir ningún beat; donde hay dos ideas (B10, «separar… o fusionar…») se resuelven como
  **dos pastillas en dos tiempos** dentro de la misma escena.
- **Criterio de rótulos:** frases nominales en mayúsculas, **sin numerar** —como V5—, porque el
  contenido no es una secuencia de pasos (el «1 · / 2 · / 3 ·» de GA4 numeraba un procedimiento).
  Se registra como decisión (§10).
- Medir el texto **después de `document.fonts.ready`** (los trazos y el ancho de la barra partida
  dependen de la longitud medida).

---

## 4. Familias de composición (5)

Una familia de composición cada 8-12 s (regla proporcional de `DESIGN.md`): para ~41,5 s tocan 4-5.

1. **La balanza del reparto** — `#sN-balance` con dos platos y un fiel que oscila; la barra partida
   (B2) y el marcador de posición (B3, `.ladder` vertical, **sin** `.scale`) cuelgan de ella. ·
   **B2, B4, B11**; **B3** se suma por el marcador de posición de la misma familia.
   Es la familia de la metáfora; enmarca toda la pieza y la cierra. La balanza propiamente dicha solo
   aparece en **B2, B4 y B11** —tres veces, como dice §1—; B1 no la usa (es el turno en la SERP).
2. **El turno en la SERP** — dos resultados **tuyos** en la misma lista y un distintivo «TURNO»
   que salta de uno a otro sin que ninguno suba. · **B1, B8**.
   Se distingue de la SERP de V5 en que aquí no hay etiquetas de intención: el tema es el turno.
3. **Dos fichas, dos dueños** — dos tarjetas / dos ventanas colocadas una frente a otra, cada una
   con su consulta o su dirección. · **B5, B7**.
4. **El solape de la consulta** — dos fichas que convergen hasta superponerse en la misma respuesta;
   la flecha de fusión las vuelve a unir. · **B6, B10**.
5. **El panel y el cierre** — el panel de datos (Search Console) con dos filas iguales y el cierre
   del marcador de guardado. · **B9, B12**.

**Reparto por beat:** B1(2) · B2(1) · B3(1) · B4(1) · B5(3) · B6(4) · B7(3) · B8(2) · B9(5) ·
B10(4) · B11(1) · B12(5). Cinco familias, ninguna escena con dos familias a la vez.

---

## 5. Profundidad y encuadre

- **Desplazamiento global con compensación por capas** (2,5D): en B9 el panel baja ~80 px mientras
  el rótulo se queda (fondo 0 · panel +40 · detalle +80).
- **Aproximación suave 1 → 1,04** al completar la idea: B5 (las fichas se separan) y B11 (una queda
  firme).
- **Cambio de foco (acercamiento fuerte):** B1 (el distintivo «TURNO» salta), B8 (el resalte pasa de
  una ficha a la otra), B10 (la flecha de fusión se dibuja y atrae la mirada).
- **El texto nunca rota y nunca pasa de 1,15×.** Las inclinaciones (≤ 8°) son para las fichas que
  cabalgan en los platos de la balanza (B2) y para las tarjetas que se colocan (B5). Las formas
  grandes fuera de cuadro solo existen en el barrido, con contraste menor que el contenido.
- **Sombras de contacto** en las fichas y los platos (capa propia, más difusa cuanto más «cerca» del
  fondo), en B1-B7 y B10-B11.

---

## 6. Transiciones

Las **seis familias** están disponibles (decisión del dueño, `DESIGN.md`). Se usan **cinco**; `cut`
queda disponible como alternativa gratuita para B11→B12. La que necesita pieza propia está marcada
con **(P)** y su coste se detalla debajo. `DESIGN.md` fija «un mecanismo distinto cada 10-12 s»
(≈3-4 para 30-45 s); V6 usa cinco porque, al ir en el límite alto de la banda (~41,5 s), encadena
cuatro cambios de tema (claro↔oscuro) y dos cambios de idea, y el barrido de acento es la única
familia que resuelve el salto más grande (B8→B9). Se registra como excepción justificada en §10.

| familia | implementación | ¿pieza propia? | dónde |
|---|---|---|---|
| **Desplazamiento continuo** (`slide`) | tween `y` sobre las dos `.s-in`, misma dirección con solape | no | B1→B2, B4→B5, B5→B6, B6→B7, B9→B10, B10→B11, B11→B12 |
| **Continuidad por forma** (`forma`) | tween `y`+`scale` sobre `.s-in` | no | B7→B8 |
| **Barrido de color** (`sweep`) | banda de acento 40 % de alto, `skewX(-12deg)`, `z-index:40` | **(P) `.sweep`** | B8→B9 |
| **Objeto que cubre** (`cover`) | panel que crece hasta tapar y despeja | **(P) `.cover`** | B2→B3 |
| **Revelado circular** (`circle`) | `clip-path` sobre `.s-in`, `r ≥ 1500` (cubre esquinas) | no (recorte) | B3→B4 |
| **Corte directo** (`cut`) | sin cruce | no | *(disponible; no usada — alternativa para B11→B12)* |

**Reparto:** primaria `slide` en **7 de 11** cortes (63,6 %); acentos: `forma`, `cover`, `circle`,
`sweep` (4), cada uno en una bisagra (dos cambios de tema y dos cambios de idea). Duraciones 0,35-0,45 s.

**Plan de cortes (con duración):**

| Corte | Familia | Dur. | Nota |
|---|---|---|---|
| B1→B2 | slide ↑ | 0,35 | mismo tema claro; entra la balanza |
| B2→B3 | **cover** (P) | 0,45 | **claro → oscuro**: el panel oscuro `#20202a` tapa y despeja |
| B3→B4 | **circle** | 0,45 | **oscuro → claro**: el recorte nace en la marca de posición |
| B4→B5 | slide ↑ | 0,40 | — |
| B5→B6 | slide ↑ | 0,35 | — |
| B6→B7 | slide ↑ | 0,40 | — |
| B7→B8 | forma | 0,45 | una ventana «se convierte» en la SERP |
| B8→B9 | **sweep** (P) | 0,45 | **claro → oscuro**: banda de acento a lo ancho |
| B9→B10 | slide ↑ | 0,40 | **oscuro → claro**; revisar el fotograma medio |
| B10→B11 | slide ↑ | 0,35 | — |
| B11→B12 | slide ↑ | 0,40 | **claro → oscuro**; `cut` 0,00 es alternativa |

**Coste de las piezas propias (asumido):**

- **`.cover` (B2→B3):** DOM nuevo de la escena B2 (`#s2-cover`), `inset:0`, `background:#20202a`,
  `z-index:40`, `transform:scale(0)` con origen en la balanza; crece `scale 0→1` y luego `1→1,3`
  (tween escrito a mano). Cada corte se revisa en su **fotograma intermedio**.
- **`.sweep` (B8→B9):** DOM nuevo de la escena B9 (`#s9-sweep`), banda de 40 % de alto, sesgada,
  `z-index:40`. **Trampa medida en V5:** el CSS arranca con `translateX(-130%)`, así que GSAP lo lee
  como `x`; hay que poner **`x: 0` explícito en el `fromTo`** o `xPercent` solo llega a
  `translateX(0)` y **la banda tapa el cuadro entero**. Un barrido es **una banda, nunca `inset:0`**.
- **`circle` (B3→B4):** recorte `clip-path` sobre `#s4-in`; no añade DOM. Radio final **1500 px**
  (> √((1080/2)²+(1920/2)²) ≈ 1102). Nace sobre la marca de posición para que el foco no se pierda.

`transiciones.py` extiende las colas (`data-duration += d`) y acepta cualquier nombre de tipo en `TR`;
ningún `<audio>` se toca.

---

## 7. Reglas de la pieza

1. **El escenario nace visible.** La ventana / tarjeta / panel / balanza de cada escena existe desde
   `t=0` y solo se asienta con `rise()`; **nunca** se anima la opacidad del escenario.
2. **Un foco dominante por escena.** Nada compite con el objeto que explica la línea.
3. **El acento es relleno**, con `accent-ink` encima. **El rojo solo cuando algo pierde** (posición
   que no sube, ficha que se descarta). Nunca dos acentos en la misma escena.
4. **Los números no suben.** La posición de B3 se escribe con `setNum` en saltos discretos
   (`setNum(sel, "8", t)`); prohibido contar hacia arriba. `setNum` se generaliza para aceptar
   selector (en V5 estaba fijado a `#s1-pos`).
5. **Seek-safe.** Estado inicial en CSS (`fade-up`, `pop`, `.tint{opacity:0}` del elemento inactivo),
   animar con `fromTo` / `.to()`. Sin `.from()`, `Math.random`, `Date.now`, `repeat` ni `yoyo`.
6. **La animación no dura más que su escena** y cierra antes del corte.
7. **La transición ES la salida**: no se anima nada «hacia fuera» salvo el último fotograma.
8. **Ningún texto repite la voz**; los rótulos son nominales y cortos.
9. **Nada de la lista de vetos** (§4 del brief): ni «cafetera», ni GUÍA/COMPARATIVA/PRODUCTO, ni las
   cuatro posiciones de V1, ni el lujo de V2, ni Enlaces de V3, ni la SERP como examen de V5.
10. **Todo elemento nuevo trae su CSS** (clase, medidas, colores) en §8, para que se implemente sin
    interpretar nada.

---

## 8. Elementos nuevos (CSS)

Todo es CSS + SVG inline (sin imágenes externas). Reutilizados del kit: `.scene`, `.s-in`, `.kicker`
(+`.dot`), `.card`, `.browser` › `.chrome`/`.lights`/`.addr`/`.lock`, `.serpbody` › `.result`/`.fav`/
`.skel`, `.chip`, `.pill`, `.tag`, `.tile`, `.cursor`, `.cta-mark`/`.cta-label`, `.progress`/
`#prog-fill`, y de GA4 `.panel` › `.phead`/`.prow`. **Nuevos:**

```css
/* ---- base de la pieza: panel nunca por debajo de #20202a ---- */
:root { --panel:#20202a; }            /* el base del sistema es #14141a; aquí se sube al mínimo */
.title { font-size:110px; font-weight:900; letter-spacing:-0.03em; line-height:0.95; }
.title .w { display:inline-block; }  /* spans que se teclean con typeWords(); nunca rotan */

/* ---- B1/B8: el turno en la SERP ---- */
.turnmark { display:inline-flex; align-items:center; padding:8px 20px; border-radius:999px;
            background:var(--accent); color:var(--accent-ink);
            font-size:30px; font-weight:800; letter-spacing:0.08em; text-transform:uppercase; }
.tint { position:absolute; inset:0; border-radius:inherit; background:#dff2b0; opacity:0;
        pointer-events:none; }              /* resalte de «tus páginas» en claro (tinte, no acento) */

/* ---- B1-B11: ficha de página / de resultado ---- */
.pcard { width:340px; background:var(--panel); border:3px solid var(--line); border-radius:22px;
         padding:26px 26px; display:flex; flex-direction:column; gap:14px;
         box-shadow:0 20px 50px rgba(0,0,0,0.45); }
.pcard .fav  { width:48px; height:48px; font-size:24px; }
.pcard .ptitle { font-size:38px; font-weight:800; color:var(--ink); line-height:1.15; }
.pcard .purl { font-family:"JetBrains Mono", monospace; font-size:26px; font-weight:600;
               color:var(--muted); white-space:nowrap; overflow:hidden; }
.pcard.ours  { background:#dff2b0; border-color:#a9c65f; }         /* en claro, como V5 */
.pcard.ours .ptitle { color:#14141a; }
.pcard.ours .purl   { color:#4d5a29; }
.pcard.faded { opacity:0.42; }

/* ---- B2/B4/B11: la balanza de dos platos ---- */
.scale { position:relative; width:760px; height:470px; margin:0 auto; }  /* 2·340 + 80 de aire */
.scale .beam { position:absolute; left:0; right:0; top:150px; height:150px;
               display:flex; align-items:flex-start; justify-content:space-between;
               transform-origin:50% 50%; }                 /* esto rota: ±6° */
.scale .beam .plank { position:absolute; left:0; right:0; top:0; height:16px; border-radius:8px;
               background:var(--ink); }
.scale .seat { position:relative; width:340px; padding-top:26px; }   /* = ancho de .pcard, sin desborde */
.scale .pivot { position:absolute; left:50%; top:158px; transform:translateX(-50%);
                width:0; height:0; border-left:32px solid transparent;
                border-right:32px solid transparent; border-bottom:150px solid var(--line); }
.scale .fiel { position:absolute; left:50%; top:40px; width:8px; height:96px; margin-left:-4px;
               border-radius:4px; background:var(--ink); transform-origin:50% 100%; }

/* ---- B2: la barra que se reparte ---- */
.splitbar { position:relative; display:flex; width:820px; height:66px; margin:0 auto;
            border-radius:16px; overflow:hidden; background:#20202a; }   /* pista ≥ mínimo */
.splitbar .seg { height:100%; flex:1 1 0; }
.splitbar .seg.l { background:#dff2b0;         transform-origin:left center; }  /* tinte, no acento: sobre papel el acento era ≈1,3:1 */
.splitbar .seg.r { background:#45454f;         transform-origin:right center; }
.splitbar .knob { position:absolute; top:-8px; bottom:-8px; left:50%; width:6px;
                  background:var(--ink); border-radius:3px; }

/* ---- B3: escala vertical de posición (lectura de la familia del reparto, sin .scale) ---- */
.ladder { position:relative; width:14px; height:430px; margin:0 auto; border-radius:7px;
          background:#26262e; }                                  /* pista, color de línea */
.ladder .lab  { position:absolute; left:50%; top:-58px; transform:translateX(-50%);
                font-size:32px; font-weight:700; letter-spacing:0.28em; text-transform:uppercase;
                color:var(--muted); white-space:nowrap; }        /* «POSICIÓN» */
.ladder .mark { position:absolute; left:50%; top:0; width:96px; height:38px; margin-left:-48px;
                border-radius:12px; background:#ff5a5a;          /* warn: solo lo que pierde */
                box-shadow:0 12px 28px rgba(0,0,0,0.5); }
.ladder .pos  { position:absolute; left:50%; bottom:-70px; transform:translateX(-50%);
                font-family:"JetBrains Mono",monospace; font-size:48px; font-weight:800;
                color:#ff5a5a; }                                 /* indicador ↓, cambia con setNum */

/* ---- B6/B10: solape y fusión ---- */
.fusearw { display:flex; justify-content:center; color:#4d5a29; }  /* trazo en tinta oscura: B10 es claro */
.fusearw svg { width:560px; height:210px; display:block; }   /* se dibuja con draw() */

/* ---- B9: panel de Search Console (sobre GA4 .panel/.phead/.prow) ---- */
.sctabs { display:flex; gap:10px; padding:0 0 18px; border-bottom:2px solid #d3d8df; }
.sctabs .t { padding:8px 22px; border-radius:999px; font-size:28px; font-weight:700;
             color:#5b6470; background:#e6eaf0; }
.sctabs .t.on { background:#16181c; color:#f5f5f7; }
.prow.dup { background:#dff2b0; color:#14141a;
            box-shadow:inset 4px 0 0 #4d5a29; }              /* relleno teñido + filo oscuro, nunca acento */
#s9-dup { position:absolute; left:24px; top:50%; width:52px; height:230px; margin-top:-115px;
          border:6px solid #4d5a29; border-right:0; border-radius:12px 0 0 12px;
          transform-origin:left center; }                    /* corchete que une las dos filas duplicadas */

/* ---- B12: onda del marcador ---- */
.savewave { position:absolute; inset:-90px; color:var(--accent); }
.savewave svg { width:100%; height:100%; display:block; }

/* ---- piezas propias de transición ---- */
.cover { position:absolute; inset:0; z-index:40; background:#20202a; transform:scale(0);
         transform-origin:50% 62%; pointer-events:none; }
.sweep { position:absolute; left:0; right:0; top:30%; height:40%; z-index:40;
         background:var(--accent); transform:translateX(-130%) skewX(-12deg); pointer-events:none; }

/* ---- escenario de la pieza (banda segura V6: 470 abajo) ---- */
.s-in { position:absolute; inset:0; display:flex; flex-direction:column; justify-content:center;
        align-items:stretch; gap:24px; padding:300px 74px 470px; }
```

**z-index:** 0 fondo · 1 retícula/halo · 2 gráficos de apoyo (balanza, barra partida) · 3
protagonista (fichas, término) · 4 texto y anotaciones · 5 primer término · 25 barra de progreso ·
30 karaoke · 40 capa de transición (`.cover`/`.sweep`). La escena de B2 lleva `z-index:5` para que
su `.cover` quede por encima de B3 durante el cruce.

---

## 9. Riesgos y mitigación

1. **Verde ilegible sobre claro** → el acento nunca como texto/trazo en claro; «tus páginas» usa el
   tinte `#dff2b0`; validar con `check`.
2. **El fiel de la balanza como trazo verde** → el fiel es `var(--ink)`, nunca acento (sería verde
   sobre papel). El acento solo aparece en rellenos (pastillas, tiles, `.fav`).
3. **Cruces claros/oscuros (B2→B3, B8→B9, B9→B10, B11→B12)** → cada escena tiene escenario visible
   desde `t=0`; B2→B3 cubre con panel `#20202a`; B8→B9 lleva la banda con `x:0` explícito;
   B9 mantiene el panel claro sobre oscuro. Revisar los fotogramas medios con
   `verificar_montaje.py` (tramo sin contenido ≤ 0,15 s).
4. **La balanza se desborda o las fichas giran demasiado** → la balanza mide 760 px = 2 platos de
   340 px + 80 de aire; la rotación del beam se limita a ±6° (≤ 8° permitido) y las fichas viven
   dentro de `.seat` (340 px = ancho de `.pcard`), dentro de la banda segura.
5. **Duraciones reales ≠ estimadas** → la estimación de ~41,5 s es de palabra/velocidad; los tiempos
   definitivos los fija `voice_pipeline.py` y los aplica `retime.py`. Toda la animación está en
   tiempos **relativos** al inicio de su beat.
6. **Fuentes de red** → las `woff2` ya están vendorizadas; medir tras `document.fonts.ready`.

---

## 10. Decisiones

1. **Metáfora (resuelto):** la balanza de dos platos. Descartados el balancín y el ping-pong/relevos
   (§1).
2. **Metáfora distinta de V5 (resuelto):** V5 usó la caída en los resultados y la SERP como examen;
   aquí la metáfora es la balanza. La SERP aparece como **escenario de apoyo** (B8), no como imagen
   central.
3. **Números de sección (resuelto):** los rótulos son nominales en mayúsculas, **sin numerar**,
   como en V5; el «1 · / 2 · / 3 ·» de GA4 numeraba un procedimiento que aquí no existe.
4. **`setNum` generalizado (resuelto):** pasa a aceptar selector (`setNum(sel, txt, t)`), porque V6
   lo necesita en B3 y no solo en el gancho.
5. **Transiciones (resuelto):** primaria `slide` (7/11, 63,6 %) + `forma`, `cover`, `circle`,
   `sweep` como acentos; `cut` disponible pero no usada.
6. **Ejemplo único (resuelto):** «instalación de luz» (página de servicio frente a artículo de
   precios), de `01-fuentes.md` §6 ejemplo 2 —nuevo, no repite el «cafetera» de V5.
7. **Cinco familias de transición (resuelto):** excepción justificada al «3-4» de `DESIGN.md` (§6):
   la pieza va en el límite alto de la banda y encadena varios cambios de tema e idea.
8. **Tamaño del término (resuelto):** `.title` se fija a **110 px** con `letter-spacing:-0.03em` en §8
   (override del kit, que lo deja en 110 px por defecto): «CANIBALIZACIÓN» debe entrar en los 932 px
   de banda útil sin partirse; medir tras `document.fonts.ready`.

---

## 11. Implementación y orden de la cadena

- **Contenedores separados** para no pisar transformaciones: `.pos` (posición y tamaño) → `.move`
  (movimiento principal) → `.sub` (movimiento secundario, 6-12 px o 1-2°) → `.mask` (recorte). El
  nombre `.slot` **ya existe** en la serie y es otra cosa; no se reutiliza.
- **Las transiciones animan `.s-in`**, nunca el clip; `.cover`/`.sweep` son DOM nuevo de la escena
  y van a `z-index:40`.
- **Karaoke y progreso** se mantienen tal cual (la barra usa pista `#1e1e26` con relleno de acento;
  es la del kit de la serie —los **elementos nuevos** de V6, como `.splitbar`, van en `#20202a` o
  por encima).
- **Orden obligatorio tras tocar escenas o línea de tiempo:**
  `retime.py` → `transiciones.py` → `check` → render. Después, `verificar_montaje.py`.
- **Revisión final** (checklist en `STORYBOARD.md`): un fotograma de lectura por escena, los
  instantes intermedios de `cover`, `circle`, `forma` y `sweep`, entradas y salidas, alineación,
  sincronía con la voz y el MP4 completo en movimiento.
