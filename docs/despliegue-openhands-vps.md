# Despliegue de OpenHands en la VPS (un solo usuario)

Objetivo: dejar de depender del cloud de OpenHands. El agente, los renders y la publicación
en una sola máquina que ya es tuya.

Datos medidos de la VPS (`srv1430096`):

| Recurso | Valor | ¿Suficiente? |
|---|---|---|
| Memoria | 7,8 GB (894 MB en uso, 6,9 disponibles) | Sí: el conjunto usa ~5,3 GB |
| Núcleos | 2 | Sí: el render va con un worker; tarda ~2:30 en vez de 1:40 |
| Disco | 34 GB libres de 96 | Sí: imágenes ~2 GB + renders |
| Swap | **0** | **No: hay que añadirla** |

---

## 1. Swap de 4 GB (hacerlo primero)

Sin swap, un pico de Chromium durante un render puede llevarse por delante un proceso o la máquina.
Es lo más barato que se puede hacer por la estabilidad del servidor.

```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
free -h          # debe aparecer Swap: 4,0Gi
```

## 2. Comprobar Docker

El renderer de n8n ya lo usa, así que debería estar:

```bash
docker --version
docker ps
```

## 3. Instalar el CLI de OpenHands

Sigue la guía oficial, que es la que manda y puede cambiar:
<https://docs.openhands.dev/openhands/usage/cli/installation>

## 4. Clonar el proyecto y lanzar la interfaz

```bash
mkdir -p /opt/openhands && cd /opt/openhands
git clone https://github.com/specialcowboy69/openframes.git
cd openframes
openhands serve --mount-cwd
```

`openhands serve` levanta la interfaz web completa en Docker (unos 2 GB de imágenes) y monta
el directorio actual en `/workspace` del contenedor, que es donde el agente trabaja.

Aviso honesto: la documentación de 2026 marca esta interfaz local como *legacy* frente al
Agent Canvas, pero sigue siendo la vía documentada para un solo usuario.

## 5. El modelo: DeepSeek

En la interfaz, `Settings > LLM`:

| Campo | Valor |
|---|---|
| Proveedor | DeepSeek (o «OpenAI compatible») |
| Base URL | `https://api.deepseek.com` |
| Modelo | `deepseek-flash` (tiene visión nativa) |
| API key | la tuya |

Y en `Settings > Secrets`, añade `DEEPSEEK_API_KEY` para que los scripts la reciban como variable
de entorno. Aquí sí se carga desde el principio, porque la conversación nace después del secreto.

## 6. Acceso sin abrirlo al mundo

No publiques el puerto 3000. Usa un túnel SSH desde tu PC:

```bash
ssh -L 3000:localhost:3000 root@72.61.161.99
```

Y abre `http://localhost:3000` en tu navegador. Si algún día quieres acceso desde fuera sin túnel,
pon delante un proxy con autenticación (Caddy o nginx + contraseña), nunca el puerto desnudo.

## 7. Los renders

Dos opciones, y recomiendo la primera:

1. **Usar el renderer de n8n que ya existe**, por el webhook `hyperframes-build-render`. El agente
   prepara el paquete y lo dispara; la máquina es la misma, así que no hay saltos de red.
2. Renderizar dentro del propio sandbox del agente. Requiere una imagen de sandbox propia con
   `ffmpeg`, `unzip` y Chromium preinstalados (<https://docs.openhands.dev/openhands/usage/advanced/custom-sandbox-guide>),
   y además obliga a reinstalar herramientas cuando la imagen se actualice. Más trabajo para el mismo resultado.

## 8. Copias

Lo que hay que salvar, y no es mucho:

- `~/.openhands/` (ajustes, secretos y perfiles de modelo)
- `/opt/openhands/openframes/` (el repositorio; lo importante ya está en GitHub)
- la cola de `hypervideo` (está en GitHub)
- `renders/` y los assets pesados, si no quieres volver a generarlos

Un `tar` semanal por cron a un disco aparte es suficiente para empezar.

---

## Qué se gana y qué se pierde

**Se gana**: control total, los secretos en casa, los ficheros en el disco propio y el fin de los
reinicios del sandbox, del fallo de creación de conversaciones y del de los adjuntos. El modelo
sigue siendo el mismo (DeepSeek por API) y no hace falta GPU.

**Se pierde**: el mantenimiento pasa a ser tuyo (actualizar, vigilar que el contenedor siga vivo,
copias), y con dos núcleos los renders son más lentos que aquí.

**Si algún día se queda corta**: mover el agente al Mac Mini es cambiar de contenedor, no de
sistema. El repositorio, las herramientas y las reglas viajan enteros.
