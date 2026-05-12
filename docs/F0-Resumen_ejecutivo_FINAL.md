# Resumen Ejecutivo · Producto 1 — Levantamiento de información

**Guía técnica de sostenibilidad para vivienda rural en los 4 climas de Colombia**
**Marco normativo:** Anexo 1 Resolución 0194/2025 (MVCT) + Resolución 0534/2025 (Ciclo de vida) + Ley 2462/2025 (Igualdad mujeres rurales) + 15 criterios CEELA
**Producto:** P1 — Levantamiento de información (insumo verificable y trazable para el Producto 2)
**Periodo de ejecución:** 2026-04 a 2026-05
**Fecha de cierre:** 2026-05-12
**Cobertura geográfica:** Nacional Colombia · 4 climas TdR (frío · templado · cálido húmedo · cálido seco)

---

## 1. Objetivo

Levantar, sistematizar y consolidar la información normativa, técnica y de casos de éxito existente en Colombia sobre vivienda rural sostenible en los cuatro climas del territorio nacional, con criterios estrictos de inclusión, trazabilidad y verificabilidad pública, como insumo de soporte para la elaboración del Producto 2 (la guía técnica que desarrollarán los arquitectos consultores en la siguiente fase de la consultoría).

---

## 2. Metodología

El levantamiento se ejecutó en dos vías complementarias y paralelas. La **Matriz de Estándares M1** se construyó priorizando marcos normativos vigentes de obligatorio cumplimiento (Resoluciones 0194/2025 y 0534/2025 del MVCT, Ley 2462/2025 sobre mujeres rurales), reglamentos técnicos sectoriales (NSR-10 Título E, RAS, RETILAP, UPME-PGEE) y referentes voluntarios internacionales como los 15 criterios CEELA. Esta primera ronda se amplió posteriormente con guías técnicas específicas de bahareque (Carazas Aedo/Misereor 2002, Manual AIS-FOREC, Ficha SURA) y con un modelo de gestión regional (VRA Bogotá-Región 2024), incorporando además el seguimiento de iniciativas legislativas en discusión (Proyecto de Ley de Bioconstrucción de la senadora Zuleta López, radicado abril 2025) como referencia normativa futura.

La **Matriz de Casos de Éxito M2** aplicó un protocolo de búsqueda secuencial con criterios estrictos: vivienda rural construida en Colombia, con al menos un eje de sostenibilidad (E1 bioclimática, E2 energía, E3 agua, E4 materiales) documentado técnicamente, autoría y ubicación verificables, y trazabilidad pública vía URL o PDF. La cosecha se organizó en seis rondas: (1) corpus inicial de 10 fuentes documentales colombianas; (2) premios nacionales (Bienal Colombiana SCA, Corona Pro Hábitat, Lápiz de Acero, BAQ Panamericano, CCCS CASA Colombia); (3) programas estatales (Fondo Adaptación, Casa Para Mí de Argos, Programa Vivienda Caldas); (4) innovación material emergente (plástico reciclado, impresión 3D de concreto); (5) memorias de arquitecto consultadas (Santiago Moreno G., 3 casos pioneros 1986-1996 y propuesta UNGRD Providencia 2024); y (6) verificación cruzada entre fuentes para corregir clasificaciones de estado (Construido vs Solo diseño). Se priorizó la calidad documental sobre la cantidad. El texto libre de las 280 celdas afectadas se validó posteriormente con corrección ortográfica profesional (LanguageTool 6.9 + diccionario español, ~900 correcciones acumuladas entre M1 y M2).

---

## 3. Productos entregados

| # | Producto | Formato | Cifra clave |
|---|---|---|---:|
| 1 | Matriz de Estándares de Sostenibilidad (M1) | CSV + app Streamlit | **218 filas · 30 referencias** |
| 2 | Matriz de Casos de Éxito (M2) | CSV + app Streamlit | **62 casos · 36 fuentes** |
| 3 | Aplicación web de consulta interactiva | Python/Streamlit | Local + VPS público |
| 4 | Diccionarios, tutoriales y nomenclatura | Markdown / HTML | 5 documentos F0 |
| 5 | Estrategias y hallazgos por matriz | Markdown / HTML | F8 (M2) + F9 (M1) |
| 6 | Biblioteca BibTeX para Zotero | `.bib` | 66 entradas (30 M1 + 36 M2) |
| 7 | Síntesis de vacíos para el Producto 2 | Markdown | F5 §3.3 + F8 §5 |
| 8 | Repositorio GitHub con historial completo | Git | 50+ commits |

---

## 4. Resultados clave

### 4.1 Matriz M1 — Estándares de Sostenibilidad

