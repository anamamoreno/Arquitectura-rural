# UIP — Incorporación de artículos académicos colombianos a M1

**Estado:** 🟨 EN ANÁLISIS — pendiente de decisión de la responsable del Producto 1.
**Fecha:** 2026-05-12
**Autor:** Ana (con asistencia de Claude)
**Track:** A (Matriz de Estándares M1) — ampliación de fuentes

---

## 1. Objetivo

Incorporar a **M1** los criterios técnicos extraídos de **10 artículos académicos arbitrados colombianos** que fueron pre-clasificados en la búsqueda OpenAlex del 2026-04-23 (`CO-resultados/clasificados_2026-04-23.csv`) pero **no fueron revisados ni incorporados** durante la fase de cosecha inicial M1.

Estos artículos complementarían los marcos normativos vigentes con:
- **Evidencia empírica** colombiana (no solo norma)
- **Datos cuantitativos** medidos en condiciones locales (confort térmico VIS Bogotá, eficiencia estufas biomasa, propiedades mecánicas de tapia/adobe reforzado)
- **Innovaciones materiales** publicadas en revistas arbitradas con DOI

---

## 2. Alcance

**Incluye:**
- Revisar los **7 artículos técnicos prioritarios** (de los 10 colombianos pre-clasificados): los relacionados con E1 (confort térmico), E2 (estufas biomasa) y E4 (materiales tierra-fibra-adobe).
- Extraer **criterios/medidas/lineamientos cuantificables** de cada artículo (estimado 1–3 filas por artículo = 7–21 filas nuevas en M1).
- Asignar **nuevo prefijo `ACAD-`** para identificar el origen académico-arbitrado.
- Cargar los PDFs a `FUENTES/` (los 10 son Open Access).
- Actualizar `F0-Lista_referencias_y_aportes.md` (sección 1, sección de categorías y total general).
- Actualizar `F9-Estrategia_y_hallazgos_M1.md` (sección 2 — nueva ronda 2.5 documentada).
- Actualizar `F0-Referencias_Zotero.bib` con las 7 entradas nuevas (campo `@article` con DOI).

**Diferir o excluir:**
- Los **3 artículos restantes** de orientación general (agroecología, climate-smart village, BIC patrimonial) — son marco contextual, no aportan criterios verificables a M1.
- El archivo `resultados/clasificados_2026-04-23.csv` (574 internacionales) — se evalúa en UIP separado si esta primera ronda resulta valiosa.
- Re-evaluación de M2 a partir de estos artículos — algunos podrían referenciar casos construidos, pero no son la fuente principal.

---

## 3. Los 7 artículos candidatos

### E1 — Confort térmico vivienda colombiana

| # | Cita | DOI / URL | Hallazgo principal | Filas estimadas |
|---|---|---|---|---:|
| 1 | **Scoping Review of Thermal Comfort Research in Colombia** (2021) — *Buildings* (MDPI), 14 citas | doi.org/10.3390/buildings11060232 | Mapeo del estado del arte del confort térmico en CO; identifica rangos operativos por clima y métodos de evaluación | 2–3 |
| 2 | **Thermal Comfort and Satisfaction in the Context of Social Housing: Case Study in Bogotá, Colombia** (2019) — *Journal of Construction in Developing Countries*, 5 citas | doi.org/10.21315/jcdc2019.24.1.6 | Datos de campo de confort térmico medido en VIS Bogotá; recomendaciones para diseño bioclimático en clima frío andino | 1–2 |

### E2 — Estufas de biomasa eficientes

| # | Cita | DOI / URL | Hallazgo principal | Filas estimadas |
|---|---|---|---|---:|
| 3 | **Effect of the air flows ratio on energy behavior and NOx emissions from a top-lit updraft biomass cookstove** (2023) — *J. Braz. Soc. Mech. Sci. Eng.*, 6 citas | doi.org/10.1007/s40430-023-04473-7 | Parámetros operacionales de estufas de leña eficientes (TLUD); emisiones NOx vs eficiencia térmica; relevante para zonas rurales sin red eléctrica | 1–2 |

### E4 — Materiales tierra cruda (tapia, adobe, bambú)

