# Tutorial: cómo llenar la Matriz de búsqueda

> **¿Qué es este documento?** Guía paso a paso para operar `F1-Matriz_busqueda.csv` durante la ejecución. Explica qué hace cada columna, cómo trabajar una fila (acción de búsqueda) y cómo registrar resultados. Para el marco conceptual (qué es un sistema constructivo, listas de materiales y complementos), consultar `F1-Marco_busqueda_sistemas_materiales.md`.

**Versión:** 0.1 · **Fecha:** 2026-04-16.

---

## 1. Qué es la Matriz de búsqueda

Es un archivo CSV (`F1-Matriz_busqueda.csv`) que organiza las **acciones de búsqueda** del Producto 1. Cada fila es una tarea concreta de investigación sobre una combinación específica de clima, sistema/material/complemento y eje de sostenibilidad.

**Diferencia clave con la Matriz M1:**

| Matriz de búsqueda (F1) | Matriz M1 (F4) |
|---|---|
| **Qué buscar** — planeación | **Qué se encontró** — hallazgos |
| 77 filas iniciales | ~100–150 filas esperadas |
| Una fila = una acción de búsqueda | Una fila = una fuente individual con un hallazgo |
| Se cierra cuando la búsqueda termina | Se puebla a medida que aparecen fuentes |

**Relación 1:N** — una acción de búsqueda (BS-NNN) puede generar múltiples filas en M1 (E1-NNN, E4-NNN, etc.).

## 2. Cómo abrirla

1. Ir a `docs/F1-Matriz_busqueda.csv`.
2. Abrir con Excel o Google Sheets.
3. Si todo aparece en una sola columna → `Datos → Desde texto/CSV` con separador **coma** y codificación **UTF-8**.

## 3. Las 13 columnas explicadas

| # | Columna | Qué poner | Ejemplo |
|---|---|---|---|
| 1 | `ID_busqueda` | Código único con prefijo `BS-` + correlativo | `BS-007` |
| 2 | `Clima_TdR` | Clima del contrato | `calido_seco` |
| 3 | `Subtipo_Köppen` | Subtipo solo si la búsqueda lo diferencia | `BWh` (vacío si es transversal) |
| 4 | `Categoria` | Tipo de objeto a buscar | `sistema` · `material` · `complemento` · `metodologia` |
| 5 | `Subsistema` | Dónde aplica (S1–S6). Multiple con espacio | `S2` · `S3 S4` |
| 6 | `Nombre` | Qué se busca | `Tapia pisada` · `Captación pluvial + jagüey` |
| 7 | `Familia` | Familia material si aplica | `tierra` · `madera-guadua` · `mamposteria` · `reciclado` · `vernaculo` · `-` |
| 8 | `Eje` | Eje de sostenibilidad dominante | `E1` · `E2` · `E3` · `E4` · `E5` |
| 9 | `Prioridad` | Urgencia de ejecución | `alta` · `media` · `baja` |
| 10 | `Estado` | Etapa del trabajo | `pendiente` · `en progreso` · `cerrado` |
| 11 | `N_fuentes` | Cuántas fuentes útiles se encontraron | `4` · `0` (vacío declarado) |
| 12 | `Fuentes_clave_M1` | IDs de M1 que salieron de esta búsqueda | `E1-005; E1-008; E4-003` |
| 13 | `Observaciones` | Notas, referencias al Anexo 1, vacíos, decisiones | `Anexo 1 MP-14` · `Vacío - sin evidencia CO` |

## 4. Lifecycle de una fila — estados

```
pendiente  ──►  en progreso  ──►  cerrado
   (aún                                 (con fuentes
   no se                                  o vacío
   ejecuta)                              declarado)
```

| Estado | Cuándo | Qué debe tener la fila |
|---|---|---|
| **`pendiente`** | Al inicio (default) | Solo los campos de definición (1–9) |
| **`en progreso`** | Al abrir la fila para trabajarla | Se empiezan a llenar `N_fuentes`, `Observaciones` |
| **`cerrado`** | Al terminar la búsqueda | `N_fuentes` definitivo + `Fuentes_clave_M1` completa + `Observaciones` con notas finales |

## 5. Paso a paso para trabajar una fila

**Ejemplo real — fila BS-007 (Tapia pisada · cálido seco · E1)**

### Paso 1 — Abrir la fila y cambiar estado
Antes de empezar: `Estado = pendiente` → **cambiar a** `en progreso`.

### Paso 2 — Ejecutar búsquedas
Consultar `F1-Protocolo_busqueda.md` §6 para las ecuaciones del eje E1 en clima cálido seco.

