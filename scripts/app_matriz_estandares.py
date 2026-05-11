"""
App interactiva — Matrices del Producto 1 (Sostenibilidad vivienda rural)
=========================================================================
Tab 1: Matriz M1 — Estándares de Sostenibilidad (lectura)
Tab 2: Matriz M2 — Casos de éxito (lectura + validación con write-back)

Uso:
    streamlit run scripts/app_matriz_estandares.py --server.port 8504
"""

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import portalocker
import os
import re
import sys
import subprocess
from datetime import date

# --- Configuración ---
st.set_page_config(
    page_title="Matrices Sostenibilidad — Vivienda Rural",
    page_icon=None,
    layout="wide"
)

DOCS = os.path.join(os.path.dirname(__file__), "..", "docs")
FUENTES = os.path.join(os.path.dirname(__file__), "..", "FUENTES")
RUTA_M1 = os.path.join(DOCS, "F0-Matriz_estandares_sostenibilidad.csv")
RUTA_M2 = os.path.join(DOCS, "F0-Matriz_casos_exito.csv")

# READ_ONLY=true en VPS: oculta validación, botón PDF y campo "¿Quién valida hoy?"
READ_ONLY = os.getenv("READ_ONLY", "false").lower() == "true"


def abrir_pdf(filename: str) -> tuple[bool, str]:
    """Abre el PDF con la app por defecto del sistema. Solo funciona en local."""
    if not filename:
        return False, "sin archivo asignado"
    path = os.path.abspath(os.path.join(FUENTES, filename))
    if not os.path.exists(path):
        return False, f"no existe: {path}"
    try:
        if sys.platform.startswith("win"):
            os.startfile(path)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
        return True, path
    except Exception as e:
        return False, str(e)

CLIMAS = ["frio", "templado", "calido_humedo", "calido_seco"]
CLIMA_COLOR = {
    "frio": "#4FC3F7",          # azul claro
    "templado": "#81C784",      # verde
    "calido_humedo": "#FFB74D", # naranja
    "calido_seco": "#E57373",   # rojo coral
}
TIPO_COLOR = {
    "vernaculo": "#8D6E63",     # tierra
    "contemporaneo": "#5C6BC0", # índigo
    "mixto": "#9575CD",         # púrpura
}
ESTADO_COLOR = {
    "Construido": "#2E7D32",    # verde
    "Solo diseño": "#EF6C00",   # naranja
}
SUBSISTEMAS = ["integral", "cimentacion", "estructura", "envolvente",
               "cubierta", "instalaciones"]
SISTEMAS_BASE = ["tapia", "adobe", "bahareque", "palafito-madera",
                 "mamposteria-confinada", "mamposteria-estructural",
                 "guadua", "madera-aserrada", "madera", "prefabricado-concreto"]


# --- Cargadores ---
@st.cache_data(ttl=30)
def cargar_m1():
    df = pd.read_csv(RUTA_M1, encoding="utf-8-sig")
    for col in df.columns:
        df[col] = df[col].fillna("").astype(str).str.strip()
    df = df.rename(columns={
        "Descripcion": "Descripción",
        "Etapa_ciclo_vida": "Etapa del ciclo de vida",
        "E1_bioclimatica": "E1 Bioclimática",
        "E2_energia": "E2 Energía",
        "E3_agua": "E3 Agua",
        "E4_materiales": "E4 Materiales",
        "Aplica_vivienda_rural": "Aplica vivienda rural",
        "Caracter_legal": "Carácter legal",
        "Nivel_cumplimiento": "Nivel de cumplimiento",
        "Parametro_indicador": "Parámetro/Indicador",
        "Correspondencia_cruzada": "Correspondencia cruzada",
        "URL_fuente": "URL fuente",
    })
    return df


def cargar_m2():
    """Sin cache — necesitamos releer tras cada escritura."""
    df = pd.read_csv(RUTA_M2, encoding="utf-8-sig")
    for col in df.columns:
        df[col] = df[col].fillna("").astype(str).str.strip()
    return df


def guardar_m2(df: pd.DataFrame):
    """Escritura con file lock (Nivel 1 multiusuario)."""
    with portalocker.Lock(RUTA_M2 + ".lock", timeout=5):
        df.to_csv(RUTA_M2, index=False, encoding="utf-8-sig")


def actualizar_caso(caso_id: str, estado: str, validado_por: str,
                    motivo: str = "", edits: dict | None = None):
    """Reabre M2, actualiza estado + (opcionalmente) campos editados, escribe con lock."""
    df = cargar_m2()
    idx = df.index[df["ID"] == caso_id]
    if len(idx) == 0:
        return False
    df.loc[idx, "Estado_validacion"] = estado
    df.loc[idx, "Fecha_validacion"] = date.today().isoformat()
    df.loc[idx, "Validado_por"] = validado_por
    df.loc[idx, "Motivo_descarte"] = motivo if estado == "descartado" else ""
    if edits:
        for col, val in edits.items():
            if col in df.columns:
                df.loc[idx, col] = val
    guardar_m2(df)
    return True


def captura_edits(row, prefix: str) -> dict:
    """Lee st.session_state buscando inputs por convención key=f'{prefix}_{ID}_{campo}'."""
    edits = {}
    cid = row["ID"]
    for campo in ["Estandares_ref", "Cumplimiento_observado", "Genero_inclusion",
                  "Fuente_principal", "URL_fuente", "Subsistemas"]:
        k = f"{prefix}_{cid}_{campo}"
        if k in st.session_state:
            val = st.session_state[k]
            if isinstance(val, list):
                val = "; ".join(val)
            edits[campo] = val
    return edits


# --- Estado de sesión ---
if "validador" not in st.session_state:
    st.session_state.validador = ""

# --- Título global (NO se muestra en la página Tutorial; se renderiza
# dentro de cada wrapper de página que lo necesite) ---
TITULO_PRINCIPAL = "Estándares de sostenibilidad para vivienda rural en Colombia"

