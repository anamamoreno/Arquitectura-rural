# Resumen ejecutivo — Producto 1: Levantamiento de información

**Proyecto:** Guía técnica de sostenibilidad para vivienda rural en los 4 climas de Colombia (Anexo 1 Res. 0194/2025 + criterios CEELA).
**Producto 1:** Levantamiento de información sobre estándares de sostenibilidad para eficiencia energética, hídrica, materiales sostenibles y confort ambiental aplicables a tipologías de vivienda rural existentes.
**Responsable Producto 1:** Ana María Moreno.
**Fecha de corte:** 2026-05-06.

---

## 1. Alcance del Producto 1 (TdR)

| Eje | Cobertura |
|---|---|
| **E1 Bioclimática pasiva** | Confort térmico/lumínico sin sistemas mecánicos |
| **E2 Eficiencia energética activa** | Sistemas mecánicos/eléctricos de bajo consumo |
| **E3 Eficiencia hídrica** | Captación, ahorro, reúso y tratamiento |
| **E4 Materiales sostenibles** | ACV, energía embebida, toxicidad, origen, circularidad |

Aplicabilidad: 4 climas TdR (frío, templado, cálido húmedo, cálido seco) + 8 subtipos Köppen como capa analítica. Enfoque obligatorio de género e inclusión (Ley 2462/2025 + Sentencia T-333/22).

---

## 2. Lo entregado a la fecha

### 2.1 Estrategia y plan de trabajo
- **`docs/F0-4-Producto1-Estrategia.md`** — estrategia adaptada a 2 semanas con base pre-validada (versión activa B-0.1)
- **`docs/F0-Plan_trabajo.md`** — cronograma de 10 días hábiles 2026-04-14 → 2026-04-28
- **Decisiones metodológicas clave:**
  - Estructura climática 4 climas TdR + capa analítica Köppen-Geiger
  - Vacíos a priori declarados: páramo (ET) y alta Guajira (BWh)
  - Protocolo trazable tipo PRISMA simplificado
  - Zotero como gestor bibliográfico
  - Productos del contrato priorizados: 1) Protocolo, 2) Biblioteca Zotero, 3) **Matrices (corazón)**, 4) Informe vacíos, 5) Fichas vernáculas

### 2.2 Protocolo de búsqueda
- **`docs/F1-Protocolo_busqueda.md`** (B-0.3, ACTIVA) — protocolo Colombia-focused:
  - 12 ecuaciones EN + 12 ES tensadas al contexto nacional
  - 6 bases consultadas incluyendo repositorios universitarios CO
  - Filtro preferencial CO con marca `origen_CO` y `tipo_fuente_CO`
  - Meta ≥60% fuentes colombianas
- **`docs/F1-Marco_busqueda_sistemas_materiales.md`** — definición de subsistemas y materiales para la búsqueda
- **`docs/F2-Ejecucion_busquedas.md`** — bitácora de ejecución de búsquedas en bases académicas (OpenAlex completado, otras parciales)
- **`docs/F2-Guia_Zotero_proyecto.md`** — guía de uso de Zotero para el proyecto
- **`docs/F6-Plan_busqueda_casos.md`** — protocolo específico para Track B (casos de éxito M2)

### 2.3 Matriz M1 — Estándares de sostenibilidad

**Archivo:** `docs/F0-Matriz_estandares_sostenibilidad.csv`

**Cifras:**
- **181 filas** (criterios, medidas, principios, enfoques, fines aplicables a vivienda rural)
- **25 referencias normativas/documentales** con URL pública verificada
- **20 columnas** estandarizadas
- **100% aplicables a vivienda rural** (`si` 157 + `condicional` 24); las 10 filas `no` se eliminaron el 2026-05-06

**Cobertura por marco:**

| Marco | Filas | Aporte clave |
|---|---|---|
| Res. 0534/2025 | 53 | Columna vertebral. Criterios sostenibilidad ciclo de vida (ambiental, social, económico) |
| Res. 0194/2025 | 38 | Anexo 1: 38 medidas técnicas obligatorias (15 pasivas + 13 activas + 10 hídricas) |
| Ley 2462/2025 | 28 | Enfoque género e inclusión rural (12 enfoques + 16 fines) |
| CEELA | 15 | Marco regional voluntario (los 15 criterios del programa COSUDE) |
| UPME-PGEE | 10 | Gestión eficiente energía (diagnóstico, IDE, ISO 50001, RETIQ) |
| RAS, RETILAP, SUDS, R0019, GuiaMej, EC-MADS, PNVISR, ParamSFVR + 13 más | 47 | Reglamentos y estándares complementarios |

