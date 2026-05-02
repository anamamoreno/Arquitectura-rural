# Revisión de normativa complementaria — hallazgos para la Matriz de Estándares

> **¿Qué es este documento?** Registro de la revisión de los documentos normativos presentes en `Referencias-estandares/`, indicando qué se encontró en cada uno, cuántas filas aportó a la Matriz de Estándares y qué vacíos o alertas se detectaron. Complementa al documento `F0-Matriz_estandares_sostenibilidad.csv` que pasó de 134 a 158 filas tras esta revisión.

**Versión:** 0.1 · **Fecha:** 2026-04-29.

---

## 1. Resumen cuantitativo

| Resultado | Cantidad |
|---|---|
| Documentos revisados | 22 |
| Documentos con filas nuevas aportadas | 14 |
| Documentos sin filas nuevas (ya capturados o no aplican) | 8 |
| **Total filas nuevas añadidas a la matriz** | **24** |
| Total filas en la matriz tras actualización | **158** |
| Alertas de archivos mal etiquetados | 2 |

---

## 2. Documentos ya procesados previamente (4 marcos principales)

Estos documentos ya estaban en la matriz antes de esta revisión. No se re-procesaron.

| Documento | Filas en matriz | Referencia del análisis |
|---|---|---|
| Res. 0194/2025 — Anexo 1 (Guía ahorro agua y energía) | 38 | `F0-3b-Medidas_Anexo1_Cap2.md` |
| Res. 0534/2025 — Guía Ciclo de Vida | 42 + 11 = 53 | `F0-3d-Criterios_Guia_Ciclo_Vida.md` |
| CEELA — 15 principios | 15 | `F0-3c-Cruce_Estandares_Ejes.md` |
| Ley 2462/2025 — Mujeres rurales | 28 | `F0-3e-Ley2462_genero_inclusion.md` |
| CONPES 3919/2018 | 0 (referenciado como política marco) | `F0-3d-Criterios_Guia_Ciclo_Vida.md` §5 |
| ENUT 2024–2025 | 0 (datos de soporte para género) | `F0-3e-Ley2462_genero_inclusion.md` §7 |

---

## 3. Documentos revisados con filas nuevas aportadas

### 3.1 Guía SUDS (MVCT/DNP, junio 2022)
**Archivo:** `Sistema Urbanos de Drenaje Sostenible_v.0.0.pdf` (2.3 MB, 2.870 líneas extraídas).

**Qué es:** Guía metodológica para formulación e implementación de Sistemas Urbanos de Drenaje Sostenible. Elaborada por MVCT y DNP.

**Hallazgos:**
- Define **14 tipologías de SUDS** clasificadas por objetivo (cantidad, calidad, reúso, recreación, biodiversidad), por mecanismo (detención, infiltración) y por escala (vivienda, barrio, ciudad).
- Incluye tipologías directamente aplicables a **escala de vivienda rural**: captación pluvial, cisternas, jardín de lluvia, pozo de infiltración, techos verdes, pavimentos permeables.
- Contiene análisis de costo-beneficio y fuentes de financiación.
- Referencia el RAS (Res. 0330/2017) como marco regulatorio.

**Filas aportadas:** 6

| ID | Criterio | Eje |
|---|---|---|
| SUDS-1 | Captación agua lluvia escala vivienda | E3 |
| SUDS-2 | Jardín de lluvia / jardín microcuenca | E3 |
| SUDS-3 | Pozo de infiltración | E3 |
| SUDS-4 | Cisterna / aljibe de almacenamiento pluvial | E3 |
| SUDS-5 | Techos verdes como SUDS | E1 + E3 |
| SUDS-6 | Pavimentos permeables | E3 |

**Conexión con género:** SUDS-1 y SUDS-4 tienen impacto directo en reducción de acarreo de agua por mujeres rurales (Ley 2462 Fin 3).

---

### 3.2 Estrategia Nacional de Economía Circular (MADS, 2019)
**Archivo:** `Estrategia Nacional de Economía Circular-2019 Final.pdf` (12 MB, 3.454 líneas extraídas).

**Qué es:** Estrategia que introduce elementos de economía circular al modelo de desarrollo colombiano. Incluye sector construcción como prioritario.

