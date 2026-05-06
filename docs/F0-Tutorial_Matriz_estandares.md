# Tutorial: Matriz de estándares de sostenibilidad

> **¿Qué es este documento?** Guía para entender, consultar y filtrar la matriz `F0-Matriz_estandares_sostenibilidad.csv`. Explica qué significa cada campo, cada código y cada nomenclatura empleada. Para que cualquier integrante del equipo pueda abrir la matriz en Excel o en la app y encontrar respuestas sin ambigüedad.

**Archivo:** `docs/F0-Matriz_estandares_sostenibilidad.csv`
**Contenido:** **191 filas** — todos los criterios, medidas, principios, enfoques y fines de **26 fuentes normativas y documentales**.
**Versión:** 0.3 · **Fecha:** 2026-05-05.

---

## 1. Qué es esta matriz

Es el **catálogo normativo consolidado** del proyecto. Reúne en una sola tabla todo lo que las normas y marcos de referencia colombianos (más CEELA y UPME-PGEE) dicen sobre sostenibilidad en edificaciones, clasificado por eje, clima, aplicabilidad rural y carácter legal.

**Distinta de la Matriz M2 (`F0-Matriz_casos_exito.csv`):**

| Esta matriz (M1 — Estándares) | Matriz M2 (Casos de éxito) |
|---|---|
| **Lo que exige la norma** | **Lo que se construyó en proyectos reales** |
| 191 filas, 26 fuentes, 20 columnas | 31 casos, 29 columnas |
| Se construyó como inventario fijo | Se llena con proyectos vernáculos y contemporáneos |
| Cada caso de M2 referencia IDs de aquí (campo `Estandares_ref`) | M2 ilustra cómo se materializan los estándares de M1 |

Para detalle del inventario completo de fuentes y su aporte por filas, ver `F0-Lista_referencias_y_aportes.md`.

## 2. Cómo abrirla

1. Ir a `docs/F0-Matriz_estandares_sostenibilidad.csv`.
2. **Excel:** doble clic. Si todo aparece en una columna → `Datos → Desde texto/CSV` → separador **coma** → codificación **UTF-8 con BOM**.
3. **Google Sheets:** subir a Drive → Abrir con Google Sheets.
4. **App Streamlit:** http://localhost:8504/m1 (local) o https://app.uxtic.co/artefactos/viviendarural/m1 (VPS) — incluye filtros y el botón "abrir" para consultar la fuente original.

## 3. Los 20 campos — nomenclatura completa

### Campo 1: `Referencia`

El marco normativo o documental de donde proviene cada fila. Hay **26 valores únicos**. Para definición completa de cada uno con URL, ver `F0-Lista_referencias_y_aportes.md`. Resumen:

| Valor | Tipo | Filas |
|---|---|---|
| `Res.0534` | Resolución 0534/2025 — Guía Técnica Ciclo de Vida (MVCT) | 53 |
| `Res.0194` | Resolución 0194/2025 — Anexo 1: Guía de ahorro agua y energía (MVCT) | 38 |
| `Ley.2462` | Ley 2462/2025 — Igualdad de oportunidades mujer rural | 28 |
| `CEELA` | Certificación de Edificaciones Eficientes en Latinoamérica (IFC/COSUDE) | 15 |
| `UPME-PGEE` | Cartilla y Guía PGEE-EP — Planes de Gestión Eficiente de Energía (UPME) | 10 |
| `GuiaMej-MVCT` | Guía de Sostenibilidad para Mejoramientos de Vivienda (MVCT) | 8 |
| `SUDS-MVCT` | Guía Metodológica SUDS (MVCT/DNP) | 6 |
| `EC-MADS`, `PNVISR`, `ParamSFVR` | Política y estrategia nacional | 4 c/u |
| `RAS`, `RETILAP` | Reglamentos técnicos sectoriales | 3 c/u |
| `R0019` | Resolución 0019/2022 — Requisitos sostenibilidad FRECH NO VIS (MVCT) | 2 |
| `D1285`, `D1467`, `D1727`, `D948`, `D1443` | Decretos reglamentarios | 1 c/u |
| `L1715`, `L373`, `L1931`, `L1819` | Leyes complementarias | 1 c/u |
| `R0472`, `R0541` | Resoluciones complementarias | 1 c/u |
| `CCCS-2024`, `ST333` | Informe sectorial / jurisprudencia | 1 c/u |

