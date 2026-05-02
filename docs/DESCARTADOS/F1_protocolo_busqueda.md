# Fase 1 — Protocolo de búsqueda

**Proyecto:** Guía técnica de estándares de sostenibilidad para vivienda rural y pública (Res. 0194/2025).
**Producto 1 — Levantamiento de información.**
**Versión:** 0.1 — borrador.
**Fecha:** 2026-04-14.

---

## 1. Propósito

Establecer un protocolo reproducible de búsqueda bibliográfica que garantice cobertura de los 5 ejes temáticos en los 4 climas TdR (con capa Köppen), trazabilidad PRISMA-simplificada y criterios homogéneos de inclusión.

## 2. Criterios de inclusión

Una fuente entra al universo si cumple **todos** los criterios obligatorios y al menos uno de los criterios de pertinencia.

### 2.1 Obligatorios

| Criterio | Regla |
|---|---|
| **Temático** | Aborda al menos uno de los 5 ejes: bioclimática pasiva / eficiencia energética activa / eficiencia hídrica / materiales sostenibles / metodologías pre-diseño |
| **Tipológico** | Vivienda rural, vivienda de interés social, vivienda unifamiliar o bifamiliar ≤2 pisos |
| **Climático** | Aplicable a clima tropical, neotropical, ecuatorial, andino o asimilable por analogía documentada |
| **Idiomático** | Español, inglés o portugués (francés si trata higrometría de materiales) |
| **Temporal** | Publicado desde 2015 en adelante. Excepción: arquitectura vernácula y normativa histórica sin límite |
| **Accesibilidad** | Texto completo accesible (abierto, institucional o solicitable) |

### 2.2 Pertinencia (al menos uno)

- Evidencia empírica medida (métricas cuantitativas de desempeño).
- Normativa, guía técnica o estándar oficial.
- Caso de estudio documentado en Colombia o región andina/tropical.
- Revisión sistemática o meta-análisis.
- Tesis de maestría/doctorado en repositorio institucional verificable.

## 3. Criterios de exclusión

Descartar si:
- Vivienda multifamiliar urbana densa (>4 pisos).
- Clima templado europeo o continental sin adaptación tropical documentada.
- Tecnologías sin viabilidad económica para vivienda rural colombiana (costo >3× VIS).
- Publicaciones de divulgación sin respaldo técnico (blogs, notas de prensa sin fuente).
- Documentos comerciales promocionales sin datos independientes.
- Duplicados (misma obra en múltiples bases) — se conserva la versión más completa.

## 4. Ejes temáticos y palabras clave

### 4.1 Tabla de términos por eje (trilingüe)

| Eje | Español | Inglés | Portugués |
|---|---|---|---|
| **E1 — Bioclimática pasiva** | diseño bioclimático, arquitectura pasiva, confort térmico, ventilación natural, inercia térmica, orientación solar, aleros, masa térmica | bioclimatic design, passive architecture, thermal comfort, natural ventilation, thermal mass, solar orientation, shading | projeto bioclimático, arquitetura passiva, conforto térmico, ventilação natural |
| **E2 — Eficiencia energética activa** | eficiencia energética, energía solar fotovoltaica, solar térmica, iluminación eficiente LED, bomba de calor, biogás doméstico, microhidro | energy efficiency, photovoltaic, solar thermal, LED lighting, heat pump, biogas, micro-hydro | eficiência energética, fotovoltaico, iluminação eficiente |
| **E3 — Eficiencia hídrica** | captación pluvial, reuso aguas grises, ahorro agua, aparatos de bajo consumo, tratamiento in situ, humedales artificiales | rainwater harvesting, greywater reuse, water efficiency, low-flow fixtures, constructed wetlands | captação pluvial, reúso águas cinzas, eficiência hídrica |
| **E4 — Materiales sostenibles** | materiales sostenibles, ecomateriales, tierra cruda, tapia pisada, adobe, bahareque, BTC bloque tierra comprimida, guadua, madera certificada, análisis de ciclo de vida, huella de carbono | sustainable materials, earthen construction, rammed earth, adobe, compressed earth block CEB, bamboo, embodied carbon, life cycle assessment | materiais sustentáveis, terra crua, taipa, adobe, bambu |
| **E5 — Metodologías pre-diseño** | análisis del sitio, diagnóstico climático, simulación energética, monitoreo post-ocupación, factor de luz día, higrometría, permeabilidad al vapor | site analysis, climate analysis, energy simulation, post-occupancy evaluation POE, daylight factor, hygrothermal, vapor permeability | análise do sítio, simulação energética |

### 4.2 Términos climáticos