**Hallazgos:**
- El sector construcción consume **91,5 millones de toneladas** de materiales al año; genera **7,4 millones de toneladas de escombros** y 22 millones de toneladas de RCD por demoliciones.
- Solo **2 % de los escombros** se aprovecha actualmente.
- Identifica 6 oportunidades para circularidad en construcción: (i) cierre de ciclos, (ii) aprovechamiento escombros, (iii) simbiosis industrial, (iv) eco-diseño, (v) modelos regionales de gestión RCD, (vi) certificaciones (LEED, BREEAM, EDGE, CASA Colombia, Sello Ambiental).
- Metas a 2030 de productividad de materiales y reducción de residuos.

**Filas aportadas:** 4

| ID | Criterio | Eje |
|---|---|---|
| EC-1 | Eco-diseño en productos y estructuras | E4 |
| EC-2 | Aprovechamiento de RCD en obra nueva | E4 |
| EC-3 | Simbiosis industrial en materiales | E4 |
| EC-4 | Certificaciones de construcción sostenible | Transversal |

---

### 3.3 Res. 0330/2017 — RAS (Reglamento Técnico de Agua Potable y Saneamiento Básico)
**Archivo:** `Resolucion 0330-2017.pdf` (70 MB — archivo grande, extracción parcial).

**Qué es:** Reglamento técnico para diseño, construcción, operación y mantenimiento de infraestructura de acueducto y alcantarillado. Incluye zona rural.

**Hallazgos:**
- Define requisitos técnicos para **sistemas de agua potable rural** (dotación l/hab/día, presión mínima).
- Define requisitos para **tratamiento de aguas residuales rurales** (DBO5, SST, porcentajes de remoción).
- Incluye **manejo de aguas lluvias y SUDS** como componente del sistema.
- Es la referencia obligatoria que la Guía Ciclo de Vida (Res. 0534) cita en su criterio A-SE-1.

**Filas aportadas:** 3

| ID | Criterio | Eje |
|---|---|---|
| RAS-1 | Sistemas de acueducto rural | E3 |
| RAS-2 | Sistemas de alcantarillado y saneamiento rural | E3 |
| RAS-3 | Sistemas de manejo de aguas lluvias | E3 |

**Nota:** por el tamaño del archivo (70 MB), se hizo extracción de criterios generales. Una revisión detallada del capítulo de sistemas rurales podría aportar 3–5 filas adicionales.

---

### 3.4 Ley 1715 de 2014 — Fuentes No Convencionales de Energía
**Archivo:** `Ley_1715_de_2014.pdf` (131 KB).

**Qué es:** Ley que introduce incentivos tributarios para inversión en energías renovables no convencionales (solar FV, solar térmica, eólica, biomasa).

**Hallazgos:**
- Exclusión de IVA en equipos de energía renovable.
- Deducción de renta por inversión.
- Aplica directamente a paneles solares FV y calentadores solares en vivienda rural.

**Filas aportadas:** 1

| ID | Criterio | Eje |
|---|---|---|
| L1715-1 | Incentivos tributarios para FNCE en vivienda | E2 (económico) |

---

### 3.5 Ley 1819 de 2016 — Reforma Tributaria
**Archivo:** `Ley_1819_de_2016.pdf` (579 KB).

**Qué es:** Reforma tributaria que amplía beneficios de la Ley 1715. Incluye exclusión de IVA en tecnologías ambientales y no causación de impuesto de carbono para quienes certifiquen ser carbono neutro.

**Filas aportadas:** 1

| ID | Criterio | Eje |
|---|---|---|
| L1819-1 | Beneficios tributarios FNCE y carbono neutro | E2 (económico) |

---

### 3.6 Ley 373 de 1997 — Uso Eficiente y Ahorro del Agua
**Archivo:** `Ley_373_de_1997.pdf` (85 KB).

**Qué es:** Ley que establece el programa de uso eficiente y ahorro del agua. Obliga a entidades a implementar programas que incluyen captación pluvial y reúso.

**Filas aportadas:** 1

| ID | Criterio | Eje |
|---|---|---|
| L373-1 | Programa uso eficiente y ahorro del agua | E3 |

**Conexión con género:** reduce necesidad de acarreo de agua en zonas rurales sin acueducto.

---

### 3.7 Ley 1931 de 2018 — Gestión del Cambio Climático
**Archivo:** `Ley_1931_de_2018.pdf` (116 KB).

**Qué es:** Directrices para gestión del cambio climático en acciones de adaptación y mitigación, incluyendo sector vivienda.

