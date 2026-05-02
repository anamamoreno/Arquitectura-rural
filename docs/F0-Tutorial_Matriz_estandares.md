# Tutorial: Matriz de estándares de sostenibilidad

> **¿Qué es este documento?** Guía para entender, consultar y filtrar la matriz `F0-Matriz_estandares_sostenibilidad.csv`. Explica qué significa cada campo, cada código y cada nomenclatura empleada. Para que cualquier integrante del equipo pueda abrir la matriz en Excel y encontrar respuestas sin ambigüedad.

**Archivo:** `docs/F0-Matriz_estandares_sostenibilidad.csv`
**Contenido:** 134 filas — todos los criterios, medidas, principios, enfoques y fines de los 4 marcos normativos del proyecto.
**Versión:** 0.1 · **Fecha:** 2026-04-23.

---

## 1. Qué es esta matriz

Es el **catálogo normativo consolidado** del proyecto. Reúne en una sola tabla todo lo que las normas y marcos de referencia dicen sobre sostenibilidad en edificaciones, clasificado por eje, clima, aplicabilidad rural y carácter legal.

**No es la Matriz M1.** La M1 registra hallazgos de la búsqueda bibliográfica. Esta matriz registra lo que dicen las normas. Relación:

| Esta matriz (F0-Estándares) | Matriz M1 (F1/F4-Hallazgos) |
|---|---|
| **Lo que exige la norma** | **Lo que se encontró en la literatura** |
| 134 filas fijas | ~100–150 filas crecientes |
| Se construyó una vez | Se llena durante la ejecución |
| Cada fila de M1 apunta aquí | Las columnas `Medida_Anexo1_ref`, `Criterio_0534_ref`, `Criterio_CEELA_ref` de M1 usan los IDs de esta matriz |

## 2. Cómo abrirla

1. Ir a `docs/F0-Matriz_estandares_sostenibilidad.csv`.
2. **Excel:** doble clic. Si todo aparece en una columna → `Datos → Desde texto/CSV` → separador **coma** → codificación **UTF-8**.
3. **Google Sheets:** subir a Drive → Abrir con Google Sheets.

## 3. Los 19 campos — nomenclatura completa

### Campo 1: `Referencia`

El marco normativo de donde proviene el criterio.

| Valor | Marco completo | Año | Entidad |
|---|---|---|---|
| `Res.0194` | Resolución 0194 de 2025 — Anexo 1: Guía de ahorro de agua y energía en edificaciones | 2025 | MVCT |
| `Res.0534` | Resolución 0534 de 2025 — Guía Técnica: Criterios de Sostenibilidad para Edificaciones — Ciclo de Vida | 2025 | MVCT |
| `CEELA` | Certificación de Edificaciones Eficientes en Latinoamérica | — | IFC / Banco Mundial |
| `Ley.2462` | Ley 2462 de 2025 — Igualdad de oportunidades mujeres rurales, campesinas y de la pesca | 2025 | Congreso de Colombia |

---

### Campo 2: `ID`

Código único de cada criterio dentro de su marco. Nomenclatura por marco:

#### Res. 0194 — 38 medidas

| Prefijo | Significado | Rango | Ejemplo |
|---|---|---|---|
| `MP-` | **M**edida **P**asiva de eficiencia energética | MP-01 a MP-15 | `MP-14` = Ventilación natural |
| `MA-` | **M**edida **A**ctiva de eficiencia energética | MA-01 a MA-13 | `MA-02` = LED >90 lm/W |
| `MW-` | **M**edida de eficiencia en agua (*W*ater) | MW-01 a MW-10 | `MW-08` = Captación aguas lluvias |

#### Res. 0534 — 42 criterios

| Prefijo | Significado | Ejemplo |
|---|---|---|
| `A-E-` | **A**mbiental — **E**nergía | `A-E-1` = Energía embebida en materiales |
| `A-A-` | **A**mbiental — **A**gua | `A-A-3` = Consumo agua proyectado |
| `A-EM-` | **A**mbiental — **EM**isiones | `A-EM-1` = Emisiones GEI fabricación |
| `A-M-` | **A**mbiental — **M**ateriales | `A-M-1` = Diseño con materiales sostenibles |
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

#### CEELA — 15 principios

| Prefijo | Rango | Ejemplo |
|---|---|---|
| `C` | C01 a C15 | `C06` = Movimiento del aire |

#### Ley 2462 — 12 enfoques + 16 fines

