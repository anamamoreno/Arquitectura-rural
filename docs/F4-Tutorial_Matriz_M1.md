# Tutorial: cómo llenar la Matriz M1

> **¿Qué es este documento?** Guía rápida paso a paso para que cualquier integrante del equipo de búsqueda pueda abrir, entender y llenar correctamente la Matriz M1 sin necesidad de leer el diccionario completo. Para definiciones detalladas de cada columna, consultar `F4-Matriz_M1_diccionario.md`.

---

## 1. Qué es la Matriz M1

Es un archivo CSV (`F4-Matriz_M1.csv`) que se abre en Excel o Google Sheets. Funciona como el **inventario central** de todo lo levantado en el Producto 1.

- **Una fila = un hallazgo** (una estrategia, un material, un complemento o una metodología) documentado en una fuente.
- **Cada columna = un atributo** del hallazgo (de dónde viene, a qué eje pertenece, en qué clima aplica, etc.).
- Al cierre del proyecto, los arquitectos y expertos filtran esta matriz para seleccionar qué entra en la guía final.

## 2. Cómo abrirla

1. Ir a `docs/F4-Matriz_M1.csv`.
2. **Excel:** doble clic en el archivo. Si todo aparece en una sola columna, ir a `Datos → Desde texto/CSV` y seleccionar separador **coma** y codificación **UTF-8**.
3. **Google Sheets:** subir el archivo a Drive → Abrir con Google Sheets.
4. Las primeras 3 filas son **ejemplos** para entender el formato. Pueden eliminarse cuando se empiece a llenar en firme.

## 3. Las 20 columnas explicadas en una frase

| # | Columna | Qué poner |
|---|---|---|
| 1 | `ID` | Código único: eje + correlativo. Ej. `E1-001`, `E4-023` |
| 2 | `Fuente` | Cita corta: Autor (Año) o Institución (Año). Ej. `MVCT (2025)` |
| 3 | `Año` | Año de publicación: `2025` |
| 4 | `Tipo_fuente` | Categoría: `normativa` · `academica` · `tesis` · `vernaculo` · `cartilla-MVCT` · `multilateral` · `gremio` · `caso-aplicado` |
| 5 | `Origen_CO` | ¿Es fuente colombiana? `si` o `no` |
| 6 | `Eje` | Eje temático: `E1` (bioclimática pasiva) · `E2` (energía activa) · `E3` (eficiencia hídrica) · `E4` (materiales sostenibles) · `transversal` (metodologías, proceso, NSR-10) |
| 7 | `Clima_TdR` | Clima del contrato: `calido_humedo` · `calido_seco` · `templado` · `frio` · `todos` |
| 8 | `Subtipo_Köppen` | Solo si la fuente diferencia: `Af` · `Am` · `Aw` · `BSh` · `BWh` · `Cfb` · `Cwb` · `ET`. Si no, dejar vacío |
| 9 | `Sistema_constructivo` | Sistema al que aplica: `tapia` · `bahareque` · `guadua` · `mamposteria-confinada` · `palafito-madera` · `todos`. Usar la taxonomía acordada con arquitectos |
| 10 | `Tipo` | Qué es el hallazgo: `estrategia` · `material` · `complemento` · `metodologia` |
| 11 | `Medida` | Naturaleza: `pasiva` · `activa` · `hibrida` · `na` (si es material o metodología) |
| 12 | `Nombre_medida` | Nombre corto: `Inercia térmica en muros de tapia` |
| 13 | `Descripcion_corta` | Máx. 200 caracteres: qué es y cómo funciona |
| 14 | `Metrica_desempeno` | Dato cuantitativo si existe: `U = 1.2 W/m²K` · `ahorro 15%`. Si no hay, dejar vacío |
| 15 | `Nivel_tecnico` | Para qué audiencia: `tecnico` · `gestor` · `usuario` · `todos` |
| 16 | `Medida_Anexo1_ref` | Código medida Res. 0194 Anexo 1: `MP-14` · `MA-02` · `MW-06`. Si no aplica, vacío |
| 17 | `Criterio_0534_ref` | Código criterio Guía Ciclo de Vida Res. 0534: `A-E-1` · `S-CT-1` · `A-M-1`. Múltiples con `;`. Si no aplica, vacío |
| 18 | `Criterio_CEELA_ref` | Código principio CEELA: `C01` a `C15`. Múltiples con `;`. Si no aplica, vacío |
| 19 | `Aplicable_VIS_VIP` | ¿Funciona para vivienda social rural? `si` · `no` · `condicional` |
| 20 | `Enfoque_genero_inclusion` | Impacto diferencial si existe. Ej. `Reduce exposición a humo en mujeres que cocinan`. Si no aplica, dejar vacío |
| 21 | `Observaciones` | Notas libres: costo, durabilidad, GWP, limitaciones. No usar comas; usar punto y coma (;) si se necesita enumerar |

## 4. Paso a paso para agregar una fila

**Ejemplo real:** encontraste en un paper de SciELO una estrategia de ventilación cruzada para clima cálido húmedo en viviendas de bahareque del Caribe.

### Paso 1 — Asignar ID
Mira el último ID del eje E1. Si el último es `E1-015`, el tuyo es `E1-016`.

### Paso 2 — Llenar la fila