**Documentación de soporte:**
- **`docs/F0-Tutorial_Matriz_estandares.md`** — tutorial completo de los 20 campos (v0.3)
- **`docs/F0-Lista_referencias_y_aportes.md`** — inventario detallado de las 25 fuentes con URL clickeable, distribución por categoría/eje/carácter legal y alertas vigentes (v0.5)

### 2.4 Matriz M2 — Casos de éxito y vernáculos

**Archivo:** `docs/F0-Matriz_casos_exito.csv`

**Cifras:**
- **31 casos** compilados (todos en estado `pendiente_revision` para validación de la responsable)
- **29 columnas** con campos enriquecidos por subagente automático
- **10 fuentes documentales** procesadas (5 en proyecto + 5 nuevas tesis universitarias)

**Distribución por clima TdR (cuotas TdR cumplidas):**
| Clima | Casos | Vs. mínimo (≥2/clima) |
|---|---|---|
| Frío | 4 | ✅ Vacío crítico cubierto (Misak, Chita, Cuche vernáculo + prototipo) |
| Templado | 9 | ✅ Sobrecubre (eje cafetero, Belén de Umbría) |
| Cálido húmedo | 16 | ✅ Sobrecubre (Pacífico, Caribe, Llanos, Amazonía) |
| Cálido seco | 2 | ✅ Mínimo (ette, wayúu) |

**Distribución por sistema constructivo:**
- Bahareque (11), palafito-madera (5), mampostería (3), madera (5), mixto (5), adobe puro (1), tapia (1, mixto)
- Vacíos relativos: tapia pisada pura, guadua estructural pura

**Tipos:** 21 vernáculos, 9 contemporáneos, 1 mixto.

**Documentación de soporte:**
- **`docs/F6-Plan_busqueda_casos.md`** — plan completo del Track B (cuotas, fuentes, criterios, protocolo)
- **`docs/F7-Ejecucion_busqueda_casos.md`** — bitácora de ejecución
- **`docs/F8-Matriz_casos_diccionario.md`** — diccionario de las 29 columnas (v0.5)

### 2.5 Glosario y terminología

**Archivo:** `docs/Glosario_terminos.md` (v0.4)

Define la jerarquía conceptual del marco normativo:

```
FIN          ← qué impacto buscamos               (Ley 2462)
ENFOQUE      ← desde qué perspectiva miramos      (Ley 2462, PNVISR)
ESTÁNDAR     ← qué referencia usamos              (TdR-CEELA, marco general)
ESTRATEGIA   ← qué táctica aplicamos              (Anexo 1: E1/E2/E3/E4)
CRITERIO     ← qué desempeño evaluamos            (CEELA: 15; Res. 0534: 56)
MEDIDA       ← qué acción técnica ejecutamos      (Anexo 1: 38 MP/MA/MW)
```

Cada término con: definición, fuente normativa que lo emplea, ejemplo concreto en M1 y relación con los demás términos.

Incluye:
- Sigla **EECA** (Eficiencia Energética y Confort Adaptativo) — marco CEELA
- Sección "Términos pragmáticos del campo `Tipo` de M1" para mapear sub-tipos (`criterio_*`, `medida_*`) a la jerarquía vertical
- Convenciones de codificación (prefijos MP-, MA-, MW-, A-, S-, E-, C, L-E, L-F, UPME-, RET-, R0019-, SUDS-, etc.)

### 2.6 Aplicación de consulta interactiva

**Archivo:** `scripts/app_matriz_estandares.py` (Streamlit)

**Acceso:**
- **Local:** http://localhost:8504/m1 y /m2
- **VPS público:** https://app.uxtic.co/artefactos/viviendarural/m1 (modo solo lectura)

**Funcionalidades:**
- **Página M1 (Estándares):** filtros por referencia, eje, clima, subsistema, carácter legal, aplicabilidad rural, etapa ciclo de vida, conexión Ley 2462. Tabla con columnas seleccionables. **URL fuente clickeable** para abrir el documento original. Métricas y distribuciones por referencia/eje/clima/tipo
- **Página M2 (Casos):** filtros sidebar (estado, clima, tipo, sistema, archivo fuente con conteo). Tarjetas por caso con badges (tipo + clima + sistema). Cruce automático con M1: cada caso muestra los IDs de estándares que materializa. **Validación con write-back protegido por file lock** (multiusuario nivel 1). Botones validar/descartar/reactivar con auditoría (`Validado_por`, `Fecha_validacion`)
- **Modo READ_ONLY** en VPS: oculta validación; muestra datos como referencia consultable

