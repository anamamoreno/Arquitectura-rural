# F6 — Plan de búsqueda de casos de éxito y vernáculos

**Producto 1 — Levantamiento de información · Track B (Matriz de Casos M2)**
**Versión:** 0.1 · **Fecha:** 2026-05-01

---

## 1. Encuadre

El Producto 1 entrega **dos matrices complementarias**:

| Matriz | Archivo | Propósito | Estado |
|---|---|---|---|
| **M1 — Estándares** | `F0-Matriz_estandares_sostenibilidad.csv` | Recoge medidas y criterios obligatorios/recomendados de la normativa CO (Anexo 1 Res. 0194/2025) y los 15 criterios CEELA | ✅ 182 filas, alimenta la app Streamlit |
| **M2 — Casos de éxito** | `F0-Matriz_casos_exito.csv` | Recoge proyectos reales —vernáculos y contemporáneos— que materializan estrategias de sostenibilidad en vivienda rural CO, como ejemplos para el Producto 2 | 🔴 Por construir (este plan) |

M2 no busca normar sino **ilustrar**: dar referentes empíricos para que los arquitectos del Producto 2 muestren "así se hace" en cada clima × sistema.

## 2. Objetivo

Construir M2 con un mínimo de casos verificables que permitan al Producto 2 ilustrar la aplicación efectiva de las estrategias de M1 en cada zona climática × sistema constructivo de Colombia.

## 3. Alcance

### 3.1 Geográfico
- **Nacional Colombia** (esta versión).
- Casos andinos / tropicales internacionales quedan fuera por ahora; podrían incorporarse en versión 2 si hay tiempo.

### 3.2 Temporal
- **Vernáculo:** sin límite inferior (tradiciones documentadas en cualquier época).
- **Contemporáneo:** desde 2000, preferencia por proyectos verificables todavía en operación.

### 3.3 Tipológico
- **Vivienda rural unifamiliar** principalmente.
- **Vivienda rural agrupada** (palafitos, corredores) si tiene replicabilidad.
- Equipamientos comunitarios rurales (escuelas, salones) **solo** si demuestran estrategia transferible a vivienda.

### 3.4 Ejes
Mismos cuatro de M1: E1 bioclimática pasiva · E2 energía activa · E3 agua · E4 materiales. Un caso vale si cubre **al menos un eje** con descripción concreta.

## 4. Cuotas mínimas y meta ideal

| Clima TdR | Mínimo absoluto | Meta ideal |
|---|---|---|
| Frío | 2 casos | 1 caso por cada sistema (≥2) |
| Templado | 2 casos | 1 caso por cada sistema (≥2) |
| Cálido húmedo | 2 casos | 1 caso por cada sistema (≥2) |
| Cálido seco | 2 casos | 1 caso por cada sistema (≥2) |
| **TOTAL** | **8 casos** | **8+ casos distribuidos** |

**Regla de marcado de vacío:** si tras búsqueda exhaustiva un par (clima × sistema) no alcanza 1 caso, se declara como vacío en el informe F5.

## 5. Estructura propuesta de M2 — columnas