La matriz consolidó **218 filas** de criterios, medidas, lineamientos, fines y enfoques agrupados en **30 referencias documentales únicas**. El **80.7% del corpus tiene carácter de cumplimiento obligatorio** y el **100% es aplicable a vivienda rural** (89% directamente y 11% condicional según tipología o región). Las cuatro guías técnicas de bahareque (Misereor + NSR-10 Título E + AIS-FOREC + SURA) aportaron 32 filas que llenaron un vacío detectado en el corpus inicial: la normativa colombiana cubre solo el bahareque encementado vía NSR-10, pero no existía documentación operativa para el bahareque tradicional vigente en el medio rural. Se documentó explícitamente la **tensión normativa** entre ambos sistemas (pie-derechos 1.5–2 m en tradicional vs 0.30–0.60 m en encementado) como sistemas distintos con marcos legales separados, y no como una contradicción a resolver.

La cobertura por eje muestra al **E4 Materiales** como el mejor representado (111 filas con marca), seguido por **E1 Bioclimática** (92), **E2 Energía** (83) y **E3 Agua** (79). Sin embargo, solo el 12% de los criterios están climáticamente acotados —el 88% es aplicable a todos los climas o a múltiples climas simultáneamente—, lo que refleja que la normativa colombiana está estructurada para aplicabilidad nacional con adaptaciones contextuales más que para criterios climáticamente diferenciados. Todos los marcos normativos clave identificados a priori quedaron cubiertos al cierre, sin vacíos críticos pendientes en M1.

### 4.2 Matriz M2 — Casos de Éxito

La matriz consolidó **62 casos** (51 construidos y 11 declarados como Solo diseño) respaldados por **36 fuentes documentales únicas**. La distribución por clima TdR sobrecumplió las cuotas mínimas en los cuatro climas: **frío 9, templado 20, cálido húmedo 25 y cálido seco 8**. Entre los casos hito se incluyen Casa Franco (tapia pisada premio Bienal SCA 2024, Ginebra Valle del Cauca), Casa Milguaduas (guadua Premio Panamericano BAQ 2022, Pereira Risaralda), Miiroku (hábitat Wayuu con certificación CCCS CASA Colombia 2025, Uribia La Guajira), las primeras viviendas 3D de Suramérica en La Unión Antioquia (Argos + Comfama + UNAL, 2025), el Albergue Guapi con ladrillos de plástico reciclado de Conceptos Plásticos (42 familias desplazadas, Cauca 2015), y los referentes pioneros del arquitecto Santiago Moreno G. (Amazonas 1996, Tolima 1987-89, Guaviare 1986). Cubre 12+ sistemas constructivos diferentes (tapia, adobe, bahareque tradicional y encementado, palafito-madera, madera-aserrada, mampostería confinada y estructural, sistemas mixtos, impresión 3D de concreto, ladrillo de plástico reciclado).

### 4.3 Vacíos declarados al cierre

| ID | Vacío | Estado al cierre |
|---|---|---|
| V-M2-01 | Tapia pisada nueva en frío Andino (Boyacá / Cundinamarca / Nariño) premiada | **Parcial** — cubierto con CAS-049 (adobe restauración Valle de Tenza), CAS-055 (guadua Cundinamarca con 4 ejes integrados) y CAS-039 (bahareque-guadua Cauca) |
| V-M2-02 | Cálido seco con sistemas NO-bahareque (Magdalena alto, Tolima seco) | **Parcial** — CAS-054 (panel caña-cal-boñiga Sucre) + CAS-060 (mampostería Tolima) |
| V-M2-03 | Eje cafetero × guadua premiada residencial | ✅ **RESUELTO** — CAS-056 Casa Milguaduas Pereira (BAQ 2022) |
| V-M2-04 | Pacífico × palafítica nueva premiada SCA | **Cubierto sin premio SCA** — CAS-044 Riosucio Chocó (Fondo Adaptación 2018, 157 viviendas) + CAS-057 Guapi Cauca (Conceptos Plásticos 2015, 42 albergues) |

---

## 5. Recomendaciones para el Producto 2

1. **Apoyarse en el 80.7% obligatorio** de M1 como base normativa firme; complementar con criterios voluntarios (CEELA, Economía Circular) donde el contexto técnico lo requiera, marcando explícitamente el carácter de cada criterio.

2. **Distinguir bahareque tradicional (BHQ-) de bahareque encementado (BHQ-E-)** según la exigencia normativa del proyecto: el primero útil en mejoramiento patrimonial y vernáculo, el segundo obligatorio para vivienda nueva certificable bajo NSR-10.

3. **Usar las 6 tipologías arquitectónicas parametrizadas** (Alargada VRSA1, L VRSL1, T VRST1, Compacta VRSC1/VRSC2, U VRSU1) como punto de partida según contexto del lote, clima y dimensiones, en línea con el Anexo C del Subsidio Familiar de Vivienda Rural (SFVR).