### Campo 2: `URL_fuente`

URL pública oficial del documento que respalda la fila. Las 191 filas tienen URL verificado.

- Sirve para abrir la fuente original en una pestaña nueva (la app la renderiza como botón clickeable)
- Apunta a sitios oficiales: `minvivienda.gov.co`, `funcionpublica.gov.co/eva/gestornormativo`, `proyectoceela.com`, `minenergia.gov.co`, etc.
- **Las filas con misma `Referencia` comparten URL** (es atributo de la fuente, no del criterio)

### Campo 3: `ID`

Código único de cada criterio dentro de su marco. Nomenclatura por marco:

#### Res. 0194 — 38 medidas

| Prefijo | Significado | Rango | Ejemplo |
|---|---|---|---|
| `MP-` | **M**edida **P**asiva de eficiencia energética | MP-01 a MP-15 | `MP-14` = Ventilación natural |
| `MA-` | **M**edida **A**ctiva de eficiencia energética | MA-01 a MA-13 | `MA-02` = LED >90 lm/W |
| `MW-` | **M**edida de eficiencia hídrica (***W**ater*) | MW-01 a MW-10 | `MW-08` = Captación aguas lluvias |

#### Res. 0534 — 53 criterios

| Prefijo | Significado | Ejemplo |
|---|---|---|
| `A-E-` | **A**mbiental — **E**nergía | `A-E-1` = Energía embebida en materiales |
| `A-A-` | **A**mbiental — **A**gua | `A-A-3` = Consumo agua proyectado |
| `A-EM-` | **A**mbiental — **EM**isiones | `A-EM-1` = Emisiones GEI fabricación |
| `A-M-` | **A**mbiental — **M**ateriales | `A-M-1` = Materiales con bajo impacto |
| `A-S-` | **A**mbiental — **S**uelo | `A-S-1` = Evaluación del sitio |
| `A-R-` | **A**mbiental — **R**esiduos | `A-R-2` = Diseño modular para disminuir RCD |
| `A-FL-` | **A**mbiental — **FL**ora y fauna | `A-FL-1` = Madera responsable |
| `A-SE-` | **A**mbiental — **S**ervicios **E**cosistémicos | `A-SE-1` = Drenaje sostenible (SUDS) |
| `S-CT-` | **S**ocial — **C**onfort **T**érmico | `S-CT-1` = Confort térmico por diseño |
| `S-CL-` | **S**ocial — **C**onfort **L**umínico | `S-CL-1` = Control contaminación lumínica |
| `S-A-` | **S**ocial — calidad del **A**ire | `S-A-1` = Calidad aire interior (ASHRAE 62) |
| `S-CA-` | **S**ocial — **C**onfort **A**cústico | `S-CA-1` = Diseño confort acústico (40 dBA) |
| `S-H-` | **S**ocial — **H**igiene y toxicidad | `S-H-1` = Materiales no tóxicos (HPD, VOC) |
| `S-AC-` | **S**ocial — **AC**cesibilidad | `S-AC-1` = Accesibilidad universal |
| `S-AS-` | **S**ocial — **A**cceso a **S**ervicios | `S-AS-1` = Distancia a servicios diarios |
| `E-CI-` | **E**conómico — **C**ostos **I**nversión | `E-CI-1` = Incidencia en costos |
| `E-CC-` | **E**conómico — **C**onsideraciones **C**omerciales | `E-CC-1` = Estrategia comercial |

