# Lista de medidas — Capítulo 2 del Anexo 1 Res. 0194/2025

> **¿Qué es este documento?** Catálogo detallado de las **38 medidas** de construcción sostenible definidas en el Capítulo 2 del Anexo 1, con descripción, parámetros técnicos y aplicabilidad a vivienda rural VIS/VIP. Complementa la síntesis general del Anexo (`F0-3-Síntesis-Anexo1.md`) con el desglose completo por medida. Sirve como referencia para llenar la columna `Medida_Anexo1_ref` de la Matriz M1.

**Fuente:** Anexo No. 1 — Guía de construcción sostenible para el ahorro de agua y energía en edificaciones (MVCT, GreenLoop, dic 2024).
**Extracción:** `docs/extracciones/anexo_0194_raw.txt` líneas 690–1310.
**Versión:** 0.1 · **Fecha:** 2026-04-23.

---

## 1. Medidas pasivas de eficiencia energética (§2.1 del Anexo — 15 medidas)

Son las que se incorporan en el **diseño arquitectónico** de la edificación y aprovechan las condiciones ambientales del entorno. No involucran sistemas mecánicos o eléctricos.

| # | Código M1 | Medida | Descripción | Parámetro técnico | Aplica vivienda rural |
|---|---|---|---|---|---|
| 1 | MP-01 | **Relación Ventana / Pared (RVP)** | Proporción entre superficie vidriada y pared externa; equilibrar luz natural vs. transferencia de calor | RVP (%) | Sí |
| 2 | MP-02 | **Protección solar horizontal** | Aleros / voladizos sobre ventanas; bloquean radiación solar con ángulo alto | Ángulo de sombreado vertical (ASV) | Sí |
| 3 | MP-03 | **Protección solar vertical** | Aletas laterales a ventanas; bloquean radiación con ángulo bajo | Ángulo de sombreado horizontal (ASH) | Sí |
| 4 | MP-04 | **Protección solar combinada** | Combinación de elementos horizontales + verticales | ASV + ASH combinado | Sí |
| 5 | MP-05 | **Valor U del vidrio** (aislamiento térmico) | Resistencia del vidrio al flujo de calor; menor U = mejor aislante. Rango típico: 2.3–5.8 W/m²K | Valor U (W/m²K) | Condicional |
| 6 | MP-06 | **SHGC del vidrio** (ganancia calor solar) | Coeficiente 0–1 que mide paso de radiación infrarroja; menor SHGC = menos ganancia solar | SHGC (adimensional) | Condicional |
| 7 | MP-07 | **Vidrio U + SHGC combinado** | En cálido: SHGC bajo + U bajo reduce refrigeración; en frío: SHGC alto captura calor solar | Valor U + SHGC | Condicional |
| 8 | MP-08 | **Valor U cubierta** | Aislamiento térmico del techo; depende de material + aislante + cámara de aire | Valor U cubierta (W/m²K) | Sí |
| 9 | MP-09 | **Valor U paredes externas** | Aislamiento térmico de fachadas; materiales: concreto, mampostería, bloque, livianos | Valor U pared (W/m²K) | Sí |
| 10 | MP-10 | **Reflectividad paredes externas (SR)** | Capacidad de reflejar radiación solar (0–1); pinturas / revestimientos reflectantes | SR (0–1) | Sí |
| 11 | MP-11 | **Reflectividad cubierta (SRI)** | Índice de reflectancia solar (0–100); pintura blanca SRI 79 refleja 79 % de energía solar | SRI (0–100) | Sí |
| 12 | MP-12 | **Cubierta verde** | Sustrato + vegetación sobre losa; mitiga isla de calor; reduce transmisión solar | Valor U resultante (W/m²K) | Condicional |
| 13 | MP-13 | **Inercia térmica** | Materiales que almacenan calor y lo liberan progresivamente; depende de calor específico, masa y densidad | Capacidad térmica (kJ/m²K) | Sí |
| 14 | MP-14 | **Ventilación natural** | Entrada y salida de aire sin sistemas mecánicos; reduce carga térmica y mejora renovación del aire | ACH (cambios aire/hora) | Sí |
| 15 | MP-15 | **Night flush** (descarga nocturna) | Eliminar calor diurno con aire fresco nocturno; aberturas abiertas de noche, cerradas de día con cortinas | Diferencial T° diurna/nocturna | Sí (cálido seco) |

## 2. Medidas activas de eficiencia energética (§2.2 del Anexo — 13 medidas)

Comprenden el uso de **sistemas mecánicos y/o eléctricos** para crear condiciones de confort interior.