**Filas aportadas:** 1

| ID | Criterio | Eje |
|---|---|---|
| L1931-1 | Medidas de mitigación y adaptación en vivienda | Transversal |

---

### 3.8 Decreto 1285 de 2015 — Lineamientos Construcción Sostenible
**Archivo:** `Decreto_1285_de_2015.pdf` (77 KB).

**Qué es:** Decreto que establece los lineamientos de construcción sostenible y dio origen a la Resolución 0549/2015 (predecesora de la Res. 0194/2025).

**Filas aportadas:** 1

| ID | Criterio | Eje |
|---|---|---|
| D1285-1 | Porcentajes obligatorios de ahorro agua y energía | E2 + E3 |

---

### 3.9 Decreto 1467 de 2019 — Precio VIS
**Archivo:** `Decreto_1467_de_2019.pdf` (78 KB).

**Qué es:** Define precio máximo de VIS (135–150 SMLV). Referencia que VIS debe cumplir "estándares de calidad en diseño urbanístico, arquitectónico y de construcción sostenible" (Ley 1955/2019 Art. 85).

**Hallazgos:** no tiene criterios técnicos propios. El valor está en la **obligación legal** de que VIS cumpla con sostenibilidad.

**Filas aportadas:** 1 (referencia legal)

| ID | Criterio | Eje |
|---|---|---|
| D1467-1 | VIS debe cumplir estándares de construcción sostenible | Transversal |

---

### 3.10 Decreto 1727 de 2021 — Ecobertura
**Archivo:** `Decreto_1727_de_2021.pdf` (77 KB).

**Qué es:** Modifica subsidio FRECH No VIS para incluir cobertura adicional de 10 SMLV para viviendas que cumplan criterios de sostenibilidad definidos por MVCT.

**Filas aportadas:** 1 (incentivo económico)

| ID | Criterio | Eje |
|---|---|---|
| D1727-1 | Subsidio adicional por sostenibilidad (Ecobertura) | Económico |

---

### 3.11 Res. 0472/2017 actualizada por Res. 1257/2021 — Gestión RCD
**Archivo:** `Resolucion 0472-de-2017.pdf` (13 MB).

**Qué es:** Reglamentación de la gestión integral de Residuos de Construcción y Demolición. Aplica a todos los generadores de RCD.

**Filas aportadas:** 1

| ID | Criterio | Eje |
|---|---|---|
| R0472-1 | Gestión integral de RCD | E4 |

---

### 3.12 Res. 0541 de 1994 — Manejo de Escombros
**Archivo:** `Resolucion 0541 - 1994.pdf` (31 KB, 249 líneas).

**Qué es:** Regula cargue, descargue, transporte, almacenamiento y disposición de escombros y materiales de construcción.

**Filas aportadas:** 1

| ID | Criterio | Eje |
|---|---|---|
| R0541-1 | Manejo de escombros y materiales de construcción | E4 (complementario) |

---

### 3.13 Decreto 948 de 1995 — Contaminación Atmosférica
**Archivo:** `Decreto 948 de 1995 Nivel Nacional.pdf` (681 KB).

**Qué es:** Prevención y control de contaminación atmosférica. Regula mallas protectoras en construcción de edificios y control de material particulado.

**Filas aportadas:** 1

| ID | Criterio | Eje |
|---|---|---|
| D948-1 | Control contaminación atmosférica en obra | E4 (complementario) |

---

### 3.14 Decreto 1443 de 2014 — SG-SST
**Archivo:** `Decreto_1443_de_2014.pdf` (129 KB).

**Qué es:** Implementación del Sistema de Gestión de Seguridad y Salud en el Trabajo. Uso de buenas prácticas y materiales de calidad para prevenir accidentes en construcción.

**Filas aportadas:** 1

| ID | Criterio | Eje |
|---|---|---|
| D1443-1 | Sistema de Gestión de Seguridad y Salud en el Trabajo | Social |

---

## 4. Documentos revisados SIN filas nuevas

### 4.1 CONPES 3934 de 2018 — Crecimiento Verde
**Archivo:** `Conpes-3934.pdf` (963 KB).

**Razón:** política marco de productividad y competitividad a 2030. No tiene criterios técnicos de construcción — define metas macroeconómicas. Ya referenciado en la Guía Ciclo de Vida.

---

