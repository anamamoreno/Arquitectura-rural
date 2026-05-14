# UIP — Enriquecimiento de fichas M2 con imágenes

**Estado:** 🟧 IMPLEMENTADA Y REVERTIDA (2026-05-12 → 2026-05-13). Pendiente re-implementación con análisis visual de contenido. Ver §14 para cronología detallada.
**Fecha de UIP:** 2026-05-02 · **Implementación:** 2026-05-12 · **Retroceso:** 2026-05-13
**Autor:** Ana (con asistencia de Claude)
**Track:** B (Casos de éxito M2) — funcionalidad complementaria

---

## 1. Objetivo

Agregar 1–2 imágenes (foto, plano, diagrama) por caso en la matriz M2 para que las fichas dejen de ser solo texto. Esto facilita:
- Verificación visual del caso por la usuaria al validar
- Insumo gráfico para el Producto 2 (guía técnica con apoyo gráfico)
- Comunicación con arquitectos consultores y supervisor

---

## 2. Alcance

**Incluye:**
- Definir un campo `Imagenes` en M2 (lista de filenames separados por `;`)
- Folder estructurado `FUENTES/imagenes/casos/CAS-NNN/` con imágenes locales por caso
- Galería compacta en cada ficha de la app (1–2 thumbnails con click → ampliación)
- Atribución por imagen (autor / fuente / página) — campo `Atribucion_imagen`
- Extracción automática de imágenes embebidas en los 3 PDFs ya en `FUENTES/`
- Curaduría manual sobre lo extraído

**No incluye (fuera de esta UIP):**
- Búsqueda de imágenes en sitios web externos (ArchDaily, etc.) — se evalúa después
- Edición/recorte de imágenes — se hace fuera de la app si se necesita
- Imágenes para el Producto 2 (otra consultoría se encarga del diseño gráfico final)
- Servicio de imágenes vía VPS (se aborda junto con UIP de despliegue)

---

## 3. Decisiones a confirmar

| # | Decisión | Opciones | Recomendación |
|---|---|---|---|
| D1 | Origen de las imágenes | A) Extracción auto de PDFs / B) Captura manual (screenshot) / C) URLs externas / D) Combinación A→B | **D** — A primero (gratis, automatizable) → B complementaria si A no aporta |
| D2 | Cantidad por caso | 1 imagen / 2 imágenes / hasta 3 | **2** (compromiso entre densidad y limpieza visual) |
| D3 | Formato | JPG comprimido / PNG / mantener original | **JPG calidad 80** (peso bajo, calidad suficiente) |
| D4 | Resolución máxima | 800px lado mayor / 1200px / sin límite | **1200px** (suficiente para zoom, ~200 KB/img) |
| D5 | Atribución | Campo libre / estructurado (autor + año + fuente) | **estructurado** mínimo (`Autor, Fuente, p. N`) |
| D6 | Visibilidad en GitHub | Versionar imágenes / gitignore / Git LFS | **versionar** (~20 MB total, manejable sin LFS) |
| D7 | Casos sin imagen disponible | Dejar placeholder / ocultar sección / no permitir validar | **placeholder discreto** ("📷 sin imagen") |

**Bloqueadores:** D1 (define el flujo de trabajo). D6 (define impacto en repo).

---

## 4. Arquitectura propuesta

```
Proyecto-Arq_Rural/
├── FUENTES/
│   ├── *.pdf                    (existente)
│   └── imagenes/
│       └── casos/
│           ├── CAS-001/
│           │   ├── img1.jpg
│           │   └── img2.jpg
│           ├── CAS-002/
│           │   └── img1.jpg
│           └── ...
├── docs/
│   └── F0-Matriz_casos_exito.csv  (+1 columna `Imagenes` y +1 `Atribucion_imagen`)
└── scripts/
    └── app_matriz_estandares.py   (modificada: galería en tarjetas)
```