### 2.1 Iluminación (§2.2.1)

| # | Código M1 | Medida | Descripción | Parámetro técnico | Aplica vivienda rural |
|---|---|---|---|---|---|
| 16 | MA-01 | **Iluminación natural + control luz día** | Aprovechar luz natural en áreas periféricas con sensores fotoeléctricos y dimerizadores | Factor de luz día (FLD) | Sí |
| 17 | MA-02 | **Densidad de potencia de luz (LPD)** | Luminarias LED >90 lm/W; menor LPD = menor consumo. Evitar CFL (mercurio). Cumplir RETILAP Res. 40150/2024 | LPD (W/m²) · lm/W | Sí — obligatoria de facto |
| 18 | MA-03 | **Controles de iluminación** | Sensores de ocupación, sensores fotométricos, dimerizadores, zonificación interior/exterior/parqueaderos | Tipo de sensor | No (no residencial) |

### 2.2 HVAC (§2.2.2)

| # | Código M1 | Medida | Descripción | Parámetro técnico | Aplica vivienda rural |
|---|---|---|---|---|---|
| 19 | MA-04 | **COP de aire acondicionado** | Coeficiente de desempeño; COP más alto = más eficiente. Referencia ASHRAE 90.1. Priorizar refrigerantes bajo GWP (RETSIT) | COP (adimensional) | Condicional (cálido húmedo) |
| 20 | MA-05 | **Sensores de CO para parqueaderos** | Regulan extracción mecánica según concentración de monóxido | ppm CO umbral | No |
| 21 | MA-06 | **Sensores de CO₂ para aire fresco** | Controlan ingreso de aire exterior según niveles de CO₂ interior | ppm CO₂ umbral | No |
| 22 | MA-07 | **Variadores de velocidad (VSD) para bombas** | Control electrónico que ajusta velocidad según demanda; reduce consumo y aumenta vida útil | % ahorro vs. velocidad fija | No (no residencial) |
| 23 | MA-08 | **Recuperación de calor de aire extracción (HRW)** | Rueda recuperadora que precalienta o pre-enfría aire de entrada con el de salida; eficiencia ≥60 % | Eficiencia recuperación (%) | No |
| 24 | MA-09 | **Variadores de velocidad torres de enfriamiento** | VSD en ventiladores de torres; operación con cargas parciales | % ahorro | No |
| 25 | MA-10 | **Agua caliente solar** | Colectores solares para agua caliente; aprovecha energía solar gratuita; reduce consumo energético | Fracción solar (%) | Sí (frío/templado) |
| 26 | MA-11 | **Enfriamiento evaporativo** | Enfría aire mediante evaporación de agua (panel húmedo o aspersores); aumenta humedad en climas secos | ΔT enfriamiento (°C) | Sí (cálido seco) |
| 27 | MA-12 | **Calentamiento radiante** | Red de tuberías con agua caliente en piso, paredes o techo; intercambio por convección y radiación | T° superficie (°C) | Condicional (frío) |

### 2.3 Potencia eléctrica (§2.2.3)

| # | Código M1 | Medida | Descripción | Parámetro técnico | Aplica vivienda rural |
|---|---|---|---|---|---|
| 28 | MA-13 | **DOAS** (sistema aire exterior dedicado) | Suministra aire frío o caliente deshumidificado independiente de unidad terminal | Eficiencia DOAS | No |

## 3. Medidas de eficiencia en agua (§2.2.4 del Anexo — 10 medidas)

| # | Código M1 | Medida | Descripción | Parámetro técnico | Aplica vivienda rural |
|---|---|---|---|---|---|
| 29 | MW-01 | **Accesorios ahorro de agua** (general) | Grifería conservadora: salidas de bajo flujo, duchas y WC de doble descarga | Caudal (l/min) o volumen (l/descarga) | Sí |
| 30 | MW-02 | **Lavamanos eficientes** | Grifos cierre automático + aireadores; público <2 l/min; privado <6.8 l/min | Caudal (l/min) | Sí |
| 31 | MW-03 | **Duchas de bajo flujo** | Caudal <8 l/min considerado eficiente | Caudal (l/min) | Sí |
| 32 | MW-04 | **Orinales eficientes** | Consumo <1.5 l/descarga | Volumen (l/descarga) | No (no residencial) |
| 33 | MW-05 | **Inodoros eficientes** | Simple: <4.8 l/descarga; doble descarga: sólidos <4.5 l/descarga | Volumen (l/descarga) | Sí |
| 34 | MW-06 | **Tratamiento y reciclaje aguas grises** | PTAR para aguas residuales excepto sanitarios y cocina; reúso en sanitarios, AA, riego | % de agua reciclada | Condicional |
| 35 | MW-07 | **Tratamiento y reciclaje aguas negras** | PTAR para todas las aguas residuales; reúso en sanitarios, riego, AA | % de agua reciclada | Condicional |
| 36 | MW-08 | **Recolección y aprovechamiento aguas lluvias** | Sistema integral: captación por cubiertas → filtrado → PTALL → tanque tratada → redistribución | Volumen captado (m³/año) | Sí — prioritaria |
| 37 | MW-09 | **Paisajismo eficiente en agua** | Vegetación nativa o adaptada; bajo consumo de riego; establecimiento <2 años | Reducción consumo riego (%) | Sí |
| 38 | MW-10 | **Recuperación condensado de AA** | Recolectar agua de condensación del aire acondicionado para reúso | Volumen recuperado (l/día) | No |

