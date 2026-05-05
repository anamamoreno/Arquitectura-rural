# F8 — Diccionario de la Matriz M2 (Casos de éxito)

**Producto 1 — Track B**
**Archivo de datos:** `F0-Matriz_casos_exito.csv`
**Versión:** 0.1 · **Fecha:** 2026-05-01

---

## Propósito

Define cada columna de M2: significado, valores permitidos, ejemplos y reglas de codificación. Sirve para que cualquier persona que llene o lea la matriz lo haga de forma consistente. Cumple el requisito de trazabilidad PRISMA simplificado del proyecto.

## Reglas generales

- **Codificación:** UTF-8 con BOM (compatibilidad Excel).
- **Separador:** coma (`,`). Si un campo contiene coma, encerrarlo en comillas dobles `"..."`.
- **Valor desconocido:** escribir literal `desconocido` (no dejar en blanco). Solo se permite blanco en columnas opcionales explícitamente marcadas.
- **Listas:** separadas por punto y coma `;` con espacio (ej. `MP-14; MA-22`).
- **Idioma:** español. Topónimos y nombres propios sin traducir.
- **Una fila = un caso.** No combinar dos proyectos en una sola fila.

---

## Columnas

### 1. `ID`
**Definición:** identificador único del caso dentro de M2.
**Formato:** `CAS-NNN` (CAS-001, CAS-002, ...).
**Reglas:** correlativo, sin huecos. No reusar IDs de casos descartados (saltar al siguiente).
**Ejemplos:** `CAS-001`, `CAS-027`.

### 2. `Nombre_proyecto`
**Definición:** nombre del proyecto tal como aparece en la fuente original.
**Formato:** texto libre, máximo ~80 caracteres.
**Reglas:** si no tiene nombre formal (típico de vernáculo), construir descriptor: `"Vivienda de tapia, vereda El Roble"`.
**Ejemplos:** `"Casa Rural en Tibasosa"`, `"Palafito tradicional Pacífico"`.

### 3. `Tipo`
**Definición:** clasificación según origen y autoría del proyecto.
**Valores permitidos:**
- `vernaculo` — tradición transmitida sin autor moderno identificable
- `contemporaneo` — proyecto con autor y año posterior a 2000
- `mixto` — intervención contemporánea sobre tipología vernácula

**Regla de duda:** si hay duda entre `vernaculo` y `mixto` → `mixto`. Si hay duda entre `contemporaneo` y `mixto` → `mixto`.

### 4. `Año`
**Definición:** año de construcción o consolidación del proyecto.
**Formato:** entero (`2018`) o `s.f.` (sin fecha) para vernáculo no datado.
**Reglas:** si solo se conoce la década, escribir `década-1990`. Si se conoce solo el año de publicación de la fuente y no de construcción, anotar publicación pero marcar en `Observaciones`.

### 5. `Ubicacion_depto`
**Definición:** departamento de Colombia donde se ubica el proyecto.
**Formato:** nombre completo del departamento, sin abreviar.
**Ejemplos:** `Boyacá`, `Chocó`, `La Guajira`, `Norte de Santander`.

### 6. `Ubicacion_municipio`
**Definición:** municipio dentro del departamento.
**Formato:** nombre oficial DIVIPOLA.
**Ejemplos:** `Tibasosa`, `Buenaventura`, `Uribia`.
**Si desconocido:** `desconocido` (a evitar — debilita el caso).

### 7. `Ubicacion_vereda`
**Definición:** vereda o corregimiento. Opcional.
**Formato:** texto libre.
**Reglas:** se permite blanco si el caso es genérico al municipio.

### 8. `Clima_TdR`
**Definición:** clima según los 4 climas del TdR/Anexo 1 Res. 0194/2025.
**Valores permitidos:**
- `frio`
- `templado`
- `calido_humedo`
- `calido_seco`

**Reglas:** un único valor. Si el municipio cubre dos climas según altitud, escoger el de la ubicación específica del proyecto y anotar en `Observaciones`.

