# Contrato de producción — V6 «Canibalización de keywords»

Pieza: **dos páginas tuyas compitiendo y ninguna gana** · 9:16 · 1080×1920 · faceless · voz es-ES
(`Pablo`) · ~40 s. Referencias montadas: **V5** `videos/seo-05-intencion-de-busqueda/index.html`
(53,041 s) y `ga4-01` (37,468 s). Todo exigible salvo excepción anotada en `DECISIONS.md`.

## 1. Reglas duras del formato

- Raíz: `data-composition-id="main" data-start="0" data-duration="<total>" data-width="1080" data-height="1920"`.
- Escena: `<section class="scene clip" id="sN" data-start data-duration data-track-index="0">` con CSS propio
  `position:absolute; inset:0; overflow:hidden`. **`.clip` solo no da caja completa**.
- Cada escena envuelve su contenido en `<div class="s-in" id="sN-in">`; **las transiciones animan `.s-in`,
  nunca el clip**.
- **Una sola timeline pausada registrada**: `window.__timelines = window.__timelines || {};` →
  `const tl = gsap.timeline({ paused: true });` → `window.__timelines["main"] = tl; tl.seek(0);`.
- Seek-safe: estado inicial en CSS (`.fade-in`, `.fade-up`, `.fade-up-sm`, `.pop`, `.slide-x` → `opacity:0`)
  y animar con `fromTo`/`.to()`. **Prohibido** `.from()`, `Math.random`, `Date.now`, contadores que suben
  (los números se cambian con `tl.set(..., {textContent})`), CSS `transition`/`@keyframes`, `repeat`/`yoyo`.
- **El escenario nace visible en el primer fotograma**: el marco no se anima con opacidad, solo se asienta
  con `rise()` (`{y:40}→{y:0}`, sin tocar opacity); los hijos usan `put()`. Nacer en `opacity:0` deja los
  cruces vacíos (medido 0,40 s > barra 0,15 s).
- Todo `<audio data-start>` **necesita `id`** (sin id = render mudo). Tracks: voz 1, karaoke 2, música 3, sfx 4.
- Zonas seguras: nada crítico en el **15 % superior** (288 px) ni el **25 % inferior** (480 px).

## 2. Paleta, contraste y luminancia

| token | oscuro | claro | uso |
|---|---|---|---|
| bg | `#0a0a0f` | `#f4f1ea` | lienzo |
| panel | `#20202a` (**mínimo**) | `#ffffff` | paneles/ventanas/tarjetas |
| line | `#26262e` | `#e0dbcf` | bordes 2-5 px |
| ink | `#f5f5f7` | `#14141a` | texto principal |
| muted | `#8b8b99` | `#6f6f78` | rótulos/notas |
| accent | `#c8ff3d` | `#c8ff3d` | **único acento** |
| accent-ink | `#0b0b10` | `#0b0b10` | tinta sobre acento |
| warn | `#ff5a5a` | `#b3161b` | señal de error |
| gold / chrome / field | `#ffd166` / `#1c1c24` / `#0e0e14` | — / `#ffffff` | lujo / barra / dirección |
| SERP claro | `#eef1f5` / `#16181c` | | único bloque claro |

- Un solo acento por escena; verde=correcto, rojo=error/pérdida, dorado=lujo. Nunca dos compitiendo.
- El acento es **siempre relleno con `accent-ink` encima**; verde sobre claro (≈1,3:1) **prohibido** como
  texto/trazo; en claro `muted`=`#6f6f78` y aviso=`#b3161b`.
- **Panel oscuro nunca por debajo de `#20202a`**: el medidor de montaje cuenta filas con luminancia media
  **> 25** (`#17171e` queda fuera; fondo `#0a0a0f`≈13, `#26262e`≈38).
- `warn` marca lo que *pierde* (tachado, caída de posición, ✕): funcional, no decorativo.
- **Lección medida en V5:** se publica sin portada → **el fotograma 0 es la miniatura del reel**. Hay que
  **medirlo antes de aprobar una escena**: luminancia y **% de filas con contenido** (gancho viejo 18,7/255
  y 33 %; bueno 230/255 y 100 %). Medidor: fila con contenido si su media **> 25**; fotograma vacío < ~**4 %**.

## 3. Tipografía y jerarquía

- **Inter** 400/600/700/800/900 + **JetBrains Mono** 600/800 (URL, consulta, código).
- Kicker 28-32 px, 700, `letter-spacing:0.28em`, mayúsculas, `muted`, con punto de color.
- Jerarquía real: **componente gráfico > rótulo > subtítulo**.
- Tamaños: protagonista 110-180, frase principal 70-110, contexto 38-56, CTA «Guarda esto» 96.
- Banda segura: `padding: 300px 74px 470px` (V5 usó 560 abajo); barra de progreso 6 px a `top:300px`;
  píldora karaoke 1000×220 con `bottom:470px`.
- Un beat = frases de 6-10 palabras. Una línea larga **no se encoge: se redistribuye** en varios tiempos
  (V5 L7, 22 palabras → tres cláusulas).

## 4. Transiciones

Seis familias, con o sin pieza propia:

| Familia | Pieza | Implementación |
|---|---|---|
| Desplazamiento continuo (`slide`) | no | tween propio sobre `.s-in`, misma dirección con solape |
| Continuidad por forma (`forma`) | no | tween y+scale sobre `.s-in` |
| Barrido de color (`sweep`) | **sí, `.sweep`** | banda 40 % alto, `skewX(-12deg)`, `z-index:40` |
| Objeto que cubre el encuadre (`cover`) | **sí, `.cover`** | `inset:0`, crece y despeja |
| Revelado circular (`circle`) | no | `clip-path` en el envoltorio, `r ≥ √((w/2)²+(h/2)²)` (≥1500 px) |
| Corte directo (`cut`) | no | sin cruce |

