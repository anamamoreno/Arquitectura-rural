# Guía de integración de Zotero — Producto 1

> **¿Qué es este documento?** Paso a paso para configurar Zotero como gestor bibliográfico del proyecto y usarlo como herramienta dinámica durante las búsquedas. Cubre: estructura de carpetas, tags, cómo guardar referencias mientras se navega, cómo enlazar con la Matriz M1 y cómo compartir con el equipo.

**Versión:** 0.1 · **Fecha:** 2026-04-22.

---

## 1. Componentes de Zotero que usaremos

| Componente | Qué es | Para qué lo usamos |
|---|---|---|
| **Zotero Desktop** | Aplicación de escritorio (ya instalada) | Organizar, etiquetar, anotar |
| **Zotero Connector** | Extensión del navegador (Chrome, Firefox, Edge) | Guardar referencias con un clic mientras se navega |
| **Zotero Groups** | Biblioteca compartida en la nube | Colaborar con el otro responsable de búsqueda |
| **Zotero PDF Reader** | Lector de PDF integrado | Subrayar, anotar y extraer citas |

## 2. Instalar Zotero Connector (si no lo tienes)

1. Abrir Zotero Desktop → debe aparecer la ventana principal.
2. Ir a https://www.zotero.org/download/ en tu navegador.
3. Hacer clic en **"Install Zotero Connector"** (para Chrome, Firefox o Edge).
4. Confirmar la instalación.
5. Verificar: debe aparecer un **icono de Zotero** (carpeta o documento) en la barra del navegador.

**Resultado:** al visitar Scopus, SciELO, Redalyc, Google Scholar o cualquier repositorio, el icono cambia según el tipo de contenido (artículo, libro, tesis, página web). Un clic guarda la referencia en Zotero con los metadatos completos.

## 3. Crear la estructura de carpetas (colecciones)

En Zotero Desktop, crear la siguiente estructura de colecciones (carpetas). Clic derecho en "Mi biblioteca" → "Nueva colección":

```
Proyecto-Arq-Rural/
├── 00_Pre_validados/         ← los 9 PDFs del Ministerio ya fichados
├── 01_E1_Bioclimatica/
├── 02_E2_Energia/
├── 03_E3_Agua/
├── 04_E4_Materiales/
├── 05_E5_Metodologias/
├── 06_Vernaculo_CO/          ← casos vernáculos por región
├── 07_Normativa_CO/          ← Res. 0194, 0549, NSR-10, NTC, CONPES, SAC
└── 08_Descartadas/           ← referencias que no pasaron screening
```

**Importante:** una referencia puede estar en **múltiples colecciones** a la vez (ej. una fuente sobre bahareque puede estar en `01_E1_Bioclimatica` y en `04_E4_Materiales`). Zotero no duplica el registro; solo crea enlaces.

## 4. Configurar los tags (etiquetas)

Los tags permiten filtrar la biblioteca de forma cruzada, independiente de las carpetas.

### 4.1 Tags obligatorios por referencia

Usar estos tags al guardar o revisar cada referencia:

**Por eje:**
- `eje:E1` · `eje:E2` · `eje:E3` · `eje:E4` · `eje:E5`

**Por clima TdR:**
- `clima:calido-humedo` · `clima:calido-seco` · `clima:templado` · `clima:frio`

**Por subtipo Köppen (solo si la fuente lo diferencia):**
- `koppen:Af` · `koppen:Am` · `koppen:Aw` · `koppen:BSh` · `koppen:BWh` · `koppen:Cfb` · `koppen:Cwb` · `koppen:ET`

**Por origen:**
- `origen-CO:si` · `origen-CO:no`

**Por tipo de fuente:**
- `tipo:tesis-CO` · `tipo:revista-CO` · `tipo:MVCT` · `tipo:MADS` · `tipo:CCCS` · `tipo:SAC` · `tipo:academica-internacional` · `tipo:vernaculo` · `tipo:normativa`

**Por estado en el proyecto:**
- `incluida-M1:si` · `incluida-M1:no` · `screening:pendiente`

### 4.2 Tags opcionales

