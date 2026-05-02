# Proyecto Arquitectura Rural — Producto 1

Levantamiento de información sobre estándares de sostenibilidad para vivienda rural y pública en los 4 climas de Colombia, alineado con el Anexo 1 de la Resolución 0194 de 2025 y los 15 criterios CEELA.

**Responsable Producto 1:** Ana María Moreno
**Marco normativo:** MinVivienda · Res. 0194/2025 · Anexo 1 Guía de Construcción Sostenible

---

## Estructura

```
Proyecto-Arq_Rural/
├── docs/                          # Plan de trabajo y entregables
│   ├── F0-Matriz_estandares_sostenibilidad.csv   # M1 — 182 estándares de 25 fuentes normativas
│   ├── F0-Matriz_casos_exito.csv                 # M2 — 19 casos de éxito y vernáculos
│   ├── F0-* a F8-*.md                            # Plan, síntesis, diccionarios, tutoriales
│   └── extracciones/                             # Texto plano extraído de los PDFs
├── scripts/
│   ├── app_matriz_estandares.py                  # App Streamlit M1 + M2 con validación
│   ├── 01_busqueda_openalex.py
│   ├── 02_analisis_cobertura_M1.py
│   ├── 03_clasificar_resultados.py
│   ├── 04_agregar_normativa.py
│   ├── 05_enriquecer_matriz.py
│   ├── 06_agregar_nuevas.py
│   ├── 07_agregar_notas_rurales.py
│   └── README.md
├── FUENTES/                        # PDFs de respaldo (gitignored, locales)
└── README.md
```

## Entregables del Producto 1

1. **Protocolo de búsqueda** — `docs/F1-Protocolo_busqueda.md`
2. **Biblioteca Zotero organizada** (externa)
3. **Matriz de estándares M1** — `docs/F0-Matriz_estandares_sostenibilidad.csv` (182 filas, 25 fuentes)
4. **Matriz de casos M2** — `docs/F0-Matriz_casos_exito.csv` (19 candidatos en validación)
5. **Informe de vacíos** — pendiente F5
6. **Fichas de casos vernáculos** — derivadas de M2

## Dos matrices, dos propósitos

| Matriz | Naturaleza | Estado |
|---|---|---|
| **M1 Estándares** | Normativa CO + CEELA: qué se debe cumplir | ✅ 182 estándares poblados |
| **M2 Casos** | Proyectos reales que ilustran cómo se cumple | 🟡 19 candidatos pendientes de validación |

## Correr la app local

```bash
pip install streamlit pandas portalocker
python -m streamlit run scripts/app_matriz_estandares.py --server.port 8504
```

La app expone dos pestañas:
- **M1 · Estándares** — exploración con filtros de los 182 criterios
- **M2 · Casos de éxito** — fichas de casos con validación colaborativa, cruce automático con M1

## Documentos clave

| Doc | Contenido |
|---|---|
| `docs/F0-Plan_trabajo.md` | Cronograma 2 semanas |
| `docs/F0-3-Síntesis-Anexo1.md` | Síntesis de medidas Anexo 1 Res. 0194/2025 |
| `docs/F0-4-Producto1-Estrategia.md` | Estrategia detallada del Producto 1 |
| `docs/F1-Protocolo_busqueda.md` | Protocolo de búsqueda 2 semanas, Colombia-focused |
| `docs/F4-Matriz_M1_diccionario.md` | Diccionario de M1 Estándares |
| `docs/F6-Plan_busqueda_casos.md` | Plan de búsqueda de casos M2 |
| `docs/F7-Ejecucion_busqueda_casos.md` | Bitácora de ejecución búsqueda casos |
| `docs/F8-Matriz_casos_diccionario.md` | Diccionario de M2 Casos |
| `docs/UIP-Despliegue_VPS.md` | Plan de despliegue al VPS |

## Notas

- PDFs de fuentes (carpeta `FUENTES/`) están gitignored por tamaño (>50 MB algunos). Existen solo en local.
- Los archivos `.xlsx` de trabajo también están gitignored.
- La app usa `portalocker` para soportar multiusuario nivel 1 (lock + auditoría con `Validado_por` + `Fecha_validacion`).
