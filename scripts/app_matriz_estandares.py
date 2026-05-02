"""
App interactiva — Matrices del Producto 1 (Sostenibilidad vivienda rural)
=========================================================================
Tab 1: Matriz M1 — Estándares de Sostenibilidad (lectura)
Tab 2: Matriz M2 — Casos de éxito (lectura + validación con write-back)

Uso:
    streamlit run scripts/app_matriz_estandares.py --server.port 8504
"""

import streamlit as st
import pandas as pd
import portalocker
import os
import sys
import subprocess
from datetime import date

# --- Configuración ---
st.set_page_config(
    page_title="Matrices Sostenibilidad — Vivienda Rural",
    page_icon="🏠",
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
        "Criterio_medida": "Criterio/Medida",
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
                  "Fuente_principal", "Subsistemas"]:
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

# --- Título ---
st.title("Matrices del Producto 1 — Sostenibilidad Vivienda Rural")
st.caption("Guía técnica · Res. 0194/2025 · 4 climas de Colombia")

tab_m1, tab_m2 = st.tabs(["📋 M1 · Estándares de sostenibilidad", "📍 M2 · Casos de éxito"])


# ============================================================
# TAB M1 — Estándares
# ============================================================
with tab_m1:
    df = cargar_m1()
    st.subheader(f"Matriz M1 — {len(df)} criterios de {df['Referencia'].nunique()} fuentes normativas")
    st.divider()

    # Filtros sidebar (solo activos en este tab vía expander)
    with st.expander("Filtros M1", expanded=False):
        c1, c2, c3 = st.columns(3)
        with c1:
            referencias = ["Todas"] + sorted(df["Referencia"].unique().tolist())
            ref_sel = st.multiselect("Referencia normativa", referencias, default=["Todas"])
            eje_opciones = ["Todos", "E1 Bioclimática", "E2 Energía", "E3 Agua", "E4 Materiales"]
            eje_sel = st.selectbox("Eje de sostenibilidad", eje_opciones)
            rel_opciones = ["Cualquiera", "Principal", "Complementario", "Transversal"]
            rel_sel = st.selectbox("Tipo de relación con el eje", rel_opciones)
        with c2:
            climas_m1 = ["Todos", "frio", "templado", "calido_seco", "calido_humedo"]
            clima_sel = st.selectbox("Clima", climas_m1)
            subsistemas = ["Todos", "Cimentación", "Estructura", "Envolvente", "Cubierta",
                           "Instalaciones", "Acabados y complementos", "Exterior"]
            sub_sel = st.selectbox("Subsistema", subsistemas)
            tipos = ["Todos"] + sorted(df["Tipo"].unique().tolist())
            tipo_sel = st.selectbox("Tipo de criterio", tipos)
        with c3:
            caracteres = ["Todos"] + sorted(df["Carácter legal"].unique().tolist())
            car_sel = st.selectbox("Carácter legal", caracteres)
            rural_opciones = ["Todos", "si", "condicional", "no"]
            rural_sel = st.selectbox("Aplica vivienda rural", rural_opciones)
            etapas = ["Todas"] + sorted(df["Etapa del ciclo de vida"].unique().tolist())
            etapa_sel = st.selectbox("Etapa del ciclo de vida", etapas)

        c4, c5 = st.columns(2)
        with c4:
            ley2462_sel = st.checkbox("Solo con conexión Ley 2462 (género/inclusión)")
            notas_sel = st.checkbox("Solo con notas de contexto rural")
        with c5:
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
        filtrado = filtrado[filtrado["Tipo"] == tipo_sel]
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
            filtrado["Criterio/Medida"].str.contains(busqueda, case=False, na=False) |
            filtrado["Descripción"].str.contains(busqueda, case=False, na=False) |
            filtrado["ID"].str.contains(busqueda, case=False, na=False)
        )
        filtrado = filtrado[mask]

    st.subheader(f"Resultados: {len(filtrado)} de {len(df)} criterios")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Obligatorios", len(filtrado[filtrado["Carácter legal"] == "obligatorio"]))
    with col2:
        st.metric("Con Ley 2462", len(filtrado[filtrado["Ref_Ley2462"] != ""]))
    with col3:
        st.metric("Aplican rural", len(filtrado[filtrado["Aplica vivienda rural"] == "si"]))
    with col4:
        st.metric("Fuentes", filtrado["Referencia"].nunique())

    cols_default = ["ID", "Referencia", "Criterio/Medida", "Tipo",
                    "E1 Bioclimática", "E2 Energía", "E3 Agua", "E4 Materiales",
                    "Clima", "Aplica vivienda rural", "Carácter legal", "Ref_Ley2462"]
    cols_mostrar = st.multiselect("Columnas a mostrar", df.columns.tolist(), default=cols_default)
    if cols_mostrar:
        st.dataframe(filtrado[cols_mostrar], width='stretch', height=500)


