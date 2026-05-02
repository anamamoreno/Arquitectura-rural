# Decisiones por resolver — Producto 1

> **¿Qué es este documento?** Registro de las decisiones estratégicas que deben tomarse con el director del proyecto y el supervisor del contrato (Ministerio) para ejecutar el Producto 1 sin ambigüedades de alcance. Cada decisión incluye contexto, opciones y estado actual. Las resueltas apuntan al documento donde quedó documentada la respuesta.

**Proyecto:** Guía técnica de estándares de sostenibilidad para vivienda rural y pública (Res. 0194/2025).
**Producto:** 1 — Levantamiento de información.
**Versión:** 0.2 · **Fecha:** 2026-04-15.

---

## Resumen de estado

| Estado | Cantidad |
|---|---|
| ✅ Resueltas | 8 |
| 🚫 Fuera de alcance del P1 | 2 |
| ⏳ Pendientes | 8 |
| **Total** | **18** |

---

## A. Decisiones para el SUPERVISOR DEL CONTRATO (Ministerio)

### A.1 — Bloqueantes

#### A.1.1 Clasificación climática del Anexo 1
**Contexto:** el TdR habla de "4 climas de Colombia" pero no precisa qué clasificación técnica adopta el Anexo 1 de la Res. 0194/2025.

**✅ RESUELTA:** Caldas (pisos térmicos IDEAM) + Lang (humedad relativa) → 4 climas: frío, templado, cálido seco, cálido húmedo.

**Documentado en:** `F0-2-Mapeo_climatico.md` §3 (mapeo TdR ↔ Köppen ↔ Caldas-Lang) y `F0-3-Síntesis-Anexo1.md` §1 (extracción directa del PDF del Anexo 1).

---

#### A.1.2 Definición de los 2 sistemas constructivos por clima
**Contexto:** el TdR del Producto 2 dice "al menos dos sistemas constructivos previamente definidos". No era claro quién los define.

**✅ RESUELTA:** el Ministerio entregó algunos sistemas constructivos; el equipo debe complementar. La selección final la hacen los 2 arquitectos del equipo.

**Documentado en:** `F0-Material_reunion_arquitectos.md` §1 (taxonomía de 6 dimensiones propuesta para validar con arquitectos) y `F0-3-AnalisisGuias_EjesSostenibilidad.md` §2.3 (análisis del Inventario de Sistemas Constructivos VIS 2000).

---

#### A.1.3 Insumos previos del Ministerio
**Contexto:** ¿qué documentos del Ministerio tomar como punto de partida obligatorio?

**✅ RESUELTA:** se compilaron 9 documentos validados por el director del proyecto como base documental oficial.

**Documentado en:** `F0-3-AnalisisGuias_EjesSostenibilidad.md` §1 (matriz de cobertura por eje de los 9 PDFs).

---

### A.2 — Ajustes de alcance

#### A.2.1 Variantes climáticas por subtipo Köppen
**Contexto:** dentro de cada uno de los 4 climas TdR hay subtipos Köppen con diferencias técnicas relevantes (ej. palafito en Af vs. bahareque en Am; páramo ET vs. altiplano Cwb).

**⏳ PENDIENTE — POR ESCOGER.** Opciones:
- **(a)** Variantes visibles como fichas adicionales.
- **(b)** Variantes en anexo técnico (no en guía principal).
- **(c)** Mantener estricto 4 climas, sin variantes.

**Propuesta técnica ya formulada en:** `F0-2-Mapeo_climatico.md` §2 — "Köppen es capa subordinada: subdividir solo cuando la literatura revela diferencias medibles en al menos uno de los 4 ejes".

**Implicación:** puede duplicar el número de fichas del Producto 2 (de 8 a hasta 16).

---

#### A.2.2 Nivel de integración del enfoque de género e inclusión social
**Contexto:** el TdR pide considerar el enfoque, pero no precisa profundidad.

**⏳ PENDIENTE — POR DEFINIR.** Opciones:
- **(a) Decorativo:** preámbulo + imágenes inclusivas.
- **(b) Capítulo dedicado:** sección específica en la guía.
- **(c) Transversal:** cada estrategia evaluada por impacto diferencial (recomendación del equipo).