| # | Cita | DOI / URL | Hallazgo principal | Filas estimadas |
|---|---|---|---|---:|
| 4 | **Experimental analysis of the cyclic behavior of rammed earth walls reinforced with arundo donax natural fiber** (2024) — *Heliyon*, 4 citas | doi.org/10.1016/j.heliyon.2024.e37084 | Ensayos cíclicos de tapia pisada reforzada con fibras vegetales (arundo donax); resistencia sísmica mejorada documentada | 2–3 |
| 5 | **Análisis de las propiedades físicas y mecánicas del adobe con asfalto reciclado** (2020) — *Inge CUC*, 2 citas | doi.org/10.17981/ingecuc.16.2.2020.06 | Innovación material: adobe estabilizado con asfalto reciclado; propiedades vs adobe tradicional | 1–2 |
| 6 | **Usage of bamboo powder as an additive in adobe bricks and bamboo canes frame for the reinforcement of adobe structures** (2019) — *Revista M*, 5 citas | doi.org/10.15332/rev.m.v15i0.2179 | Refuerzo de adobe con polvo de bambú y bastidor de caña; alternativa al bahareque encementado | 1–2 |

### Bonus (a discutir)

| # | Cita | DOI | Justificación |
|---|---|---|---|
| 7 | **The climate-smart village approach** (2018) — *Ecology and Society*, 247 citas | doi.org/10.5751/es-09844-230114 | Aunque enfoque general (no específico de vivienda), aporta marco metodológico para escalar adaptación rural — podría entrar como `lineamiento` con 1 fila |

**Total estimado nuevas filas M1:** 9–17 filas (sin contar #7); 10–18 si entra #7.

---

## 4. Estructura de las nuevas filas en M1

Cada fila seguirá el esquema actual de M1 con valores:

| Campo | Valor propuesto |
|---|---|
| `Referencia` | `ACAD-Buildings2021`, `ACAD-JCDC2019`, `ACAD-JBSME2023`, `ACAD-Heliyon2024`, `ACAD-IngeCUC2020`, `ACAD-RevistaM2019` (uno por artículo) |
| `URL_fuente` | DOI completo (https://doi.org/...) |
| `ID` | `ACAD-NN` correlativo (ej. `ACAD-01` a `ACAD-15`) |
| `Tema` | Tema corto del criterio extraído |
| `Descripcion` | Cita textual o paráfrasis fiel del hallazgo, con métrica si la hay |
| `Jerarquía` | `criterio` / `medida_pasiva` / `medida_activa` / `medida_estructural` según corresponda |
| `Etapa_ciclo_vida` | Mayormente `diseño` u `operación` |
| `E1`/`E2`/`E3`/`E4` | Principal/Complementario/Transversal según el eje que cubre |
| `Notas` | "Evidencia empírica colombiana arbitrada — N citas en Scopus/OpenAlex" |
| `Aplica_vivienda_rural` | `si` (todos pasan filtro) |
| `Clima` | Específico según el artículo (frío/templado para confort Bogotá, todos para materiales) |
| `Subsistema` | Según el caso (`Envolvente`, `Estructura`, `Instalaciones`) |
| `Caracter_legal` | `voluntario` (es evidencia empírica, no obligatoria) |
| `Nivel_cumplimiento` | `deseable` / `recomendada` |
| `Parametro_indicador` | Métrica cuantitativa específica si el artículo la documenta |
| `Correspondencia_cruzada` | Cruce con criterios existentes de M1 (ej. el Scoping Review puede cruzar con S-CT-1, MP-14, etc.) |

---

## 5. Decisiones a confirmar

| # | Decisión | Opciones | Recomendación |
|---|---|---|---|
| D1 | ¿Cuáles de los 7 artículos incluir? | A) Los 7 completos / B) Solo los 6 técnicos (no climate-smart village) / C) Solo top 3 (Scoping Review + Tapia con fibras + Bogotá VIS) | **B** — los 6 técnicos. El climate-smart village mejor en F1 marco como contexto |
| D2 | ¿Cargar PDFs a `FUENTES/`? | Sí (descarga automática vía DOI/URL) / No (solo referenciar URL) | **Sí** — todos son Open Access; tener PDF local para verificación |
| D3 | ¿Crear un prefijo `ACAD-` o usar `EVID-`? | `ACAD-` (académico) / `EVID-` (evidencia empírica) / Usar el DOI corto como ID | **`ACAD-`** — claro, breve, distingue de obligatorios |
| D4 | ¿`Caracter_legal`? | `voluntario` / `recomendado` / dejar vacío | **`voluntario`** — son referentes científicos, no obligatorios; el carácter de "evidencia académica" se explicita en `Notas` |
| D5 | ¿Lanzar agente para extracción automática de criterios desde los PDFs? | Sí (1 agente, 6 PDFs) / Manual (revisión humana) / Híbrido (agente propone, humano valida) | **Híbrido** — agente extrae candidatos a filas; la responsable del Producto 1 valida cada propuesta antes de escribir al CSV |
| D6 | ¿Revisar también los 574 internacionales? | Sí ahora / UIP separada / No revisar | **UIP separada** (UIP-004) si esta resulta valiosa |

