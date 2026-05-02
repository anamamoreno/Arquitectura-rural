# F7 — Ejecución de búsqueda de casos de éxito

**Producto 1 — Track B**
**Plantilla operativa:** se llena en vivo durante la búsqueda.
**Versión:** 0.1 · **Fecha de inicio:** _pendiente_

---

## 1. Propósito

Registrar la ejecución concreta del protocolo definido en `F6-Plan_busqueda_casos.md`: qué fuente se consultó, qué candidatos surgieron, cuáles pasaron screening y entraron a `F0-Matriz_casos_exito.csv`. Sirve como evidencia de trazabilidad PRISMA simplificado para el Track B.

## 2. Bitácora de fuentes consultadas

Una fila por sesión de consulta a una fuente. Se llena al ejecutar.

| ID | Fuente consultada | Categoría (§6 F6) | Fecha | Candidatos brutos | Tras screening | Aceptados a M2 | Observaciones |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

**Convenciones de ID:**
- `BIE-N` — Bienal Colombiana de Arquitectura
- `SCA-N` — Premios SCA
- `CAF-N` — Premios CAF
- `PROA-N`, `ESCA-N`, `ARCH-N`, `PLAT-N` — revistas
- `UNAL-N`, `UNIA-N`, `JAVE-N`, `TADEO-N`, `UCAT-N` — repositorios universitarios
- `HABITAT-N`, `TIERRA-N`, `HPLP-N`, `CARV-N` — ONGs
- `MINCUL-N`, `DNP-N`, `FINDETER-N`, `MVCT-N` — Estado
- `DOC-N` — relectura de PDFs ya en `Referencias-proyecto/`
- `SNOW-N` — snowballing desde un caso aceptado

## 3. Registro de candidatos

Una fila por candidato bruto identificado, antes de screening. Se llena al ir cosechando.

| ID candidato | Nombre | Fuente (ID §2) | Año | Ubicación | Sistema constructivo | Eje principal | ¿Pasa screening? | Si descartado, motivo | Si aceptado, ID en M2 |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

**Convenciones:**
- ID candidato: `CAND-NNN` correlativo
- ¿Pasa screening?: `si` / `no` / `pendiente_lectura_completa`
- Motivos típicos de descarte: `urbano`, `sin_estrategia`, `sin_evidencia`, `solo_conceptual`, `clima_no_atribuible`, `duplicado`, `fuera_alcance_rural`

## 4. Cobertura por celda (clima × sistema)

Tablero vivo para saber qué celdas están cubiertas y cuáles faltan. Actualizar al cerrar cada sesión.

| Clima TdR \ Sistema | tapia | adobe | bahareque | palafito-madera | mampostería confinada | guadua | madera-aserrada | otro |
|---|---|---|---|---|---|---|---|---|
| frio |  |  |  |  |  |  |  |  |
| templado |  |  |  |  |  |  |  |  |
| calido_humedo |  |  |  |  |  |  |  |  |
| calido_seco |  |  |  |  |  |  |  |  |

**Convención:** número de casos aceptados en cada celda. Cuando una celda llega a 2, marcar ` 2 ✓` y bajar prioridad.

## 5. Bitácora diaria

Una entrada al cerrar cada día de trabajo.

### YYYY-MM-DD
- **Fuentes consultadas:** ...
- **Candidatos nuevos:** ...
- **Aceptados a M2:** ...
- **Vacíos detectados:** ...
- **Decisiones:** ...
- **Bloqueos:** ...

## 6. Snowballing

Cada caso aceptado puede generar nuevos candidatos vía sus referencias citadas.

| Caso fuente (ID en M2) | Referencia citada | Candidato generado (ID §3) |
|---|---|---|
|  |  |  |

## 7. Vacíos y decisiones de marcado

Lista de pares `clima × sistema` donde tras búsqueda exhaustiva no se logró cubrir el mínimo. Se trasladan al informe F5.

| Clima | Sistema | Casos encontrados | Razón del vacío | Acción |
|---|---|---|---|---|
|  |  |  |  |  |

## 8. Cierre de F7

F7 se considera completa cuando:
- Cobertura mínima de §4 alcanzada (≥2 por clima, idealmente ≥1 por celda clima×sistema)
- Bitácora §5 cerrada con resumen de fuentes con mayor rendimiento
- Vacíos §7 listados y trasladados a F5
- `F0-Matriz_casos_exito.csv` poblada con todos los casos aceptados