| Prefijo | Significado | Rango | Ejemplo |
|---|---|---|---|
| `L-E` | Enfoque de la **L**ey (perspectiva/lente desde el cual mirar) | L-E01 a L-E12 | `L-E10` = Enfoque de cuidado |
| `L-F` | Fin de la **L**ey (resultado concreto a lograr) | L-F01 a L-F16 | `L-F03` = Reducir carga trabajo doméstico |

---

### Campo 3: `Criterio_medida`

Nombre corto del criterio, medida, principio, enfoque o fin. Texto libre.

---

### Campo 4: `Descripcion`

Descripción en máximo 200 caracteres. Explica qué es y cómo funciona.

---

### Campo 5: `Tipo`

Naturaleza del criterio. Indica de qué clase de instrumento se trata.

| Valor | Significado | Marcos donde aparece |
|---|---|---|
| `medida_pasiva` | Estrategia de diseño arquitectónico sin sistemas mecánicos | Res. 0194 |
| `medida_activa` | Sistema mecánico/eléctrico de bajo consumo | Res. 0194 |
| `medida_hidrica` | Estrategia de ahorro, captación o reúso de agua | Res. 0194 |
| `criterio_ambiental` | Criterio técnico de la dimensión ambiental | Res. 0534 |
| `criterio_social` | Criterio técnico de la dimensión social (confort, salud, accesibilidad) | Res. 0534 |
| `criterio_economico` | Criterio técnico de la dimensión económica (costos, comercial) | Res. 0534 |
| `principio` | Principio conceptual de diseño sostenible | CEELA |
| `enfoque` | Perspectiva/lente obligatorio para políticas públicas de mujer rural | Ley 2462 |
| `fin` | Resultado concreto que el Estado debe lograr para mujeres rurales | Ley 2462 |

---

### Campo 6: `Etapa_ciclo_vida`

Fase del ciclo de vida de la edificación donde aplica el criterio.

| Valor | Significado |
|---|---|
| `extracción/manufactura` | Extracción de materias primas y fabricación de materiales |
| `diseño` | Fase de diseño arquitectónico y estructural |
| `construcción` | Fase de obra |
| `operación` | Uso y mantenimiento de la edificación |
| `deconstrucción` | Desmontaje o demolición al final de la vida útil |
| `todas` | Aplica en todas las fases |
| `na` | No aplica a una fase específica (ej. enfoques de ley) |

---

### Campos 7–10: `E1_bioclimatica`, `E2_energia`, `E3_agua`, `E4_materiales`

Los 4 ejes de sostenibilidad del TdR. Cada criterio se clasifica por su relación con cada eje.

| Valor | Significado |
|---|---|
| `P` | **Principal** — el eje es el destino natural de este criterio |
| `C` | **Complementario** — toca el eje como efecto secundario |
| `T` | **Transversal** — aplica a todos los ejes por igual (no es técnico sino de proceso o política) |
| *(vacío)* | No tiene relación con este eje |

**Los 4 ejes:**

| Código | Eje | Qué incluye |
|---|---|---|
| **E1** | Estrategias bioclimáticas pasivas | Confort térmico y lumínico sin sistemas mecánicos: orientación solar, ventilación cruzada, inercia térmica, protección solar, aleros, night flush |
| **E2** | Estrategias de eficiencia energética de sistemas activos | Sistemas mecánicos/eléctricos: LED, paneles solares, estufas eficientes, calentadores solares, FNCE, HVAC eficiente |
| **E3** | Estrategias de eficiencia hídrica | Ahorro, captación, reúso y tratamiento de agua: captación pluvial, aparatos bajo consumo, aguas grises, SUDS |
| **E4** | Estrategias de uso de materiales con atributos de sostenibilidad | Selección por impacto ambiental: energía embebida (GWP), ciclo de vida (ACV), toxicidad, contenido reciclado, origen regional, madera responsable, circularidad |

---

### Campo 11: `Notas`

Campo de texto libre para **cualquier observación relevante** sobre el criterio. Sirve para todos los ejes, no solo género/inclusión. Incluye:
- Implicaciones para **vivienda rural** (aplicabilidad, alternativas vernáculas, viabilidad económica VIS).
- Conexiones con **género** y datos ENUT 2024–2025.
- Conexiones con **inclusión social** (accesibilidad, adecuación cultural, saberes ancestrales).
- Observaciones técnicas (métricas, materiales locales, particularidades climáticas).
- Vacíos normativos y alertas.

