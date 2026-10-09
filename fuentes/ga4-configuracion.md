# Fuente: configurar Google Analytics 4 en una web

Resumen de partida facilitado por el dueño (2026-10-09). **Esto es material, no un guion**:
de aquí sale cada guion, una idea por vídeo. El plan y el estado viven en `IDEAS.md` (serie GA4).

**Tesis de la serie:** tener Analytics instalado no es tenerlo bien configurado. La parte útil
empieza cuando defines las acciones importantes para el negocio y compruebas qué canales y
páginas las generan.

**Las tres preguntas que debe responder GA4** (hilo conductor de toda la serie):

1. ¿De dónde llegan los usuarios? → adquisición (GA7, GA8)
2. ¿Qué hacen dentro de la web? → comportamiento (GA3, GA8)
3. ¿Cuántos realizan una acción valiosa? → resultados (GA5)

GA4 funciona **registrando eventos**: una visita a una página, un clic, el envío de un
formulario, una compra o cualquier acción relevante. El objetivo no es acumular datos.

**Reglas de producción** (ver `WORKFLOW.md` y `PUBLICACION.md`): 9:16 faceless, 30-40 s,
voz `Pablo`, una idea por vídeo, jerga definida antes de usarla, CTA "Guarda esto",
copy corto + 2-3 hashtags, sin avisos de autoría.

---

## Mapa de la serie: 8 piezas en 3 bloques

| ID | Carpeta prevista | Idea (una sola) | Formato |
|----|------------------|-----------------|---------|
| GA1 | `videos/ga4-01-instalar-sin-duplicar` | Instalar GA4 sin duplicar las visitas (3 métodos, elige uno) | ~35 s |
| GA2 | `videos/ga4-02-comprobar-si-mide` | Cómo saber si GA4 está midiendo de verdad (y por qué los informes tardan) | ~30 s |
| GA3 | `videos/ga4-03-que-mide-solo` | Lo que GA4 ya mide por ti: eventos automáticos y medición mejorada | ~35 s |
| GA4 | `videos/ga4-04-eventos-recomendados` | No inventes nombres de eventos: Google ya tiene los suyos | ~35 s |
| GA5 | `videos/ga4-05-eventos-clave` | Marcar la acción que vale dinero (y medir la confirmación, no el clic) | ~35 s |
| GA6 | `videos/ga4-06-ajustes-que-se-olvidan` | Los ajustes de GA4 que casi nadie hace | ~40 s |
| GA7 | `videos/ga4-07-utm-campanas` | Saber qué publicación te trae clientes (UTM bien puestas) | ~35 s |
| GA8 | `videos/ga4-08-informes-que-importan` | Los informes que sí importan en una pequeña empresa | ~40 s |

Bloques: **1 → GA1-GA2** (instalar y comprobar) · **2 → GA3-GA5** (eventos y conversiones) ·
**3 → GA6-GA8** (leer y ajustar). La serie empieza por **GA1**.

---

## Brief por pieza

### GA1 — Instalar GA4 sin duplicar las visitas (la que se hace ahora)

- **Idea única:** hay tres formas de conectar Analytics con la web y **conviene elegir solo una**;
  si instalas por plugin *y* por Tag Manager, se duplican visitas y eventos.
- **Datos:** estructura Cuenta → Propiedad → Flujo de datos → ID de medición (`G-XXXXXXXXXX`);
  configuración inicial (España, zona horaria, euros); los tres métodos:
  1. **CMS** (WordPress, Shopify, Wix): pegar el ID o conectar la cuenta. Lo más sencillo.
  2. **Etiqueta de Google** (JavaScript en el `<head>` de todas las páginas): válido, pero cada
     cambio exige tocar código.
  3. **Google Tag Manager**: lo más completo cuando quieres medir formularios, botones, teléfono,
     WhatsApp, compras o varias herramientas publicitarias. Pasos: cuenta y contenedor → instalar
     el código → etiqueta de Google con el ID de GA4 → activación en todas las páginas → probar en
     Vista previa → publicar el contenedor.
- **Hook:** "Instalar Analytics es el paso fácil. El error es hacerlo dos veces."
- **Visual sugerido:** el árbol cuenta/propiedad/flujo con el ID; tres puertas (CMS, etiqueta, GTM);
  un contador de visitas que se **duplica** al activar el segundo método.
- **Ojo:** no prometer "mide mejor": la idea es *no duplicar*.

### GA2 — Cómo saber si GA4 está midiendo de verdad

- **Idea única:** se comprueba con herramientas concretas y el retraso de los informes es normal.
- **Datos:** Informes → **Tiempo real** (tu visita aparece en segundos); para eventos concretos:
  **Tag Assistant** (qué etiquetas se activan), **Vista previa** de Tag Manager (probar antes de
  publicar) y **DebugView** (eventos y parámetros en el momento; es lo que Google recomienda para
  revisar eventos configurados). Los informes normales tardan en procesarse: **no está roto**.
- **Hook:** "Tu Analytics no está roto: está tardando."
- **Visual sugerido:** panel de Tiempo real con 1 usuario; tres tarjetas de herramientas; reloj.

### GA3 — Lo que GA4 ya mide por ti

- **Idea única:** hay eventos automáticos y una "medición mejorada" que se activa sin programar,
  pero hay que revisarla porque formularios y búsquedas internas suelen necesitar ajustes.
- **Datos:** eventos recogidos automáticamente (inicio de sesión, primera visita). Medición
  mejorada (Administrador → Flujos de datos → Web → Medición mejorada): visitas a páginas,
  desplazamientos, clics hacia otras webs, búsquedas internas, descargas de archivos,
  interacciones con formularios e interacciones con algunos vídeos insertados.