### 9. `Subtipo_Koppen`
**Definición:** subtipo Köppen-Geiger del proyecto. Opcional pero recomendado.
**Valores permitidos:** códigos Köppen estándar (`Af`, `Am`, `Aw`, `BSh`, `BWh`, `Cfb`, `Cwb`, `ET`, etc.).
**Reglas:** consultar `F0-Mapeo_climatico.md` si hay duda.

### 10. `Sistema_constructivo`
**Definición:** sistema constructivo principal del proyecto.
**Valores recomendados** (extender si aparece nuevo):
- `tapia` (tapia pisada)
- `adobe`
- `bahareque` (bahareque encementado o tradicional)
- `palafito-madera`
- `mamposteria-confinada`
- `mamposteria-estructural`
- `guadua`
- `madera-aserrada`
- `prefabricado-concreto`
- `mixto-<sistema1>-<sistema2>`

**Reglas:** un solo sistema dominante. Si el proyecto combina dos en proporción ~50/50, usar `mixto-...`.

### 11. `Subsistemas`
**Definición:** subsistemas constructivos del edificio donde el caso aplica estrategias de sostenibilidad.
**Valores permitidos** (lista separada por `;`):
- `cimentacion`
- `estructura`
- `envolvente` (muros, ventanas, aislamiento)
- `cubierta`
- `instalaciones` (eléctricas, hidrosanitarias)
- `integral` — el caso aplica estrategias de forma transversal a todos los subsistemas (típico de viviendas vernáculas y prototipos completos)

**Reglas:**
- Si el caso describe una vivienda completa con estrategias en toda la envolvente y sistema → usar `integral`
- Si el caso es una innovación específica (ej. retrofit de cubierta sostenible, biodigestor) → listar solo el/los subsistema(s) tocados
- Combinaciones válidas: `cubierta; instalaciones`, `envolvente; cubierta`, etc.

**Ejemplos:** `integral`, `cubierta`, `envolvente; cubierta`, `instalaciones`.

### 12–15. Ejes E1–E4 (texto descriptivo)

#### `E1_bioclimatica`
**Definición:** estrategias pasivas implementadas (ventilación, orientación, masa térmica, sombreamiento, aislamiento, captación solar pasiva, etc.).
**Formato:** texto libre, 1–3 frases por estrategia, separadas por `;`.
**Ejemplo:** `"Muros de tapia 40 cm para inercia térmica; ventanas pequeñas al norte; alero de 80 cm en fachada sur"`.

#### `E2_energia`
**Definición:** sistemas activos de eficiencia energética (iluminación LED, FV aislado, calentador solar térmico, eficiencia en electrodomésticos, biodigestor para gas).
**Formato:** texto libre.

#### `E3_agua`
**Definición:** estrategias hídricas (captación pluvial, almacenamiento, tratamiento de grises, aparatos de bajo consumo, SUDS, biodigestor para aguas negras, baño seco).
**Formato:** texto libre.

#### `E4_materiales`
**Definición:** materiales sostenibles usados (atributos: origen local, reciclados, baja huella, bajo COV, certificación ambiental, materia prima renovable).
**Formato:** texto libre.

**Reglas comunes E1–E4:** si el caso no aborda un eje, escribir `no aplica` (no dejar blanco). Al menos uno de los cuatro debe tener contenido sustantivo.

### 16. `Estandares_ref`
**Definición:** lista de IDs de estándares de M1 (`F0-Matriz_estandares_sostenibilidad.csv`) que el caso materializa.
**Formato:** lista separada por `;`.
**Cobertura:** cualquiera de las 25 fuentes de M1 (Res.0194, CEELA, Res.0534, RETILAP, RAS, L1715, L1819, L1931, L373, Ley.2462, decretos D948–D1727, ST333, EC-MADS, GuiaMej-MVCT, ParamSFVR, PNVISR, SUDS-MVCT, R0472, R0541, CCCS-2024, TdR-CEELA).
**Ejemplo:** `MP-14; MA-22; SUDS-3; CEELA-C03`.
**Regla:** mínimo 1 ID. Si el caso no materializa ningún estándar identificable de M1, no entra en M2.