#### CEELA — 15 criterios (originalmente "principios")

| Prefijo | Rango | Ejemplo |
|---|---|---|
| `C` | C01 a C15 | `C06` = Movimiento del aire |

> En CEELA original se llaman "principios"; en M1 se codifican como `Tipo=criterio` para alineación con el TdR. Ver `Glosario_terminos.md`.

#### Ley 2462 — 12 enfoques + 16 fines

| Prefijo | Significado | Rango | Ejemplo |
|---|---|---|---|
| `L-E` | **E**nfoque de la Ley (perspectiva/lente desde el cual mirar) | L-E01 a L-E12 | `L-E10` = Enfoque de cuidado |
| `L-F` | **F**in de la Ley (resultado concreto a lograr) | L-F01 a L-F16 | `L-F03` = Reducir carga trabajo doméstico |

#### UPME-PGEE — 10 filas

| Prefijo | Rango | Ejemplo |
|---|---|---|
| `UPME-` | UPME-1 a UPME-10 | `UPME-3` = Indicadores Desempeño Energético (IDE) |

#### Otras

| Prefijo | Marco | Ejemplo |
|---|---|---|
| `RET-` | RETILAP | `RET-2` = Diseño iluminación interior vivienda |
| `R0019-` | Resolución 0019/2022 | `R0019-1` = Sellos verdes FRECH NO VIS |
| `SUDS-` | Guía SUDS-MVCT | `SUDS-4` = Cisterna/aljibe |
| `PNVISR-`, `ParamSFVR-`, `GM-X-`, etc. | Otros | Códigos específicos de cada fuente |
| `Decretos`, `Leyes`, `Resoluciones` | Sigla del documento | `D1727-1`, `L1715-1`, `R0472-1`, `ST333-1` |

### Campo 4: `Criterio_medida`

Nombre corto del criterio, medida, principio, enfoque o fin. Texto libre.

### Campo 5: `Descripcion`

Descripción técnica con cita del marco normativo. Hasta ~300 caracteres.

### Campo 6: `Tipo`

Naturaleza del criterio. Indica de qué clase de instrumento se trata. **12 valores activos** en M1:

| Valor | Significado | Marcos donde aparece | Filas |
|---|---|---|---|
| `criterio_ambiental` | Criterio técnico de la dimensión ambiental | Res. 0534 | 68 |
| `criterio_social` | Criterio técnico de la dimensión social (confort, salud, accesibilidad) | Res. 0534 | 23 |
| `criterio` | Criterio genérico (incluye los 15 CEELA renombrados de "principio") | CEELA + otros | 18 |
| `fin` | Resultado concreto que el Estado debe lograr | Ley 2462 | 16 |
| `medida_pasiva` | Estrategia de diseño arquitectónico sin sistemas mecánicos | Res. 0194 | 15 |
| `medida_activa` | Sistema mecánico/eléctrico de bajo consumo | Res. 0194 | 13 |
| `enfoque` | Perspectiva/lente obligatoria para políticas públicas | Ley 2462 + PNVISR | 12 |
| `medida_hidrica` | Estrategia de ahorro, captación o reúso de agua | Res. 0194 | 10 |
| `criterio_economico` | Criterio técnico de la dimensión económica | Res. 0534 | 7 |
| `criterio_metodologico` | Procedimiento técnico o método de evaluación (renombrado de `metodologia`) | UPME-PGEE | 5 |
| `lineamiento` | Directriz institucional general (intermedia entre Estándar y Criterio) | UPME-PGEE | 1 |
| `medida` | Medida genérica que no encaja en pasiva/activa/hídrica | UPME-PGEE | 1 |

> Para la jerarquía conceptual completa (Fin → Enfoque → Estándar → Estrategia → Criterio → Medida), ver `Glosario_terminos.md`.

### Campo 7: `Etapa_ciclo_vida`