```
ID                     │ CAS-001, CAS-002...
Nombre_proyecto        │ "Casa de tapia en Boyacá"
Tipo                   │ vernaculo / contemporaneo / mixto
Año                    │ 2018 / s.f. (vernáculo)
Ubicacion_depto        │ Boyacá
Ubicacion_municipio    │ Tibasosa
Ubicacion_vereda       │ (opcional)
Clima_TdR              │ frio / templado / calido_humedo / calido_seco
Subtipo_Koppen         │ Cfb, Aw, etc. (opcional)
Sistema_constructivo   │ tapia / bahareque / palafito-madera / mampostería confinada / guadua / etc.
Subsistemas            │ lista separada por ";": cimentacion / estructura / envolvente / cubierta / instalaciones / integral
E1_bioclimatica        │ texto descriptivo de estrategias pasivas
E2_energia             │ texto descriptivo de estrategias activas
E3_agua                │ texto descriptivo
E4_materiales          │ texto descriptivo
Estandares_ref         │ lista de IDs de M1 separados por ";" (ej: MP-14; MA-22; SUDS-3); cubre cualquiera de las 25 fuentes de F0-Matriz_estandares
Cumplimiento_observado │ texto libre con desviaciones, cumplimiento parcial u observaciones por estándar (ej: "MP-14: muro 35cm vs 40cm requeridos")
Genero_inclusion       │ texto si aplica
Estado                 │ construido / en_operacion / abandonado / desconocido
Verificable            │ foto / publicacion / visita / referencia_indirecta
Fuente_principal       │ cita corta + página opcional (ej: "Hábitat Para La Paz, p. 45") o URL
Archivo_fuente         │ nombre del PDF en FUENTES/ (la app lo abre con la app por defecto del sistema, solo en local)
URL_fuente             │ URL pública (repositorio / DOI / sitio oficial); abre en pestaña nueva, funciona local y VPS
Tipo_fuente            │ premio / bienal / revista / tesis / ONG / oficial / libro / documento_proyecto
Lecciones_aprendidas   │ qué replicar, qué evitar
Observaciones          │ libre
Estado_validacion      │ pendiente_revision / aceptado / descartado (gestionado vía botones de la app)
Motivo_descarte        │ razón si Estado_validacion = descartado
Fecha_validacion       │ ISO YYYY-MM-DD, autocompletada por la app
Validado_por           │ persona que validó/descartó (autocompletado por la app desde session_state)
```

(Diccionario detallado se construye en F8.)

## 6. Fuentes priorizadas (orden de ataque)

### 6.1 Premios y bienales (mayor densidad de casos verificables)
- **Bienal Colombiana de Arquitectura** (categorías: vivienda rural, hábitat, sostenibilidad)
- **Premios Sociedad Colombiana de Arquitectos (SCA)**
- **Premios CAF** vivienda y desarrollo rural

### 6.2 Revistas de arquitectura
- **Proa** (archivo histórico — vernáculo CO)
- **Escala**
- **ArchDaily Colombia / Plataforma Arquitectura** (proyectos contemporáneos)
- **Arquine** (referentes andinos, baja prioridad)

### 6.3 Repositorios universitarios — tesis
- UNAL (sede Bogotá, Manizales, Medellín)
- Uniandes — Departamento de Arquitectura
- Javeriana
- U. Tadeo Lozano
- U. Católica de Colombia

### 6.4 ONGs y fundaciones
- Hábitat para la Humanidad Colombia
- Fundación Tierra Viva
- Hábitat Para La Paz (ya en `Referencias-proyecto/`)
- Fundación Carvajal
- Asociación Nacional de Arquitectura Vernácula (si existe registro)

### 6.5 Estado y banca de desarrollo
- MinCultura — patrimonio inmueble rural (PEMP, BIC)
- DNP — casos exitosos de vivienda rural
- Findeter — proyectos financiados con sello sostenible
- MVCT — proyectos VISR construidos

### 6.6 Documentos ya en el proyecto (releer en clave de **casos**)
- `Habitat-Para-La-Paz.pdf` — diversidad étnica + vernáculo post-conflicto
- `Vivienda-Nueva-Rural.pdf`
- `Vivienda+Cultura_Digital.pdf`
- `Guia-de-vivienda-Rural.pdf` — incluye páramo Sumapaz
- `2000_Inventario_de_Sistemas_Constructiv.pdf` — taxonomía sistemas

### 6.7 Snowballing
Desde cada caso encontrado: revisar bibliografía citada, autores afines, proyectos del mismo arquitecto/colectivo.

## 7. Criterios de inclusión / exclusión

### 7.1 Inclusión
- Vivienda rural CO o equipamiento rural con estrategia transferible.
- Documentación verificable: foto + descripción técnica mínima.
- Cubre ≥1 eje (E1–E4) con descripción concreta de la estrategia.
- Ubicación atribuible a un clima TdR.

### 7.2 Exclusión
- Vivienda urbana o suburbana.
- Vivienda rural sin estrategia de sostenibilidad identificable.
- Casos solo descritos sin foto ni evidencia (referencia indirecta sin autor verificable).
- Proyectos solo conceptuales / no construidos.

### 7.3 Marcas especiales
- `Verificable=foto` → caso completo
- `Verificable=referencia_indirecta` → se acepta solo si origen es académico o institucional, marcar para revisión

## 8. Protocolo operativo

### Paso 1 — Cosecha amplia
Recorrer fuentes 6.1 → 6.6 listando candidatos en hoja de trabajo. Meta: 30–40 candidatos brutos antes de filtrar.