| Clima TdR | Términos |
|---|---|
| Cálido húmedo | "cálido húmedo", "hot humid", "tropical húmedo", "quente úmido", "equatorial", "tropical rainforest", "Af Köppen", "Am Köppen" |
| Cálido seco | "cálido seco", "hot arid", "hot dry", "semiárido", "árido tropical", "Aw Köppen", "BSh Köppen", "BWh Köppen", "savanna climate" |
| Templado | "templado", "temperate", "subtropical highland", "clima andino medio", "Cfb Köppen" |
| Frío | "frío", "cold", "highland", "altiplano", "páramo", "Cwb Köppen", "ET Köppen", "alpine tundra" |

### 4.3 Términos tipológicos y de contexto

- **Vivienda rural:** "vivienda rural", "rural housing", "habitação rural", "vivienda campesina", "rural dwelling", "rural home".
- **Vivienda social:** "vivienda de interés social", "VIS", "social housing", "affordable housing", "vivienda popular".
- **Contexto geográfico:** "Colombia", "Andes", "Andean", "América Latina", "Latin America", "neotropical", "tropics".

## 5. Estructura de las ecuaciones

Sintaxis base (adaptar por base de datos):

```
(TERM_EJE) AND (TERM_TIPOLOGÍA) AND (TERM_CLIMA) AND (TERM_GEOGRÁFICO)
```

Operadores:
- `AND` — obligatorio.
- `OR` — alternativas dentro de un grupo (entre paréntesis).
- `*` — truncamiento (si la base lo permite).
- `" "` — frase exacta.
- `NOT` — solo para eliminar ruido confirmado.

## 6. Las 20 ecuaciones de búsqueda

Estructura: 5 ejes × 4 climas = 20 búsquedas base. En subtipos Köppen con evidencia esperada diferenciada, se añaden sub-búsquedas dirigidas.

### E1 — Bioclimática pasiva

**E1-C1 Cálido húmedo**
```
("bioclimatic design" OR "passive architecture" OR "natural ventilation" OR "thermal comfort")
AND ("rural housing" OR "social housing" OR "vivienda rural")
AND ("hot humid" OR "tropical humid" OR "equatorial" OR "cálido húmedo")
AND (Colombia OR tropical OR neotropical OR Andes)
```
Sub-búsquedas Köppen: añadir `AND ("Pacific coast" OR "Chocó" OR "palafito")` para Af; `AND ("Caribbean" OR "bahareque")` para Am.

**E1-C2 Cálido seco**
```
("passive cooling" OR "thermal mass" OR "shading" OR "cross ventilation")
AND ("rural housing" OR "vivienda rural")
AND ("hot arid" OR "hot dry" OR "semi-arid" OR "savanna climate")
AND (Colombia OR "Latin America" OR Andes)
```
Sub-búsquedas Köppen: `AND ("Guajira" OR "Wayuu")` para BWh; `AND "Tatacoa"` para BSh.

**E1-C3 Templado**
```
("bioclimatic design" OR "passive design" OR "thermal comfort")
AND ("rural housing" OR "vivienda rural")
AND ("temperate" OR "subtropical highland" OR "Andean" OR "templado")
AND (Colombia OR Andes OR "eje cafetero")
```

**E1-C4 Frío**
```
("passive heating" OR "thermal insulation" OR "solar gain" OR "high altitude")
AND ("rural housing" OR "vivienda rural")
AND ("highland" OR "cold climate" OR "altiplano" OR "páramo")
AND (Colombia OR Andes OR Bolivia OR Peru OR Ecuador)
```
Sub-búsquedas Köppen: `AND ("páramo" OR "alpine")` para ET.

---

### E2 — Eficiencia energética activa

**E2-C1 Cálido húmedo**
```
("energy efficiency" OR "photovoltaic" OR "solar PV" OR "LED lighting" OR "biogas")
AND ("rural housing" OR "off-grid" OR "vivienda rural")
AND ("hot humid" OR "tropical" OR "equatorial")
AND (Colombia OR "Latin America")
```

**E2-C2 Cálido seco**
```
("photovoltaic" OR "solar PV" OR "solar thermal" OR "energy efficiency")
AND ("rural housing" OR "off-grid")
AND ("arid" OR "semi-arid" OR "savanna")
AND (Colombia OR Andes)
```

**E2-C3 Templado**
```
("energy efficiency" OR "photovoltaic" OR "biomass stove" OR "efficient cookstove")
AND ("rural housing" OR "social housing")
AND ("temperate" OR "Andean" OR "subtropical highland")
AND (Colombia OR Andes)
```

**E2-C4 Frío**
```
("efficient heating" OR "biomass stove" OR "improved cookstove" OR "solar thermal" OR "heat pump")
AND ("rural housing" OR "highland housing")
AND ("cold climate" OR "highland" OR "altiplano" OR "páramo")
AND (Colombia OR Andes OR Bolivia OR Peru)
```