# ============================================================
# PÁGINA M1 — Estándares
# ============================================================
def page_m1():
    df = cargar_m1()
    bcol1, bcol2, bcol3, bcol4, bcol5, bcol6 = st.columns([1, 1, 1, 1, 1, 1])
    with bcol1:
        if st.button("Fuentes", help="Listado de las referencias normativas con link a cada documento oficial", width='stretch'):
            mostrar_referencias()
    with bcol2:
        if st.button("Glosario", help="Ver definiciones de Fin, Enfoque, Estándar, Estrategia, Criterio, Medida", width='stretch'):
            mostrar_glosario()
    with bcol3:
        if st.button("Campos", help="Descripción de las 20 columnas de la matriz", width='stretch'):
            mostrar_campos()
    with bcol4:
        if st.button("Nomenclatura", help="Códigos de IDs unificados + valores de ejes E1–E4", width='stretch'):
            mostrar_nomenclatura()
    with bcol5:
        # Botón Tutorial: abre en una ventana nueva del navegador (popup),
        # no como pestaña. Requiere components.html porque st.markdown
        # filtra los handlers JS inline (onclick). El iframe se hace exactamente
        # de la altura del botón nativo Streamlit (38px) y se elimina el margen
        # default del body para alinear verticalmente con los otros botones.
        components.html(
            """
            <html><head><style>
              html,body{margin:0;padding:0;height:100%;
                        font-family:'Source Sans Pro','Segoe UI',sans-serif;
                        background:transparent;}
              button{width:100%;height:38px;box-sizing:border-box;
                     background-color:#FFFFFF;color:rgb(49,51,63);
                     border:1px solid rgba(49,51,63,0.2);border-radius:0.5rem;
                     cursor:pointer;font-size:0.875rem;font-weight:400;
                     line-height:1.6;display:block;}
              button:hover{border-color:#FF4B4B;color:#FF4B4B;}
            </style></head><body>
            <button type="button" onclick="
                var u = window.parent.location.href.split('?')[0].replace(/\\/[^\\/]*$/, '/tutorial');
                window.open(u, 'tutorial_window', 'popup=yes,width=1200,height=900,scrollbars=yes,resizable=yes');
            "
            title="Cómo organizar las columnas y usar la tabla — abre en ventana nueva del navegador">
              Tutorial
            </button>
            </body></html>
            """,
            height=38,
        )
    with bcol6:
        csv_bytes = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "Exportar",
            data=csv_bytes,
            file_name="F0-Matriz_estandares_sostenibilidad.csv",
            mime="text/csv",
            help="Descargar la matriz M1 completa como CSV (UTF-8 con BOM, abre en Excel)",
            width='stretch',
        )
    st.divider()

    # Filtros en sidebar izquierdo (aplican solo a esta página M1)
    with st.sidebar:
        st.markdown("### Filtros · Estándares M1")
        st.caption("Aplican solo en esta página.")

        referencias = ["Todas"] + sorted(df["Referencia"].unique().tolist())
        ref_sel = st.multiselect("Referencia normativa", referencias, default=["Todas"])

        eje_opciones = ["Todos", "E1 Bioclimática", "E2 Energía", "E3 Agua", "E4 Materiales"]
        eje_sel = st.selectbox("Eje de sostenibilidad", eje_opciones)

        rel_opciones = ["Cualquiera", "Principal", "Complementario", "Transversal"]
        rel_sel = st.selectbox("Tipo de relación con el eje", rel_opciones)

        st.markdown("---")
        climas_m1 = ["Todos", "frio", "templado", "calido_seco", "calido_humedo"]
        clima_sel = st.selectbox("Clima", climas_m1)

        subsistemas = ["Todos", "Cimentación", "Estructura", "Envolvente", "Cubierta",
                       "Instalaciones", "Acabados y complementos", "Exterior"]
        sub_sel = st.selectbox("Subsistema", subsistemas)

        tipos = ["Todos"] + sorted(df["Jerarquía"].unique().tolist())
        tipo_sel = st.selectbox("Jerarquía", tipos)

        st.markdown("---")
        caracteres = ["Todos"] + sorted(df["Carácter legal"].unique().tolist())
        car_sel = st.selectbox("Carácter legal", caracteres)

        rural_opciones = ["Todos", "si", "condicional", "no"]
        rural_sel = st.selectbox("Aplica vivienda rural", rural_opciones)

        etapas = ["Todas"] + sorted(df["Etapa del ciclo de vida"].unique().tolist())
        etapa_sel = st.selectbox("Etapa del ciclo de vida", etapas)

        st.markdown("---")
        ley2462_sel = st.checkbox("Solo con conexión Ley 2462 (género/inclusión)")
        notas_sel = st.checkbox("Solo con notas de contexto rural")

        busqueda = st.text_input("Buscar en nombre o descripción")

    # Aplicar filtros
    filtrado = df.copy()
    if "Todas" not in ref_sel and ref_sel:
        filtrado = filtrado[filtrado["Referencia"].isin(ref_sel)]
    if eje_sel != "Todos":
        col_eje = eje_sel
        if rel_sel == "Cualquiera":
            filtrado = filtrado[filtrado[col_eje] != ""]
        else:
            filtrado = filtrado[filtrado[col_eje] == rel_sel]
    if clima_sel != "Todos":
        filtrado = filtrado[filtrado["Clima"].str.contains(clima_sel, na=False)]
    if sub_sel != "Todos":
        filtrado = filtrado[filtrado["Subsistema"].str.contains(sub_sel, na=False)]
    if tipo_sel != "Todos":
        filtrado = filtrado[filtrado["Jerarquía"] == tipo_sel]
    if car_sel != "Todos":
        filtrado = filtrado[filtrado["Carácter legal"] == car_sel]
    if rural_sel != "Todos":
        filtrado = filtrado[filtrado["Aplica vivienda rural"] == rural_sel]
    if ley2462_sel:
        filtrado = filtrado[filtrado["Ref_Ley2462"] != ""]
    if notas_sel:
        filtrado = filtrado[filtrado["Notas"] != ""]
    if etapa_sel != "Todas":
        filtrado = filtrado[filtrado["Etapa del ciclo de vida"] == etapa_sel]
    if busqueda:
        mask = (
            filtrado["Tema"].str.contains(busqueda, case=False, na=False) |
            filtrado["Descripción"].str.contains(busqueda, case=False, na=False) |
            filtrado["ID"].str.contains(busqueda, case=False, na=False)
        )
        filtrado = filtrado[mask]

    st.subheader(f"Resultados: {len(filtrado)} de {len(df)} ítems")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Obligatorios", len(filtrado[filtrado["Carácter legal"] == "obligatorio"]))
    with col2:
        st.metric("Con Ley 2462", len(filtrado[filtrado["Ref_Ley2462"] != ""]))
    with col3:
        st.metric("Aplican rural", len(filtrado[filtrado["Aplica vivienda rural"] == "si"]))
    with col4:
        st.metric("Fuentes", filtrado["Referencia"].nunique())

    cols_default = ["ID", "Referencia", "URL fuente", "Tema", "Jerarquía",
                    "E1 Bioclimática", "E2 Energía", "E3 Agua", "E4 Materiales",
                    "Clima", "Aplica vivienda rural", "Carácter legal", "Ref_Ley2462"]
    cols_mostrar = st.multiselect("Columnas a mostrar", df.columns.tolist(), default=cols_default)
    if cols_mostrar:
        col_cfg = {}
        if "URL fuente" in cols_mostrar:
            col_cfg["URL fuente"] = st.column_config.LinkColumn(
                "URL fuente", display_text="abrir", help="Abre el documento original en una pestaña nueva"
            )
        st.dataframe(filtrado[cols_mostrar], width='stretch', height=500, column_config=col_cfg)