**Propuesta técnica ya formulada en:** `F0-4-Producto1-Estrategia.md` — recomienda tratamiento transversal con columna dedicada en M1.

**Implicación:** la opción (c) requiere levantar evidencia adicional sobre impactos diferenciales (salud, carga doméstica, seguridad, accesibilidad, autonomía económica).

---

#### A.2.3 Inclusión social ampliada — comunidades étnicas
**Contexto:** "inclusión social" en Colombia rural incluye comunidades indígenas, afro, raizales, ROM, con saberes constructivos vernáculos propios.

**⏳ PENDIENTE — POR DEFINIR.**

**Propuesta parcial en:** `F0-4-Producto1-Estrategia.md` — lista 5 dimensiones: comunidades étnicas, discapacidad, adultos mayores, víctimas del conflicto, economía campesina.

**Implicación:** diferenciación étnica implica consulta previa o validación con representantes — ¿contempla el cronograma este paso?

---

#### A.2.4 Metodologías de cumplimiento
**Contexto:** el TdR pide "metodologías o procedimientos de cumplimiento" pero la literatura académica raramente las documenta.

**⏳ PENDIENTE — POR DEFINIR.** ¿Es responsabilidad del P1 o del P2?

**Estado actual:** declarado como **vacío** en `F0-4-Producto1-Estrategia.md` §8 — "Metodologías de verificación de cumplimiento: no desarrolladas a profundidad; requieren cruce normativo específico con NTC, NSR-10, RAS, RETIE".

**Implicación:** si es responsabilidad del P1, hay un cruce normativo adicional que debe preverse en tiempos y esfuerzos.

---

#### A.2.5 Tratamiento del páramo y vacíos normativos
**Contexto:** el páramo (Köppen ET) y la alta Guajira (BWh) no están cubiertos por el Anexo 1 ni por CEELA.

**⏳ PENDIENTE — RELACIONADO CON A.2.1.** Opciones:
- **(a)** Excluirlos explícitamente del alcance.
- **(b)** Incluirlos documentando el vacío (recomendación del equipo).
- **(c)** Incluirlos proponiendo adaptación desde literatura andina internacional.

**Vacíos ya declarados en:** `F0-2-Mapeo_climatico.md` §4.1 y `F0-3-Síntesis-Anexo1.md` §1.2.

**Implicación:** la opción (c) requiere fuentes extranjeras y validación experta adicional.

---

#### A.2.6 Cambio climático y horizonte temporal
**Contexto:** las viviendas que se diseñen con esta guía vivirán 40–60 años; el clima en 2070 será distinto al actual.

**⏳ PENDIENTE — SIN RESPUESTA.**

**Propuesta mencionada en:** `F0-2-Mapeo_climatico.md` — incorporar proyecciones IDEAM 2040/2070 como filtro de futuro.

**Implicación:** agregar dimensión futura amplía el levantamiento a escenarios climáticos y adaptación.

---

#### A.2.7 Idioma y versiones del entregable

**🚫 FUERA DE ALCANCE DEL PRODUCTO 1.** No corresponde al equipo de búsqueda de información.

---

## B. Decisiones para el DIRECTOR DE PROYECTO (interno)

### B.1 — Bloqueantes

#### B.1.1 Cronograma del Producto 1

**✅ RESUELTA:** 2 semanas (10 días hábiles), del 2026-04-14 al 2026-04-28.

**Documentado en:** `F0-4-Producto1-Estrategia.md` §3 y `F0-Plan_trabajo.md` (cronograma diario).

---

#### B.1.2 Composición del equipo

**✅ RESUELTA:** 2 personas para el Producto 1 (uno full-time, uno con dedicación parcial). Equipo ampliado: 6 personas (2 expertos + 2 arquitectos + 2 responsables de búsqueda).

**Documentado en:** `F0-Plan_trabajo.md` §1–2 y `F0-4-Producto1-Estrategia.md` §9.

---

#### B.1.3 Acceso a bases de datos indexadas