### 17. `Cumplimiento_observado`
**Definición:** observaciones sobre desviaciones, cumplimiento parcial o matices respecto a los estándares listados en `Estandares_ref`.
**Formato:** texto libre. Si hay varias observaciones, separar por `;` y prefijar con el ID del estándar.
**Ejemplo:** `"MP-14: muro 35 cm vs 40 cm requeridos; SUDS-3: tanque 800 L vs 1000 L recomendados"`.
**Reglas:** se permite blanco si el cumplimiento es total respecto a los estándares listados.

### 18. `Genero_inclusion`
**Definición:** consideraciones de género o inclusión social presentes en el proyecto (Ley 2462/2025).
**Formato:** texto libre.
**Ejemplo:** `"Cocina con extracción mecánica para reducir exposición de mujeres a humo de leña; baño accesible para PCD"`.
**Reglas:** se permite blanco si no aplica o no se detectó.

### 19. `Estado`
**Definición:** estado actual del proyecto.
**Valores permitidos:**
- `construido` — construido pero estado de operación desconocido
- `en_operacion` — construido y en uso confirmado
- `abandonado` — construido pero no en uso
- `desconocido`

### 20. `Verificable`
**Definición:** tipo de evidencia que respalda el caso.
**Valores permitidos:**
- `foto` — foto disponible (mínimo aceptable)
- `publicacion` — descripción técnica publicada
- `visita` — visita en sitio del consultor
- `referencia_indirecta` — solo mención en otra fuente; usar con cautela

**Regla:** `referencia_indirecta` solo se acepta si el origen es académico o institucional.

### 21. `Fuente_principal`
**Definición:** referencia bibliográfica del documento que respalda el caso. Si se conoce la página, incluirla aquí mismo (no hay columna dedicada).
**Formato:** cita corta + página opcional, o URL.
**Ejemplos:** `"Hábitat Para La Paz (PUJ, 2021), p. 45"`, `"Vivienda y cultura (U. del Valle / ICANH, 2022), p. 120-125"`, `"https://archdaily.co/co/..."`.

### 22. `Archivo_fuente`
**Definición:** nombre del archivo PDF dentro de la carpeta `FUENTES/` que respalda el caso.
**Formato:** nombre del archivo con extensión, sin ruta.
**Reglas:**
- El archivo debe existir en `C:/Users/user/Proyecto-Arq_Rural/FUENTES/`
- La app abre el PDF con la aplicación por defecto del sistema (clic en botón "📄 Abrir PDF")
- Solo funciona cuando la app corre en local (no en VPS)
**Ejemplos:** `Vivienda-Nueva-Rural.pdf`, `Habitat-Para-La-Paz.pdf`.

### 23. `URL_fuente`
**Definición:** URL pública del documento fuente (PDF en repositorio universitario, DOI de revista, link de descarga oficial). Permite acceder al documento desde la versión web de la app sin necesidad del PDF local.
**Formato:** URL completa que empieza con `http://` o `https://`. Vacío si no hay URL pública.
**Reglas:**
- Debe responder con un PDF, una página de catálogo del repositorio, o un DOI válido
- No usar enlaces de Google Scholar (búsqueda, no documento)
- En la app se renderiza como botón **🔗 Abrir en navegador** que abre en nueva pestaña
- Funciona en local **y** en VPS (a diferencia del botón "📄 Abrir PDF" que solo funciona en local)
- Editable en la app para casos pendientes
**Ejemplos:** `https://repositorio.ucp.edu.co/handle/10785/12345`, `https://doi.org/10.18389/dearq30.2023.04`.

