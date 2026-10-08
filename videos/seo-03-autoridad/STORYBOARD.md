---
format: 1080x1920
duration: 32.05s
message: "Tu web no sube por el contenido: sube por la autoridad, y la autoridad son los enlaces que otros te dan"
arc: Hook → Definición → Qué no cuenta → Qué sí cuenta → Calidad → Consecuencia → Compruébalo → Compara → Se construye → CTA
audience: gente que hace SEO o marketing digital en redes
mode: collaborative
---

**Regla de montaje:** cada escena dura exactamente lo que dura su clip de voz
(**escena = clip**). No hay silencios entre frases: la voz va continua de principio a fin.

**Capa de sonido:** música de fondo (`assets/music/track.wav`, volumen 0.18) + pista de
efectos `assets/sfx/sfx.wav` (volumen 0.5), generada con `tools/sfx.py` desde
`assets/sfx/events.json` (54 efectos) y anclada a la aparición de cada elemento.

**Regla de diseño:** el peso lo llevan los gráficos (medidor de autoridad, tarjetas de dominio,
informe de enlaces, barras comparativas). El texto en pantalla queda reducido al mínimo: solo
etiquetas de sección, los dominios y los números.

**Regla de movimiento:** entradas con `fromTo` y asentamiento **`power3.out`** (nunca rebote);
cada elemento aparece **cuando la voz lo nombra** (tiempos por palabra del karaoke) y el
**escenario entra con la escena** (toda escena necesita una tarjeta o marco presente desde
t=0, o durante un push llega vacía).

**Transiciones:** una primaria (`push-slide`) + dos acentos (`zoom-through` en el giro,
`blur-crossfade` en el clímax). Los push sobre escenas oscuras van cortos (0,25 s) para que el
cruce no se quede sin contenido. Animan la capa interna `#sN-in`; el audio no se toca.

| Corte | `transition_in` | Dur. | Por qué |
|---|---|---|---|
| F1→F2 | `push-slide` ↑ | 0,45 s | primaria |
| F2→F3 | `push-slide` ↑ | 0,40 s | primaria |
| F3→F4 | `crossfade` | 0,40 s | mismo contexto (lo que no cuenta → lo que sí) |
| F4→F5 | `push-slide` ↑ | 0,25 s | punto nuevo, corto (escena oscura) |
| F5→F6 | `zoom-through` | 0,50 s | clímax: el golpe de la consecuencia |
| F6→F7 | `blur-crossfade` | 0,50 s | el dato útil: contención |
| F7→F8 | `push-slide` ↓ | 0,25 s | la comparación, corta (escena oscura) |
| F8→F9 | `crossfade` | 0,35 s | continuidad |
| F9→F10 | `crossfade` | 0,50 s | outro |

## Frame 1 — Hook (0,000 – 4,333 s)

- scene: ventana de navegador con una SERP; dos resultados ajenos y, abajo, el propio atenuado
  con la posición `8` y una flecha roja hacia abajo
- sfx: whoosh + pop (ventana) + pop (fila propia) + tick (posición) + thud (la flecha)
- texto en pantalla: `AUTORIDAD`, `medio.com`, `otratienda.com`, `8`

## Frame 2 — Qué es (4,333 – 6,903 s)

- scene: tarjeta de dominio (`tuweb.com`) con un medidor que se llena hasta `22/100`
- sfx: whoosh + pop (tarjeta) + pop (dominio) + swoosh_up (medidor) + ding (cifra)
- la definición: la autoridad es cuánto se fía Google de ese dominio

## Frame 3 — Qué no cuenta (6,903 – 9,564 s)

- scene: artículo impecable (líneas de texto) con un check verde que **se tacha** con un aspa roja
- sfx: whoosh + pop (tarjeta) + ding (el check) + buzz (el aspa)
- el contraste que prepara la línea siguiente

## Frame 4 — Qué sí cuenta (9,564 – 11,747 s)

- scene: tres webs (`medio.com`, `blog.com`, `foro.com`) con una flecha hacia `tuweb.com`;
  el medidor sube a `58/100`
- sfx: whoosh + 3 pops + swoosh_up ×2
- el mecanismo: los enlaces de otras webs son lo que mueve el medidor

## Frame 5 — Calidad, no cantidad (11,747 – 14,385 s)

- scene: tarjeta con dos barras comparadas: un enlace de `medio.com` (barra llena, `1`) contra
  cien de foros (barra mínima, `100`)
- sfx: pop + pop + swoosh_up (barra grande) + pop + swoosh_down (barra pequeña)

## Frame 6 — La consecuencia (14,385 – 17,676 s)

- scene: la SERP otra vez; los resultados ajenos y un **hueco vacío** con un aspa roja donde
  debería estar tu web
- sfx: whoosh + pop + pop + thud (el aspa)

## Frame 7 — Compruébalo (17,676 – 21,671 s)

- scene: panel tipo Search Console, sección **Enlaces**, con tres dominios que te enlazan y sus
  barras azules llenándose
- sfx: whoosh + pop + tick (el encabezado) + 3×(pop + swoosh_up)
- es el dato accionable del vídeo: se puede mirar hoy

## Frame 8 — Compara (21,671 – 25,453 s)

- scene: tarjeta con dos barras: `tuweb.com` con `3` y `competencia` con `118` (en rojo)
- sfx: pop + pop + tick + pop + swoosh_up

## Frame 9 — Se construye (25,453 – 29,679 s)

- scene: los enlaces llegan de tres webs y el medidor **crece** hasta `83/100` durante la escena
- sfx: whoosh + pop + 3 pops + swoosh_up ×2

## Frame 10 — CTA (29,679 – 32,047 s)

- scene: marcador de guardar con onda + píldora `Guarda esto`
- sfx: pop + ding + pop