### 4.2 Res. 0549/2015 — Guía ahorro agua y energía (predecesora)
**Archivo:** `Resolución 549 de 2015 con Anexos.pdf` (9 MB).

**Razón:** reemplazada íntegramente por la Res. 0194/2025. Las 38 medidas de la Res. 0194 ya las cubren. Valor histórico — no aporta filas nuevas.

---

### 4.3 Ley 1955 de 2019 — Plan Nacional de Desarrollo 2018–2022
**Archivo:** `Ley_1955_de_2019.pdf` (577 KB).

**Razón:** define objetivos y estrategias de vivienda social sostenible, pero los criterios técnicos están en los decretos y resoluciones que la reglamentan (ya capturados).

---

### 4.4 NDC 2020 — Contribución Determinada a Nivel Nacional
**Archivo:** `informe-actualizacion-contribucion-determinada-Colombia-ndc-2020.pdf` (5.5 MB).

**Razón:** meta de reducción 176 Mt CO₂eq a 2030 para todos los sectores. No tiene criterios específicos de construcción — es contexto para la Ley 1931/2018 y la Estrategia 2050.

---

### 4.5 Estrategia 2050
**Archivo:** `Estrategia-Climatica-de-Largo-Plazo-de-Colombia-E2050.pdf` (7.4 MB).

**Razón:** ruta de carbono neutralidad a largo plazo. Menciona "acelerador de edificaciones neto cero carbono" pero sin criterios técnicos verificables. Contexto para el eje E2.

---

### 4.6 Otros documentos estratégicos/analíticos

| Archivo | Razón de no aportar filas |
|---|---|
| `Modelacion_Adaptacion_Riesgo_Colombia.pdf` (27 MB) | Documento analítico de riesgo climático — no normativo |
| `Plan_trabajo_Metodologia_Ingeniar.pdf` (6.3 MB) | Metodología de consultoría — no normativo |
| `Resolucion 196 de 2020.pdf` (1.1 MB) | Procedimiento para acceder a incentivos tributarios UPME — complementa L1715-1 sin criterios nuevos |
| `Resolucion 41286_2016.pdf` (53 KB) | Plan PROURE 2017–2022 — metas sectoriales de eficiencia energética sin criterios de diseño |
| `Resolucion 260 de 2011.pdf` (118 KB) | Tarifas de evaluación ambiental — procedimiento administrativo |
| `Resolucion 0831 - 2020.pdf` (214 KB) | Sistema MRV de mitigación — monitoreo de emisiones, ya capturado en CEELA C15 |

---

## 5. Alertas detectadas

### 5.1 Archivo mal etiquetado: Res. 40031/2025
**Archivo:** `Resolución 40031 de 2025 Ministerio de Minas y Energía.pdf`
**Contenido real:** Plan de Abastecimiento de Gas Natural 2023–2032.
**Lo que debería ser:** RETILAP (Reglamento Técnico de Iluminación y Alumbrado Público) — Res. 40150/2024.
**Impacto:** el RETILAP real no está en la carpeta. Si se consigue, aportaría 2–3 filas sobre iluminación natural y artificial (complementaría MA-01, MA-02, S-CL-1).

### 5.2 Archivo de otro país: RITE 2017
**Archivo:** `RITE-REGLAMENTO-DE-INSTALACIONES-TERMICAS-EN-LOS-EDIFICIOS.pdf`
**Contenido real:** Real Decreto 1751/1998 de España — reglamento español de instalaciones térmicas.
**Lo que debería ser:** RITE colombiano (si existe como reglamento independiente).
**Impacto:** no aplica como normativa colombiana. Puede servir como referencia técnica internacional.

### 5.3 Documento pendiente de revisión detallada: RAS
**Archivo:** `Resolucion 0330-2017.pdf` (70 MB)
**Estado:** se extrajeron 3 criterios generales. El capítulo de sistemas rurales del RAS podría aportar 3–5 filas adicionales con requisitos específicos de dotación, tratamiento y calidad de agua para vivienda rural dispersa.

### 5.4 Documento nuevo no revisado
**Archivo:** `anexo1.-guia-criterios-de-sostenibilidad-ago-23.pdf` (1.8 MB)
**Observación:** podría ser una versión anterior (agosto 2023) de la Guía Ciclo de Vida. Pendiente de verificar si contiene criterios adicionales o es borrador de lo ya capturado.