**✅ RESUELTA:** los 2 expertos directores facilitan acceso a Scopus/WoS. Se complementa con fuentes abiertas (SciELO, Redalyc, Google Scholar, repositorios universitarios CO).

**Documentado en:** `F1-Protocolo_busqueda.md` §9 (bases priorizadas) y §11 (fuentes colombianas con URLs).

---

### B.2 — Coordinación con el Producto 2

#### B.2.1 Interlocución con el equipo del Producto 2

**⏳ PENDIENTE — SIN RESPUESTA.** ¿Quién lidera el Producto 2 y cuál es el canal y frecuencia de coordinación? ¿Hay espacios formales de entrega parcial?

**Implicación:** el P1 es insumo del P2. Entregas parciales permiten al P2 empezar sin esperar el cierre total.

---

#### B.2.2 Formato de entrega de las matrices

**✅ RESUELTA:** se acepta la recomendación del equipo → Excel (CSV) + Zotero por portabilidad.

**Documentado en:** `F4-Matriz_M1.csv` (plantilla operativa) y `F4-Matriz_M1_diccionario.md` (diccionario de datos).

---

#### B.2.3 Imagen institucional y plantillas

**🚫 FUERA DE ALCANCE DEL PRODUCTO 1.** No corresponde al equipo de búsqueda de información.

---

### B.3 — Validación y calidad

#### B.3.1 Expertos para validación cruzada

**✅ RESUELTA:** los expertos para validar son los 2 líderes del proyecto (internos), no expertos externos.

**Documentado en:** `F0-Plan_trabajo.md` §7.2 (coordinación con expertos).

---

#### B.3.2 Revisión jurídica del mapeo normativo

**⏳ PENDIENTE — "NO SÉ".** ¿Las estrategias de sostenibilidad (Res. 0194 + CEELA) requieren revisión jurídica formal antes de entregarlas?

**Implicación:** si sí, hay que prever tiempo adicional e interlocutor legal.

---

## C. Preguntas de cierre — ambos interlocutores

### C.1 Criterios de aceptación del Producto 1

**⏳ PENDIENTE — NO EXISTEN.** No hay criterios formales de aceptación ni lista de chequeo del Ministerio.

**Riesgo:** sin criterios de aceptación, la aprobación queda subjetiva. El equipo propone usar el checklist de `F5-Sintesis_y_cierre.md` §5 como referencia interna de completitud.

---

### C.2 Entregables opcionales valorados

**⏳ PENDIENTE — POR REVISAR.** Subproductos propuestos:
- Estrategias de sostenibilidad aplicables a vivienda rural — obligatorias (Res. 0194) y recomendadas (CEELA).
- Informe de vacíos normativos.
- Fichas de casos vernáculos con diversidad étnico-territorial.
- Mapa de calor de densidad de evidencia.

¿El Ministerio los valora como parte del entregable o son "valor agregado" del consultor?

---

## Síntesis ejecutiva — las 5 decisiones más urgentes aún pendientes

| # | Decisión | Estado | Impacto |
|---|---|---|---|
| 1 | **A.2.1** Variantes Köppen (fichas / anexo / ninguna) | POR ESCOGER | Define volumen del P2 |
| 2 | **A.2.2** Nivel de integración de género | POR DEFINIR | Condiciona columna transversal de M1 |
| 3 | **A.2.5** Tratamiento del páramo y vacíos (excluir / declarar / adaptar) | VINCULADO A A.2.1 | Define si buscamos literatura andina |
| 4 | **B.2.1** Interlocución con equipo del P2 | SIN RESPUESTA | Sin canal no hay entrega parcial posible |
| 5 | **C.1** Criterios de aceptación del P1 | NO EXISTEN | Riesgo de rechazo subjetivo al cierre |

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | 2026-04-14 | Borrador inicial — 18 preguntas organizadas por audiencia y urgencia |
| 0.2 | 2026-04-15 | Cruce con documentos F0: 8 preguntas marcadas ✅ con referencia cruzada, 2 marcadas 🚫 fuera de alcance, 8 pendientes ⏳. Síntesis ejecutiva reducida a 5 decisiones urgentes reales. Título y función actualizados. |