- **Hook:** "Antes de programar nada, mira lo que Google ya mide."
- **Visual sugerido:** interruptores que se encienden uno a uno; lista de 7 con marcas.

### GA4 — No inventes nombres de eventos

- **Idea única:** cuando existe un evento recomendado hay que usar su nombre oficial; solo si no
  existe se crea uno personalizado, y los parámetros hay que registrarlos para verlos en informes.
- **Datos:** recomendados (acción → nombre): contacto/presupuesto → `generate_lead`; registro →
  `sign_up`; añadir al carrito → `add_to_cart`; iniciar pago → `begin_checkout`; compra →
  `purchase`. Personalizados de ejemplo: `click_whatsapp`, `click_phone`, `request_audit`,
  `download_catalog`, `booking_completed`. En Tag Manager: etiqueta **Evento de GA4** + nombre +
  activador (botón, formulario, página). Parámetros de ejemplo en `generate_lead`: `form_name`,
  `lead_type`, `page_location`, `value`. Para usarlos en informes hay que registrarlos como
  dimensión/métrica personalizada.
- **Hook:** "`generate_lead` ya existe. Inventarte `formulario_ok` solo te rompe los informes."
- **Visual sugerido:** tabla acción → nombre recomendado; un nombre inventado tachado.

### GA5 — El evento que vale dinero

- **Idea única:** no todos los eventos importan igual; los que representan un resultado se marcan
  como **eventos clave** (antes "conversiones") y hay que medir la **confirmación real**.
- **Datos:** eventos clave típicos de una web de servicios: envío correcto del formulario, clic en
  teléfono, clic en WhatsApp, reserva de cita, compra/pago completado. Un clic en "Enviar" no
  garantiza que el formulario se procesó. Si hay campañas, vincular Google Ads e importar las
  conversiones publicitarias.
- **Hook:** "Un clic en Enviar no es un cliente."
- **Visual sugerido:** embudo de eventos con solo uno marcado; check de confirmación frente a clic.

### GA6 — Los ajustes que casi nadie hace

- **Idea única:** una configuración básica incluye más cosas que pegar el código.
- **Datos:** conservación de datos a **14 meses** (tope de la propiedad gratuita; necesario para
  Exploraciones y comparar periodos largos); **excluir tráfico interno** (probar el filtro antes:
  al activarlo la exclusión es permanente); vincular **Search Console** (tráfico orgánico con
  páginas de destino); vincular **Google Ads** si hay campañas; **medición multidominio** si la
  reserva, tienda o pago ocurren en otro dominio; **excluir referencias no deseadas** (una
  plataforma de pago que aparece como origen de la venta); **consentimiento de cookies y Consent
  Mode** para usuarios europeos (Analytics adapta la recogida según la señal del banner).
- **Hook:** "Instalar Analytics es el paso 1 de 6."
- **Visual sugerido:** checklist que se va marcando; aviso de "permanente" en el filtro interno.

### GA7 — Saber qué publicación te trae clientes

- **Idea única:** los enlaces de correos, redes y colaboraciones llevan parámetros UTM para que
  Analytics sepa qué los generó.
- **Datos:** ejemplo `https://misitio.com/auditoria?utm_source=instagram&utm_medium=social&utm_campaign=auditoria_seo`;
  `utm_source` (origen), `utm_medium` (tipo de canal), `utm_campaign` (campaña), `utm_content`
  (creatividad). Se ven en los informes de adquisición. **No usar UTMs en enlaces internos**:
  sustituyen la atribución original de la visita.
- **Hook:** "Si no etiquetas tus enlaces, no sabrás qué publicación te trajo el cliente."
- **Visual sugerido:** URL que se parte en etiquetas; un enlace interno con UTM tachado.

### GA8 — Los informes que sí importan

- **Idea única:** no hace falta revisarlo todo; hay siete informes que responden a lo importante.
- **Datos:** adquisición de tráfico (de qué canales llegan las sesiones); páginas de destino (por
  dónde entran y cuál genera resultados); páginas y pantallas (qué contenido consultan); eventos
  (qué acciones hacen); eventos clave (cuántos contactos, reservas o ventas); exploración de
  embudos (en qué paso abandonan); comparaciones (móvil vs ordenador, orgánico vs anuncios,
  nuevos vs recurrentes).
- **Hook:** "Tu Analytics tiene 40 informes. Con estos siete tomas decisiones."
- **Visual sugerido:** lista de siete con la pregunta que responde cada uno; embudo con abandono.

---

## Material de consulta directa

**Estructura de GA4:** Cuenta (la empresa) → Propiedad (la web o app) → Flujo de datos (web,
Android, iOS) → ID de medición (`G-XXXXXXXXXX`). Ejemplo: cuenta "Crecimiento Sin
Complicaciones", propiedad `crecimientosincomplicaciones.com`, flujo "Web principal".

**Pasos de alta:** entrar en analytics.google.com → crear cuenta → crear propiedad GA4 → elegir
España, zona horaria y euros → crear flujo de tipo Web → introducir el dominio y copiar el ID.

**Fuentes que cita el resumen de partida** (Ayuda de Analytics/Google): la documentación de
Google sobre medición mejorada, eventos recomendados y eventos clave; `support.google.com` para
crear eventos en Tag Manager; y las páginas de Ayuda sobre conservación de datos, exclusión de
tráfico interno, DebugView y Consent Mode.