Fase del ciclo de vida de la edificación donde aplica el criterio.

| Valor | Significado |
|---|---|
| `extracción/manufactura` | Extracción de materias primas y fabricación de materiales |
| `pre-diseño` | Antes del diseño formal (diagnóstico, línea base) |
| `diseño` | Fase de diseño arquitectónico y estructural |
| `construcción` | Fase de obra |
| `operación` | Uso y mantenimiento de la edificación |
| `deconstrucción` | Desmontaje o demolición al final de la vida útil |
| `todas` | Aplica en todas las fases |
| `na` | No aplica a una fase específica (ej. enfoques de ley) |

### Campos 8–11: `E1_bioclimatica`, `E2_energia`, `E3_agua`, `E4_materiales`

Los **4 ejes de sostenibilidad del TdR**. Cada criterio se clasifica por su relación con cada eje. **Los valores son palabras completas** (no códigos):

| Valor | Significado |
|---|---|
| `Principal` | El eje es el **destino natural** del criterio. La fila aborda ese eje como tema central |
| `Complementario` | El criterio **toca el eje como efecto secundario**, no es su foco principal |
| `Transversal` | El criterio **aplica a todos los ejes por igual** (típico de C01 Diseño integrado, C11 Comportamiento usuario) |
| *(vacío)* | El criterio no tiene relación con este eje |

**Los 4 ejes:**

| Código | Eje | Qué incluye |
|---|---|---|
| **E1** | Estrategias bioclimáticas pasivas | Confort térmico y lumínico sin sistemas mecánicos: orientación solar, ventilación cruzada, inercia térmica, protección solar, aleros, night flush |
| **E2** | Estrategias de eficiencia energética de sistemas activos | Sistemas mecánicos/eléctricos: LED, paneles solares, estufas eficientes, calentadores solares, FNCE, HVAC eficiente, monitoreo |
| **E3** | Estrategias de eficiencia hídrica | Ahorro, captación, reúso y tratamiento de agua: captación pluvial, aparatos bajo consumo, aguas grises, SUDS |
| **E4** | Estrategias de uso de materiales con atributos de sostenibilidad | Selección por impacto ambiental: energía embebida (GWP), ciclo de vida (ACV), toxicidad, contenido reciclado, origen regional, madera responsable, circularidad |

**Ejemplos de lectura:**

| Fila | E1 | E2 | E3 | E4 | Lectura |
|---|---|---|---|---|---|
| MP-14 Ventilación natural | Principal | — | — | — | Es bioclimática pura |
| MP-09 Valor U paredes externas | Principal | — | — | Complementario | Aislamiento bioclimático con efecto en materiales |
| MA-01 Iluminación natural + sensores | Complementario | Principal | — | — | Foco en sistema activo, aporta a bioclimática |
| C01 Diseño integrado (CEELA) | Transversal | Transversal | Transversal | Transversal | Enfoque de proceso, toca los 4 ejes |

### Campo 12: `Notas`

Texto libre con observaciones sobre el criterio. Sirve para todos los temas:
- Aplicabilidad y alternativas vernáculas en vivienda rural
- Conexiones con género y datos ENUT 2024–2025
- Conexiones con inclusión social (accesibilidad, adecuación cultural)
- Métricas técnicas, materiales locales
- Vacíos normativos y alertas

**Ejemplos:**
- *"Aleros >80 cm son la estrategia vernácula más común en vivienda rural colombiana. Bajo costo; alta efectividad; fácil de construir con mano de obra local"*
- *"ENUT 2024-25: mujeres rurales 8h53min/día trabajo no remunerado; captación pluvial elimina acarreo agua (Ley 2462 Fin 3)"*
- *"Vidrios especiales tienen costo alto para VIS rural (70 SMLV). Alternativa: reducir área vidriada + protección solar externa"*

Cuando combina varios temas, se separan con ` | `.

