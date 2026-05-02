# B — Matriz M1: diccionario de datos

**Archivo operativo:** `F4-Matriz_M1.csv` (misma carpeta).
**Propósito:** definir el significado, valores permitidos y ejemplos de cada columna de M1.
**Versión:** B-0.1 · **Fecha:** 2026-04-15.

---

## 1. Reglas generales de llenado

- **Una fila = un estándar, estrategia, material o complemento** documentado en una fuente.
- Si una misma estrategia aparece en 2 fuentes distintas, son **2 filas** (para preservar trazabilidad), con IDs distintos.
- Si una misma fuente reporta varias estrategias, son **varias filas** con el mismo campo `Fuente` pero distinto `ID`.
- Campos sin aplicación: dejar **vacío** (no "N/A", no "-"), excepto donde se indique lo contrario.
- Los textos largos van en `Descripcion_corta` u `Observaciones`. No usar comas en celdas (rompen el CSV); usar `;` si es necesario enumerar.
- Idioma de llenado: **español**. Citar términos originales entre paréntesis si son en EN/PT.

## 2. Diccionario de columnas

| # | Columna | Tipo | Valores permitidos / formato | Ejemplo |
|---|---|---|---|---|
| 1 | `ID` | texto | `EJE-NNN` correlativo por eje | `E1-001`, `E4-045` |
| 2 | `Fuente` | texto | Cita corta: Autor (Año) o Institución (Año) | `MVCT (2025)` · `Uniandes-CCCS (2021)` |
| 3 | `Año` | entero | YYYY | `2025` |
| 4 | `Tipo_fuente` | categórica | `normativa` · `academica` · `tesis` · `vernaculo` · `cartilla-MVCT` · `multilateral` · `gremio` · `caso-aplicado` | `normativa` |
| 5 | `Origen_CO` | binaria | `si` · `no` | `si` |
| 6 | `Eje` | categórica | `E1` (bioclimática pasiva) · `E2` (energía activa) · `E3` (eficiencia hídrica) · `E4` (materiales sostenibles) · `transversal` (metodologías pre-diseño, NSR-10, proceso) | `E1` |
| 7 | `Clima_TdR` | categórica | `calido_humedo` · `calido_seco` · `templado` · `frio` · `todos` · `no_aplica` | `frio` |
| 8 | `Subtipo_Köppen` | categórica | `Af` · `Am` · `Aw` · `BSh` · `BWh` · `Cfb` · `Cwb` · `ET` · `todos` · vacío | `ET` |
| 9 | `Sistema_constructivo` | texto | Valor de la taxonomía (pendiente cierre con arquitectos). Ejemplos provisionales: `tapia`, `bahareque`, `adobe`, `BTC`, `mamposteria-confinada`, `guadua`, `palafito-madera`, `prefabricado-ligero`, `todos` | `tapia` |
| 10 | `Tipo` | categórica | `estrategia` · `material` · `complemento` · `metodologia` | `estrategia` |
| 11 | `Medida` | categórica | `pasiva` · `activa` · `hibrida` · `na` (si es material o metodología) | `pasiva` |
| 12 | `Nombre_medida` | texto | Nombre corto de la medida o material | `Inercia térmica con muro de tapia` |
| 13 | `Descripcion_corta` | texto | Máx. 200 caracteres; qué es y cómo funciona | `Muro de tapia pisada ≥40 cm aprovecha masa térmica para estabilizar temperatura en clima frío con alta oscilación diaria` |
| 14 | `Metrica_desempeno` | texto | Valor + unidad cuando exista; si no, vacío | `U = 1.2 W/m²K` · `ahorro 15%` · `50 l/persona/día` |
| 15 | `Nivel_tecnico` | categórica | `tecnico` · `gestor` · `usuario` · `todos` | `tecnico` |
| 16 | `Medida_Anexo1_ref` | texto | Código de medida del Anexo 1 Res. 0194: `MP-NN` (pasiva), `MA-NN` (activa), `MW-NN` (agua). Ver `F0-3b-Medidas_Anexo1_Cap2.md` | `MP-14` |
| 17 | `Criterio_0534_ref` | texto | Código de criterio de la Guía Ciclo de Vida Res. 0534: `A-E-N`, `A-A-N`, `A-EM-N`, `A-M-N`, `A-S-N`, `A-R-N`, `A-FL-N`, `A-SE-N`, `S-CT-N`, `S-CL-N`, `S-A-N`, `S-CA-N`, `S-H-N`, `S-AC-N`, `S-AS-N`, `E-CI-N`, `E-CC-N`. Múltiples separados por `;`. Vacío si no aplica. Ver `F0-3d-Criterios_Guia_Ciclo_Vida.md` | `S-CT-1` · `A-E-1; A-M-1` |
| 18 | `Criterio_CEELA_ref` | texto | Código de principio CEELA: `C01` a `C15`. Múltiples separados por `;`. Vacío si no aplica. Ver `F0-3c-Cruce_Estandares_Ejes.md` | `C04` |
| 19 | `Aplicable_VIS_VIP` | categórica | `si` · `no` · `condicional` | `si` |
| 20 | `Enfoque_genero_inclusion` | texto | Describe impacto diferencial si aplica; vacío si no | `Reduce exposición a humo en mujeres que cocinan >3h/día` |
| 21 | `Observaciones` | texto | Notas libres: vacíos; costo; durabilidad; requisitos específicos; GWP/EPD si aplica a material | `GWP: 0.08 kg CO2eq/kg; origen regional <300km` |

## 3. Campos especialmente sensibles

### `Eje` y `Clima_TdR`
Son las dos columnas con las que filtrará el 80 % de las consultas. **Obligatorias siempre**.