| Columna | Valor de ejemplo |
|---|---|
| ID | `E1-016` |
| Fuente | `Rodríguez & Pérez (2021)` |
| Año | `2021` |
| Tipo_fuente | `academica` |
| Origen_CO | `si` |
| Eje | `E1` |
| Clima_TdR | `calido_humedo` |
| Subtipo_Köppen | `Am` |
| Sistema_constructivo | `bahareque` |
| Tipo | `estrategia` |
| Medida | `pasiva` |
| Nombre_medida | `Ventilación cruzada con aberturas opuestas` |
| Descripcion_corta | `Aberturas en fachadas opuestas orientadas al viento dominante permiten flujo continuo que reduce temperatura interior 3-5°C en clima Am` |
| Metrica_desempeno | `Reducción 3-5°C; 12 ACH promedio` |
| Nivel_tecnico | `tecnico` |
| Medida_Anexo1_ref | `MP-14` |
| Criterio_0534_ref | `S-CT-1; S-A-1` |
| Criterio_CEELA_ref | `C06` |
| Aplicable_VIS_VIP | `si` |
| Enfoque_genero_inclusion | |
| Observaciones | `Requiere orientación NE-SO según vientos alisios del Caribe; no funciona en terrenos encañonados` |

### Paso 3 — Verificar
- ¿`Eje` y `Clima_TdR` coinciden con lo que dice la fuente?
- ¿`Origen_CO` está marcado?
- ¿Las 3 columnas normativas están bien? Consultar:
  - `F0-3b-Medidas_Anexo1_Cap2.md` para códigos MP/MA/MW.
  - `F0-3d-Criterios_Guia_Ciclo_Vida.md` para códigos A-E, S-CT, etc.
  - `F0-3c-Cruce_Estandares_Ejes.md` para códigos C01–C15.

### Paso 4 — Guardar
Guardar el CSV. Si trabajas en Excel, guardar como **CSV UTF-8** (no como .xlsx) para mantener compatibilidad.

## 5. Reglas de oro

| Regla | Por qué |
|---|---|
| **Una fuente con 5 estrategias = 5 filas** | Cada hallazgo es una fila independiente |
| **Misma estrategia en 2 fuentes = 2 filas** | Preserva trazabilidad; cada fila apunta a su fuente |
| **No inventar métricas** | Si la fuente no da dato cuantitativo, dejar `Metrica_desempeno` vacío |
| **No usar comas en las celdas** | Rompen el CSV; usar punto y coma (;) para listas |
| **Dejar vacío lo que no aplica** | No escribir "N/A" ni "-"; simplemente dejar la celda sin contenido |
| **Marcar siempre `Origen_CO`** | Es la columna que permite medir si la meta ≥60% fuentes colombianas se cumple |
| **Llenar `Eje` y `Clima_TdR` siempre** | Son las 2 columnas más usadas para filtrar; nunca dejarlas vacías |

## 6. Errores comunes y cómo evitarlos

| Error | Consecuencia | Solución |
|---|---|---|
| Poner el eje equivocado | Una estrategia de captación pluvial queda en E1 (bioclimática) en vez de E3 (agua) | Preguntarse: ¿es diseño arquitectónico (E1)? ¿sistema mecánico/eléctrico (E2)? ¿agua (E3)? ¿sobre el material (E4)? ¿método de análisis (E5)? |
| No llenar `Subtipo_Köppen` cuando la fuente sí diferencia | Se pierde granularidad para el análisis post-hoc | Si la fuente habla de "Pacífico chocoano" → poner `Af`; si dice "Caribe" → poner `Am` |
| Poner `Sistema_constructivo = todos` cuando aplica a uno | Dificulta el filtrado posterior de los arquitectos | Solo usar `todos` cuando realmente la estrategia es agnóstica al sistema |
| Escribir descripciones largas | Celda difícil de leer en Excel | Máximo 200 caracteres en `Descripcion_corta`; el detalle va en `Observaciones` |
| Olvidar guardar como CSV UTF-8 | Caracteres especiales (ñ, tildes, ° ) se corrompen | En Excel: Archivo → Guardar como → CSV UTF-8 (delimitado por comas) |

## 7. Checklist rápido antes de cerrar el día

- [ ] ¿Todas las filas nuevas tienen `ID`, `Fuente`, `Eje`, `Clima_TdR` y `Origen_CO`?
- [ ] ¿El correlativo del `ID` sigue en orden sin saltos ni duplicados?
- [ ] ¿Guardé como CSV UTF-8?
- [ ] ¿Actualicé la referencia en Zotero con el tag correspondiente?

## 8. Dónde consultar más

- **Diccionario completo** (valores permitidos, reglas de llenado, campos diferidos): `F4-Matriz_M1_diccionario.md`
- **Matriz de búsqueda BS-** (de qué acción de búsqueda proviene cada fila de M1): `F1-Matriz_busqueda.csv` + tutorial `F1-Tutorial_Matriz_busqueda.md`
- **Marco de sistemas y materiales** (listas de referencia para columnas `Sistema_constructivo`, materiales y complementos): `F1-Marco_busqueda_sistemas_materiales.md`
- **Códigos de medidas del Anexo 1** (MP-01 a MP-15, MA-01 a MA-14, MW-01 a MW-07): `F0-3-Síntesis-Anexo1.md` §4
- **Mapeo climático** (qué región va con qué clima/Köppen): `F0-2-Mapeo_climatico.md` §3
- **Tesauro colombiano** (términos vernáculos, regiones, autores): `F1-Protocolo_busqueda.md` §5

## 9. Flujo conjunto F1 ↔ F4

Cada fila de M1 proviene de una acción de búsqueda planeada en `F1-Matriz_busqueda.csv`:

```
F1-Matriz_busqueda.csv        F4-Matriz_M1.csv
(qué buscar)                  (qué se encontró)

BS-007 tapia cálido seco  ──► E1-005 Fonseca 2019
                          ──► E1-008 Rodríguez 2021
                          ──► E1-012 Chávez 2020
                          ──► E4-003 Uniandes-CCCS 2021
```

Al agregar una fila a M1, **anotar en BS- el nuevo ID** en la columna `Fuentes_clave_M1` (separados por `;`). Eso mantiene trazabilidad en ambas direcciones.