4. **Documentar las restricciones culturales como condicionantes de diseño explícitos**: los tres casos Wayuu del corpus M2 (Miiroku, Walirumana, CasaSolea) coinciden en no usar concreto ni adobe, construir solo en madera y elevar la vivienda sobre palafitos (suelo sagrado). Estos lineamientos deben formar parte del marco de adecuación cultural exigido por la Sentencia T-333/22.

5. **Monitorear el Proyecto de Ley de Bioconstrucción** (Sen. Zuleta López, radicado 7 abril 2025) en su trámite legislativo. Si se aprueba durante la ejecución del Producto 2, deberá incorporarse como marco normativo activo. Mientras tanto, sus tres pilares (bioconstrucción, construcción sostenible, arquitectura tradicional) pueden usarse como guía conceptual.

---

## 6. Limitaciones reconocidas

Un vacío estructural del corpus arquitectónico colombiano publicado persiste al cierre: **no existe documentación pública verificable de vivienda nueva construida en tapia pisada en clima frío andino con autor, año y ubicación específicos**. Solo se localizaron tradición vernácula patrimonial sin autor (Ráquira, Tibasosa, Yacuanquer), propuestas no construidas (FP Arquitectura/Sumapaz 2019) y casos en Santander en clima templado (Tierra Viva). Casa Franco (Valle del Cauca, clima templado) es el único referente nacional reciente de tapia pisada construida y premiada. Esta carencia se documenta como **hallazgo metodológico** y se sugiere convertir en lineamiento prioritario para el Producto 2.

Adicionalmente, 11 casos quedaron en estado *Solo diseño* (sin construcción confirmada al cierre); la búsqueda de premios SCA no abarcó el 100% de las ediciones históricas; la presunta categoría *Premios CAF de Construcción Sostenible Colombia* no existe como tal —corresponde a una confusión con el Premio Líderes que Transforman del CCCS o con Corona Pro Hábitat—; las imágenes y fotografías de los casos M2 no se integraron en esta fase (UIP-002 diferida); y 10 artículos académicos colombianos pre-clasificados en la búsqueda OpenAlex (`CO-resultados/clasificados_2026-04-23.csv`) quedaron pendientes de integración a M1 (UIP-003 en estado de análisis).

---

## 7. Acceso a los productos

| Recurso | Ubicación |
|---|---|
| **Repositorio GitHub** | https://github.com/anamamoreno/Arquitectura-rural |
| **Aplicación web (M1)** | https://app.uxtic.co/artefactos/viviendarural/m1 |
| **Aplicación web (M2)** | https://app.uxtic.co/artefactos/viviendarural/m2 |
| **Descarga de CSVs** | Botón *Exportar* dentro de la app (UTF-8 con BOM, abre en Excel) |
| **Documentación completa** | Directorio `docs/` del repositorio |
| **Biblioteca para Zotero** | `docs/F0-Referencias_Zotero.bib` (66 entradas) |

---

## 8. Documentos de soporte referenciados

| Código | Documento | Función |
|---|---|---|
| F0-Lista_referencias_y_aportes.md | Inventario M1 | 30 referencias narradas con aporte cualitativo |
| F0-Lista_fuentes_casos.md | Inventario M2 | 36 fuentes narradas con casos asociados |
| F0-Tutorial_Matriz_estandares.md | Tutorial M1 | Uso de la app para los 20 campos M1 |
| F1-Protocolo_busqueda.md | Plan original M1 | Marco metodológico inicial (referencia) |
| F5-Sintesis_y_cierre.md | Síntesis | Vacíos declarados §3 (M1 a priori + M2 ejecutados) |
| F6-Plan_busqueda_casos.md | Plan original M2 | Marco metodológico inicial (referencia) |
| **F8-Estrategia_y_hallazgos_M2.md** | **Búsqueda ejecutada M2** | Cronología real + tablas por clima |
| **F9-Estrategia_y_hallazgos_M1.md** | **Búsqueda ejecutada M1** | Cronología real + cobertura por eje |
| UIP-001-Despliegue_VPS.md | Operación | Comandos exactos de despliegue |
| UIP-002-Imagenes_M2.md | Diferida | Enriquecimiento gráfico de fichas M2 |
| UIP-003-Articulos_academicos_M1.md | Análisis | Propuesta de integración 6-7 artículos OpenAlex |

---

**Control de versiones del Resumen Ejecutivo**

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | 2026-05-12 | Documento inicial de cierre del Producto 1 |

---

*Producto 1 entregado por: responsable del levantamiento de información (Producto 1)*
*Documento de cierre · 2026-05-12*