### 24. `Tipo_fuente`
**Definición:** tipo de fuente que documenta el caso.
**Valores permitidos:**
- `premio` — Bienal Colombiana, SCA, CAF
- `bienal`
- `revista` — Proa, Escala, ArchDaily, Plataforma Arquitectura
- `tesis` — repositorio universitario
- `ONG` — Hábitat para la Humanidad, Tierra Viva, etc.
- `oficial` — MinCultura, DNP, MVCT, Findeter
- `libro`
- `documento_proyecto` — uno de los PDFs ya en `Referencias-proyecto/`

### 25. `Lecciones_aprendidas`
**Definición:** qué replicar y qué evitar del caso. Insumo directo para el Producto 2.
**Formato:** texto libre, 1–4 frases.
**Ejemplo:** `"Replicar: orientación E-O minimiza ganancia solar; alero protege tapia de lluvia. Evitar: humedad por capilaridad sin sobrecimiento de piedra"`.

### 26. `Observaciones`
**Definición:** campo libre para cualquier información que no encaja en otra columna.
**Formato:** texto libre.

### 27. `Estado_validacion`
**Definición:** estado del caso en el flujo de validación del equipo.
**Valores permitidos:**
- `pendiente_revision` — extraído automáticamente o agregado manualmente; aún no revisado
- `aceptado` — validado por el equipo, entra a la matriz definitiva M2
- `descartado` — revisado y rechazado; se conserva la fila para trazabilidad

**Regla:** se modifica vía botones de la app (`✓ Validar` / `✗ Descartar`). Al cambiar de estado, la app autocompleta `Fecha_validacion` y `Validado_por`.

### 28. `Motivo_descarte`
**Definición:** razón por la cual el caso fue descartado. Solo se llena si `Estado_validacion = descartado`.
**Formato:** texto libre breve.
**Ejemplos:** `"sin estrategia identificable"`, `"urbano, no rural"`, `"duplicado de CAS-008"`, `"solo conceptual no construido"`.
**Reglas:** se permite blanco si `Estado_validacion ≠ descartado`.

### 29. `Fecha_validacion`
**Definición:** fecha en que se cambió `Estado_validacion` por última vez.
**Formato:** ISO `YYYY-MM-DD`.
**Reglas:** autocompletada por la app al hacer click en validar/descartar/reactivar. No editar a mano salvo correcciones.

### 30. `Validado_por`
**Definición:** persona que tomó la decisión de validación.
**Formato:** texto libre, recomendado iniciales o nombre corto (ej. `Ana`, `Philippe`, `AM`, `PB`).
**Reglas:** la app pide al inicio de cada sesión "¿Quién valida hoy?" y guarda el nombre en `st.session_state`. Se autocompleta al hacer click en validar/descartar.

---

## Validaciones recomendadas (para QA al cierre)

- `ID` único, sin huecos
- `Clima_TdR` ∈ {frio, templado, calido_humedo, calido_seco}
- `Tipo` ∈ {vernaculo, contemporaneo, mixto}
- `Estado` ∈ {construido, en_operacion, abandonado, desconocido}
- `Verificable` ∈ {foto, publicacion, visita, referencia_indirecta}
- Al menos uno de E1–E4 con contenido (no `no aplica` en los 4)
- `Estandares_ref` tiene ≥1 ID válido (que exista en M1)
- Cuotas: ≥2 casos por `Clima_TdR`

---

## Cambios

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | 2026-05-01 | Versión inicial. 23 columnas. Decisiones según F6 v0.1 |
| 0.2 | 2026-05-01 | +5 columnas: Pagina_referencia, Estado_validacion, Motivo_descarte, Fecha_validacion, Validado_por. Soporte multiusuario Nivel 1 (lock + auditoría) |
| 0.3 | 2026-05-01 | +1 columna: Subsistemas (cimentacion/estructura/envolvente/cubierta/instalaciones/integral). Total 29 cols |
| 0.4 | 2026-05-01 | -1 Pagina_referencia (página va en Fuente_principal); +1 Archivo_fuente (PDF en FUENTES/, abrible desde la app). Total 29 cols |
| 0.5 | 2026-05-03 | +1 URL_fuente (link público al documento — repositorio universitario / DOI / sitio oficial). Total 30 cols |