### Campo 13: `Ref_Ley2462`

Códigos de la Ley 2462/2025 (enfoques y fines) que aplican a este criterio. Permite **filtrar** todos los criterios con conexión a género e inclusión social sin leer el texto libre.

| Formato | Ejemplo |
|---|---|
| Códigos separados por `;` | `L-F03; L-E10` |
| Vacío si no aplica | *(vacío)* |

Para detalle de cada código, ver fila correspondiente en M1 (`Referencia=Ley.2462`).

### Campo 14: `Aplica_vivienda_rural`

¿Es viable o pertinente para vivienda rural unifamiliar VIS/VIP de un piso?

| Valor | Significado |
|---|---|
| `si` | Aplica directamente |
| `condicional` | Aplica según clima, presupuesto o infraestructura disponible |
| `no` | No aplica — diseñado para edificaciones comerciales/industriales o programas urbanos (ej. R0019 FRECH NO VIS) |

**Para trabajar solo con lo relevante:** filtrar `si` + `condicional`.

### Campo 15: `Clima`

Clima(s) donde aplica el criterio. Basado en la clasificación Caldas-Lang adoptada por el Anexo 1.

| Valor | Significado |
|---|---|
| `frio` | Clima frío (>3.000 msnm; <12°C) — Bogotá, Tunja, Pasto, páramos |
| `templado` | Clima templado (2.000–2.999 msnm; 12–18°C) — Medellín, Ibagué, eje cafetero |
| `calido_seco` | Cálido seco (HR <75%) — Cali, Guajira, Tatacoa, Llanos secos |
| `calido_humedo` | Cálido húmedo (HR >75%) — Barranquilla, Pacífico, Amazonía |
| `todos` | Aplica en los 4 climas |

Cuando un criterio aplica a varios climas pero no a todos, se separan con espacio: `frio templado`.

### Campo 16: `Subsistema`

Subsistema constructivo donde se implementa el criterio. **Valores con nombre completo** (no códigos):

| Valor | Función |
|---|---|
| `Cimentación` | Transmite cargas al suelo; aísla de humedad |
| `Estructura` | Soporta cargas verticales y laterales (muros portantes, pórticos) |
| `Envolvente` | Cierra el volumen interior (muros divisorios, ventanas, puertas) |
| `Cubierta` | Protege de lluvia y radiación (estructura techo + cobertura + aleros) |
| `Instalaciones` | Hidráulica, sanitaria, eléctrica, gas, paneles solares, biodigestor |
| `Acabados y complementos` | No estructurales: pintura, pisos, aislantes, protección solar añadida |
| `Exterior` | Patios, jardines, paisajismo, drenaje |
| `todos` | Toda la vivienda (criterios de proceso o política general) |
| `na` | No aplica a un subsistema específico (enfoques legales, políticas) |

Cuando aplica a varios se separan con espacio: `Estructura Envolvente`.

### Campo 17: `Caracter_legal`

¿Es exigible por ley colombiana o es voluntario?

| Valor | Significado | Marcos típicos |
|---|---|---|
| `obligatorio` | Exigible por ley o resolución ministerial — puede haber sanción por incumplimiento | Res. 0194, Res. 0534, Ley 2462, RAS, RETILAP, R0019 |
| `voluntario` | Buena práctica recomendada — sin sanción por no cumplir | CEELA |
| `recomendado` | Sugerido por la entidad sectorial pero no obligatorio | UPME-PGEE (mayoría) |
| `condicional` | El nivel mínimo es obligatorio pero los niveles superiores son voluntarios | Algunos criterios de Res. 0534 |

### Campo 18: `Nivel_cumplimiento`

Nivel de exigencia **dentro** del criterio. Diferente del carácter legal.

