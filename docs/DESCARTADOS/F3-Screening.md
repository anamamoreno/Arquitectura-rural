# Fase 3 — Screening y selección

**Producto 1 — Levantamiento de información**
**Plantilla operativa:** se llena en vivo durante la ejecución (días V5 a L6).
**Versión:** 0.1 (vacía) · **Fecha:** _pendiente de inicio_.

---

## 1. Propósito

Filtrar el universo bruto generado en Fase 2 a un conjunto de fuentes definitivas que entrarán a la matriz M1. Documentar inclusiones y descartes de forma trazable para satisfacer requisitos tipo PRISMA simplificado.

## 2. Flujo de screening

El proceso se ejecuta en 2 pasos secuenciales:

**Paso 1 — Lectura conjunta de título + resumen.** Ambos responsables revisan los títulos/resúmenes juntos; descarte por consenso rápido.

**Paso 2 — Lectura a texto completo.** Solo para las fuentes que pasan el paso 1. Verificación contra criterios de inclusión/exclusión detallados.

**Dudas:** se marcan en la columna `Observaciones` y se resuelven en sync diaria.

## 3. Criterios aplicados

### 3.1 Inclusión (ver `F1-Protocolo_busqueda.md` §3)
- Trata ≥1 de los 5 ejes (E1–E5).
- Aplicable a vivienda rural, VISR, VIPR o unifamiliar baja en contexto rural colombiano.
- Clima colombiano o asimilable por analogía andina/tropical.
- Idioma: español, inglés o portugués.
- Publicado ≥2015 (excepciones: vernáculo y normativa histórica CO).
- Accesible a texto completo.
- **Filtro preferencial Colombia** ante fuentes equivalentes.

### 3.2 Exclusión (ver `F1-Protocolo_busqueda.md` §4)
- Vivienda multifamiliar urbana >4 pisos.
- Clima templado europeo/continental sin adaptación tropical.
- Publicaciones comerciales sin datos independientes.
- Duplicados (se conserva la más completa).
- Países no andinos sin analogía climática útil.

## 4. Embudo PRISMA simplificado

Al cierre de F3, reportar números del flujo completo:

| Etapa | Número de fuentes |
|---|---|
| Identificación (brutas de F2) |  |
| Tras deduplicación |  |
| Cribado por título/resumen (paso 1) — incluidas |  |
| Cribado por título/resumen — descartadas |  |
| Lectura a texto completo (paso 2) — incluidas |  |
| Lectura a texto completo — descartadas |  |
| **Total incluidas definitivas (entran a M1)** |  |

## 5. Registro de descartes justificados

Cualquier fuente descartada en el paso 2 debe registrarse con razón explícita. No es necesario registrar descartes del paso 1 (se describen agregados).

| ID | Fuente | Eje | Clima | Razón de descarte | Criterio violado |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

**Categorías típicas de razón:** temporal (pre-2015 no excepcional) · tipológico (urbano o >4 pisos) · climático (sin adaptación al contexto CO) · metodológico (sin evidencia cuantitativa o documental) · acceso (texto completo no disponible) · duplicado · otro.

## 6. Registro de dudas resueltas

Fuentes que generaron discusión entre responsables durante el screening.

| ID | Fuente | Duda | Resolución | Quién decidió |
|---|---|---|---|---|
|  |  |  |  |  |

## 7. Balance por eje y clima al cierre

Conteo de fuentes incluidas definitivas, para detectar desequilibrios antes de pasar a F4:

| Eje \ Clima | Frío | Templado | Cálido seco | Cálido húmedo | Total eje |
|---|---|---|---|---|---|
| E1 Bioclimática |  |  |  |  |  |
| E2 Energía |  |  |  |  |  |
| E3 Agua |  |  |  |  |  |
| E4 Materiales |  |  |  |  |  |
| E5 Metodologías |  |  |  |  |  |
| **Total clima** |  |  |  |  |  |

**Alerta:** combinaciones con <2 fuentes definitivas se marcan como **vacíos** y se documentan en Fase 5.

## 8. Indicadores de calidad

- % de fuentes con `origen_CO = sí`: _%_ (meta ≥60%)
- % de fuentes con evidencia cuantitativa: _%_
- % de fuentes con año ≥2020: _%_
- Dudas resueltas vs. dudas escaladas a expertos: _N / N_

## 9. Entregables de la fase

1. Este documento con todos los registros y números cerrados.
2. Embudo PRISMA consolidado (sección 4).
3. Biblioteca Zotero con tag `incluida-M1:si/no` en cada referencia.
4. Lista preliminar de vacíos por combinación eje × clima — para alimentar Fase 5.

## 10. Transición a Fase 4

Las fuentes marcadas como "incluidas definitivas" pasan a Fase 4 (Extracción a matriz M1). Cada fila de M1 debe poder rastrearse hasta una fuente incluida en este documento.

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | _pendiente_ | Plantilla inicial vacía, lista para llenar durante ejecución |