---

## 6. Distribución final de la Matriz de Estándares (158 filas)

| Marco / Fuente | Filas | % | Carácter |
|---|---|---|---|
| Res. 0534/2025 (Guía Ciclo de Vida) | 53 | 34 % | Obligatorio |
| Res. 0194/2025 (Anexo 1) | 38 | 24 % | Obligatorio |
| Ley 2462/2025 (género/inclusión) | 28 | 18 % | Obligatorio |
| CEELA | 15 | 9 % | Voluntario |
| SUDS (MVCT/DNP 2022) | 6 | 4 % | Obligatorio |
| Economía Circular (MADS 2019) | 4 | 3 % | Voluntario |
| RAS (Res. 0330/2017) | 3 | 2 % | Obligatorio |
| Leyes complementarias (1715, 1819, 373, 1931) | 4 | 3 % | Obligatorio |
| Decretos complementarios (1285, 1467, 1727) | 3 | 2 % | Obligatorio/Voluntario |
| Resoluciones complementarias (0472, 0541) | 2 | 1 % | Obligatorio |
| Decretos procedimentales (948, 1443) | 2 | 1 % | Obligatorio |
| **Total** | **158** | **100 %** | |

### Distribución por eje (filas con P = Principal)

| Eje | Filas con P | % de cobertura |
|---|---|---|
| E1 Bioclimática pasiva | ~25 | Bien cubierto |
| E2 Eficiencia energética activa | ~22 | Bien cubierto |
| E3 Eficiencia hídrica | ~28 | **Fortalecido** con SUDS + RAS |
| E4 Materiales sostenibles | ~30 | **Fortalecido** con Economía Circular + RCD |
| Transversal / Económico | ~20 | Cubierto con leyes e incentivos |
| Género / Inclusión | ~28 | Cubierto con Ley 2462 + ENUT |

### Distribución por carácter legal

| Carácter | Filas | % |
|---|---|---|
| Obligatorio | ~125 | 79 % |
| Voluntario | ~23 | 15 % |
| Condicional | ~10 | 6 % |

---

## 7. Recomendaciones para completar

| Acción | Prioridad | Impacto esperado |
|---|---|---|
| Conseguir el **RETILAP real** (Res. 40150/2024) | Alta | 2–3 filas de iluminación natural/artificial |
| Revisar capítulo rural del **RAS** en detalle | Media | 3–5 filas de requisitos agua rural |
| Verificar `anexo1.-guia-criterios-sostenibilidad-ago-23.pdf` | Baja | Posible versión anterior — probablemente 0 filas nuevas |
| Buscar **RITE colombiano** (si existe como reglamento independiente) | Baja | 2–3 filas de instalaciones térmicas |
| Revisar **Res. 0019/2022** (reglamenta criterios sostenibilidad para subsidio Ecobertura) | Media | 3–5 filas de criterios verificables |

---

## 8. Documentos relacionados

- `F0-Matriz_estandares_sostenibilidad.csv` — matriz actualizada con 158 filas.
- `F0-Tutorial_Matriz_estandares.md` — tutorial de uso de la matriz.
- `F0-3b-Medidas_Anexo1_Cap2.md` — detalle de las 38 medidas Res. 0194.
- `F0-3d-Criterios_Guia_Ciclo_Vida.md` — detalle de los 42 criterios Res. 0534.
- `F0-3c-Cruce_Estandares_Ejes.md` — cruce de los 3 marcos técnicos × 4 ejes.
- `F0-3e-Ley2462_genero_inclusion.md` — Ley 2462 y ENUT 2024–2025.
- `scripts/04_agregar_normativa.py` — script que ejecutó la adición de las 24 filas.

---

---

## 9. Fase 2 — Contextualización (ejecutada 2026-04-29)

Se revisaron 6 documentos de prioridad media para enriquecer celdas existentes con metas cuantitativas, incentivos y contexto estratégico. **No se añadieron filas nuevas; se enriquecieron 29 celdas en 20 filas.**

### Datos incorporados