### `Sistema_constructivo`
**Provisional** hasta validación con arquitectos hoy 2026-04-15. Posibles ajustes se aplicarán en bloque.

### `Subtipo_Köppen`
Solo poblar cuando la fuente diferencie. Si la fuente habla genéricamente de "cálido húmedo", dejar vacío y el clima TdR basta.

### `Medida_Anexo1_ref`, `Criterio_0534_ref`, `Criterio_CEELA_ref`
Son las 3 columnas de **trazabilidad normativa**. Permiten demostrar que cada estrategia está respaldada por al menos uno de los 3 marcos (Res. 0194, Res. 0534, CEELA). Si una estrategia no aparece en ninguno de los 3, dejar las 3 vacías — es un **hallazgo fuera de norma** que puede ser vernáculo o innovador.

Para llenar, consultar:
- `F0-3b-Medidas_Anexo1_Cap2.md` — códigos MP/MA/MW.
- `F0-3d-Criterios_Guia_Ciclo_Vida.md` — códigos A-E, A-A, A-EM, A-M, etc.
- `F0-3c-Cruce_Estandares_Ejes.md` — cruce de los 95 criterios × 4 ejes.

### `Origen_CO`
Útil al cierre para contar qué % de M1 tiene anclaje colombiano. Meta sugerida: ≥60 %.

## 4. Cómo se cruza con M2

Al cierre del P1, filtrar M1 por cada combinación clima × sistema da el subconjunto de estrategias candidatas. Los arquitectos + expertos priorizan 3–5 de cada subconjunto para llenar M2. Por eso las columnas 9 (sistema), 7 (clima) y 10 (tipo) son críticas — son los **ejes de pivoteo de M2**.

## 5. Control de calidad al llenar

- Al cerrar cada día, revisar 5 filas aleatorias: ¿campos obligatorios completos? ¿Eje y Clima_TdR coherentes con la fuente?
- Al llegar a 50 filas, hacer primer conteo: ¿distribución razonable por eje? ¿por clima?
- Al cierre del día 9: QA cruzado 10 % (cada responsable de búsqueda revisa el 10 % de las filas ingresadas por el otro).

## 6. Campos diferidos a versión ampliada (no en B-0.1)

Se excluyen de M1 B-0.1 para no sobrecargar en 2 semanas; quedan como mejora futura:
- `Representabilidad_grafica` (alta/media/baja).
- `Costo_relativo` (bajo/medio/alto).
- `Disponibilidad_local`.
- `Metodologia_verificacion` (cómo se comprueba en obra).
- Columnas E4 detalladas: `GWP_kgCO2eq_kg`, `Contenido_reciclado_pct`, `Origen_regional_km`, `ACV_disponible`, `EPD_disponible`, `Certificacion_SAC`, `Categoria_MasterFormat`. En B-0.1 estas van en `Observaciones` como texto estructurado.

## 7. Ejemplos completos (las 3 filas del CSV)

### Fila 1 — Estrategia pasiva del Anexo 1
- `E1-001`
- `Fuente:` MVCT Anexo 1 Res. 0194/2025
- `Tipo_fuente:` normativa
- `Eje:` E1 · `Clima_TdR:` frio · `Sistema:` tapia · `Tipo:` estrategia · `Medida:` pasiva
- `Nombre:` Inercia térmica en muros
- `Descripcion:` Muros de tapia pisada o adobe de espesor ≥40 cm para estabilizar oscilación diurna en clima frío andino
- `Metrica:` Estabilidad ±3°C; ahorro energético 15% vs línea base
- `Medida_Anexo1_ref:` MP-14 · `Nivel_tecnico:` tecnico
- `Aplicable_VIS_VIP:` si · `Origen_CO:` si

### Fila 2 — Material sostenible de la Cartilla
- `E4-001`
- `Fuente:` Uniandes-CCCS (2021)
- `Tipo_fuente:` cartilla-MVCT
- `Eje:` E4 · `Clima_TdR:` todos · `Tipo:` material · `Medida:` na
- `Nombre:` Tapia pisada
- `Descripcion:` Tierra cruda compactada entre encofrados; tradición colombiana vigente en altiplano y templado
- `Metrica:` GWP ≈ 0.08 kg CO₂eq/kg; origen regional <100 km típico
- `Observaciones:` MasterFormat: Estructura + Mampostería; ACV disponible; EPD no; certificación SAC no aplica a material artesanal
- `Aplicable_VIS_VIP:` si · `Origen_CO:` si

### Fila 3 — Sistema vernáculo
- `E1-002`
- `Fuente:` Fonseca & Saldarriaga (1984) · referencia vía Hábitat Para La Paz
- `Tipo_fuente:` vernaculo
- `Eje:` E1 · `Clima_TdR:` calido_humedo · `Subtipo_Köppen:` Af · `Sistema:` palafito-madera · `Tipo:` estrategia · `Medida:` pasiva
- `Nombre:` Elevación sobre pilotes
- `Descripcion:` Vivienda elevada 1.5–2.5 m sobre pilotes de madera para evacuar pluvial permanente y habilitar ventilación inferior
- `Metrica:` Sin métrica cuantitativa documentada en la fuente
- `Nivel_tecnico:` tecnico
- `Enfoque_genero_inclusion:` Espacio inferior usado típicamente para actividades productivas femeninas (secado pescado, procesamiento alimentos) en comunidades del Pacífico
- `Aplicable_VIS_VIP:` condicional · `Origen_CO:` si

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| B-0.1 | 2026-04-15 | Diccionario inicial — 20 columnas core, 3 filas ejemplo |
