# Verificación de MK3 — anuncios de ataque y defensa de marca

Fecha: 2026-10-19. Sobre `renders/video.mp4` (el render final, con las cinco anotaciones del dueño).

## Especificaciones del fichero

| Campo | Valor | Esperado |
|---|---|---|
| Contenedor de vídeo | H.264 | H.264 |
| Resolución | 1080×1920 | 1080×1920 |
| Fotogramas por segundo | 30 | 30 |
| Duración | 36,100 s | ~36 s |
| Audio | AAC, 48 000 Hz, estéreo | AAC |

## Montaje

`verificar_montaje.py` sobre el directorio del proyecto:

- **MONTAJE OK**
- Peor tramo sin contenido: **0,00 s** (barra ≤ 0,15 s)
- Huecos de audio > 0,12 s por debajo de −48 dBFS: **0**
- Audio total: 36,05 s

## Sincronía de sonido

Medida sobre el render:

- Cortes (whoosh) dentro de barra: **10/10**
- Cues dentro de barra: **34/34** medibles
- Latidos locales: **2/2** medibles

## Composición

- `hyperframes check`: **0 errores**, 34/34 comprobaciones de contraste AA.
- 11 escenas, una por línea de guion.
- Las cinco anotaciones del dueño aplicadas: reacción en la oficina (s01), ladrón (s02),
  espada (s03), logo real de Basecamp como fichero local (s04) y mano con dinero más cursor (s10).
- Los subtítulos del karaoke se mantienen en toda la pieza.

## Conclusión

El vídeo está listo para publicar. Falta la Release pública (hecha el mismo día), la entrada en la
cola de `hypervideo` y el lanzamiento de la Action.