| Documento | Dato extraído | Filas enriquecidas |
|---|---|---|
| **CONPES 3934** (Crecimiento Verde) | Tasa reciclaje materiales construcción CO = 2% (meta potencial 50%); intensidad materiales 2.28 kg/USD PIB (2.8× OCDE); 91.5M ton materiales/año; 7.4M ton escombros | EC-1, EC-2, A-R-1 |
| **Res. 41286/2016 PROURE** | Meta ahorro sector residencial 2017–2022: 56.121 TJ (0.73% total nacional) | D1285-1, MA-02 |
| **NDC 2020** | Compromiso reducción 176 Mt CO₂eq a 2030; sector vivienda incluido | A-EM-5, L1931-1 |
| **Estrategia 2050** | 100% edificaciones nuevas Net Zero a 2030; existentes Net Zero a 2050 (WorldGBC); 75% RCD aprovechables en peso materiales | A-EM-8, A-R-4 |
| **Ley 1955/2019 PND** | Art. 85: VIS cumple estándares calidad en diseño urbanístico; arquitectónico y construcción sostenible | D1467-1 |
| **Res. 196/2020 UPME** | Requisitos y procedimiento para acceder a beneficios tributarios eficiencia energética; requiere certificación UPME | L1715-1, L1819-1 |

---

## 10. Fase 3 — Verificación cruzada (ejecutada 2026-04-29)

Se verificaron 5 documentos de prioridad baja para confirmar que las referencias legales en la columna `Correspondencia_cruzada` son correctas y completas. **Se añadieron 8 referencias cruzadas a filas existentes.**

### Verificaciones realizadas

| Documento | Verificación | Filas actualizadas |
|---|---|---|
| **Decreto 3930/2010** (vertimientos) | Confirmado que MW-06, MW-07 y A-A-5 deben referenciar este decreto como norma de control de vertimientos | MW-06, MW-07, A-A-5 |
| **Res. 0831/2020** (MRV emisiones) | Confirmado que A-EM-1 referencia correctamente el sistema MRV para validar metodologías de línea base | A-EM-1 |
| **Ley 1333/2009** (sanciones ambientales) | Añadida como referencia de procedimiento sancionatorio en caso de incumplimiento de gestión RCD y contaminación atmosférica | R0472-1, D948-1 |
| **CONPES 3934** | Verificada correspondencia con criterios de materiales y compras sostenibles | A-M-1, A-M-2 |
| **Modelación Adaptación Riesgo** | No aporta verificaciones adicionales — documento analítico sin criterios normativos | Ninguna |

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | 2026-04-29 | Revisión inicial: 22 documentos; 24 filas nuevas; 2 alertas de archivo; 5 recomendaciones |
| 0.2 | 2026-04-29 | Fase 2 + Fase 3 ejecutadas: 29 celdas enriquecidas en 20 filas + 8 referencias cruzadas verificadas. Corrección de alineación de columnas en 8 filas. |
| 0.3 | 2026-04-29 | Revisión carpeta NUEVAS: 11 documentos; 20 filas nuevas de 7 fuentes; matriz pasa de 158 a 178 filas. Incluye TdR oficial CEELA 2026, PNVISR, Guía Mejoramientos, Parametrización SFVR, Estado CS 2024, Sentencia T-333/22. |

---

## 11. Documentos de la carpeta NUEVAS (revisados 2026-04-29)

### 11.1 Inventario: 11 archivos

| # | Documento | Tamaño | Resultado |
|---|---|---|---|
| 1 | **TdR Guía Sostenibilidad Rural CEELA 2026** | 546 KB | ✅ 2 filas — TdR oficial del contrato |
| 2 | **PNVISR — Plan Nacional Vivienda Social Rural** | 2.4 MB | ✅ 4 filas — enfoque diferencial; vivienda integral; agua rural; subsidio |
| 3 | **Guía Sostenibilidad Mejoramientos MVCT** | 2.7 MB | ✅ 8 filas — estufas eficientes; biogás; eólica; durabilidad; mano obra local; compromiso social; gestión comunitaria; proveeduría local |
| 4 | **Anexo C — Parametrización SFVR** | 5.6 MB | ✅ 4 filas — asoleación; protección solar; iluminación natural; ventilación rural |
| 5 | **Estado Construcción Sostenible 2024 (CCCS)** | 14 MB | ✅ 1 fila — estado certificaciones CO |
| 6 | **Sentencia T-333/22** | 2.6 MB | ✅ 1 fila — derecho vivienda digna como fundamental |
| 7 | Guía Materiales Construcción Sostenible (MADS) | 47 MB | ⏭ Ya procesada — duplicado de `Referencias-proyecto/` |
| 8 | Lineamientos VIS Nueva Rural | 7.1 MB | ⏭ Ya procesada — duplicado de `Referencias-proyecto/` |
| 9 | Guía Ciclo de Vida (anexo Res. 0534) | 15 MB | ⏭ Ya procesada — duplicado |
| 10 | Estado CS 2024 (duplicado) | 14 MB | ⏭ Copia del #3 |
| 11 | Ley 1844/2017 (Acuerdo de París) | 15 MB | ⏭ Contexto — ya referenciado vía NDC 2020 |