**Ejemplos:**
- `Aleros >80 cm son la estrategia vernácula más común en vivienda rural colombiana. Bajo costo; alta efectividad; fácil de construir con mano de obra local`
- `ENUT 2024-25: mujeres rurales 8h53min/día trabajo no remunerado; captación pluvial elimina acarreo agua (Ley 2462 Fin 3)`
- `NTC 6047 accesibilidad; Sentencia T-333 adecuación cultural obligatoria`
- `Vidrios especiales tienen costo alto para VIS rural (70 SMLV). Alternativa: reducir área vidriada + protección solar externa`
- *(vacío)* = sin observación adicional (la descripción del criterio es suficiente)

Cuando una nota combina temas de género + inclusión + técnico, se separan con ` | `.

---

### Campo 12: `Ref_Ley2462`

Códigos de la Ley 2462/2025 (enfoques y fines) que aplican a este criterio. Permite **filtrar** todos los criterios que tienen conexión con género e inclusión social sin leer el texto libre.

| Formato | Ejemplo |
|---|---|
| Códigos separados por `;` | `L-F03; L-E10` |
| Vacío si no aplica | *(vacío)* |

**Prefijos:**
- `L-E` = Enfoque de la Ley (perspectiva obligatoria). Ej: `L-E10` = Enfoque de cuidado.
- `L-F` = Fin de la Ley (resultado concreto a lograr). Ej: `L-F03` = Reducir carga trabajo doméstico.

Para el detalle de cada código, consultar `F0-3e-Ley2462_genero_inclusion.md`.

---

### Campo 13: `Aplica_vivienda_rural`

¿Es viable o pertinente para vivienda rural unifamiliar VIS/VIP de un piso?

| Valor | Significado | Cuántas filas |
|---|---|---|
| `si` | Aplica directamente | 110 |
| `condicional` | Aplica según clima, presupuesto o infraestructura disponible | 16 |
| `no` | No aplica — diseñado para edificaciones comerciales/industriales | 8 |

**Para trabajar solo con lo relevante:** filtrar `si` + `condicional` → quedan **126 criterios**.

---

### Campo 14: `Clima`

Clima(s) donde aplica el criterio. Basado en la clasificación Caldas-Lang adoptada por el Anexo 1.

| Valor | Significado |
|---|---|
| `frio` | Clima frío (>3.000 msnm; <12°C) — Bogotá, Tunja, Pasto, páramos |
| `templado` | Clima templado (2.000–2.999 msnm; 12–18°C) — Medellín, Ibagué, eje cafetero |
| `calido_seco` | Cálido seco (HR <75%) — Cali, Guajira, Tatacoa, Llanos |
| `calido_humedo` | Cálido húmedo (HR >75%) — Barranquilla, Pacífico, Amazonía |
| `todos` | Aplica en los 4 climas |

Cuando un criterio aplica a varios climas pero no a todos, se separan con espacio: `frio templado`.

---

### Campo 15: `Subsistema`

Subsistema constructivo donde se implementa el criterio.

| Código | Subsistema | Función |
|---|---|---|
| `S1` | Cimentación | Transmite cargas al suelo; aísla de humedad |
| `S2` | Estructura | Soporta cargas verticales y laterales (muros portantes, pórticos) |
| `S3` | Envolvente | Cierra el volumen interior (muros divisorios, ventanas, puertas) |
| `S4` | Cubierta | Protege de lluvia y radiación (estructura techo + cobertura + aleros) |
| `S5` | Instalaciones | Hidráulica, sanitaria, eléctrica, gas, paneles solares, biodigestor |
| `S6` | Acabados y complementos | No estructurales: pintura, pisos, aislantes, protección solar añadida |
| `Exterior` | Espacio exterior | Patios, jardines, paisajismo, drenaje |
| `todos` | Aplica a toda la vivienda | Criterios de proceso o política general |
| `na` | No aplica a un subsistema específico | Enfoques legales, políticas de compras |

Cuando aplica a varios se separan con espacio: `S2 S3`.

---

### Campo 16: `Caracter_legal`

¿Es exigible por ley colombiana o es voluntario?

| Valor | Significado | Marcos |
|---|---|---|
| `obligatorio` | Exigible por ley o resolución ministerial — puede haber sanción por incumplimiento | Res. 0194, Res. 0534, Ley 2462 |
| `voluntario` | Buena práctica recomendada — sin sanción por no cumplir | CEELA |
| `condicional` | El nivel mínimo es obligatorio pero los niveles superiores (deseable/avanzado) son voluntarios | Algunos criterios de Res. 0534 |