---

### E3 — Eficiencia hídrica

**E3-C1 Cálido húmedo**
```
("rainwater harvesting" OR "greywater reuse" OR "water efficiency" OR "constructed wetlands")
AND ("rural housing" OR "vivienda rural")
AND ("hot humid" OR "tropical humid" OR "equatorial")
AND (Colombia OR "Latin America" OR neotropical)
```

**E3-C2 Cálido seco**
```
("rainwater harvesting" OR "water storage" OR "desalination" OR "atmospheric water")
AND ("rural housing" OR "vivienda rural")
AND ("arid" OR "semi-arid" OR "drought" OR "Guajira")
AND (Colombia OR "Latin America")
```
Sub-búsquedas Köppen: BWh requiere `AND ("desalination" OR "fog harvesting" OR "atmospheric water generation")`.

**E3-C3 Templado**
```
("rainwater harvesting" OR "greywater" OR "water efficiency" OR "low-flow fixtures")
AND ("rural housing" OR "social housing")
AND ("temperate" OR "Andean" OR "subtropical highland")
AND (Colombia OR Andes)
```

**E3-C4 Frío**
```
("rainwater harvesting" OR "spring water" OR "water quality cold" OR "freezing protection")
AND ("rural housing" OR "highland housing")
AND ("cold climate" OR "highland" OR "páramo" OR "altiplano")
AND (Colombia OR Andes)
```

---

### E4 — Materiales sostenibles

**E4-C1 Cálido húmedo**
```
("sustainable materials" OR "bamboo construction" OR "guadua" OR "certified timber" OR "earthen construction")
AND ("rural housing" OR "tropical housing")
AND ("hot humid" OR "tropical humid" OR "high humidity")
AND (Colombia OR "Latin America" OR tropical)
```

**E4-C2 Cálido seco**
```
("rammed earth" OR "adobe" OR "compressed earth block" OR "earthen construction" OR "tapia" OR "BTC")
AND ("rural housing" OR "vivienda rural")
AND ("arid" OR "semi-arid" OR "hot dry")
AND (Colombia OR "Latin America")
```

**E4-C3 Templado**
```
("bahareque" OR "rammed earth" OR "adobe" OR "sustainable materials" OR "life cycle assessment")
AND ("rural housing" OR "social housing")
AND ("temperate" OR "Andean" OR "Andes")
AND (Colombia OR "eje cafetero")
```

**E4-C4 Frío**
```
("adobe" OR "rammed earth" OR "stone masonry" OR "insulation materials" OR "straw bale")
AND ("rural housing" OR "highland housing")
AND ("cold climate" OR "highland" OR "altiplano")
AND (Colombia OR Andes OR Bolivia OR Peru)
```

---

### E5 — Metodologías pre-diseño

**E5-C1 Cálido húmedo**
```
("site analysis" OR "climate analysis" OR "daylight factor" OR "hygrothermal" OR "post-occupancy evaluation")
AND ("rural housing" OR "tropical building")
AND ("hot humid" OR "tropical humid")
AND (Colombia OR tropical OR neotropical)
```

**E5-C2 Cálido seco**
```
("site analysis" OR "climate analysis" OR "energy simulation" OR "thermal monitoring")
AND ("rural housing" OR "vernacular")
AND ("arid" OR "semi-arid" OR "hot dry")
AND (Colombia OR "Latin America")
```

**E5-C3 Templado**
```
("site analysis" OR "daylight factor" OR "energy simulation" OR "post-occupancy evaluation")
AND ("rural housing" OR "social housing")
AND ("temperate" OR "Andean")
AND (Colombia OR Andes)
```

**E5-C4 Frío**
```
("site analysis" OR "hygrothermal monitoring" OR "energy simulation" OR "thermal performance")
AND ("rural housing" OR "highland housing")
AND ("cold climate" OR "highland" OR "páramo")
AND (Colombia OR Andes OR Bolivia OR Peru)
```

## 7. Adaptación por base de datos

| Base | Sintaxis particular | Notas |
|---|---|---|
| **Scopus** | `TITLE-ABS-KEY()` con operadores | Usar filtros por año y tipo de documento |
| **Web of Science** | `TS=()` (topic search) | Exportar a RIS/BibTeX |
| **ScienceDirect** | Búsqueda avanzada por campo | Límite 8 operadores booleanos |
| **Redalyc** | Español nativo | Útil para literatura latinoamericana |
| **SciELO** | Trilingüe ES/EN/PT | Cobertura fuerte en América Latina |
| **DOAJ** | Solo open access | Filtrar por tema y país |
| **Google Scholar** | Sintaxis limitada | Usar como complemento, no como fuente primaria |
| **Repositorios tesis CO** | UNAL (bdigital), UniAndes (sénéca), Javeriana, UPB | Buscar por palabras clave sin operadores complejos |