# ============================================================
# TAB M2 — Casos de éxito
# ============================================================
with tab_m2:
    df_m2 = cargar_m2()
    df_m1 = cargar_m1()

    st.subheader(f"Matriz M2 — {len(df_m2)} casos compilados")

    if READ_ONLY:
        st.info("🔒 Modo solo lectura. La validación/descarte de casos se hace en el entorno local de la responsable del Producto 1.")
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
    m1.metric("⏳ Pendientes", n_pend)
    m2.metric("✅ Aceptados", n_acep)
    m3.metric("❌ Descartados", n_desc)

    # Heatmap cobertura
    with st.expander("📊 Cobertura clima × sistema (solo aceptados)", expanded=False):
        aceptados = df_m2[df_m2["Estado_validacion"] == "aceptado"]
        if len(aceptados) == 0:
            st.info("Aún no hay casos aceptados.")
        else:
            pivot = pd.crosstab(aceptados["Clima_TdR"], aceptados["Sistema_constructivo"])
            st.dataframe(pivot, width='stretch')
            st.caption("Meta mínima: ≥2 casos por clima · Meta ideal: ≥1 caso por (clima × sistema)")

    st.divider()

    # Filtros
    fc1, fc2, fc3, fc4 = st.columns(4)
    with fc1:
        estado_filtro = st.selectbox(
            "Mostrar",
            ["Pendientes", "Aceptados", "Descartados", "Todos"],
            index=0
        )
    with fc2:
        clima_filt = st.multiselect("Clima TdR", CLIMAS, default=[])
    with fc3:
        tipos_unicos = sorted([t for t in df_m2["Tipo"].unique() if t])
        tipo_filt = st.multiselect("Tipo", tipos_unicos, default=[])
    with fc4:
        sistemas_unicos = sorted([s for s in df_m2["Sistema_constructivo"].unique() if s])
        sis_filt = st.multiselect("Sistema constructivo", sistemas_unicos, default=[])

    # Aplicar filtros
    f = df_m2.copy()
    estado_map = {
        "Pendientes": "pendiente_revision",
        "Aceptados": "aceptado",
        "Descartados": "descartado",
    }
    if estado_filtro != "Todos":
        f = f[f["Estado_validacion"] == estado_map[estado_filtro]]
    if clima_filt:
        f = f[f["Clima_TdR"].isin(clima_filt)]
    if tipo_filt:
        f = f[f["Tipo"].isin(tipo_filt)]
    if sis_filt:
        f = f[f["Sistema_constructivo"].isin(sis_filt)]

    st.markdown(f"**{len(f)} casos** con los filtros actuales")

    if len(f) == 0:
        st.info("No hay casos con los filtros seleccionados.")
    else:
        # Tarjetas
        for _, row in f.iterrows():
            estado = row["Estado_validacion"]
            icono = {"pendiente_revision": "⏳", "aceptado": "✅", "descartado": "❌"}.get(estado, "❓")
            es_pendiente = estado == "pendiente_revision"
            es_editable = es_pendiente and not READ_ONLY
            cid = row["ID"]

            with st.container(border=True):
                # Header
                head1, head2 = st.columns([4, 1])
                with head1:
                    st.markdown(f"### {icono} {cid} · {row['Nombre_proyecto']}")
                    st.caption(
                        f"{row['Año']} · {row['Ubicacion_depto']}"
                        + (f" · {row['Ubicacion_municipio']}" if row['Ubicacion_municipio'] else "")
                        + (f" · {row['Ubicacion_vereda']}" if row['Ubicacion_vereda'] else "")
                    )
                with head2:
                    if estado != "pendiente_revision":
                        st.caption(f"por **{row['Validado_por']}** el {row['Fecha_validacion']}")
                        if estado == "descartado" and row["Motivo_descarte"]:
                            st.caption(f"motivo: _{row['Motivo_descarte']}_")

                # Badges prominentes: tipo + clima + sistema
                clima = row["Clima_TdR"] or "desconocido"
                clima_c = CLIMA_COLOR.get(clima, "#9E9E9E")
                tipo = row["Tipo"] or "desconocido"
                tipo_c = TIPO_COLOR.get(tipo, "#9E9E9E")
                tipo_icono = {"vernaculo": "🏛️", "contemporaneo": "🏗️", "mixto": "🔀"}.get(tipo, "•")
                koppen = f" ({row['Subtipo_Koppen']})" if row['Subtipo_Koppen'] else ""
                badge_html = (
                    f'<div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap; margin:8px 0;">'
                    f'<span style="background:{tipo_c}; color:white; padding:6px 14px; border-radius:6px; '
                    f'font-size:1.1rem; font-weight:600;">{tipo_icono} {tipo.upper()}</span>'
                    f'<span style="background:{clima_c}; color:white; padding:6px 14px; border-radius:6px; '
                    f'font-size:1.1rem; font-weight:600;">🌡️ {clima.upper()}{koppen}</span>'
                    f'<span style="background:#455A64; color:white; padding:6px 14px; border-radius:6px; '
                    f'font-size:1.1rem; font-weight:600;">🧱 {row["Sistema_constructivo"]}</span>'
                    f'</div>'
                )
                st.markdown(badge_html, unsafe_allow_html=True)

                # Subsistemas (editable si pendiente)
                subs_actuales = [s.strip() for s in (row["Subsistemas"] or "").split(";") if s.strip()]
                if es_editable:
                    st.multiselect(
                        "🧱 Subsistemas que toca el caso",
                        SUBSISTEMAS,
                        default=subs_actuales or ["integral"],
                        key=f"edit_{cid}_Subsistemas",
                    )
                else:
                    st.markdown(f"🧱 **Subsistemas:** {', '.join(subs_actuales) or '_sin definir_'}")

                # Estrategias por eje (read-only — vienen del fichaje)
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

                # Estándares M1 (editable si pendiente)
                st.markdown("---")
                st.markdown("🔗 **Normativa / estándares M1 que materializa**")
                if es_editable:
                    st.text_input(
                        "IDs separados por ; (ej: MP-14; MA-22; SUDS-3)",
                        value=row["Estandares_ref"],
                        key=f"edit_{cid}_Estandares_ref",
                        label_visibility="collapsed",
                        placeholder="MP-14; MA-22; SUDS-3 ...",
                    )
                    st.text_input(
                        "Cumplimiento observado (desviaciones, parciales)",
                        value=row["Cumplimiento_observado"],
                        key=f"edit_{cid}_Cumplimiento_observado",
                        placeholder="ej: MP-14: muro 35cm vs 40cm requeridos",
                    )
                # Mostrar cruce con M1 si hay IDs
                refs_actuales = [r.strip() for r in (row["Estandares_ref"] or "").split(";") if r.strip()]
                if refs_actuales:
                    cruce = df_m1[df_m1["ID"].isin(refs_actuales)]
                    if len(cruce) > 0:
                        with st.expander(f"Ver detalle de {len(refs_actuales)} estándares cruzados"):
                            st.dataframe(cruce[["ID", "Referencia", "Criterio/Medida"]],
                                         width='stretch')
                            faltantes = set(refs_actuales) - set(cruce["ID"].tolist())
                            if faltantes:
                                st.warning(f"IDs no encontrados en M1: {sorted(faltantes)}")
                    else:
                        st.warning(f"Ningún ID de M1 reconocido: {refs_actuales}")
                if not es_pendiente and row["Cumplimiento_observado"]:
                    st.markdown(f"_Cumplimiento observado:_ {row['Cumplimiento_observado']}")

                # Género e inclusión social (editable si pendiente)
                st.markdown("♀ **Género / inclusión social** (Ley 2462/2025)")
                if es_editable:
                    st.text_area(
                        "Consideraciones de género/inclusión",
                        value=row["Genero_inclusion"],
                        key=f"edit_{cid}_Genero_inclusion",
                        label_visibility="collapsed",
                        placeholder="ej: Cocina con extracción mecánica para reducir exposición de mujeres a humo de leña; baño accesible",
                        height=68,
                    )
                else:
                    st.markdown(row["Genero_inclusion"] or "_no especificado_")

                # Fuente + botón abrir PDF
                st.markdown("---")
                fcol1, fcol2 = st.columns([3, 1])
                with fcol1:
                    if es_editable:
                        st.text_input(
                            "📖 Fuente (incluir página si se conoce)",
                            value=row["Fuente_principal"],
                            key=f"edit_{cid}_Fuente_principal",
                            placeholder='ej: "Hábitat Para La Paz (PUJ, 2021), p. 45"',
                        )
                    else:
                        st.markdown(f"📖 **Fuente:** {row['Fuente_principal']}")
                    st.caption(f"_{row['Tipo_fuente']}_ · verificable: {row['Verificable']}"
                               + (f" · archivo: `{row['Archivo_fuente']}`" if row['Archivo_fuente'] else ""))
                with fcol2:
                    if READ_ONLY:
                        if row["Archivo_fuente"]:
                            st.caption(f"📄 `{row['Archivo_fuente']}`")
                    elif row["Archivo_fuente"]:
                        if st.button("📄 Abrir PDF", key=f"pdf_{cid}",
                                     help=f"Abre {row['Archivo_fuente']} con la app por defecto"):
                            ok, msg = abrir_pdf(row["Archivo_fuente"])
                            if not ok:
                                st.error(f"No se pudo abrir: {msg}")
                    else:
                        st.caption("_sin PDF asignado_")

                if row["Lecciones_aprendidas"]:
                    st.markdown(f"💡 **Lecciones:** {row['Lecciones_aprendidas']}")
                if row["Observaciones"]:
                    st.caption(f"Obs.: {row['Observaciones']}")

                # Botones (ocultos en modo solo lectura del VPS)
                if READ_ONLY:
                    pass
                elif not st.session_state.validador.strip():
                    st.warning("⚠️ Define tu nombre arriba para poder validar/descartar.")
                else:
                    bcol1, bcol2, bcol3, bcol4 = st.columns([1, 1, 2, 4])
                    if es_pendiente:
                        with bcol1:
                            if st.button("✅ Validar", key=f"acc_{cid}", type="primary"):
                                edits = captura_edits(row, "edit")
                                actualizar_caso(cid, "aceptado",
                                                st.session_state.validador, edits=edits)
                                st.rerun()
                        with bcol2:
                            if st.button("❌ Descartar", key=f"desc_{cid}"):
                                st.session_state[f"confirm_desc_{cid}"] = True
                        with bcol3:
                            if st.session_state.get(f"confirm_desc_{cid}"):
                                motivo = st.text_input(
                                    "Motivo del descarte",
                                    key=f"motivo_{cid}",
                                    placeholder="ej: solo conceptual",
                                )
                                if st.button("Confirmar descarte", key=f"conf_desc_{cid}"):
                                    edits = captura_edits(row, "edit")
                                    actualizar_caso(cid, "descartado",
                                                    st.session_state.validador,
                                                    motivo=motivo, edits=edits)
                                    st.session_state.pop(f"confirm_desc_{cid}", None)
                                    st.rerun()
                    else:
                        with bcol1:
                            if st.button("↩ Reactivar", key=f"react_{cid}"):
                                actualizar_caso(cid, "pendiente_revision",
                                                st.session_state.validador)
                                st.rerun()


# --- Footer ---
st.divider()
st.caption(
    "Producto 1 — Levantamiento de información sobre estándares de sostenibilidad "
    "para vivienda rural (Res. 0194/2025) · v0.2"
)