---

### Campo 17: `Nivel_cumplimiento`

Nivel de exigencia **dentro** del criterio. Diferente del carácter legal.

| Valor | Significado | Marco |
|---|---|---|
| `recomendada` | El Anexo 1 la recomienda para obtener el % de ahorro mínimo | Res. 0194 |
| `a_discrecion` | A criterio del constructor (evaluar viabilidad técnica y económica) | Res. 0194 |
| `minimo` | Nivel base obligatorio que todo proyecto debe cumplir | Res. 0534 |
| `deseable` | Nivel intermedio voluntario que mejora el desempeño | Res. 0534 |
| `avanzado` | Nivel superior voluntario de excelencia | Res. 0534 |
| `na` | No aplica (principios CEELA y enfoques/fines Ley 2462 no tienen niveles) | CEELA, Ley 2462 |

---

### Campo 18: `Parametro_indicador`

Métrica cuantitativa asociada al criterio, si existe. Vacío si no tiene indicador numérico.

**Ejemplos:**
- `Valor U (W/m²K)` — aislamiento térmico
- `SHGC (0-1)` — ganancia solar del vidrio
- `ACH (cambios/hora)` — ventilación
- `l/min` — caudal de grifería
- `kg CO₂eq/kg` — huella de carbono
- `% ahorro vs línea base` — eficiencia
- `dBA` — ruido

---

### Campo 19: `Correspondencia_cruzada`

IDs de criterios **equivalentes en otros marcos** que cubren el mismo tema. Permite ver qué dice cada norma sobre un mismo asunto.

**Formato:** `Marco:ID; Marco:ID`

**Ejemplos:**
- `Res.0534:S-CT-1; CEELA:C04` → inercia térmica está en Res. 0194 (MP-13), en Res. 0534 (S-CT-1) y en CEELA (C04)
- `Ley.2462:L-F03` → captación pluvial tiene conexión con el Fin 3 de la Ley 2462 (reducir carga doméstica)

---

## 4. Consultas frecuentes (cómo filtrar)

### "¿Qué debo cumplir obligatoriamente en clima cálido seco?"
1. Filtrar `Caracter_legal` = `obligatorio`
2. Filtrar `Clima` contiene `calido_seco` o `todos`
3. Filtrar `Aplica_vivienda_rural` = `si` o `condicional`

### "¿Qué criterios hay sobre materiales sostenibles?"
1. Filtrar `E4_materiales` = `P`
2. Ver los resultados de los 4 marcos

### "¿Qué criterios tienen enfoque de género o inclusión social?"
1. Filtrar `Ref_Ley2462` ≠ vacío
2. Resultado: todos los criterios con conexión a Ley 2462 (género, cuidado, inclusión, étnico)
3. Para ver el detalle: leer columna `Notas` de cada fila

### "¿Qué dice cada norma sobre ventilación?"
1. Buscar `ventilación` o `aire` en columna `Criterio_medida`
2. O buscar `MP-14` en `Correspondencia_cruzada` para ver equivalentes

### "¿Qué criterios de la Res. 0534 son nuevos (no estaban en Res. 0194)?"
1. Filtrar `Referencia` = `Res.0534`
2. Filtrar `Correspondencia_cruzada` = vacío
3. Resultado: criterios exclusivos de la Guía Ciclo de Vida

### "¿Cuáles NO aplican a vivienda rural?"
1. Filtrar `Aplica_vivienda_rural` = `no`
2. Resultado: 8 medidas de infraestructura comercial

### "¿Qué criterios aplican al subsistema de cubierta?"
1. Filtrar `Subsistema` contiene `Cubierta`

### "¿Qué criterios tienen notas sobre contexto rural?"
1. Filtrar `Notas` ≠ vacío
2. Buscar texto "rural" o "vernácula" o "ENUT" en `Notas`

### "¿Qué criterios conectan con un fin específico de la Ley 2462?"
1. Filtrar `Ref_Ley2462` contiene `L-F03` (ej. reducir carga doméstica)
2. Resultado: todos los criterios que impactan ese fin

## 5. Relación con los otros documentos del proyecto