- Reparto: **una primaria (60-70 %)** + 1-2 acentos; duración **0,3-0,5 s** (máx. 2 s) **ajustada a la escena**
  (1,2 s → 0,3 s).
- **Coste**: las que no salen del bucle `up/down/fade/zoom/blur` (slide mismo sentido, `cover`, `sweep`,
  `circle`) se escriben a mano y **cada corte se revisa en su fotograma intermedio** con el medidor de montaje.
- **`transiciones.py`** extiende colas (`data-duration += d`) sin tocar los `<audio>` y acepta cualquier
  nombre de tipo en `TR`.
- **Trampa medida en V5:** si el CSS arranca con `translateX(...)`, GSAP lo lee como `x` y **`xPercent` es
  aditivo** → el barrido acaba en `translateX(0)` y **cubre el cuadro** (72-86 % de verde). **Solución:
  `x: 0` explícito en el `fromTo`**. Un barrido es **una banda**, nunca `inset:0`.

## 5. Duración y ritmo

- **Escena = clip**: cada escena dura exactamente su frase, **sin silencio de relleno** (`--min-frame 0`,
  D23); escenas de **1,2 a 4,2 s**; total 30-40 s (V5 justificó 53 s); la animación no dura más que la escena.
- **Los tiempos reales salen de la voz**: `voice_pipeline.py` escribe `.openhands/tools/voice-timing.json`
  (`clip`, `scene`, `start`, `total`); **`retime.py` los aplica** a raíz, escenas, voz, `prog`, karaoke, música,
  sfx, array `S` y `prog-fill`, reconstruye la música y regenera el `TRANSCRIPT`.
- **Orden obligatorio:** `retime.py` → `transiciones.py` → `check` → render. Nunca a mano (30 valores se
  desincronizan); tras tocar escenas, rehacer la cadena entera o la saliente desaparece (lienzo negro).

## 6. Cadena de herramientas y barras de calidad

```bash
sudo apt-get update && sudo apt-get install -y ffmpeg unzip && npx hyperframes browser ensure
FISH_API_KEY="$FISH_API_KEY" python3 .openhands/tools/voice_pipeline.py \
  --dir videos/<p> --ref 1bd666ea8ada44c789e0fec21cf78f33 --tail 0.08 --min-frame 0
# editar index.html → eventos (assets/sfx/events.json) → sfx → música
python3 .openhands/tools/sfx.py --dir videos/<p> && mkdir -p videos/<p>/assets/music
python3 .openhands/tools/retime.py --dir videos/<p>
python3 .openhands/tools/transiciones.py --dir videos/<p>
npm run check && npx hyperframes render -o renders/video.mp4
python3 .openhands/tools/verificar_montaje.py --dir videos/<p>
```

- `check` con **0 errores** (`nested_structure_needs_subcomposition` y `timeline_track_too_dense` son
  esperados en composición de un solo fichero, D10).
- **Contraste WCAG AA**: texto normal **≥ 4,5:1**; grande (**≥ 24 px**, o **≥ 19 px con peso ≥ 700**) **≥ 3:1**.
- **Cruces sin tramo vacío ≤ 0,15 s**, por fotograma a 30 fps con **umbral de luminancia fijo 25**.
- **Audio sin huecos**: silencio **> 0,12 s por debajo de −48 dBFS = CERO** (RMS lo confirma).

## 7. Activos reutilizables (V6 no crea nada nuevo)

- **Fuentes**: `assets/fonts/fonts.css` + `inter-latin(-ext).woff2` y `jetbrains-mono-latin(-ext).woff2`
  (`@font-face`, sin red en el render).
- **Voz**: Fish Audio **`Pablo`**, `reference_id 1bd666ea8ada44c789e0fec21cf78f33`, modelo `s2.1-pro`, wav,
  cola recortada a 0,08 s.
- **Música**: `assets/music/track.wav`, `<audio id="music" data-volume="0.18">`; `retime.py` la reconstruye
  desde `.openhands/tools/music_bed.wav` (`acrossfade=d=1.5` + `afade`). `assets/music/` no lo crea `init`.
- **Efectos**: `assets/sfx/sfx.wav`, `<audio id="sfx" data-volume="0.5">` (track 4); los sintetiza
  `.openhands/tools/sfx.py` (determinista) y se anclan con `events.json` por proyecto
  (`[{"scene","local","kind","gain"}]`, ganancia 0,25-0,85, un efecto por aparición). 9 tipos: `whoosh, pop,
  tick, click, swoosh_up, swoosh_down, ding, thud, buzz`.
- **Karaoke**: `npx hyperframes add caption-pill-karaoke` → `compositions/components/caption-pill-karaoke.html`
  (con su propio `window.__timelines`), `data-composition-src` + `data-start` (track 2); `TRANSCRIPT`
  `{text,start,end}` con tiempos **absolutos**; palabra activa `#c8ff3d`.
- **Helpers** (en `index.html`): `put(sel,t,{x,y,scale,rot,dur,ease})` · `rise(sel,t,{y,dur})` (sin opacidad) ·
  `draw(sel,t,dur)` (`stroke-dashoffset` L→0) · `grow(sel,t,to,{from,dur,ease})` · `bar(sel,t,to)` (`scaleX`) ·
  `typeWords(sel,t,step)` · `swap(a,b,t)` · `setNum(sel,txt,t)` (generalizado en V6 para B3; ver
  `DIRECCION.md` §10).
- **Componentes/CSS**: `.browser/.chrome/.lights/.addr`, `.serpbody/.result/.fav/.skel`, `.card`,
  `.kicker/.dot`, `.chip/.pill/.tag`, `.tile`, `.cta`, `.progress`.