| Valor | Significado | Marco |
|---|---|---|
| `recomendada` | El Anexo 1 la recomienda para obtener el % de ahorro mínimo | Res. 0194 |
| `a_discrecion` | A criterio del constructor (evaluar viabilidad técnica y económica) | Res. 0194 |
| `minimo` | Nivel base obligatorio que todo proyecto debe cumplir | Res. 0534, RETILAP, R0019 |
| `deseable` | Nivel intermedio voluntario que mejora el desempeño | Res. 0534, UPME-PGEE |
| `avanzado` | Nivel superior voluntario de excelencia | Res. 0534, UPME-PGEE |
| `na` | No aplica (enfoques/fines de Ley 2462 no tienen niveles) | Ley 2462 |

### Campo 19: `Parametro_indicador`

Métrica cuantitativa asociada al criterio, si existe. Vacío si no tiene indicador numérico.

**Ejemplos:**
- `Valor U (W/m²K)` — aislamiento térmico
- `SHGC (0-1)` — ganancia solar del vidrio
- `ACH (cambios/hora)` — ventilación
- `l/min` — caudal de grifería
- `kg CO₂eq/kg` — huella de carbono
- `% ahorro vs línea base` — eficiencia
- `dBA` — ruido
- `kWh/m²/año` — desempeño energético (UPME-PGEE)
- `Clase RETIQ (A; B; C…)` — etiquetado eficiencia (UPME-PGEE)
- `≥25% energía; 25% agua; 20% materiales` — niveles EDGE (R0019)

### Campo 20: `Correspondencia_cruzada`

IDs de criterios **equivalentes en otros marcos** que cubren el mismo tema. Permite ver qué dice cada norma sobre un mismo asunto.

**Formato:** `Marco:ID; Marco:ID`

**Ejemplos:**
- `Res.0534:S-CT-1; CEELA:C04` → inercia térmica está en Res. 0194 (MP-13), Res. 0534 (S-CT-1) y CEELA (C04)
- `Ley.2462:L-F03` → captación pluvial conecta con el Fin 3 de la Ley 2462 (reducir carga doméstica)
- `Res.0194:MA-02; CEELA:C10; PROURE Res.41286/2016` → eficiencia LED conecta múltiples marcos

---

## 4. Consultas frecuentes (cómo filtrar)

### "¿Qué debo cumplir obligatoriamente en clima cálido seco?"
1. Filtrar `Caracter_legal` = `obligatorio`
2. Filtrar `Clima` contiene `calido_seco` o `todos`
3. Filtrar `Aplica_vivienda_rural` = `si` o `condicional`

### "¿Qué criterios hay sobre materiales sostenibles?"
1. Filtrar `E4_materiales` = `Principal`
2. Ver los resultados de los 26 marcos

### "¿Qué criterios tienen enfoque de género o inclusión social?"
1. Filtrar `Ref_Ley2462` ≠ vacío
2. Resultado: todos los criterios con conexión a Ley 2462
3. Para ver el detalle: leer columna `Notas`

### "¿Qué dice cada norma sobre ventilación?"
1. Buscar `ventilación` o `aire` en columna `Criterio_medida`
2. O buscar `MP-14` en `Correspondencia_cruzada` para ver equivalentes

### "¿Qué criterios de la Res. 0534 son nuevos (no estaban en Res. 0194)?"
1. Filtrar `Referencia` = `Res.0534`
2. Filtrar `Correspondencia_cruzada` = vacío
3. Resultado: criterios exclusivos de la Guía Ciclo de Vida

### "¿Cuáles NO aplican a vivienda rural?"
1. Filtrar `Aplica_vivienda_rural` = `no`
2. Resultado: medidas de infraestructura comercial + R0019 (FRECH NO VIS)

### "¿Qué criterios aplican al subsistema de cubierta?"
1. Filtrar `Subsistema` contiene `Cubierta`

### "¿Qué criterios tienen notas sobre contexto rural?"
1. Filtrar `Notas` ≠ vacío
2. Buscar texto "rural" o "vernácula" o "ENUT"