**Convención de naming:**
- Folder: `CAS-NNN/` (mismo ID que el caso en M2)
- Archivos: `img1.jpg`, `img2.jpg` (o nombres descriptivos cortos: `tapia-fachada.jpg`, `planta.jpg`)
- Auto-detección: la app lista los archivos del folder y los muestra en orden alfabético

**Versionado en GitHub:**
- Si D6 = versionar → `.gitignore` permite `FUENTES/imagenes/`
- Imágenes de respaldo viajan con el repo, colaboradores las ven sin descargar PDFs

---

## 5. Modificaciones a M2

### Columnas a agregar (de 29 a 31)

| Columna | Tipo | Ejemplo |
|---|---|---|
| `Imagenes` | lista separada por `;` | `img1.jpg; img2.jpg` |
| `Atribucion_imagen` | texto libre estructurado | `"img1: Hábitat Para La Paz, p. 67; img2: VIVA Antioquia, p. 23"` |

**Reglas:**
- Si `Imagenes` vacío → galería oculta, placeholder en su lugar
- Auto-detección complementaria: si el folder `FUENTES/imagenes/casos/CAS-NNN/` existe pero la columna `Imagenes` está vacía, la app lista todos los archivos del folder por defecto

---

## 6. Componentes a crear

### 6.1 Subagente de extracción (Opción A)
Script Python o llamada a subagente que:
- Recorra los 3 PDFs en `FUENTES/`
- Extraiga todas las imágenes embebidas con su número de página
- Genere índice en `docs/extracciones/imagenes_indice.md` con: `archivo.pdf · pág. N · imagen X · descripción aproximada (de leyenda cercana)`
- Guarde las imágenes en `FUENTES/imagenes/_extraidas_brutas/`

### 6.2 Asignación a casos
Tres formas:
- **Manual (recomendada):** abrir el índice, identificar imágenes relevantes por caso, mover/renombrar a `FUENTES/imagenes/casos/CAS-NNN/`
- **Asistida:** subagente sugiere asignaciones cruzando rangos de página del índice con líneas de cada caso (ya tenemos las líneas aprox)
- **Diferida:** dejar `FUENTES/imagenes/_extraidas_brutas/` y asignar progresivamente al validar en la app

### 6.3 Modificación de la app
- Detectar imágenes del caso (de columna `Imagenes` o auto-listado del folder)
- Mostrar galería de 1–2 thumbnails al inicio de la ficha (después del título, antes de los badges)
- Click en thumbnail → expansor con imagen grande + atribución
- Placeholder discreto si no hay imágenes
- Botón "📷 Asignar imágenes" en pendientes → muestra imágenes de `_extraidas_brutas/` y permite seleccionar

### 6.4 Actualización de docs
- `F8-Matriz_casos_diccionario.md`: definir las 2 nuevas columnas
- `F6-Plan_busqueda_casos.md` §5: actualizar estructura
- `README.md`: mencionar la carpeta de imágenes

---

## 7. Pasos de implementación (en orden)

### Fase 1 — Datos y estructura
1. Crear carpeta `FUENTES/imagenes/casos/`
2. Agregar columnas `Imagenes` y `Atribucion_imagen` a M2 (script + commit)
3. Actualizar diccionario F8 y plan F6

### Fase 2 — Extracción
4. Subagente con `PyMuPDF (fitz)` extrae imágenes de los 3 PDFs
5. Genera índice `docs/extracciones/imagenes_indice.md`
6. Imágenes brutas a `FUENTES/imagenes/_extraidas_brutas/`

### Fase 3 — Curaduría inicial (1 ronda)
7. Tú revisas el índice y haces selección por caso (puede ser solo 5–10 casos en primera ronda, no los 19)
8. Mover/renombrar imágenes seleccionadas a `FUENTES/imagenes/casos/CAS-NNN/`

### Fase 4 — App
9. Modificar app para mostrar galería en tarjetas
10. Validar en local con los casos que tienen imágenes asignadas