---

## 6. Plan de ejecución (tras aprobación)

| Paso | Acción | Estimación |
|---|---|---|
| 1 | Confirmar D1-D6 con la responsable | 10 min |
| 2 | Descargar los 6-7 PDFs Open Access a `FUENTES/M1-ACAD-*.pdf` | 5 min |
| 3 | Lanzar agente que extrae criterios cuantificables de cada PDF (1 reporte por artículo) | 30-45 min |
| 4 | Revisión humana de cada propuesta de fila (validar/corregir/descartar) | 20-30 min |
| 5 | Generar script Python que escribe las filas aprobadas a `F0-Matriz_estandares_sostenibilidad.csv` | 5 min |
| 6 | Actualizar `F0-Lista_referencias_y_aportes.md` con 6 nuevas referencias (sección 1 + total) | 5 min |
| 7 | Actualizar `F0-Referencias_Zotero.bib` con 6-7 entradas `@article` (DOI completo) | 5 min |
| 8 | Actualizar `F9-Estrategia_y_hallazgos_M1.md` con ronda 2.5 documentada | 5 min |
| 9 | Commit + push | 2 min |
| | **Total** | **~90-110 min** |

---

## 7. Impacto esperado en M1

| Métrica | Antes UIP | Después UIP (estimado) |
|---|---:|---:|
| Filas totales M1 | 218 | 227-235 (+9 a +17) |
| Referencias en M1 | 30 | 36 (+6 nuevas `ACAD-`) |
| % evidencia empírica arbitrada | 0% | ~4-7% |
| Cobertura E4 materiales | 111 con marca | ~115-120 (mejora con tapia fibras + adobe asfalto + bambú powder) |
| Cobertura E1 bioclimática | 92 con marca | ~95-98 (mejora con confort térmico Bogotá + Scoping Review) |
| Cobertura E2 energía | 83 con marca | ~85-86 (mejora con cookstove TLUD) |

---

## 8. Riesgos y mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| El agente extrae criterios mal interpretados o demasiado abstractos | Media | Medio | Paso 4 de revisión humana obligatorio antes de escribir al CSV |
| Los criterios académicos contradicen normativos (ej. recomiendan parámetros distintos) | Baja | Medio | Documentar tensión explícitamente en `Notas` y en F9 (igual que se hizo con bahareque tradicional vs encementado) |
| Algunos PDFs son Open Access en abstract pero no full-text | Baja | Bajo | Trabajar con abstract + metadatos disponibles; marcar la fila con nota "extracción desde abstract" si full-text no accesible |
| Sumar artículos académicos cambia la "voz" de M1 (que era 80% obligatorio) | Baja | Bajo | Marcar `Caracter_legal=voluntario` explícitamente; mantener mayoría obligatoria |
| Las métricas cuantitativas (citaciones, OA) cambian con el tiempo | N/A | N/A | Documentar fecha de consulta (`2026-04-23`) en `Notas` |

---

## 9. Próximos pasos

1. **Esperar decisión D1-D6** de la responsable del Producto 1.
2. Si se aprueba: ejecutar plan §6.
3. Si se difiere: anotar como pendiente en F9 §2 ("ronda académica 2.5 pendiente — ver UIP-003") y dejarlo registrado para una segunda fase del contrato.
4. Si se descarta: documentar la decisión + razones en F9 (transparencia metodológica — la fuente existió y se decidió no integrarla).

---

**Control de versiones:**

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | 2026-05-12 | UIP inicial — propuesta de incorporación de 6-7 artículos académicos colombianos a M1 con prefijo `ACAD-` |