### Paso 2 — Screening
Aplicar criterios §7. Descartar los que no pasan. Guardar registro de descartes para trazabilidad.

### Paso 3 — Fichaje
Por cada caso aceptado, llenar fila en `F0-Matriz_casos_exito.csv` con todas las columnas posibles. Marcar campos vacíos como `desconocido` (no en blanco).

### Paso 4 — Cruce con M1
Para cada caso, identificar qué estándares de M1 materializa: rellenar `Estandares_ref` con la lista de IDs (cualquiera de las 25 fuentes: Anexo 1, CEELA, RETILAP, RAS, leyes, decretos, etc.). Si hay desviaciones o cumplimiento parcial, anotarlo en `Cumplimiento_observado`. Esto es lo que hace el caso útil para el Producto 2.

### Paso 5 — Snowballing
Por cada caso confirmado, revisar referencias citadas → ciclo paso 1.

### Paso 6 — Cierre por celda
Cuando un par (clima × sistema) llega a 2 casos verificables, marcar la celda como cubierta y bajar prioridad.

## 9. Entregables del Track B

| Entregable | Archivo | Cuándo |
|---|---|---|
| Plan (este doc) | `docs/F6-Plan_busqueda_casos.md` | Ya |
| Bitácora ejecución | `docs/F7-Ejecucion_busqueda_casos.md` | Plantilla en F7, se llena durante búsqueda |
| Matriz M2 poblada | `docs/F0-Matriz_casos_exito.csv` | Resultado de F8 |
| Diccionario M2 | `docs/F8-Matriz_casos_diccionario.md` | Junto con F8 |
| Tab "Casos" en app Streamlit | modificar `scripts/app_matriz_estandares.py` | Tras tener M2 con ≥8 filas |

## 10. Cambios al alcance global del Producto 1

### 10.1 Renombres y limpieza ya hechos
- `F1-Matriz_M1.csv` (vacía) → eliminada. La "matriz oficial" es `F0-Matriz_estandares_sostenibilidad.csv`.

### 10.2 Pendientes de revisar (no urgentes)
- `F4-Matriz_M1_diccionario.md` y `F4-Tutorial_Matriz_M1.md` referencian M1; mantenerlos como diccionario/tutorial de la **matriz de estándares** o renombrarlos para evitar confusión.

### 10.3 Impacto en F5 (síntesis y cierre)
F5 ahora incluye:
- Tabla CEELA ↔ Anexo 1 (ya prevista)
- **Cruce M1 × M2:** qué medidas tienen al menos un caso ilustrativo y cuáles no
- Informe de vacíos: vacíos normativos (de M1) **+ vacíos de evidencia empírica** (pares clima × sistema sin caso)
- Fichas vernáculas (ahora son una salida natural de M2, no una construcción aparte)

## 11. App Streamlit — extensión prevista

Tab adicional **"Casos de éxito"** con:
- Filtros: Clima TdR, Sistema constructivo, Eje, Tipo (vernáculo/contemporáneo)
- Vista de tarjeta por caso con campos clave
- Cruce automático: para cada caso, mostrar la lista enriquecida de estándares (ID → Referencia → Descripción) vía JOIN con M1 sobre la columna `ID`, más la observación de cumplimiento
- Indicador de cobertura por clima × sistema (cuántos casos hay en cada celda)

Implementación: tras poblar M2 con un mínimo viable (≥8 filas).

## 12. Definición de "terminado" para Track B

M2 se considera entregable cuando:
- ≥8 casos cumplen criterios de inclusión §7.1
- ≥2 casos por clima TdR
- Cada caso tiene `Estandares_ref` poblado con ≥1 ID de M1
- Tab "Casos" en app Streamlit funcionando
- Vacíos por celda declarados en F5

## 13. Próximo paso

Una vez aprobado este plan:
1. Crear plantilla `docs/F7-Ejecucion_busqueda_casos.md` (bitácora vacía)
2. Crear `docs/F0-Matriz_casos_exito.csv` con header definido en §5
3. Crear `docs/F8-Matriz_casos_diccionario.md`
4. Empezar paso 1 del protocolo (§8) por la fuente con mayor densidad: relectura de los 5 PDFs ya en proyecto en clave de casos