### Fase 5 — Versionado
11. Si D6 = versionar: ajustar `.gitignore` para incluir `FUENTES/imagenes/`
12. Commit + push

### Fase 6 — Curaduría progresiva
13. Ir asignando imágenes a los demás casos en sesiones posteriores, conforme se validan

---

## 8. Criterios de aceptación

- [ ] M2 tiene columnas `Imagenes` y `Atribucion_imagen`
- [ ] Al menos 5 casos representativos tienen ≥1 imagen asignada
- [ ] La app muestra la galería sin romper layout
- [ ] Click en thumbnail abre vista grande con atribución
- [ ] Casos sin imagen muestran placeholder, no error
- [ ] Si D6=versionar: imágenes están en GitHub y el repo sigue <30 MB
- [ ] Diccionario F8 actualizado

---

## 9. Plan de rollback

- **Galería rompe la app:** comentar el bloque de galería en `scripts/app_matriz_estandares.py` y revertir
- **Imágenes pesan demasiado:** mover `FUENTES/imagenes/` a `.gitignore`, las imágenes quedan solo locales
- **Atribución incorrecta:** las columnas `Imagenes` y `Atribucion_imagen` son editables en la app — corrección en línea
- **Asignación equivocada caso↔imagen:** mover archivo entre carpetas `FUENTES/imagenes/casos/CAS-NNN/`

Como las imágenes son archivos discretos, todo es reversible localmente. Sin riesgo de pérdida.

---

## 10. Riesgos y mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| PDFs producen 200+ imágenes ruido (logos, ornamentos) | Alta | Medio | Subagente filtra por tamaño mínimo (>100KB) y resolución mínima (>400px) |
| Imágenes con derechos no claros para Producto 2 | Alta | Bajo (M2 es trabajo interno) | Atribución obligatoria; uso solo interno hasta clarificar derechos |
| Repo crece >100 MB | Media | Medio | Límite de 1200px y JPG q80; revisar tamaño antes de cada commit |
| App se vuelve lenta cargando muchas imágenes | Baja | Bajo | Streamlit cachea; thumbnails compresos sirven primero |
| Extracción auto pierde imágenes vectoriales o embebidas raro | Media | Bajo | Curaduría manual cubre los huecos |

---

## 11. Estimación

- **Trabajo del desarrollador (Claude):** ~3 horas
  - Fase 1 (datos): 30 min
  - Fase 2 (extracción): 30 min subagente + setup
  - Fase 4 (app): 1.5 h
  - Fase 5 (versionado): 30 min
- **Trabajo de la usuaria:** ~1 h primera ronda (curaduría 5–10 casos)
- **Tiempo calendario:** 1 día asumiendo todas las decisiones tomadas

---

## 12. Implicaciones para otras UIPs

### UIP Despliegue VPS
- Las imágenes locales habrá que servirlas vía Streamlit static (mismo problema que los PDFs)
- Si D6 = versionar → al hacer `git pull` en VPS las imágenes llegan automáticamente
- Si D6 = no versionar → hay que sincronizar `FUENTES/imagenes/` por scp aparte

### Producto 2
- Las imágenes de M2 son **referencia interna**, no producto final
- El Producto 2 necesita imágenes con derechos claros y tratamiento gráfico institucional
- M2 alimenta de "qué buscar / qué encargar" al equipo gráfico de Producto 2

---

## 13. Próximo paso

Resolver decisiones D1, D6 (las que bloquean). Recomendación: D1=D, D6=versionar.

Una vez confirmadas, esta UIP se vuelve plan ejecutable y se pasa a Fase 1.

---

## 14. Bitácora de implementación y retroceso

### 14.1 Cronología