**Ecuaciones a ejecutar:**
- E1-C2 EN en Scopus (con credenciales de expertos).
- E1-C2 ES en SciELO + Redalyc.
- Repositorios UNAL, UPTC, UIS (manualmente con palabras clave).
- Revistas Dearq, Apuntes, Bitácora (búsqueda por keyword `tapia rural`).

**Términos a usar (desde F1-Marco §5 y F1-Protocolo §5):**
- `"tapia pisada" OR "tapial"` + `"vivienda rural"` + `"Villa de Leyva" OR "Boyacá"` + Colombia

### Paso 3 — Registrar resultados brutos
Cada búsqueda se registra individualmente en `F2-Ejecucion_busquedas.md` §3 (registro PRISMA).

Ejemplo del registro F2:
```
E1-C2-SC | Scopus | 2026-04-21 | 34 brutos | 12 tras filtros | 4 incluidos
E1-C2-RE | Redalyc | 2026-04-21 | 18 brutos | 7 tras filtros | 3 incluidos
E1-C2-UNAL | UNAL repo | 2026-04-22 | 9 brutos | 5 tras filtros | 2 incluidos
```

### Paso 4 — Trasladar hallazgos a M1
Cada fuente útil genera una fila en `F4-Matriz_M1.csv`. Asignar IDs correlativos:
- `E1-005` — Fonseca (2019) sobre tapia en Villa de Leyva.
- `E1-008` — Rodríguez (2021) sobre masa térmica en Boyacá.
- `E1-012` — Chávez (2020) sobre tapia en Patía.
- `E4-003` — Uniandes-CCCS (2021) sobre GWP de tapia.

### Paso 5 — Cerrar la fila
Volver a `F1-Matriz_busqueda.csv` y actualizar:

| Campo | Valor final |
|---|---|
| `Estado` | `cerrado` |
| `N_fuentes` | `4` |
| `Fuentes_clave_M1` | `E1-005; E1-008; E1-012; E4-003` |
| `Observaciones` | `Evidencia sólida CO (3 fuentes nacionales). Uniandes-CCCS cuantifica GWP. Snowballing saturó.` |

## 6. Casos especiales

### 6.1 Vacío declarado — 0 o 1 fuente tras búsqueda exhaustiva
Si tras ejecutar todas las ecuaciones y bola de nieve no aparecen ≥2 fuentes útiles:

| Campo | Valor |
|---|---|
| `Estado` | `cerrado` |
| `N_fuentes` | `0` o `1` |
| `Fuentes_clave_M1` | (vacío o solo 1 ID) |
| `Observaciones` | `VACÍO DECLARADO: búsqueda agotada sin evidencia CO. Posible adaptación andina pendiente.` |

Estos vacíos alimentan el informe final (`F5-Sintesis_y_cierre.md` §3).

### 6.2 Casos vernáculos específicos — NO crear fila BS nueva

Cuando una fuente (ej. documento exploratorio del líder) menciona un **caso vernáculo geográficamente específico** (ej. bahareque + boñiga en Tuchín Córdoba; sistemas tradicionales de Riosucio Caldas), **NO se crea una fila BS** propia. Se tratan como **fuentes semilla para bola de nieve** dentro de una fila BS existente:

- Tuchín, Córdoba → buscar dentro de BS-002 (bahareque Caribe).
- Riosucio, Caldas → buscar dentro de BS-013 (bahareque eje cafetero).

Los casos vernáculos que resulten se documentan al final del levantamiento como **fichas vernáculas** en `F5-Sintesis_y_cierre.md` §4 (3–5 casos por clima), no como filas propias en la matriz BS.

### 6.3 Filas transversales — NSR-10 y metodologías

Algunas filas no corresponden a un sistema/material/complemento específico sino a un **criterio transversal** que se verifica en todas las demás. Ejemplo:

- **BS-077** — Verificación de cumplimiento NSR-10 aplica a **todas las filas de sistemas estructurales (S1, S2)**. Se cierra revisando que cada sistema levantado tenga referencia explícita a su título correspondiente (E mampostería, G madera, H guadua).
- **BS-065 a BS-069** — metodologías (análisis del sitio, higrometría, simulación, POE, factor luz día) son referencias que pueden citar muchas fuentes de M1; no se asocian a un clima o sistema único.

Para estas filas, la columna `Clima_TdR` se llena con `todos` y `Subsistema` con `todos` o `-`.