# ============================================================
# PÁGINA M2 — Casos de éxito
# ============================================================
def page_m2():
    df_m2 = cargar_m2()
    df_m1 = cargar_m1()

    st.subheader(f"Matriz M2 — {len(df_m2)} casos compilados")

    if READ_ONLY:
        st.info("Modo solo lectura. La validación/descarte de casos se hace en el entorno local de la responsable del Producto 1.")
    else:
        # Identificación del validador
        st.session_state.validador = st.text_input(
            "¿Quién valida hoy? (iniciales o nombre corto)",
            value=st.session_state.validador,
            max_chars=20,
            help="Se guarda con cada decisión de validar/descartar para trazabilidad."
        )

    # Métricas de progreso
    n_pend = len(df_m2[df_m2["Estado_validacion"] == "pendiente_revision"])
    n_acep = len(df_m2[df_m2["Estado_validacion"] == "aceptado"])
    n_desc = len(df_m2[df_m2["Estado_validacion"] == "descartado"])

    m1, m2, m3 = st.columns(3)
    m1.metric("Pendientes", n_pend)
    m2.metric("Aceptados", n_acep)
    m3.metric("Descartados", n_desc)

    # Heatmap cobertura
    with st.expander("Cobertura clima × sistema (solo aceptados)", expanded=False):
        aceptados = df_m2[df_m2["Estado_validacion"] == "aceptado"]
        if len(aceptados) == 0:
            st.info("Aún no hay casos aceptados.")
        else:
            pivot = pd.crosstab(aceptados["Clima_TdR"], aceptados["Sistema_constructivo"])
            st.dataframe(pivot, width='stretch')
            st.caption("Meta mínima: ≥2 casos por clima · Meta ideal: ≥1 caso por (clima × sistema)")

    st.divider()

    # Filtros en sidebar (aplican solo al tab M2)
    with st.sidebar:
        st.markdown("### Filtros · Casos M2")
        st.caption("Aplican solo en esta página.")

        clima_filt = st.multiselect("Clima TdR", CLIMAS, default=[])

        tipos_unicos = sorted([t for t in df_m2["Tipo"].unique() if t])
        tipo_filt = st.multiselect("Tipo", tipos_unicos, default=[])

        sistemas_unicos = sorted([s for s in df_m2["Sistema_constructivo"].unique() if s])
        sis_filt = st.multiselect("Sistema constructivo", sistemas_unicos, default=[])

        estados_unicos = sorted([e for e in df_m2["Estado"].unique() if e])
        estado_proy_filt = st.multiselect("Estado del proyecto", estados_unicos, default=[])

        st.markdown("---")
        st.markdown("**Archivo fuente**")
        st.caption("Marca/desmarca para mostrar/ocultar.")
        archivos_unicos = sorted([a for a in df_m2["Archivo_fuente"].unique() if a])
        # Casos sin PDF local (solo URL) — se representan como entrada virtual
        n_solo_url = int((df_m2["Archivo_fuente"].fillna("").str.strip() == "").sum())
        # Lista total de claves para los atajos (incluye '' si hay casos solo-URL)
        archivos_keys = list(archivos_unicos)
        if n_solo_url > 0:
            archivos_keys.append("")

        # Atajos (van ANTES de los checkboxes — usan callbacks para evitar race condition)
        def _set_all_archivos(val: bool):
            for a in archivos_keys:
                st.session_state[f"archivo_{a}"] = val

        col_a, col_b = st.columns(2)
        with col_a:
            st.button("Todas", key="archivo_all", width='stretch',
                      on_click=_set_all_archivos, args=(True,))
        with col_b:
            st.button("Ninguna", key="archivo_none", width='stretch',
                      on_click=_set_all_archivos, args=(False,))

        archivo_filt = []
        for a in archivos_unicos:
            # nombre corto sin .pdf y con conteo
            n_casos = int((df_m2["Archivo_fuente"] == a).sum())
            label = f"{a.replace('.pdf', '')}  ·  {n_casos}"
            if st.checkbox(label, value=True, key=f"archivo_{a}"):
                archivo_filt.append(a)
        # Entrada virtual para casos solo-URL (sin PDF local)
        if n_solo_url > 0:
            label_url = f"(sin PDF · solo URL)  ·  {n_solo_url}"
            if st.checkbox(label_url, value=True, key="archivo_"):
                archivo_filt.append("")

    # Aplicar filtros
    f = df_m2.copy()
    if clima_filt:
        f = f[f["Clima_TdR"].isin(clima_filt)]
    if tipo_filt:
        f = f[f["Tipo"].isin(tipo_filt)]
    if sis_filt:
        f = f[f["Sistema_constructivo"].isin(sis_filt)]
    if estado_proy_filt:
        f = f[f["Estado"].isin(estado_proy_filt)]
    # Archivo fuente: a diferencia de los otros, default es "todas seleccionadas"
    # → siempre filtramos por la lista actual (vacía = nada visible)
    f = f[f["Archivo_fuente"].isin(archivo_filt)]

    st.markdown(f"**{len(f)} casos** con los filtros actuales")

    if len(f) == 0:
        st.info("No hay casos con los filtros seleccionados.")
    else:
        cols_tabla = [
            "ID", "Nombre_proyecto", "Tipo", "Año",
            "Ubicacion_depto", "Ubicacion_municipio",
            "Clima_TdR", "Sistema_constructivo",
        ]
        st.caption("Click en cualquier fila para abrir el detalle del caso.")
        event = st.dataframe(
            f[cols_tabla],
            width='stretch',
            height=500,
            hide_index=True,
            on_select="rerun",
            selection_mode="single-row",
            key="m2_tabla",
        )
        if event.selection and event.selection.rows:
            sel_idx = event.selection.rows[0]
            sel_id = f.iloc[sel_idx]["ID"]
            if st.session_state.get("m2_last_shown_id") != sel_id:
                st.session_state["m2_last_shown_id"] = sel_id
                st.session_state["detalle_caso_id"] = sel_id
                mostrar_detalle_caso()


