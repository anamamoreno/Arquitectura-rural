# Tabla maestra — Anexo 1 Res. 0194/2025

> **¿Qué es este documento?** Síntesis estructurada del **Anexo 1 de la Resolución 0194 de 2025** (Guía de Construcción Sostenible del MVCT), que es el marco normativo obligatorio del proyecto. Extrae y organiza en tablas consultables: la clasificación climática oficial, los porcentajes mínimos de ahorro de energía y agua exigidos por tipología y clima, el catálogo completo de medidas pasivas, activas e hídricas con su aplicabilidad, y los objetivos bioclimáticos por clima. Su función es servir como **referencia rápida** durante todo el levantamiento — evita tener que buscar dentro de las 14.659 líneas del PDF original cada vez que se necesita verificar si una estrategia tiene respaldo normativo o no.

**Fuente:** Anexo No. 1 — Guía de construcción sostenible para el ahorro de agua y energía en edificaciones (MVCT, GreenLoop, dic 2024).
**Extracción:** automatizada desde PDF + validación manual de tablas clave.
**Archivo base:** `docs/extracciones/anexo_0194_raw.txt` (14.659 líneas).
**Versión:** 0.1 — borrador.
**Fecha:** 2026-04-14.

---

## 1. Hallazgo crítico — resuelve pregunta A.1.1

**El Anexo 1 adopta la clasificación Caldas (pisos térmicos IDEAM) complementada con Lang (humedad relativa).** Resultado: **4 climas** idénticos a los del TdR.

Esto **confirma** la espina dorsal de nuestra estrategia. Köppen sigue siendo capa analítica complementaria válida.

### 1.1 Umbrales oficiales (Tabla 1 del Anexo)

| Clima | Temperatura | Altitud | Humedad relativa | Ciudad representativa |
|---|---|---|---|---|
| **Frío** | < 12 °C | > 3.000 msnm | (no diferenciada) | Bogotá (2.640 m)* |
| **Templado** | 12–18 °C | 2.000–2.999 msnm | (no diferenciada) | Medellín (1.405 m), Ibagué (1.168 m) |
| **Cálido seco** (incluye semihúmedo) | 18–24 °C y >24 °C | 1.000–1.999 y <1.000 | HR < 75 % | Cali (926 m), Bucaramanga (950 m) |
| **Cálido húmedo** | > 24 °C | < 1.000 msnm | HR > 75 % | Barranquilla (24 m) |

*Nota: Bogotá aparece en fila de "Frío" en el Anexo aunque esté a 2.640 m. La clasificación es indicativa; el listado oficial de municipios está en **Anexo 2** de la Resolución (mapa + listado por municipio).

### 1.2 Problemas lógicos relativos a los TdR

- **El Anexo no diferencia páramo (ET Köppen)** dentro de "frío". Nuestro vacío normativo declarado se confirma.
- **Alta Guajira (BWh)** queda dentro de "cálido seco" sin tratamiento diferenciado. Confirma vacío.
- **La guía original apunta a edificaciones urbanas** (incluye hoteles, centros comerciales, hospitales). Para vivienda rural, las aplicables son **Vivienda VIS y VIP unifamiliar**.

## 2. Objetivos de diseño por clima (Tabla 16 del Anexo)

| Clima | Objetivos bioclimáticos |
|---|---|
| **Frío** | Maximizar calentamiento por radiación solar (orientación). Reducir impacto del viento. Reducir volúmenes este-oeste para aumentar ganancia solar |
| **Templado** | Maximizar sol en áreas de vivienda principales. Sombra en alcobas y cocina. Controlar viento para circulación en periodos cálidos |
| **Cálido seco** | Edificio como disipador de calor. Maximizar sombra. Reducir fachada oeste |
| **Cálido húmedo** | Maximizar flujo de viento (ventilación cruzada y amontonada). Zonificación según viento (ubicación habitaciones). Máxima sombra |

**Referencia citada:** Szokolay, *Introducción a la ciencia arquitectónica — Lo básico en diseño sostenible* (metáfora de las "tres pieles").

## 3. Porcentajes mínimos de ahorro (Tablas 10 y 11)

Filtrados para tipologías rurales relevantes (Vivienda VIS y VIP).

### 3.1 Energía (% mínimo de ahorro vs. línea base)

| Tipología | Frío | Templado | Cálido seco | Cálido húmedo |
|---|---|---|---|---|
| Vivienda No VIS Unifamiliar | 15 | 20 | 20 | 20 |
| Vivienda VIS Unifamiliar | 15 | 15 | 15 | 15 |
| Vivienda VIP Unifamiliar | 10 | 10 | 10 | 10 |

### 3.2 Agua (% mínimo de ahorro vs. línea base)

| Tipología | Frío | Templado | Cálido seco | Cálido húmedo |
|---|---|---|---|---|
| Vivienda No VIS Unifamiliar | 25 | 25 | 20 | 20 |
| Vivienda VIS Unifamiliar | 15 | 15 | 15 | 15 |
| Vivienda VIP Unifamiliar | 15 | 15 | 15 | 15 |