| Documento | Relación |
|---|---|
| `F0-3b-Medidas_Anexo1_Cap2.md` | Detalle de las 38 medidas Res. 0194 (fichas técnicas) |
| `F0-3d-Criterios_Guia_Ciclo_Vida.md` | Detalle de los 42 criterios Res. 0534 (niveles mínimo/deseable/avanzado) |
| `F0-3c-Cruce_Estandares_Ejes.md` | Cruce de los 3 marcos técnicos × 4 ejes con conteos |
| `F0-3e-Ley2462_genero_inclusion.md` | Análisis de la Ley 2462 y su aplicación al proyecto |
| `F1-Matriz_M1.csv` | Matriz de hallazgos — columnas `Medida_Anexo1_ref`, `Criterio_0534_ref`, `Criterio_CEELA_ref` apuntan a los IDs de esta matriz |
| `F1-Matriz_busqueda.csv` | Matriz de búsqueda — las filas BS referencian criterios de esta matriz en `Observaciones` |
| `F1-Marco_busqueda_sistemas_materiales.md` | Definición de subsistemas S1–S6 usados en columna `Subsistema` |

## 6. Resumen de nomenclaturas

### Todos los prefijos de ID

| Prefijo | Marco | Tipo | Total |
|---|---|---|---|
| `MP-` | Res. 0194 | Medida pasiva | 15 |
| `MA-` | Res. 0194 | Medida activa | 13 |
| `MW-` | Res. 0194 | Medida hídrica | 10 |
| `A-E-` | Res. 0534 | Criterio ambiental — energía | 6 |
| `A-A-` | Res. 0534 | Criterio ambiental — agua | 7 |
| `A-EM-` | Res. 0534 | Criterio ambiental — emisiones | 8 |
| `A-M-` | Res. 0534 | Criterio ambiental — materiales | 2 |
| `A-S-` | Res. 0534 | Criterio ambiental — suelo | 1 |
| `A-R-` | Res. 0534 | Criterio ambiental — residuos | 6 |
| `A-FL-` | Res. 0534 | Criterio ambiental — flora/fauna | 3 |
| `A-SE-` | Res. 0534 | Criterio ambiental — ecosistémicos | 2 |
| `S-CT-` | Res. 0534 | Criterio social — confort térmico | 3 |
| `S-CL-` | Res. 0534 | Criterio social — confort lumínico | 2 |
| `S-A-` | Res. 0534 | Criterio social — calidad aire | 3 |
| `S-CA-` | Res. 0534 | Criterio social — confort acústico | 2 |
| `S-H-` | Res. 0534 | Criterio social — higiene/toxicidad | 3 |
| `S-AC-` | Res. 0534 | Criterio social — accesibilidad | 2 |
| `S-AS-` | Res. 0534 | Criterio social — acceso servicios | 1 |
| `E-CI-` | Res. 0534 | Criterio económico — costos | 1 |
| `E-CC-` | Res. 0534 | Criterio económico — comercial | 1 |
| `C` | CEELA | Principio | 15 |
| `L-E` | Ley 2462 | Enfoque legal | 12 |
| `L-F` | Ley 2462 | Fin legal (objetivo a lograr) | 16 |
| | | **Total** | **134** |

### Valores del campo E1–E4

| Valor | Significado |
|---|---|
| `P` | Principal |
| `C` | Complementario |
| `T` | Transversal |
| *(vacío)* | No aplica |

### Valores del campo Caracter_legal

| Valor | Significado |
|---|---|
| `obligatorio` | Exigible por ley colombiana |
| `voluntario` | Buena práctica sin sanción |
| `condicional` | Solo el nivel mínimo es obligatorio |

### Subsistemas constructivos

| Valor en la matriz | Función |
|---|---|
| `Cimentación` | Transmite cargas al suelo; aísla de humedad |
| `Estructura` | Soporta cargas verticales y laterales |
| `Envolvente` | Cierra el volumen interior (muros, ventanas, puertas) |
| `Cubierta` | Protege de lluvia y radiación |
| `Instalaciones` | Hidráulica, sanitaria, eléctrica, gas, paneles solares |
| `Acabados y complementos` | No estructurales: pintura, pisos, aislantes |
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
| 0.2 | 2026-04-29 | Columnas actualizadas: `Enfoque_genero` + `Inclusion_social` reemplazadas por `Notas` (texto libre general) + `Ref_Ley2462` (códigos filtrable). Subsistemas con nombre completo (no códigos S1–S6). Ejes con nombre completo (no P/C/T). Consultas frecuentes actualizadas. |