# ============================================================
# DIALOG Referencias — listado completo de F0-Lista_referencias_y_aportes.md
# ============================================================
@st.dialog("Referencias normativas que sustentan los estándares de sostenibilidad", width="large")
def mostrar_referencias():
    doc_path = os.path.join(DOCS, "F0-Lista_referencias_y_aportes.md")
    try:
        with open(doc_path, "r", encoding="utf-8") as f:
            contenido = f.read()
        # Extraer sección 1 (tabla principal con descripciones)
        match = re.search(r"## 1\..*?(?=\n## 2\.)", contenido, re.DOTALL)
        if match:
            seccion = match.group(0)
            # Quitar el encabezado "## 1. Distribución..." (primera línea)
            seccion = re.sub(r"^## 1\.[^\n]*\n+", "", seccion)
            st.markdown(seccion, unsafe_allow_html=False)
        else:
            st.warning("No se encontró la sección 1 en el documento.")
            st.markdown(contenido)
    except FileNotFoundError:
        st.error(f"No se encontró el archivo: {doc_path}")
    except Exception as e:
        st.error(f"Error leyendo el documento: {e}")

    # Sección de referencias en proceso (no incluidas en la matriz)
    st.markdown("---")
    st.markdown("### Próximas referencias normativas (no incluidas en M1)")
    st.markdown(
        """
**Proyecto de Ley sobre Bioconstrucción, Construcción Sostenible y Arquitectura Tradicional**
(`#LeyDeBioconstrucción`)

- **Autora:** Senadora Isabel Cristina Zuleta López (Pacto Histórico)
- **Estado:** **Radicado el 7 de abril de 2025** en la Secretaría de la Cámara de Representantes. **Aún NO aprobado** — sin número definitivo asignado.
- **Tres pilares definidos:**
  1. **Bioconstrucción** — materiales naturales, diseño bioclimático, bajo impacto ambiental durante todo el ciclo de vida.
  2. **Construcción sostenible** — uso racional de recursos, energías limpias, materiales reciclables, eficiencia energética.
  3. **Arquitectura tradicional** — saberes ancestrales, materiales locales, valores comunitarios.
- **Foco regulatorio:** incentivos para prácticas constructivas responsables, reducción de Residuos de Construcción y Demolición (RCD), economía circular en construcción, tecnologías limpias.

> **Nota:** este Proyecto de Ley **no se ha incluido en la matriz M1** porque aún no es ley vigente. Se documenta aquí como referencia normativa en discusión que podría incorporarse en versiones futuras de la guía si avanza su trámite legislativo.

🔗 [Comunicado oficial — Sen. Zuleta López](https://isabelzuleta.com/radicado-proyecto-ley-que-impulsa-bioconstruccion-construccion-sostenible-y-arquitectura-tradicional-en-colombia/)
        """,
        unsafe_allow_html=False,
    )


# ============================================================
# DIALOG Detalle de caso M2 — vista de tarjeta completa de un caso
# Título dinámico: "{ID} · {Nombre_proyecto}"
# ============================================================
def mostrar_detalle_caso():
    cid = st.session_state.get("detalle_caso_id")
    if not cid:
        return
    df_m2 = cargar_m2()
    df_m1 = cargar_m1()
    sel = df_m2[df_m2["ID"] == cid]
    if len(sel) == 0:
        return
    row = sel.iloc[0].fillna("")
    title = f"{cid} · {row['Nombre_proyecto']}"

    @st.dialog(title, width="large")
    def _show_detalle():
        ubicacion = (
            f"{row['Año']} · {row['Ubicacion_depto']}"
            + (f" · {row['Ubicacion_municipio']}" if row['Ubicacion_municipio'] else "")
            + (f" · {row['Ubicacion_vereda']}" if row['Ubicacion_vereda'] else "")
        )
        st.markdown(
            f'<div style="font-size:1.05rem; color:#37474F; margin:4px 0 8px 0;">{ubicacion}</div>',
            unsafe_allow_html=True,
        )

        # Badges tipo + clima + sistema + estado
        clima = row["Clima_TdR"] or "desconocido"
        clima_c = CLIMA_COLOR.get(clima, "#9E9E9E")
        tipo = row["Tipo"] or "desconocido"
        tipo_c = TIPO_COLOR.get(tipo, "#9E9E9E")
        koppen = f" ({row['Subtipo_Koppen']})" if row['Subtipo_Koppen'] else ""
        estado = row["Estado"] or "desconocido"
        estado_c = ESTADO_COLOR.get(estado, "#9E9E9E")
        badge_html = (
            f'<div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap; margin:8px 0;">'
            f'<span style="background:{tipo_c}; color:white; padding:6px 14px; border-radius:6px; '
            f'font-size:1.05rem; font-weight:600;">{tipo.upper()}</span>'
            f'<span style="background:{clima_c}; color:white; padding:6px 14px; border-radius:6px; '
            f'font-size:1.05rem; font-weight:600;">{clima.upper()}{koppen}</span>'
            f'<span style="background:#455A64; color:white; padding:6px 14px; border-radius:6px; '
            f'font-size:1.05rem; font-weight:600;">{row["Sistema_constructivo"]}</span>'
            f'<span style="background:{estado_c}; color:white; padding:6px 14px; border-radius:6px; '
            f'font-size:1.05rem; font-weight:600;">{estado.upper()}</span>'
            f'</div>'
        )
        st.markdown(badge_html, unsafe_allow_html=True)

        if row.get("Subsistemas"):
            st.markdown("---")
            st.markdown(f"**Subsistemas:** {row['Subsistemas']}")
            st.markdown("---")

        cE1, cE2, cE3, cE4 = st.columns(4)
        with cE1:
            st.markdown("**E1 Bioclimática**")
            st.markdown(row["E1_bioclimatica"] or "_no aplica_")
        with cE2:
            st.markdown("**E2 Energía**")
            st.markdown(row["E2_energia"] or "_no aplica_")
        with cE3:
            st.markdown("**E3 Agua**")
            st.markdown(row["E3_agua"] or "_no aplica_")
        with cE4:
            st.markdown("**E4 Materiales**")
            st.markdown(row["E4_materiales"] or "_no aplica_")

        if row.get("Genero_inclusion"):
            st.markdown("---")
            st.markdown("**Género / inclusión social** (Ley 2462/2025)")
            st.markdown(row["Genero_inclusion"])

        st.markdown("---")
        st.markdown("**Estándares que materializa este proyecto**")
        refs = [r.strip() for r in (row.get("Estandares_ref") or "").split(";") if r.strip()]
        if refs:
            cruce = df_m1[df_m1["ID"].isin(refs)]
            if len(cruce) > 0:
                st.dataframe(cruce[["ID", "Referencia", "Tema"]], width='stretch', hide_index=True)
        else:
            st.markdown("_sin asignar_")
        if row.get("Cumplimiento_observado"):
            st.markdown(f"_Cumplimiento observado:_ {row['Cumplimiento_observado']}")

        st.markdown("---")
        if row.get("Lecciones_aprendidas"):
            st.markdown(f"**Lecciones:** {row['Lecciones_aprendidas']}")
        if row.get("Observaciones"):
            st.markdown(f"_Observaciones:_ {row['Observaciones']}")

        st.markdown("---")
        st.markdown(f"**Fuente:** {row['Fuente_principal']}")
        st.caption(
            f"Tipo de fuente: _{row['Tipo_fuente']}_"
            + (f" · Nombre del archivo en la carpeta: `{row['Archivo_fuente']}`" if row['Archivo_fuente'] else "")
        )
        url = (row.get("URL_fuente") or "").strip()
        if url and url.startswith(("http://", "https://")):
            st.markdown(f"URL: [{url}]({url})")

    _show_detalle()


