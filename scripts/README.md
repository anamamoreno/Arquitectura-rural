# Scripts de automatización — Producto 1

## Requisitos
- Python 3.10+ (verificado con 3.14.2)
- Librerías: `pandas`, `requests`, `openpyxl` (ya instaladas con Anaconda)

## Uso

Abrir terminal en la carpeta del proyecto y ejecutar:

### 1. Búsqueda automática en OpenAlex
```bash
cd C:/Users/user/Proyecto-Arq_Rural
python scripts/01_busqueda_openalex.py
```
Ejecuta 15 ecuaciones de búsqueda en la API gratuita de OpenAlex (250M+ artículos, incluye Scopus/SciELO/Redalyc). Guarda resultados deduplicados en `resultados/openalex_FECHA.csv`.

**Tiempo estimado:** ~2 minutos (15 búsquedas × 0.5s pausa cortesía).

### 2. Análisis de cobertura de M1
```bash
python scripts/02_analisis_cobertura_M1.py
```
Lee `docs/F4-Matriz_M1.csv` y genera:
- Tabla cruzada Eje × Clima (qué celdas están llenas/vacías).
- % de fuentes colombianas (meta ≥60%).
- Distribución por tipo de fuente y tipo de medida.
- Cobertura de referencias Anexo 1 y CEELA.

Guarda reporte en `resultados/cobertura_M1_FECHA.txt`.

### 3. Clasificación semi-automática
```bash
python scripts/03_clasificar_resultados.py
```
Lee el CSV de OpenAlex y clasifica cada artículo por eje (E1–E4) y clima usando reglas de palabras clave. Guarda resultado en `resultados/clasificados_FECHA.csv`.

**⚠ La clasificación es sugerida — revisar manualmente antes de incorporar a M1.**

## Flujo recomendado

```
Paso 1: Ejecutar 01_busqueda_openalex.py
           ↓
Paso 2: Ejecutar 03_clasificar_resultados.py
           ↓
Paso 3: Abrir resultados/clasificados_FECHA.csv en Excel
           ↓
Paso 4: Revisar manualmente → transferir los útiles a F4-Matriz_M1.csv
           ↓
Paso 5: Ejecutar 02_analisis_cobertura_M1.py para ver progreso
           ↓
Paso 6: Repetir desde paso 1 ajustando términos si hay vacíos
```

## Carpeta de salida
Todos los resultados se guardan en `resultados/` (se crea automáticamente).