### "¿Qué criterios conectan con un fin específico de la Ley 2462?"
1. Filtrar `Ref_Ley2462` contiene `L-F03` (ej. reducir carga doméstica)
2. Resultado: todos los criterios que impactan ese fin

### "¿Cómo abrir directamente el documento original de un criterio?"
- En la app: click en el botón "abrir" de la columna `URL fuente`
- En Excel: copiar URL de la columna y pegar en navegador

### "¿Qué criterios de UPME-PGEE son aplicables a vivienda rural?"
1. Filtrar `Referencia` = `UPME-PGEE`
2. Filtrar `Aplica_vivienda_rural` ≠ `no`

### "¿Qué criterios son transversales a los 4 ejes?"
1. Filtrar cualquier `E1_bioclimatica`, `E2_energia`, `E3_agua` o `E4_materiales` = `Transversal`
2. Resultado: criterios de proceso o política (ej. C01 Diseño integrado, C11 Comportamiento)

---

## 5. Relación con otros documentos del proyecto

| Documento | Relación |
|---|---|
| `F0-Lista_referencias_y_aportes.md` | Inventario detallado de las 26 referencias con URL clickeable, distribución por categoría/eje/carácter, alertas |
| `F0-Matriz_casos_exito.csv` | Matriz M2 — casos vernáculos y contemporáneos que materializan estos estándares |
| `F8-Matriz_casos_diccionario.md` | Diccionario de M2 (casos) |
| `F6-Plan_busqueda_casos.md` | Plan de búsqueda de casos M2 |
| `Glosario_terminos.md` | Definiciones de Fin, Enfoque, Estándar, Estrategia, Criterio, Medida + términos pragmáticos del campo `Tipo` |
| `F1-Matriz_busqueda.csv` | Matriz de búsqueda bibliográfica — referencias BS apuntan a IDs de aquí en `Observaciones` |
| `F1-Marco_busqueda_sistemas_materiales.md` | Definición de subsistemas usados en la columna `Subsistema` |

> Documentos de análisis temprano (F0-3-AnalisisGuias, F0-3-Síntesis-Anexo1, F0-3b-Medidas_Anexo1_Cap2, F0-3c-Cruce_Estandares_Ejes, F0-3d-Criterios_Guia_Ciclo_Vida, F0-3e-Ley2462_genero_inclusion, F0-3f-Revision_normativa_complementaria) están archivados en `docs/DESCARTADOS/`. Su contenido fue consolidado en M1 + Lista de referencias + Glosario.

## 6. Resumen de nomenclaturas

### Todos los prefijos de ID en M1

| Prefijo | Marco | Tipo | Filas |
|---|---|---|---|
| `MP-` | Res. 0194 | Medida pasiva | 15 |
| `MA-` | Res. 0194 | Medida activa | 13 |
| `MW-` | Res. 0194 | Medida hídrica | 10 |
| `A-E-`, `A-A-`, `A-EM-`, `A-M-`, `A-S-`, `A-R-`, `A-FL-`, `A-SE-` | Res. 0534 | Criterios ambientales (8 sub-prefijos) | ~42 |
| `S-CT-`, `S-CL-`, `S-A-`, `S-CA-`, `S-H-`, `S-AC-`, `S-AS-` | Res. 0534 | Criterios sociales (7 sub-prefijos) | ~12 |
| `E-CI-`, `E-CC-` | Res. 0534 | Criterios económicos (2 sub-prefijos) | ~2 |
| `C` | CEELA | Criterio CEELA (renombrado de "principio") | 15 |
| `L-E` | Ley 2462 | Enfoque legal | 12 |
| `L-F` | Ley 2462 | Fin legal (objetivo a lograr) | 16 |
| `UPME-` | UPME-PGEE | Criterios y metodologías PGEE | 10 |
| `RET-` | RETILAP | Iluminación y URE | 3 |
| `SUDS-` | SUDS-MVCT | Tipologías de drenaje sostenible | 6 |
| `R0019-` | R0019 | Sellos verdes y niveles EDGE | 2 |
| `GM-X-`, `PNVISR-`, `ParamSFVR-`, etc. | Otros | Códigos específicos | varios |
| Decretos / Leyes / Sentencia / Otros | varios | 1 fila por documento | varios |
| | | **Total** | **191** |