## 4. Resumen por categoría

| Categoría | Cantidad | Rango # | Códigos M1 |
|---|---|---|---|
| Pasivas energéticas | 15 | #1–#15 | MP-01 a MP-15 |
| Activas — Iluminación | 3 | #16–#18 | MA-01 a MA-03 |
| Activas — HVAC | 9 | #19–#27 | MA-04 a MA-12 |
| Activas — Potencia eléctrica | 1 | #28 | MA-13 |
| Eficiencia en agua | 10 | #29–#38 | MW-01 a MW-10 |
| **Total** | **38** | | |

## 5. Aplicabilidad a vivienda rural VIS/VIP — resumen

### Siempre aplicables (18 medidas)

MP-01, MP-02, MP-03, MP-04, MP-08, MP-09, MP-10, MP-11, MP-13, MP-14 (todas las pasivas de envolvente + ventilación + inercia).
MA-01, MA-02 (iluminación natural + LED).
MW-01, MW-02, MW-03, MW-05, MW-08, MW-09 (aparatos bajo consumo + captación pluvial + paisajismo).

### Aplicables según clima (6 medidas)

| Medida | Clima donde aplica |
|---|---|
| MP-15 Night flush | Cálido seco (oscilación térmica alta) |
| MA-10 Agua caliente solar | Frío y templado |
| MA-11 Enfriamiento evaporativo | Cálido seco |
| MA-12 Calentamiento radiante | Frío |
| MW-06 Tratamiento aguas grises | Donde hay volumen suficiente |
| MW-07 Tratamiento aguas negras | Donde no hay red de alcantarillado |

### Aplicabilidad condicional (5 medidas)

MP-05, MP-06, MP-07 (vidrios especiales — depende de disponibilidad y presupuesto VIS).
MP-12 (cubierta verde — requiere losa y mantenimiento).
MA-04 COP (solo si se instala AA en cálido húmedo extremo).

### No aplicables a vivienda rural (9 medidas)

MA-03 (controles iluminación no residencial), MA-05 (CO parqueaderos), MA-06 (CO₂ aire fresco), MA-07 (VSD bombas), MA-08 (HRW), MA-09 (VSD torres enfriamiento), MA-13 (DOAS), MW-04 (orinales), MW-10 (condensado AA).

Estas 9 medidas están diseñadas para edificaciones **comerciales, hospitalarias u hoteleras** y no son viables ni necesarias en vivienda rural unifamiliar de un piso.

## 6. Cómo usar este documento con la Matriz M1

Al llenar una fila de `F4-Matriz_M1.csv`:

1. Identificar si la estrategia encontrada en la fuente corresponde a alguna de las 38 medidas.
2. Poner el **código M1** (MP-01 a MP-15, MA-01 a MA-13, MW-01 a MW-10) en la columna `Medida_Anexo1_ref`.
3. Si la estrategia **no está** en esta lista, dejar la columna vacía — es un hallazgo que va más allá del Anexo 1 (frecuente en eje E4 materiales y en vernáculo).

## 7. Documentos relacionados

- `F0-3-Síntesis-Anexo1.md` — síntesis general del Anexo 1 (clasificación climática, % ahorros, objetivos por clima, cruce con ejes).
- `F4-Matriz_M1_diccionario.md` — diccionario de la columna `Medida_Anexo1_ref`.
- `F1-Marco_busqueda_sistemas_materiales.md` §6 — lista de complementos sostenibles con referencia cruzada a estos códigos.
- `F1-Matriz_busqueda.csv` — columna `Observaciones` referencia códigos MP/MA/MW.

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | 2026-04-23 | Extracción completa: 38 medidas del capítulo 2 con descripción, parámetros y aplicabilidad rural |