# ============================================================
# PÁGINA Tutorial — abre en ventana nueva desde el botón Tutorial de M1
# ============================================================
def page_tutorial():
    # Ocultar barra lateral solo en esta página
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {display: none !important;}
        [data-testid="collapsedControl"] {display: none !important;}
        [data-testid="stSidebarCollapsedControl"] {display: none !important;}
        section[data-testid="stSidebar"] + div {margin-left: 0 !important;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("# Tutorial")
    st.markdown("## Cómo organizar las columnas de la matriz de Estándares de sostenibilidad")

    with st.expander("**1. Seleccionar las columnas a mostrar en la tabla**"):
        st.markdown("""
En el campo "Columnas a mostrar" arriba de la tabla:
- **Click** en un campo vacío → aparece menú desplegable con todas las columnas disponibles
- **Click** en un nombre de columna → se agrega a la vista
- **Click en la `×`** de una etiqueta → quita esa columna
- Por defecto vienen 13 columnas; puedes agregar las 7 restantes (`Descripcion`, `Etapa_ciclo_vida`, `Notas`, `Subsistema`, `Nivel_cumplimiento`, `Parametro_indicador`, `Correspondencia_cruzada`)
""")

    with st.expander("**2. Reordenar columnas en la tabla**"):
        st.markdown("""
Sobre la tabla:
- En la tabla, **arrastrar lateralmente el encabezado de una columna (color gris)** → la mueves de posición
- El cambio es solo visual (no modifica el CSV)
""")

    with st.expander("**3. Ordenar filas**"):
        st.markdown("""
- **Click** sobre el encabezado de una columna → ordena ascendente
- **Click otra vez** → ordena descendente
- **Click otra vez** → vuelve al orden original
""")

    with st.expander("**4. Buscar dentro de la tabla**"):
        st.markdown("""
- En la esquina superior derecha de la tabla aparece un ícono 🔍 al pasar el mouse
- Permite buscar texto en cualquier columna visible
""")

    with st.expander("**5. Ajustar ancho de columna**"):
        st.markdown("""
- Arrastra el **borde derecho** de un encabezado para hacer la columna más ancha o angosta
""")

    with st.expander("**6. Columnas especiales**"):
        st.markdown("""
- `URL fuente` aparece como botón **abrir** que lleva al documento original en pestaña nueva
- `Notas` y `Descripcion` pueden tener texto largo → la celda se trunca; click sobre la celda para ver el texto completo
""")

    with st.expander("**7. Descargar la vista actual**"):
        st.markdown("""
- Pasa el mouse sobre la tabla → ícono de descarga ⬇ en la esquina superior derecha
- Descarga las filas + columnas que tienes visibles como CSV
""")


# ============================================================
# DIALOG Campos — descripción de las 20 columnas de M1
# ============================================================
@st.dialog("Campos de la matriz M1", width="large")
def mostrar_campos():
    st.caption(
        "La matriz tiene 20 columnas. Cada fila (criterio, medida, principio, enfoque o fin) "
        "se describe con estos campos."
    )
    st.markdown("""
| # | Campo | Qué guarda |
|---|---|---|
| 1 | `Referencia` | Marco normativo o documental del que proviene la fila (ej. `Res.0194`, `CEELA`, `Ley.2462`) |
| 2 | `URL_fuente` | URL pública oficial del documento. Renderizada como botón clickeable en la app |
| 3 | `ID` | Código único de la fila dentro de su marco (ej. `MP-14`, `A-SE-1`, `C06`, `L-F03`). Ver Nomenclatura para todos los prefijos |
| 4 | `Tema` | Nombre/título del término. Ej: "Ventilación natural", "Inercia térmica", "Reducir carga doméstica no remunerada" |
| 5 | `Descripcion` | Descripción técnica con cita textual del marco normativo (~300 caracteres) |
| 6 | `Jerarquía` | Clasificación según la jerarquía conceptual (Fin → Enfoque → Estándar → Estrategia → Criterio → Medida). Valores: `criterio_ambiental` / `criterio_social` / `criterio_economico` / `criterio` / `criterio_metodologico` / `medida_pasiva` / `medida_activa` / `medida_hidrica` / `medida` / `fin` / `enfoque` / `lineamiento` |
| 7 | `Etapa_ciclo_vida` | Fase: `pre-diseño` / `diseño` / `construcción` / `operación` / `deconstrucción` / `extracción/manufactura` / `todas` |
| 8 | `E1_bioclimatica` | Relación con eje E1 (estrategias bioclimáticas pasivas): `Principal` / `Complementario` / `Transversal` / vacío |
| 9 | `E2_energia` | Relación con eje E2 (eficiencia energética activa) |
| 10 | `E3_agua` | Relación con eje E3 (eficiencia hídrica) |
| 11 | `E4_materiales` | Relación con eje E4 (materiales sostenibles) |
| 12 | `Notas` | Texto libre con observaciones: aplicabilidad rural, alternativas vernáculas, datos ENUT, métricas técnicas, alertas |
| 13 | `Ref_Ley2462` | Códigos de la Ley 2462/2025 (enfoques `L-E*` y fines `L-F*`) que conectan con este criterio. Permite filtrar criterios con enfoque género/inclusión |
| 14 | `Aplica_vivienda_rural` | Aplicabilidad a vivienda rural unifamiliar VIS/VIP: `si` / `condicional` (filas `no` se eliminaron de la matriz) |
| 15 | `Clima` | Clima(s) donde aplica: `frio` / `templado` / `calido_seco` / `calido_humedo` / `todos` (separados por espacio si aplica a varios) |
| 16 | `Subsistema` | Subsistema constructivo: `Cimentación` / `Estructura` / `Envolvente` / `Cubierta` / `Instalaciones` / `Acabados y complementos` / `Exterior` / `todos` (separados por espacio) |
| 17 | `Caracter_legal` | Carácter normativo: `obligatorio` / `voluntario` / `recomendado` / `condicional` |
| 18 | `Nivel_cumplimiento` | Nivel de exigencia: `recomendada` / `a_discrecion` (Res. 0194); `minimo` / `deseable` / `avanzado` (Res. 0534) |
| 19 | `Parametro_indicador` | Métrica cuantitativa verificable (ej. `Valor U (W/m²K)`, `SHGC (0-1)`, `ACH (cambios/hora)`, `kg CO₂eq/kg`, `% ahorro vs línea base`) |
| 20 | `Correspondencia_cruzada` | IDs equivalentes en otros marcos que cubren el mismo tema (ej. `Res.0534:S-CT-1; CEELA:C04`) |
""")

# ============================================================
# DIALOG Nomenclatura — códigos de ID unificados + valores de ejes
# ============================================================
@st.dialog("Nomenclatura · Códigos de M1", width="large")
def mostrar_nomenclatura():
    st.markdown("## Tabla unificada de prefijos de ID")
    st.caption(
        "Cada fila de M1 tiene un código único. El prefijo identifica la fuente normativa "
        "y el tipo de criterio/medida."
    )
    st.markdown("""
| Prefijo | Significado | Marco | Ejemplo |
|---|---|---|---|
| `MP-` | **M**edida **P**asiva de eficiencia energética | Res. 0194 (Anexo 1) | `MP-14` = Ventilación natural |
| `MA-` | **M**edida **A**ctiva de eficiencia energética | Res. 0194 (Anexo 1) | `MA-02` = LED >90 lm/W |
| `MW-` | **M**edida hídrica (***W**ater*) | Res. 0194 (Anexo 1) | `MW-08` = Captación aguas lluvias |
| `A-E-` | **A**mbiental — **E**nergía | Res. 0534 | `A-E-1` = Energía embebida en materiales |
| `A-A-` | **A**mbiental — **A**gua | Res. 0534 | `A-A-3` = Consumo agua proyectado |
| `A-EM-` | **A**mbiental — **EM**isiones | Res. 0534 | `A-EM-1` = Emisiones GEI fabricación |
| `A-M-` | **A**mbiental — **M**ateriales | Res. 0534 | `A-M-1` = Materiales bajo impacto |
| `A-S-` | **A**mbiental — **S**uelo | Res. 0534 | `A-S-1` = Evaluación del sitio |
| `A-R-` | **A**mbiental — **R**esiduos | Res. 0534 | `A-R-2` = Diseño modular para disminuir RCD |
| `A-FL-` | **A**mbiental — **FL**ora y fauna | Res. 0534 | `A-FL-1` = Madera responsable |
| `A-SE-` | **A**mbiental — **S**ervicios **E**cosistémicos | Res. 0534 | `A-SE-1` = Drenaje sostenible (SUDS) |
| `S-CT-` | **S**ocial — **C**onfort **T**érmico | Res. 0534 | `S-CT-1` = Confort térmico por diseño |
| `S-CL-` | **S**ocial — **C**onfort **L**umínico | Res. 0534 | `S-CL-1` = Control contaminación lumínica |
| `S-A-` | **S**ocial — calidad del **A**ire | Res. 0534 | `S-A-1` = Calidad aire interior (ASHRAE 62) |
| `S-CA-` | **S**ocial — **C**onfort **A**cústico | Res. 0534 | `S-CA-1` = Diseño confort acústico (40 dBA) |
| `S-H-` | **S**ocial — **H**igiene y toxicidad | Res. 0534 | `S-H-1` = Materiales no tóxicos (HPD, VOC) |
| `S-AC-` | **S**ocial — **AC**cesibilidad | Res. 0534 | `S-AC-1` = Accesibilidad universal |
| `S-AS-` | **S**ocial — **A**cceso a **S**ervicios | Res. 0534 | `S-AS-1` = Distancia a servicios diarios |
| `E-CI-` | **E**conómico — **C**ostos **I**nversión | Res. 0534 | `E-CI-1` = Incidencia en costos |
| `E-CC-` | **E**conómico — **C**onsideraciones **C**omerciales | Res. 0534 | `E-CC-1` = Estrategia comercial |
| `C` | Criterio CEELA (originalmente "principio") | CEELA | `C06` = Movimiento del aire |
| `L-E` | **E**nfoque de la Ley (perspectiva/lente) | Ley 2462 | `L-E10` = Enfoque de cuidado |
| `L-F` | **F**in de la Ley (resultado a lograr) | Ley 2462 | `L-F03` = Reducir carga trabajo doméstico |
| `UPME-` | Cartilla y Guía PGEE-EP | UPME | `UPME-3` = Indicadores Desempeño Energético |
| `RET-` | RETILAP — Iluminación | MinMinas | `RET-2` = Diseño iluminación interior vivienda |
| `SUDS-` | Guía SUDS-MVCT — drenaje sostenible | MVCT/DNP | `SUDS-4` = Cisterna/aljibe |
| `PNVISR-` | Plan Nacional Vivienda Social Rural | MVCT | `PNVISR-1` = Enfoque diferencial obligatorio |
| `ParamSFVR-` | Parametrización Subsidio Vivienda Rural | MVCT | Códigos específicos |
| `GM-X-` | Guía Mejoramientos MVCT | MVCT | `GM-S1` = Mano de obra local |
| `D{XXXX}-N` | Decretos reglamentarios | varios | `D1727-1` = Ecobertura subsidio |
| `L{XXX}-N` | Leyes complementarias | Congreso | `L1715-1` = FNCE incentivos IVA |
| `R{XXXX}-N` | Resoluciones complementarias | varios | `R0472-1` = RCD gestión integral |
| `ST{XXX}-N` | Sentencias Corte Constitucional | Corte | `ST333-1` = Vivienda digna |
| `CCCS-N` | Estado Construcción Sostenible | CCCS | `CCCS-1` = Adopción ASG 93% |
""")

    st.divider()

    st.markdown("## Valores de ejes de sostenibilidad")
    st.caption(
        "Los 4 ejes E1–E4 del TdR. Cada criterio se clasifica por su relación con cada eje "
        "usando palabras completas (no códigos)."
    )
    st.markdown("""
**Valores que puede tomar cada uno de E1, E2, E3, E4:**

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
| `MP-14` Ventilación natural | Principal | — | — | — | Es bioclimática pura |
| `MP-09` Valor U paredes externas | Principal | — | — | Complementario | Aislamiento bioclimático con efecto en materiales |
| `MA-01` Iluminación natural + sensores | Complementario | Principal | — | — | Foco en sistema activo, aporta a bioclimática |
| `C01` Diseño integrado (CEELA) | Transversal | Transversal | Transversal | Transversal | Enfoque de proceso, toca los 4 ejes |
""")

# ============================================================
# DIALOG Glosario — se invoca desde botón en M1 (no es página propia)
# ============================================================
@st.dialog("Glosario · Términos normativos", width="large")
def mostrar_glosario():
    # CSS para expanders con fondo gris (aplica a los expanders de la app pero
    # se inyecta cada vez que se abre el dialog)
    st.markdown(
        """
        <style>
        [data-testid="stExpander"] {
            background-color: #f0f2f6;
            border-radius: 6px;
        }
        [data-testid="stExpander"] details summary {
            background-color: #e6e9ef;
            border-radius: 6px 6px 0 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "Cada término se define según cómo lo emplea la documentación normativa que respalda la matriz "
        "de estándares de sostenibilidad. Las definiciones no son propias: se reconstruyen a partir del "
        "uso textual en cada fuente y se citan con el documento de origen."
    )

    st.markdown("**De lo más abstracto a lo más concreto. Cómo leer la jerarquía:**")
    st.markdown("- **Hacia arriba** se sube en abstracción y se contestan preguntas de *para qué*.")
    st.markdown("- **Hacia abajo** se baja a la ejecución y se contestan preguntas de *cómo*.")
    st.caption("Click en cada término para ver definición, fuente, ejemplo y relación con otros.")
    st.markdown("")  # espacio

    # Datos de los 6 términos
    terminos = [
        {
            "linea": "FIN  ←  qué impacto buscamos  (Ley 2462)",
            "nombre": "Fin",
            "definicion": (
                "Resultado o impacto final que se busca lograr — el *para qué* último de las políticas, "
                "estrategias y medidas. Es la unidad más abstracta: dice qué se quiere transformar, "
                "no cómo hacerlo."
            ),
            "fuente": """
- **Ley 2462/2025**, sección "Fines" — define **16 fines** que orientan toda actuación pública sobre mujer rural. Los más relevantes para vivienda:
  1. Respeto de los saberes y conocimientos tradicionales de las mujeres rurales, campesinas y de la pesca
  2. Reconocer y visibilizar los aportes de la mujer rural como agente transformadora
  3. **Reconocer, redistribuir y reducir la carga de trabajo doméstico y de cuidados no remunerados** (clave para diseño de vivienda)
  4. Promover el desarrollo rural eficaz, inclusivo, sostenible y resiliente
  5. Garantizar acceso integral a recursos productivos y financieros
  6. Promover la autonomía económica
  7. Fomentar alianzas sostenibles
  8. Reconocer la labor de mujeres rurales en el cuidado de los ecosistemas y mitigación del cambio climático
  9. Promover trabajo digno y decente
  10. Fortalecer acceso al sistema de salud
  11. Garantizar participación incidente en instancias de decisión
  12. Proteger las organizaciones de mujeres rurales
  13. Garantizar la igualdad de trato y eliminación de discriminación
  14. Invertir en bienes públicos, infraestructura, transferencias tecnológicas
""",
            "ejemplo": (
                "El `L-F03` (fin: reducir carga de trabajo doméstico no remunerado) justifica medidas como "
                "conexión a acueducto rural (elimina acarreo de agua), estufas eficientes (elimina recolección "
                "de leña), o cocina con extracción mecánica (reduce exposición a humo)."
            ),
            "relacion": (
                "El fin es el más abstracto de toda la jerarquía. Un fin se persigue con varios enfoques, "
                "que orientan estrategias, que se evalúan con criterios y se ejecutan con medidas."
            ),
        },
        {
            "linea": "ENFOQUE  ←  desde qué perspectiva miramos  (Ley 2462, PNVISR)",
            "nombre": "Enfoque",
            "definicion": (
                "Perspectiva o lente de análisis que se aplica de forma transversal a toda intervención. "
                "No es una acción ni un parámetro técnico: es el principio que orienta cómo se diseña, "
                "ejecuta y evalúa cualquier estrategia, criterio o medida."
            ),
            "fuente": """
- **Ley 2462/2025 — Igualdad de oportunidades para mujeres rurales, campesinas y de la pesca** (Congreso de Colombia). Define **12 enfoques obligatorios** que toda política pública para mujer rural debe incorporar:
  1. Enfoque territorial
  2. Enfoque de equidad para la mujer
  3. Enfoque de derechos humanos de las mujeres rurales
  4. Enfoque interseccional y diferencial
  5. Enfoque campesinado
  6. Enfoque curso de vida
  7. Enfoque de discapacidad
  8. Enfoque étnico
  9. Enfoque ambiental
  10. Enfoque de cuidado
- También usado por **PNVISR** (Plan Nacional de Construcción y Mejoramiento de Vivienda Social Rural) — exige enfoque diferencial obligatorio (género, étnico, discapacidad, víctimas, territorial).
""",
            "ejemplo": (
                "El `L-E10` (enfoque de cuidado) no prescribe una medida — exige reconocer que la cocina "
                "y el lavadero concentran trabajo doméstico no remunerado feminizado y diseñar en consecuencia. "
                "Cualquier medida (MP, MA, MW) puede revisarse desde este enfoque."
            ),
            "relacion": (
                "El enfoque opera por encima de las estrategias. Una misma medida (ej. ubicación de la cocina) "
                "cambia su forma según los enfoques aplicados (cuidado, étnico, discapacidad)."
            ),
        },
        {
            "linea": "ESTÁNDAR  ←  qué referencia usamos  (TdR-CEELA, marco general)",
            "nombre": "Estándar",
            "definicion": (
                "Referencia técnica o normativa con la que se compara el desempeño de una vivienda en alguna "
                "dimensión (ahorro energético, hídrico, materiales, confort). Puede ser **obligatorio** "
                "(cuando proviene de una resolución o ley) o **referencial** (voluntario, cuando proviene de "
                "certificaciones internacionales o lineamientos no vinculantes)."
            ),
            "fuente": """
- **TdR de la Guía Técnica de Sostenibilidad Rural CEELA 2026** — usa "estándares de sostenibilidad" como categoría paraguas que abarca tanto Anexo 1 (obligatorio) como criterios CEELA (referenciales).
- Práctica internacional (ISO 21931, IFC EDGE, LEED, CASA Colombia).
""",
            "ejemplo": (
                "Un estándar es la cobertura entera de la matriz — incluye criterios CEELA, medidas Anexo 1, "
                "criterios Res. 0534, etc. La columna `Referencia` indica el origen del estándar "
                "(Res.0194, CEELA, Res.0534…)."
            ),
            "relacion": (
                "Es el más amplio. Un estándar puede contener estrategias, que a su vez se materializan en "
                "medidas o se evalúan con criterios."
            ),
        },
        {
            "linea": "ESTRATEGIA  ←  qué táctica aplicamos  (Anexo 1: E1/E2/E3/E4)",
            "nombre": "Estrategia",
            "definicion": (
                "Agrupación de orden superior que reúne medidas o criterios afines orientados a un mismo "
                "objetivo (ahorro energético, confort térmico, eficiencia hídrica). Es la categoría táctica "
                "entre el objetivo amplio y la acción específica."
            ),
            "fuente": """
- **Resolución 0194/2025 — Anexo 1, secciones 1.4 y 2** ("Las medidas fueron clasificadas según su potencial de ahorro… El resultado es una herramienta de toma de decisiones denominada Matriz de Implementación").
- **TdR-CEELA** (objetivo 2.1: "estrategias bioclimáticas pasivas, estrategias de eficiencia energética de sistemas activos, estrategias de eficiencia hídrica, estrategias de uso de materiales con atributos de sostenibilidad").

**Tipos de estrategia que reconoce el Anexo 1:**

| Estrategia | Sigla | Ámbito |
|---|---|---|
| Bioclimática pasiva | E1 | aprovecha clima sin consumo energético |
| Eficiencia energética activa | E2 | sistemas/equipos que consumen energía |
| Eficiencia hídrica | E3 | reducción de consumo y manejo de aguas |
| Materiales sostenibles | E4 | propiedades y origen de los materiales |
""",
            "ejemplo": (
                "*Ventilación natural cruzada* es una estrategia de E1 que se materializa en varias medidas "
                "concretas (orientación, posición de vanos, distancia entre fachadas)."
            ),
            "relacion": (
                "Una estrategia es **más específica que un estándar** y **más general que una medida o un criterio**."
            ),
        },
        {
            "linea": "CRITERIO  ←  qué desempeño evaluamos  (CEELA: 15 criterios; Res. 0534: 56 criterios)",
            "nombre": "Criterio",
            "definicion": (
                "Enunciado evaluable que permite verificar si una vivienda o proyecto cumple con un aspecto "
                "puntual de sostenibilidad. A diferencia de la medida, el criterio no prescribe la solución "
                "técnica: define qué se debe lograr y cómo se mide."
            ),
            "fuente": """
- **CEELA — 15 criterios** (Certificación de Edificaciones Eficientes en Latinoamérica, IFC/Banco Mundial). Cada criterio es un enunciado de desempeño con métrica asociada.
- **Resolución 0534/2025 — 56 criterios** clasificados en **42 ambientales** + **12 sociales** + **2 económicos**, organizados por 7 fases del ciclo de vida con 3 niveles de cumplimiento (mínimo / deseable / avanzado).
""",
            "ejemplo": """
- `C03` (CEELA) — *Energía incorporada en los materiales*: criterio evaluable mediante el cálculo de kgCO₂eq/m² del material elegido.
- `A-M-1` (Res. 0534) — *Materiales con bajo impacto ambiental*: criterio con 3 niveles de cumplimiento (% de materiales locales / certificados).
""",
            "relacion": (
                "Un criterio puede contener varias medidas que lo satisfacen. Es la unidad evaluable; "
                "la medida es la unidad ejecutable."
            ),
        },
        {
            "linea": "MEDIDA  ←  qué acción técnica ejecutamos  (Anexo 1: 38 medidas MP/MA/MW)",
            "nombre": "Medida",
            "definicion": (
                "Acción técnica concreta y prescriptiva que se implementa en el diseño o construcción para "
                "lograr un ahorro de recursos o un beneficio ambiental específico. Tiene parámetro técnico "
                "verificable (Valor U, SHGC, factor de forma, número de aparatos por m²)."
            ),
            "fuente": """
- **Resolución 0194/2025 — Anexo 1** define **38 medidas** clasificadas en:
  - **15 medidas pasivas** (MP-01 a MP-15): RVP, protección solar, aislamiento, ventilación natural, masa térmica, night flush
  - **13 medidas activas** (MA-01 a MA-13): iluminación LED, HVAC eficiente, solar térmica, enfriamiento evaporativo
  - **10 medidas hídricas** (MW/MH-01 a MW-10): aparatos de bajo consumo, captación pluvial, reúso de aguas grises, paisajismo eficiente
- Cita textual: *"Para determinar el costo de implementación de las medidas… las medidas fueron clasificadas según su potencial de ahorro"* (Anexo 1, p. 7).
""",
            "ejemplo": """
- `MP-14` — Inercia térmica en muros (≥40 cm de masa) para clima frío
- `MA-07` — Calentador solar térmico de placa plana
- `MW-03` — Sanitarios de doble descarga (≤4.5 / 3 L)
""",
            "relacion": (
                "La medida es la **acción concreta** que materializa una estrategia y satisface uno o más criterios. "
                "Es la unidad operacional más concreta del Anexo 1."
            ),
        },
    ]

    for i, t in enumerate(terminos):
        with st.expander(t["linea"], expanded=False):
            st.markdown(f"**Definición:** {t['definicion']}")
            st.markdown("**Fuente / origen del término:**")
            st.markdown(t["fuente"])
            st.markdown("**Ejemplo en M1:**")
            st.markdown(t["ejemplo"])
            st.markdown("**Relación con otros términos:**")
            st.markdown(t["relacion"])
        if i < len(terminos) - 1:
            st.markdown(
                "<div style='text-align:center; font-size:1.6rem; line-height:1; "
                "margin:0.2rem 0; color:#888;'>↓</div>",
                unsafe_allow_html=True,
            )

    st.divider()
    st.markdown("### Ejemplo de encadenamiento jerárquico")
    with st.expander("Ejemplo encadenado de los 6 niveles", expanded=False):
        st.markdown("""
- **Fin** `L-F03`: reducir la carga de trabajo doméstico no remunerado en mujer rural
- **Enfoque** `L-E10`: enfoque de cuidado
- **Estándar** Res. 0194/2025 (obligatorio para VIS rural)
- **Estrategia** E3: eficiencia hídrica
- **Criterio** Res. 0534 `A-SE-1`: provisión confiable de agua potable
- **Medida** `MW-08`: captación pluvial dimensionada con tratamiento (PTALL)
""")

    st.caption(
        "Para más detalle (sub-tipos del campo `Tipo`, sigla EECA, convenciones de codificación), "
        "ver `docs/Glosario_terminos.md`."
    )


def _footer():
    st.divider()
    st.caption(
        "Producto 1 — Levantamiento de información sobre estándares de sostenibilidad "
        "para vivienda rural (Res. 0194/2025) · v0.3"
    )


# Wrap pages to add footer
def _page_m1():
    st.title(TITULO_PRINCIPAL)
    page_m1()
    _footer()

def _page_m2():
    st.title(TITULO_PRINCIPAL)
    page_m2()
    _footer()

def _page_tutorial():
    page_tutorial()
    _footer()


# ============================================================
# Navegación multi-página (cada página tiene su propio sidebar)
# ============================================================
pg = st.navigation([
    st.Page(_page_m1, title="M1 · Estándares de sostenibilidad", url_path="m1"),
    st.Page(_page_m2, title="M2 · Casos de éxito", url_path="m2"),
    st.Page(_page_tutorial, title="Tutorial M1", url_path="tutorial"),
])
pg.run()