| Fecha | Evento |
|---|---|
| 2026-05-02 | UIP redactada (estado inicial: EN COLA — diferida) |
| 2026-05-12 | Implementación completa con decisiones confirmadas por la usuaria |
| 2026-05-13 | Retroceso completo solicitado por la usuaria por baja calidad de la curaduría automática |

### 14.2 Decisiones confirmadas durante la implementación

| # | Decisión confirmada | Cambio vs UIP original |
|---|---|---|
| D1 | A) Extracción automática desde PDFs | Se descartó la combinación D (A→B); se optó por A pura |
| D2 | 2 imágenes por caso | = recomendación |
| D3 | **Mantener formato original** (jpg, png, jpx) | Cambió de "JPG q80" → preservar extensión nativa del PDF |
| D4 | **800px lado mayor** | Reducido desde 1200px |
| D5 | Atribución estructurada (autor + año + fuente) | = recomendación |
| D6 | **Versionar imágenes en git** (.gitignore con exception) | = recomendación |
| D7 | Placeholder discreto | = recomendación |
| Arquitectura | Carpeta plana `FUENTES/IMAGENES/` (no subcarpetas por caso); naming `CAS-NNN-imgXX.<ext>` | Cambió respecto a la UIP original que proponía subcarpetas `FUENTES/imagenes/casos/CAS-NNN/` |

### 14.3 Cambios técnicos aplicados (commit `14fc32d`)

- **`FUENTES/IMAGENES/`** creada con 80 archivos (~13 MB) — 40 casos cubiertos
- **CSV M2** ampliado de 30 → 32 columnas (`Imagenes`, `Atribucion_imagen`)
- **App Streamlit** modificada: popup de detalle con galería en 2 columnas + caption de atribución + placeholder discreto cuando no hay imágenes
- **`.gitignore`** ampliado con `FUENTES/**/*.docx`, `*.xlsx`, `*.html` + exception `!FUENTES/IMAGENES/**` para versionar la carpeta de imágenes
- **Filtros automáticos durante extracción:**
  - Tamaño mínimo: 30 KB
  - Dimensiones mínimas: 200×200 px
  - Pixeles mínimos: 60.000 (filtra logos/iconos)
  - Selección: primeras N imágenes que pasan filtros, distribuidas secuencialmente (2 por caso)
- **Resize:** Pillow LANCZOS si supera 800px lado mayor; preservación de extensión original
- **Cobertura:** 40 casos con galería · 22 sin (19 sin PDF local + 3 docx sin imágenes embebidas)

### 14.4 Análisis del problema detectado

Tras revisión visual de las imágenes asignadas, la usuaria detectó que la selección automática estaba **sesgada hacia contenido de contextualización** y NO hacia las viviendas:

| Tipo de imagen seleccionada | Frecuencia observada | Por qué |
|---|---|---|
| Mapas geográficos | Alta | Suelen ir al inicio del PDF (introducción/contextualización) y son grandes/legibles |
| Paisajes territoriales | Alta | Mismo motivo: ilustran el lugar antes de mostrar la casa |
| Diagramas climáticos | Media | Suelen ir en secciones de análisis previo al diseño |
| Retratos / fotos de equipo | Media | Páginas de créditos al inicio |
| **Fotos de la vivienda (fachada/interior)** | **Baja** | Suelen estar en la mitad o final del documento |
| **Plantas arquitectónicas** | **Baja** | Suelen ir después de la presentación del caso |

**Causa raíz:** el script seleccionó las primeras N imágenes que pasaban los filtros de tamaño/dimensión, sin análisis de contenido. En documentos académicos y memorias arquitectónicas, las primeras imágenes son típicamente contextuales (mapas, paisajes, diagramas), no las viviendas que son el objeto del caso.

### 14.5 Retroceso aplicado (commit `3a488af`)

Se eliminaron **selectivamente** los cambios relacionados con imágenes, preservando los productos independientes generados en la misma jornada:

| Cambio del commit `14fc32d` | Acción al revertir |
|---|---|
| Carpeta `FUENTES/IMAGENES/` con 80 archivos | ❌ Eliminada físicamente y del git tracking |
| Columnas `Imagenes` + `Atribucion_imagen` en CSV M2 | ❌ Eliminadas (CSV vuelve a 30 columnas) |
| Galería de imágenes en popup de la app | ❌ Removida (popup vuelve al estado pre-imágenes) |
| `.gitignore` con exception `!FUENTES/IMAGENES/**` y reglas `*.docx/*.xlsx/*.html` | ❌ Revertido a estado anterior (sólo `FUENTES/**/*.pdf`) |
| Estado de UIP-002 a "✅ EJECUTADA" | ❌ Revertido a "🟧 IMPLEMENTADA Y REVERTIDA" |
| `F0-Resumen_ejecutivo_FINAL.md` | ✅ Conservado (independiente de imágenes) |
| `F0-Fichas_M2_todos_los_casos.md/.html` | ✅ Conservado (independiente) |

Resultado: working tree limpio sin imágenes, app funcional, documentos de cierre preservados.

### 14.6 Aprendizajes para futura re-implementación

1. **Filtrado por tamaño no equivale a filtrado por relevancia.** Una imagen grande puede ser un mapa o una fachada; el script no puede distinguir sin análisis visual.

2. **El orden secuencial de imágenes en PDF típicamente NO favorece a las viviendas.** Las primeras imágenes son contextuales; las viviendas suelen estar en la segunda mitad del documento (capítulos de propuesta, fichas técnicas, fotografías de obra).

3. **La "extracción automática pura" (D1=A) no es viable sin curación.** Hace falta uno de:
   - **D1=A híbrida con análisis visual** (Claude Vision o modelo similar): re-extraer todas las imágenes válidas, clasificar por contenido (vivienda / planta / contexto / logo / retrato), seleccionar 2 mejores
   - **D1=B manual asistida**: extraer todas las candidatas a una carpeta staging y dejar que la usuaria seleccione (1 minuto por caso, ~40 casos = 40 min)
   - **D1=C URLs externas**: capturar fotos de ArchDaily / sitios de arquitectos / Bienal SCA cuando las haya. Mejora calidad y atribución, requiere más trabajo
   - **Estrategia heurística por rango de páginas**: en PDFs académicos, ignorar primer 30% del documento (donde están portadas/intros/mapas)

4. **La arquitectura plana (`FUENTES/IMAGENES/`) sin subcarpetas funciona bien** (cambio respecto a UIP original) — más fácil de listar y manipular.

5. **El versionado (`D6=versionar`) es operativamente correcto:** 80 imágenes a 800px sumaron solo 13 MB, manejable sin Git LFS. Cuando se re-implemente, mantener esta decisión.

6. **El placeholder discreto funcionó bien** en los 22 casos sin imágenes — no rompe layout, comunica claramente la ausencia.

### 14.7 Recomendaciones para próximo intento

| Componente | Cambio sugerido |
|---|---|
| **D1 (origen)** | Cambiar de A pura → **A híbrida con análisis visual** (Claude Vision): extraer todas las candidatas, clasificar y elegir las que muestran vivienda |
| **Naming** | Reemplazar genérico `CAS-NNN-imgXX.ext` por descriptivo `CAS-NNN-{fachada/planta/interior/detalle}.ext` (lo permite identificar sin abrir) |
| **Filtro por página** | Agregar regla heurística: ignorar primer 25% de páginas del PDF para reducir mapas/portadas |
| **Validación humana** | Agregar paso de revisión visual antes de comprometer al CSV (mostrar candidatas en notebook o app temporal) |
| **Atribución por imagen** | En lugar de una atribución general por caso (autor + año + fuente), agregar página específica del PDF de origen — útil para reclamar derechos |
| **Estado del UIP** | Mantener este documento como **lección aprendida**: documentar tanto la implementación como el retroceso para futura iteración |