## 8. Registro por búsqueda (PRISMA simplificado)

Para cada ejecución, registrar en hoja de control:

| Campo | Descripción |
|---|---|
| ID búsqueda | E1-C1, E1-C1a (sub-búsqueda), etc. |
| Base de datos | Scopus, WoS, Redalyc, etc. |
| Ecuación exacta | Texto literal usado |
| Fecha de ejecución | YYYY-MM-DD |
| N resultados brutos | Total de la base |
| N tras filtros automáticos | Por año, idioma, tipo documento |
| N tras lectura de título | Descartar off-topic |
| N tras lectura resumen | Descartar no pertinentes |
| N tras lectura completa | Definitivos para matriz M1 |
| Observaciones | Hallazgos, ajustes a próxima búsqueda |

## 9. Búsquedas complementarias (no estructuradas)

Paralelo a las 20 ecuaciones, ejecutar búsquedas dirigidas:

- **Normativa:** web MVCT, MADS, UPME, IDEAM, ICONTEC (descarga directa).
- **Cooperación:** sitios CEELA, BID Cities, CAF, GIZ, PNUD, ONU-Habitat (publicaciones regionales).
- **Vernáculo:** libros de referencia colombianos (Arango, Téllez, Fonseca-Saldarriaga); revistas Dearq, Bitácora, Apuntes, Revista AV.
- **Casos:** bases de proyectos Findeter, DNP, SENA.
- **Snowballing:** revisar referencias citadas en las 10 fuentes más relevantes de cada eje.

## 10. Organización en Zotero

**Estructura de carpetas:**
```
Proyecto-Arq-Rural/
├── 00_Normativa/
│   ├── Res-0194-2025-Anexo1/
│   ├── CEELA/
│   └── NSR-RETIE-RAS/
├── 01_E1_Bioclimatica/
│   ├── C1_Calido_humedo/
│   ├── C2_Calido_seco/
│   ├── C3_Templado/
│   └── C4_Frio/
├── 02_E2_Energia_activa/
├── 03_E3_Hidrica/
├── 04_E4_Materiales/
├── 05_E5_Metodologias/
├── 06_Vernaculo/
└── 07_Genero_inclusion/
```

**Tags obligatorios por referencia:**
- `eje:E1 / E2 / E3 / E4 / E5`
- `clima-TdR:calido-humedo / calido-seco / templado / frio`
- `koppen:Af / Am / Aw / BSh / BWh / Cfb / Cwb / ET`
- `sistema:tierra / madera-guadua / mamposteria / prefabricado / hibrido`
- `tipo:estrategia / material / complemento / metodologia`
- `origen:vernaculo / industrializado / hibrido`
- `medida:activa / pasiva / hibrida`
- `evidencia:empirica-CO / empirica-otros / revision / normativa`
- `genero:aplica / no-aplica`

## 11. Umbrales de decisión

- **Por búsqueda:** si una ecuación devuelve <10 resultados después de filtros, ampliar términos o relajar clima. Si devuelve >500, restringir.
- **Por celda de matriz:** si después de las 20 búsquedas + complementarias una celda (clima × sistema × eje) tiene <3 fuentes, marcar como **vacío de evidencia** en informe final.
- **Saturación:** cuando 3 búsquedas consecutivas no añaden fuentes nuevas, se considera saturada esa celda.

## 12. Cronograma estimado F1→F4

| Fase | Duración estimada | Entregable |
|---|---|---|
| F1 — Protocolo (este documento) | 3 días | Protocolo validado |
| F2 — Priorización fuentes + accesos | 2 días | Lista de fuentes con credenciales |
| F3 — Ejecución de búsquedas | 3–4 semanas | Zotero poblado + hoja PRISMA |
| F4 — Extracción a matrices | 2–3 semanas | M1 + M2 versión borrador |

*Ajustar con respuesta del director sobre cronograma real del contrato (pregunta B.1.1).*

## 13. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Baja densidad de evidencia en ET (páramo) y BWh | Usar literatura andina (Perú, Bolivia, Ecuador) y búsquedas etnográficas |
| Sesgo hacia literatura urbana | Forzar términos "rural" en todas las ecuaciones; filtrar manualmente |
| Terminología vernácula no indexada | Complementar con búsqueda manual en revistas de arquitectura CO |
| Ruido por ambigüedad de "sustainable" | Requerir evidencia cuantitativa en criterios de pertinencia |
| Falta de acceso a Scopus/WoS | Planificar desde el inicio ruta alterna con SciELO + Redalyc + DOAJ |

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | 2026-04-14 | Borrador inicial — criterios + 20 ecuaciones + registro PRISMA |