### 11.2 Hallazgos por documento

#### TdR Guía Sostenibilidad Rural CEELA 2026

**Hallazgo clave:** este es el **TdR oficial del contrato**. Confirma:
- Proyecto CEELA financiado por COSUDE (Suiza), ejecutado por EBP/Carbon Trust/Efizity.
- La guía será de **obligatorio cumplimiento** por contratistas en estructuración y ejecución de proyectos VISR.
- Presupuesto: 8.000 CHF; duración 110 días calendario.
- Subdirección de Subsidio y Ejecución de Vivienda Rural (SSEVR) del MVCT como contraparte.
- Subsidio rural: hasta 70 SMLV + 20 SMLV transporte (Res. 0536/2020).
- Enfoque de género e inclusión social explícito.
- **15 criterios CEELA** como referencia obligatoria.

#### Guía Sostenibilidad Mejoramientos MVCT

**Hallazgo clave:** esta guía ya tiene una **estructura de 5 dimensiones** para vivienda rural:

| Dimensión | Estrategias rurales | Filas añadidas |
|---|---|---|
| Eficiencia en agua | A1 aparatos; A2 aguas lluvias; A3 aguas residuales | Ya cubiertas |
| Eficiencia energética | E1–E7 (eléctricas, estufas, iluminación, solar, ventilación, protección) | GM-E2 (estufas) |
| Materialidad sostenible | M2 durabilidad y garantías | GM-M2 |
| Energías alternativas | T1 solar FV; T2 solar térmica; T3 biogás; T4 eólica | GM-T3, GM-T4 |
| Sociocultural | S1 mano obra local; S2 compromiso social; S3 gestión comunitaria | GM-S1, GM-S2, GM-S3 |

**Aporte principal:** las estrategias **socioculturales** (S1–S3) y la **proveeduría local** (GM-A1) no estaban en la matriz.

#### PNVISR — Plan Nacional Vivienda Social Rural

**Hallazgos:**
- Define vivienda rural como **integral, saludable y productiva** — no solo habitacional.
- Enfoque diferencial obligatorio (género, étnico, discapacidad, víctimas, territorial).
- Acceso a agua y saneamiento como componente obligatorio.
- Subsidio rural con topes SMLV.
- Conecta directamente con Ley 2462/2025 en enfoque de género.

#### Anexo C — Parametrización SFVR

**Hallazgos:**
- Documento técnico del MVCT para parametrización del Subsidio Familiar de Vivienda Rural.
- Define estrategias pasivas específicas para vivienda rural: asoleación, orientación por clima, protección solar, iluminación natural, ventilación cruzada.
- Referencia Res. 0549/2015 (ahora 0194/2025) como base normativa.
- **Confirma que páramo y glacial están excluidos** de la zonificación (vacío declarado).
- Incluye referencias a Lorenzo Fonseca y Alberto Saldarriaga (autores vernáculos ya en nuestro tesauro).

#### Estado Construcción Sostenible 2024 (CCCS)

**Hallazgos:**
- 93% de constructores y 80% de operadores incorporan criterios ASG.
- Certificaciones más usadas: EDGE, CASA Colombia, LEED.
- Meta sectorial: edificaciones neto cero carbono con materiales de bajo impacto.
- 192 estrategias de sostenibilidad en materiales identificadas por el sector.

#### Sentencia T-333/22 (Corte Constitucional)

**Hallazgos:**
- Vivienda digna es **derecho fundamental** (no solo prestacional).
- Incluye: habitabilidad, disponibilidad de servicios, accesibilidad, **adecuación cultural**.
- La adecuación cultural obliga a respetar prácticas constructivas de comunidades étnicas.
- Conecta con Ley 2462 Enfoque 3 (derechos humanos mujeres rurales) y Res. 0534 S-AC-1 (accesibilidad).