**Observación:** los ahorros exigidos a VIS y VIP son menores que a No VIS — reflejo del compromiso costo-beneficio. Relevante para el Producto 1: las estrategias que se recomienden deben viabilizar **mínimo esos porcentajes** con presupuesto de vivienda social.

*Nota técnica: la extracción del PDF mezcla filas de tipologías VIS/VIP con otros usos (comercial, oficinas, hotel, educativo, hospital). Los valores aquí mostrados corresponden a las filas etiquetadas como "Vivienda"; validar contra la versión oficial para fines de cumplimiento.*

## 4. Catálogo de medidas del Anexo 1

Clasificación según estructura del Anexo: **pasivas** (arquitectónicas) y **activas** (mecánicas/eléctricas). Tercera categoría: **agua**.

### 4.1 Medidas pasivas de eficiencia energética

| ID | Medida | Aplicabilidad por clima (viviendas VIS/VIP) |
|---|---|---|
| MP-01 | Cubierta verde | Todos los climas (opcional en cálido húmedo) |
| MP-02 | Relación ventana-pared (RVP) | Todos |
| MP-03 | Elementos de protección solar horizontal | Templado, cálido seco, cálido húmedo (alero) |
| MP-04 | Elementos de protección solar vertical | Templado, cálido seco |
| MP-05 | Elementos de protección solar combinados | Templado, cálido seco, cálido húmedo |
| MP-06 | Vidrios de aislamiento térmico (Valor U) | Frío principalmente |
| MP-07 | Vidrios de protección solar (SHGC) | Templado, cálido seco, cálido húmedo |
| MP-08 | Vidrios de protección solar + aislamiento (U + SHGC) | Uso mixto |
| MP-09 | Cubierta de protección solar (Valor U) | Todos |
| MP-10 | Cubierta de protección solar (SRI) | Cálido seco, cálido húmedo |
| MP-11 | Pared de protección solar (Valor U) | Frío, templado |
| MP-12 | Pared de protección solar (SR) | Cálido seco, cálido húmedo |
| MP-13 | **Ventilación natural** | Templado, cálido seco, cálido húmedo |
| MP-14 | **Inercia térmica** | Todos, especialmente frío y cálido seco |
| MP-15 | Night flush (purga nocturna) | Cálido seco principalmente |

### 4.2 Medidas activas de eficiencia energética

| ID | Medida | Aplicabilidad |
|---|---|---|
| MA-01 | Sensores de ocupación / fotométricos / dimerizadores | No residencial principalmente |
| MA-02 | **Iluminación eficiente (LED, CFL, T5) >90 lm/W** | **Todos — obligatoria de facto** |
| MA-03 | Sensores de CO₂ | No residencial |
| MA-04 | Sensores de CO (parqueaderos) | No aplica en vivienda rural |
| MA-05 | Variadores de velocidad para bombas | No residencial |
| MA-06 | Variadores de velocidad para torres de enfriamiento | No aplica en vivienda rural |
| MA-07 | Recuperación de calor aire de extracción | No aplica en vivienda rural |
| MA-08 | DOAS (Dedicated Outdoor Air System) | No aplica en vivienda rural |
| MA-09 | COP de aire acondicionado | Cálido húmedo principalmente |
| MA-10 | Sub-medición de electricidad | Opcional |
| MA-11 | Factores de corrección de potencia | No residencial |
| MA-12 | **Agua caliente solar** | Frío, templado |
| MA-13 | Enfriamiento evaporativo | Cálido seco |
| MA-14 | Calentamiento radiante | Frío |

### 4.3 Medidas de eficiencia en agua

| ID | Medida | Aplicabilidad |
|---|---|---|
| MW-01 | **Lavamanos de bajo consumo** | Todos |
| MW-02 | **Duchas de bajo consumo** | Todos |
| MW-03 | Orinales eficientes | No residencial |
| MW-04 | **Inodoros de bajo consumo** | Todos |
| MW-05 | Tratamiento de aguas residuales y reciclaje (aguas grises) | Opcional, depende capacidad |
| MW-06 | **Recolección y reutilización de aguas lluvias** | Todos (a discreción en VIS) |
| MW-07 | Paisajismo eficiente en agua | Donde aplique |

## 5. Estrategias bioclimáticas por clima — síntesis para matriz M2

Basado en Tabla 16 + Tablas 12–15 del Anexo, filtrado para **Vivienda VIS/VIP unifamiliar**:

### 5.1 Clima frío — estrategias prioritarias

**Energía pasiva:** inercia térmica (MP-14), aislamiento térmico en cubierta (MP-09) y paredes (MP-11), orientación para ganancia solar.
**Energía activa:** iluminación eficiente (MA-02), agua caliente solar (MA-12), calentamiento radiante (MA-14).
**Agua:** aparatos de bajo consumo (MW-01, MW-02, MW-04), captación pluvial a discreción (MW-06).

### 5.2 Clima templado — estrategias prioritarias