**Despliegue VPS (`docs/UIP-001-Despliegue_VPS.md`):**
- Patrón Docker estilo `uxtic-artefacto-enjambres`
- Container: `uxtic-artefacto-viviendarural` en red `uxtic-git_uxtic-network`
- Nginx Docker en `app.uxtic.co/artefactos/viviendarural/` con WebSocket support
- Repo: https://github.com/anamamoreno/Arquitectura-rural

- Actualización: `git push` local → `git pull && docker compose up -d --build` en VPS

---

## 3. Cifras clave consolidadas

| Indicador | Valor |
|---|---|
| Documentos normativos revisados | 35 |
| Referencias en M1 | 25 |
| Filas en M1 | 181 |
| Casos en M2 | 31 (todos pendientes de validación) |
| Climas TdR cubiertos en M2 | 4/4 ✅ |
| Sistemas constructivos identificados | 8 |
| Productos documentales entregados | 16 docs activos en `docs/` |
| Extracciones de texto plano de PDFs | 50+ archivos |
| Líneas de código de la app | ~600 |
| Commits en GitHub | 5 |

---

## 4. Pendientes y alertas vigentes

### Pendientes del Producto 1
- **Validación de los 31 casos M2** por la responsable (proceso interactivo en la app)
- **Bitácora F2 retroactiva** — completar bitácora de ejecución de las búsquedas OpenAlex realizadas
- **Bitácora F3 Screening** — documentar el embudo PRISMA simplificado de los hallazgos
- **F5 Síntesis y cierre** — 3 entregables aún por construir:
  - Tabla de mapeo Anexo 1 ↔ CEELA
  - Informe preliminar de vacíos normativos y de evidencia
  - Fichas cortas de casos vernáculos (5–10 por clima)

### Alertas en el inventario de referencias
- **CEELA**: PDF parcial obtenido (landing page proyectoceela.com); el detalle de los 15 principios está en biblioteca web del programa
- **RAS** (70 MB): revisado parcialmente — posibles 3–5 filas adicionales de agua rural
- **Caja de la Vivienda Popular Bogotá**: 241 mejoramientos 2014–2018 en Sumapaz/Usme/Ciudad Bolívar identificados como universo, fichas individuales pendientes de obtener para cubrir vacío frío Cundinamarca

### Diferidos (UIPs)
- **Imágenes en fichas M2** (`docs/UIP-Imagenes_M2.md`) — diferida explícitamente por usuaria

---

## 5. Cómo acceder a los productos

| Producto | Ubicación |
|---|---|
| Repositorio Git | https://github.com/anamamoreno/Arquitectura-rural |
| App pública (solo lectura) | https://app.uxtic.co/artefactos/viviendarural/m1 |
| App local (validación) | http://localhost:8504/m1 |
| Carpeta proyecto local | `C:\Users\user\Proyecto-Arq_Rural\` |
| Matriz M1 (CSV) | `docs/F0-Matriz_estandares_sostenibilidad.csv` |
| Matriz M2 (CSV) | `docs/F0-Matriz_casos_exito.csv` |
| Tutorial M1 | `docs/F0-Tutorial_Matriz_estandares.md` |
| Lista de referencias con URL | `docs/F0-Lista_referencias_y_aportes.md` |
| Glosario | `docs/Glosario_terminos.md` |
| Plan búsqueda casos | `docs/F6-Plan_busqueda_casos.md` |
| Diccionario M2 | `docs/F8-Matriz_casos_diccionario.md` |
| Estrategia Producto 1 | `docs/F0-4-Producto1-Estrategia.md` |
| PDFs fuente (locales) | `FUENTES/` y `Referencias-estandares/` |

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | 2026-05-05 | Resumen ejecutivo inicial — estado del Producto 1 a la fecha |
| 1.1 | 2026-05-06 | Sincronización con M1 reducida: 191 → 181 filas, 26 → 25 referencias (eliminadas 10 filas `Aplica_vivienda_rural=no`: 8 medidas Res.0194 no rurales + 2 R0019 FRECH NO VIS) |
