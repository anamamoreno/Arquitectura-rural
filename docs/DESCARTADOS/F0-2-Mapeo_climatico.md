# Fase 0 — Mapeo climático: TdR ↔ Köppen-Geiger ↔ Caldas-Lang

> **¿Qué es este documento?** Define la **espina dorsal climática** sobre la que se organiza todo el levantamiento: cruza las 3 clasificaciones relevantes (los 4 climas del contrato, los 8 subtipos Köppen-Geiger y los pisos térmicos Caldas-Lang que usan la NSR-10 y la Res. 0549) para que cada fuente, estrategia y sistema pueda ubicarse sin ambigüedad. Su función es servir como tabla de referencia durante las búsquedas (qué términos geográficos usar por clima), durante la extracción a la matriz M1 (qué etiquetas climáticas poner a cada fila) y al declarar vacíos (páramo, alta Guajira) que la normativa colombiana no cubre.

**Producto 1 — Levantamiento de información**
Guía técnica de estándares de sostenibilidad para vivienda rural y pública (Res. 0194/2025).

## 1. Propósito

Establecer la espina dorsal climática de la matriz de estándares, manteniendo cumplimiento estricto del TdR (4 climas) y habilitando una capa analítica Köppen-Geiger para detectar diferencias significativas dentro de cada categoría contractual.

## 2. Principio rector

> Las **4 categorías del TdR** son la estructura de entrega.
> **Köppen-Geiger** es capa analítica subordinada: subdivide solo cuando la literatura revela diferencias medibles en al menos uno de los 4 ejes (bioclimática / energía / agua / materiales).

## 3. Tabla maestra de mapeo

| Clima TdR | Subtipo Köppen | Nombre | Regiones representativas CO | Rango T° | Precipitación | Altitud | Justificación de subdividir |
|---|---|---|---|---|---|---|---|
| **Cálido húmedo** | **Af** | Ecuatorial sin estación seca | Pacífico (Quibdó, Buenaventura), Amazonía occidental | 24–28 °C | >2000 mm, sin estación seca; localmente >8000 mm | 0–1000 m | Lluvia permanente → estrategias de evacuación pluvial extrema, durabilidad de madera, ventilación con alta HR |
| | **Am** | Monzónico | Caribe húmedo interior, piedemonte amazónico | 24–28 °C | 1500–4000 mm con estación seca corta | 0–1000 m | Lluvia estacional → captación pluvial viable; estrategias mixtas seco/húmedo |
| **Cálido seco** | **Aw** | Sabana tropical | Llanos Orientales, valles interandinos secos (Patía, alto Magdalena), Caribe seco | 24–28 °C | 1000–1800 mm bimodal | 0–1000 m | Estación seca marcada → captación + almacenamiento estacional |
| | **BSh** | Semiárido cálido | Guajira media, Tatacoa, Villa de Leyva, Cañón del Chicamocha | 24–30 °C | 300–700 mm | 0–2000 m | Déficit hídrico → estrategias agresivas de captación/reuso, masa térmica alta |
| | **BWh** | Árido cálido | Alta Guajira | 27–32 °C | <300 mm | 0–500 m | Déficit extremo + salinidad + viento → desalinización, protección anticorrosiva, ventilación cruzada con alisios |
| **Templado** | **Cfb** | Oceánico templado | Andes medios (Bogotá altiplano bajo, eje cafetero, Medellín, Popayán) | 14–22 °C | 1000–2500 mm | 1000–2400 m | Sin subdivisión — categoría homogénea para fines de diseño |
| **Frío** | **Cwb** | Subtropical de tierras altas | Bogotá, Tunja, Pasto, altiplano cundiboyacense | 8–16 °C | 700–1200 mm con verano seco | 2400–3000 m | Confort térmico estándar — base CEELA aplica |
| | **ET** | Tundra alpina (páramo) | Páramos (Sumapaz, Chingaza, Santurbán, Los Nevados) | 0–10 °C | 800–1500 mm, neblina constante | >3000 m | **Vacío normativo:** CEELA y Anexo 1 no cubren páramo; requiere aislamiento térmico extremo y manejo de humedad de niebla |

## 4. Cruces críticos detectados

### 4.1 Vacíos normativos
- **ET (páramo):** ni Anexo 1 Res. 0194/2025 ni los 15 criterios CEELA tienen estrategias específicas. Documentar como **hallazgo del Producto 1**. En caso de no exixtir ¿cuál es el plan B para llenar el vacío? Ej.: "adaptación desde literatura andina (Perú, Bolivia, Ecuador)".
- **BWh (alta Guajira):** la salinidad atmosférica y el déficit hídrico extremo no aparecen explícitamente en estándares nacionales de vivienda rural.

### 4.2 Equivalencia con Caldas-Lang (NSR-10 / Res. 0549)
| Caldas-Lang | Köppen aproximado |
|---|---|
| Cálido | Af, Am, Aw, BSh, BWh |
| Templado | Cfb |
| Frío | Cwb |
| Páramo | ET |

NSR-10 usa pisos térmicos por altitud; Köppen incorpora régimen de precipitación. **Ambos son complementarios**, no sustitutos.

## 5. Filtro de población (decisión de priorización)

Antes de invertir esfuerzo de levantamiento por subtipo, cruzar con **DANE CNPV 2018 — vivienda rural dispersa** para ponderar:

- ¿Cuántas viviendas rurales hay realmente en cada Köppen?
- ¿La subdivisión vale el esfuerzo si la población es marginal?

Regla práctica: si un subtipo tiene <5% de la vivienda rural nacional Y la evidencia no muestra diferencias críticas, agregar al subtipo dominante con nota al pie.

## 6. Insumos cartográficos requeridos

- **Beck et al. (2018)** — mapa global Köppen-Geiger 1 km, dominio público.
- **IDEAM** — Atlas climatológico de Colombia (capas de precipitación, temperatura, humedad).
- **DANE** — Censo Nacional de Población y Vivienda 2018, vivienda rural dispersa.
- **IGAC** — pisos térmicos y zonificación.

## 7. Próximos pasos (Fase 1)

1. Validar este mapeo con supervisor del contrato (presentarlo como mejora metodológica).
2. Construir tabla maestra normativa: ejes × clima TdR × subtipo Köppen.
3. Diseñar las 16 ecuaciones de búsqueda (4 ejes × 4 climas TdR) con sub-búsquedas por Köppen donde aplique.
4. Inicializar biblioteca Zotero con etiquetas: `clima_TdR/`, `koppen/`, `eje/`, `sistema_constructivo/`.

---

**Versión:** 0.1 — borrador para validación
**Fecha:** 2026-04-14