**Energía pasiva:** protección solar horizontal+vertical (MP-03, MP-04), ventilación natural (MP-13), cubierta SRI (MP-10), vidrios SHGC (MP-07).
**Energía activa:** iluminación eficiente (MA-02), agua caliente solar opcional (MA-12).
**Agua:** aparatos de bajo consumo + captación pluvial.

### 5.3 Clima cálido seco — estrategias prioritarias

**Energía pasiva:** inercia térmica alta (MP-14), protección solar combinada (MP-05), night flush (MP-15), cubierta SRI (MP-10), ventilación cruzada (MP-13).
**Energía activa:** iluminación eficiente (MA-02), enfriamiento evaporativo (MA-13).
**Agua:** aparatos de bajo consumo + **captación pluvial prioritaria** + reuso de aguas grises.

### 5.4 Clima cálido húmedo — estrategias prioritarias

**Energía pasiva:** ventilación cruzada máxima (MP-13), sombra total (MP-03, MP-05), cubierta SRI (MP-10), protección pared oeste (MP-12).
**Energía activa:** iluminación eficiente (MA-02), COP de AA eficiente si aplica (MA-09).
**Agua:** aparatos de bajo consumo; captación pluvial **a discreción del constructor** (el Anexo la marca como opcional por alta disponibilidad).

## 6. Cruce con los ejes del Producto 1

| Eje P1 | Cobertura del Anexo 1 | Vacíos detectados para la matriz |
|---|---|---|
| E1 Bioclimática pasiva | **Amplia** — Tabla 16 + 15 medidas MP | Sin estrategias específicas para páramo ni alta Guajira |
| E2 Eficiencia energética activa | **Amplia** — 14 medidas MA | Sesgo a edificación urbana; faltan soluciones off-grid rural (solar FV aislado, biogás) |
| E3 Eficiencia hídrica | Media — 7 medidas MW | Faltan soluciones para zonas sin red (pozos, manantiales, tratamiento autónomo) |
| E4 Materiales sostenibles | **Débil / ausente** | El Anexo trata desempeño de envolvente pero **no materiales con atributos de sostenibilidad** (tierra, guadua, reciclados). **Vacío grande** — el P1 deberá cubrirlo con otras fuentes |
| E5 Metodologías pre-diseño | Parcial | Menciona simulación y confort (ASHRAE 55) pero no desarrolla protocolos |

### 6.1 Implicación crítica
El Anexo 1 cubre **E1, E2 y E3** con solvencia para vivienda urbana, pero el **eje E4 (materiales sostenibles)** está prácticamente ausente. Como el TdR del Producto 1 lo exige explícitamente, **tu levantamiento debe apoyarse en otras fuentes** para este eje: Cartilla de Materiales del Ministerio (ya en `Referencias-proyecto/`), Sello Ambiental Colombiano, literatura de arquitectura vernácula.

## 7. Estructura completa del Anexo 1 (para navegación)

| Capítulo | Contenido | Líneas (archivo raw) |
|---|---|---|
| 1. Descripción | Introducción, antecedentes, edificaciones sostenibles, metodología | ~70–700 |
| 2. Lista de medidas | Catálogo de pasivas + activas + agua | ~700–1.400 |
| 3. Análisis de costos | Costo-beneficio por medida | ~1.400–1.500 |
| 4. Matriz de implementación | **Tablas 6–9: matriz por clima** | 1.540 / 3.044 / 4.555 / 6.130 |
| 5. Porcentaje mínimo de ahorro | **Tablas 10–11 energía y agua** | 7.721 / 7.759 |
|   | **Tablas 12–15: medidas recomendadas por clima** | 7.801 / 7.903 / 7.996 / 8.081 |
| 6. Energía — medidas pasivas | Técnicas, estrategias, objetivos | 8.177–8.560 |
|   | Tabla 16: objetivos por clima | 8.235 |
| 7. Energía — medidas activas | HVAC, iluminación, economizadores, COP, VFD, recuperación calor | 8.562–9.400 |
|   | Tablas 17–18: requerimientos eficiencia AA | 8.846 / 8.890 |
| 8. Agua | Estrategias y principios | ~9.400–9.600 |
|   | Tablas 19–20: accesorios, tratamiento, reciclaje | 9.412 / 9.481 |
| 9. Buenas prácticas | Ascensores, viento, almacenamiento de reciclables | 9.600–10.000+ |

## 8. Próximos pasos sugeridos

1. **Descargar Anexo 2** de la Resolución (listado oficial de municipios por clima) — crítico para aplicación territorial.
2. **Validar manualmente las tablas 10 y 11** contra el PDF original (la extracción automática mezcló filas).
3. **Extraer tablas 6–9 (matriz de implementación)** para obtener criterios de priorización: potencial de ahorro, costo, periodo de retorno, disponibilidad en mercado, facilidad de inclusión.
4. **Construir las estrategias de sostenibilidad aplicables a vivienda rural (Res. 0194 + CEELA)** como subproducto de valor agregado.
5. **Flaggear ante el director:** el eje E4 (materiales sostenibles) no está cubierto por el Anexo → el P1 asume cobertura propia desde otras fuentes.

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | 2026-04-14 | Extracción inicial + estructura navegable + identificación de vacíos |