### 6.4 Dividir una fila en dos
Si al ejecutar BS-044 (captación pluvial cálido seco) se ve que BSh y BWh tienen estrategias muy distintas, se divide:
- `BS-044a` — captación en BSh (jagüey, cisterna con primer lavado)
- `BS-044b` — captación en BWh (atrapanieblas, cisterna con desalinización)

Se conserva BS-044 como fila padre con `Observaciones: dividida en 044a y 044b`.

### 6.5 Agregar una fila nueva
Si durante la ejecución surge un sistema/material/complemento que no estaba en la lista inicial:
- Asignar siguiente correlativo a partir de `BS-078` (la matriz tiene 77 filas al 2026-04-16).
- Llenar las columnas 1–9 igual que las demás.
- Estado inicial `pendiente`.

## 7. Reglas de oro

| Regla | Razón |
|---|---|
| **Trabajar filas de prioridad `alta` primero** | Cubrir lo crítico antes de lo accesorio |
| **Cerrar cada fila antes de abrir la siguiente** | Evita filas "abiertas eternas" que no se cierran |
| **Registrar cada búsqueda ejecutada en F2** | Trazabilidad PRISMA obligatoria |
| **Transferir cada fuente útil a M1 antes de cerrar la fila** | M1 es la despensa final; BS- es solo la planeación |
| **Los IDs de M1 en `Fuentes_clave_M1` separados por `;`** | No comas (romperían el CSV) |
| **Un `N_fuentes = 0` no es fracaso** | Es un **vacío declarable** valioso para el informe final |

## 8. Errores comunes y cómo evitarlos

| Error | Consecuencia | Solución |
|---|---|---|
| Dejar filas en `en progreso` varios días sin cerrar | Pérdida de contexto al retomar | Cerrar la fila antes de pasar a la siguiente, aunque `N_fuentes` sea bajo |
| Mezclar categorías en una sola fila (ej. sistema + material) | Pierde precisión del levantamiento | Separar en dos filas BS- distintas |
| No poblar `Fuentes_clave_M1` aunque M1 ya tenga las filas | Se rompe la trazabilidad inversa | Copiar los IDs de M1 en cuanto se agregan |
| Usar comas en `Observaciones` | Rompe el formato CSV | Usar punto y coma (;) o paréntesis |
| Buscar solo en inglés o solo en español | Cobertura incompleta | Ejecutar ambas versiones de la ecuación (EN + ES) |
| Saltarse la prioridad y trabajar lo más fácil primero | Queda lo crítico sin tiempo | Ordenar por columna `Prioridad` al inicio del día |

## 9. Checklist diario al cierre

- [ ] ¿Cambié el estado de las filas trabajadas hoy?
- [ ] ¿Registré cada búsqueda ejecutada en `F2-Ejecucion_busquedas.md`?
- [ ] ¿Trasladé cada fuente útil a M1 con su ID correspondiente?
- [ ] ¿Poblé `Fuentes_clave_M1` en todas las filas cerradas hoy?
- [ ] ¿Guardé el CSV en UTF-8?

## 10. Cómo leer el tablero de progreso

Al ordenar la matriz por `Estado`, se obtiene un tablero de avance:

```
cerrado      — lo hecho    (ej. 20 filas)
en progreso  — en curso    (ej. 5 filas)
pendiente    — por hacer   (ej. 44 filas)
```

Meta diaria estimada (10 días hábiles, 77 filas): **~8 filas cerradas/día** entre los dos responsables. Si al final del día 5 la barra de progreso muestra <35 filas cerradas, replanificar.

## 11. Documentos relacionados

- `F1-Marco_busqueda_sistemas_materiales.md` — definiciones conceptuales, listas completas.
- `F1-Protocolo_busqueda.md` — ecuaciones booleanas y criterios de inclusión/exclusión.
- `F2-Ejecucion_busquedas.md` — registro PRISMA simplificado.
- `F4-Matriz_M1.csv` — matriz de hallazgos (destino de las fuentes encontradas).
- `F4-Tutorial_Matriz_M1.md` — tutorial de cómo llenar M1.
- `F0-3-Síntesis-Anexo1.md` — códigos MP/MA/MW del Anexo 1 para la columna Observaciones.

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | 2026-04-16 | Tutorial inicial — 69 filas base, 3 estados, flujo BS-→M1, casos especiales |
| 0.2 | 2026-04-16 | Actualización tras ampliación de matriz a 77 filas: casos vernáculos como semillas (no filas BS), filas transversales (NSR-10, metodologías), meta diaria ajustada a ~8 filas/día |