### Valores del campo Tipo

| Valor | Significado | Filas |
|---|---|---|
| `criterio_ambiental` / `_social` / `_economico` | Sub-tipos de Criterio (Res. 0534) | 68 / 23 / 7 |
| `criterio` | Criterio genérico (incluye los 15 CEELA) | 18 |
| `fin` | Fin legal (Ley 2462) | 16 |
| `medida_pasiva` / `_activa` / `_hidrica` | Sub-tipos de Medida (Res. 0194) | 15 / 13 / 10 |
| `enfoque` | Enfoque legal (Ley 2462, PNVISR) | 12 |
| `criterio_metodologico` | Procedimiento o método de evaluación (UPME-PGEE) | 5 |
| `lineamiento` | Directriz institucional general | 1 |
| `medida` | Medida genérica | 1 |

### Valores del campo E1–E4

| Valor | Significado |
|---|---|
| `Principal` | Eje destino natural del criterio |
| `Complementario` | Toca el eje como efecto secundario |
| `Transversal` | Aplica a todos los ejes por igual |
| *(vacío)* | No aplica |

### Valores del campo Caracter_legal

| Valor | Significado |
|---|---|
| `obligatorio` | Exigible por ley/resolución colombiana |
| `voluntario` | Buena práctica sin sanción (CEELA) |
| `recomendado` | Sugerido por entidad sectorial (UPME-PGEE) |
| `condicional` | Solo nivel mínimo es obligatorio |

### Subsistemas constructivos

| Valor | Función |
|---|---|
| `Cimentación` | Transmite cargas al suelo; aísla de humedad |
| `Estructura` | Soporta cargas verticales y laterales |
| `Envolvente` | Cierra el volumen interior |
| `Cubierta` | Protege de lluvia y radiación |
| `Instalaciones` | Hidráulica, sanitaria, eléctrica, gas, FV |
| `Acabados y complementos` | No estructurales |
| `Exterior` | Patios, jardines, paisajismo, drenaje |
| `todos` | Toda la vivienda |
| `na` | No aplica a subsistema |

Cuando aplica a varios se separan con espacio: `Estructura Envolvente`.

### Climas

| Valor | Nombre |
|---|---|
| `frio` | Frío (>3.000 msnm) |
| `templado` | Templado (2.000–2.999 msnm) |
| `calido_seco` | Cálido seco (HR <75%) |
| `calido_humedo` | Cálido húmedo (HR >75%) |
| `todos` | Los 4 climas |

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | 2026-04-23 | Tutorial inicial: 19 campos, nomenclaturas completas, consultas frecuentes |
| 0.2 | 2026-04-29 | Columnas: `Enfoque_genero` + `Inclusion_social` reemplazadas por `Notas` + `Ref_Ley2462`. Subsistemas con nombre completo. Ejes con nombre completo |
| 0.3 | 2026-05-05 | Total filas 134 → 191. Total referencias 4 → 26 (+UPME-PGEE, +RETILAP, +R0019, +todas las demás del proyecto). +Campo `URL_fuente` (col 2; 191/191 con URL clickeable). Tipo: `principio` renombrado a `criterio` (CEELA), `metodologia` renombrado a `criterio_metodologico` (UPME-PGEE), +`lineamiento`. Ejes E1–E4 valores corregidos a palabras completas (Principal/Complementario/Transversal en lugar de P/C/T). Sección 5 actualizada con docs vigentes (varios F0-3-* movidos a DESCARTADOS) |