- `region-CO:pacifico` · `region-CO:caribe` · `region-CO:andes` · `region-CO:orinoquia` · `region-CO:amazonia` · `region-CO:insular`
- `prevalidado:si`
- `genero-inclusion:aplica`
- `sistema:tapia` · `sistema:bahareque` · `sistema:guadua` · etc. (según taxonomía acordada con arquitectos)

### 4.3 Cómo crear tags masivamente

1. Seleccionar varias referencias (Ctrl+clic).
2. En el panel derecho → pestaña **Tags** → arrastrar el tag deseado.
3. Para asignar tag a muchas a la vez: seleccionar todas → clic derecho → "Añadir etiqueta" → escribir el tag.

## 5. Flujo de trabajo diario — guardar mientras se navega

### 5.1 Desde Scopus / SciELO / Redalyc / Google Scholar

1. Ejecutar la ecuación de búsqueda en el navegador.
2. En la página de resultados: el icono del Connector aparece como **carpeta** (múltiples resultados). Hacer clic → seleccionar las referencias que pasaron filtro de título.
3. Zotero las guarda con metadatos completos (título, autores, año, DOI, resumen).
4. En Zotero Desktop: arrastrar a la colección correspondiente (ej. `01_E1_Bioclimatica`).
5. Agregar tags: `eje:E1` + `clima:calido-seco` + `origen-CO:si` + `screening:pendiente`.

### 5.2 Desde repositorios universitarios CO

Los repositorios colombianos (UNAL, UniAndes, etc.) tienen soporte **parcial** del Connector. Si el icono no aparece o falla:

1. Copiar la URL de la tesis/documento.
2. En Zotero Desktop: `Archivo → Añadir por identificador` (pegar DOI si existe).
3. Si no tiene DOI: `Archivo → Nueva referencia → Tesis` → llenar a mano título, autor, año, universidad.
4. Adjuntar el PDF manualmente: arrastrar el archivo descargado sobre la referencia en Zotero.

### 5.3 Desde los 9 PDFs pre-validados

1. En Zotero: arrastrar cada PDF directamente a la colección `00_Pre_validados`.
2. Zotero intentará extraer metadatos automáticamente del PDF.
3. Verificar y corregir los campos (título, autor, año).
4. Agregar tags: `prevalidado:si` + `origen-CO:si` + los ejes que cubra.

### 5.4 Desde una referencia de bola de nieve

Al revisar las citas de un paper clave:

1. Hacer clic en el DOI o título de la referencia citada.
2. Si llega a la página del artículo → usar el Connector para guardar.
3. En Zotero, agregar nota: `"Encontrada por snowballing desde [título del paper clave]"`.
4. Agregar tag: `screening:pendiente`.

## 6. Adjuntar PDFs y anotar

### 6.1 Adjuntar PDF a una referencia

- **Automático:** si el Connector guardó la referencia y el PDF está disponible en Open Access, Zotero lo descarga solo.
- **Manual:** arrastrar el PDF sobre la referencia en Zotero → queda adjunto.

### 6.2 Anotar dentro del PDF (Zotero PDF Reader)

1. Doble clic en el PDF adjunto → se abre el lector integrado.
2. Herramientas disponibles:
   - **Resaltar texto** (amarillo, rojo, verde, azul) → se extrae como nota.
   - **Añadir nota al margen** → agregar anotación propia.
   - **Seleccionar área** → captura una región como imagen (útil para tablas/gráficos).
3. Las anotaciones se sincronizan y son buscables.

**Consejo para el proyecto:** usar colores con significado:
- 🟡 Amarillo = dato relevante general.
- 🟢 Verde = estrategia/medida para M1.
- 🔵 Azul = métrica cuantitativa (dato que va a columna `Metrica_desempeno`).
- 🔴 Rojo = dato que contradice o cuestiona otra fuente.

## 7. Enlazar Zotero con la Matriz M1

### 7.1 De Zotero a M1

Cuando una referencia pasa screening y se decide incluir en M1:

1. En Zotero: cambiar tag `screening:pendiente` → `incluida-M1:si`.
2. Abrir `F4-Matriz_M1.csv` y crear la(s) fila(s) correspondiente(s).
3. En la columna `Fuente` de M1: usar la **cita corta** (ej. `Rodríguez & Pérez (2021)`).
4. En la columna `Observaciones` de M1: opcionalmente poner la **clave Zotero** (el identificador interno que aparece en Zotero al hacer clic derecho → "Generar clave de cita").

### 7.2 De M1 a Zotero

Si alguien consulta M1 y quiere ir a la fuente original:

1. Buscar la cita corta en la barra de búsqueda de Zotero.
2. Zotero localiza la referencia con PDF adjunto, notas y tags.

### 7.3 Trazabilidad completa

```
Ecuación BS-007        Zotero                     Matriz M1
(qué buscar)           (dónde vive la fuente)      (qué se extrajo)

BS-007 tapia     ───►  Rodríguez 2021.pdf    ───►  E1-005 (fila en M1)
cálido seco            con tags, notas,             con fuente, eje,
                       PDF anotado                  clima, métrica
```

## 8. Colaborar con el otro responsable de búsqueda

### Opción A — Biblioteca grupal Zotero (recomendada)

1. Ir a https://www.zotero.org/groups/ → **Crear nuevo grupo**.
2. Nombre: `Proyecto-Arq-Rural-P1`.
3. Tipo: **Privado** (solo miembros invitados).
4. Invitar al otro responsable con su correo.
5. En Zotero Desktop: la biblioteca grupal aparece bajo "Bibliotecas de grupo".
6. Crear la misma estructura de colecciones (§3) dentro del grupo.
7. **Ambos responsables** guardan directamente en la biblioteca grupal.

**Ventaja:** sincronización automática. Lo que uno guarda, el otro lo ve.

### Opción B — Exportar/importar periódicamente

Si no se quiere o no se puede crear grupo:

1. Cada responsable trabaja en su biblioteca local.
2. Al cierre de cada día: `Archivo → Exportar colección` → formato **RIS** o **BibTeX**.
3. Enviar el archivo exportado por correo/compartido.
4. El otro importa: `Archivo → Importar` → seleccionar el archivo.

**Desventaja:** manual, propenso a duplicados. Solo usar si la Opción A no es viable.

## 9. Exportar bibliografía al cierre del proyecto

Al terminar el Producto 1, exportar la biblioteca como entregable:

1. Seleccionar la colección `Proyecto-Arq-Rural` completa.
2. `Archivo → Exportar colección`:
   - **RIS** → compatible con cualquier gestor bibliográfico.
   - **BibTeX** → compatible con LaTeX.
   - **CSV** → abre en Excel (útil para cruzar con M1).
3. Guardar en `docs/entregables/Biblioteca_Zotero_exportada.ris`.

Este archivo es uno de los **6 entregables del Producto 1** (ver `F0-4-Producto1-Estrategia.md` §6).

## 10. Checklist de configuración inicial (una sola vez)

- [ ] Zotero Desktop abierto y funcional.
- [ ] Connector instalado en el navegador principal.
- [ ] Colecciones creadas según estructura §3.
- [ ] Tags obligatorios probados (crear uno de cada familia al menos).
- [ ] 9 PDFs pre-validados importados a `00_Pre_validados` con tags.
- [ ] Biblioteca grupal creada e invitación enviada (si aplica).
- [ ] PDF Reader probado con anotaciones de color.

## 11. Documentos relacionados

- `F1-Protocolo_busqueda.md` §14 — estructura Zotero y tags obligatorios (definición normativa).
- `F1-Tutorial_Matriz_busqueda.md` — cómo enlazar BS- con M1 a través de Zotero.
- `F4-Tutorial_Matriz_M1.md` — cómo llenar M1 con referencias de Zotero.
- `F2-Ejecucion_busquedas.md` — registro diario de búsquedas ejecutadas.

---

**Control de versiones**

| Versión | Fecha | Cambios |
|---|---|---|
| 0.1 | 2026-04-22 | Guía inicial: instalación, estructura, tags, flujo diario, enlace con M1, colaboración |
