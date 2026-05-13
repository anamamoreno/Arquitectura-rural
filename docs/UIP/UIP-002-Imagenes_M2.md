# UIP — Enriquecimiento de fichas M2 con imágenes

**Estado:** 🟦 EN COLA / REVERTIDA — Se intentó ejecutar el 2026-05-12 con extracción automática de PDFs (D1=A) pero el resultado fue de baja calidad: las imágenes seleccionadas automáticamente (por orden secuencial + tamaño) tendían a ser mapas, paisajes y diagramas contextuales en lugar de fotos de las viviendas. Cambios revertidos el 2026-05-13. **Pendiente:** re-implementar con análisis visual de contenido (clasificar imágenes como vivienda vs contexto) — opción D1=A híbrida con curación visual, o D1=C URLs externas (ArchDaily, sitios de arquitectos), o D1=B captura manual de PDF.
**Fecha:** 2026-05-02
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
