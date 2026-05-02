"""
Script 2: Análisis de cobertura de la Matriz M1
================================================
Lee F4-Matriz_M1.csv y genera un reporte de:
- Cuántas filas hay por eje × clima
- Qué celdas están vacías (vacíos declarables)
- % de fuentes colombianas
- Distribución por tipo de fuente

Uso:
    python 02_analisis_cobertura_M1.py

Salida:
    resultados/cobertura_M1_YYYY-MM-DD.txt (reporte texto)
    resultados/cobertura_M1_YYYY-MM-DD.csv (tabla cruzada)
"""

import pandas as pd
import os
from datetime import date

# --- CONFIGURACIÓN ---

DOCS = os.path.join(os.path.dirname(__file__), "..", "docs")
M1_PATH = os.path.join(DOCS, "F4-Matriz_M1.csv")
SALIDA = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(SALIDA, exist_ok=True)

EJES = ["E1", "E2", "E3", "E4", "E5"]
CLIMAS = ["frio", "templado", "calido_seco", "calido_humedo", "todos"]
UMBRAL_VACIO = 2  # <2 fuentes = vacío declarable


def main():
    # Leer M1
    if not os.path.exists(M1_PATH):
        print(f"⚠ No se encontró {M1_PATH}")
        return

    df = pd.read_csv(M1_PATH, encoding="utf-8-sig")
    n_total = len(df)

    print("=" * 60)
    print("ANÁLISIS DE COBERTURA — MATRIZ M1")
    print(f"Fecha: {date.today()}")
    print(f"Total filas en M1: {n_total}")
    print("=" * 60)

    if n_total == 0:
        print("⚠ La matriz está vacía. No hay nada que analizar.")
        return

    # --- 1. Tabla cruzada Eje × Clima ---
    print("\n📊 TABLA CRUZADA: Eje × Clima (conteo de filas)")
    print("-" * 50)

    # Expandir filas con clima "todos" a los 4 climas
    df_expandido = df.copy()
    climas_reales = ["frio", "templado", "calido_seco", "calido_humedo"]

    filas_todos = df_expandido[df_expandido["Clima_TdR"] == "todos"]
    filas_especificos = df_expandido[df_expandido["Clima_TdR"] != "todos"]

    expandidas = []
    for _, row in filas_todos.iterrows():
        for c in climas_reales:
            nueva = row.copy()
            nueva["Clima_TdR"] = c
            expandidas.append(nueva)

    if expandidas:
        df_expandido = pd.concat([filas_especificos, pd.DataFrame(expandidas)], ignore_index=True)

    tabla = pd.crosstab(df_expandido["Eje"], df_expandido["Clima_TdR"])

    # Reordenar columnas
    cols_ordenadas = [c for c in climas_reales if c in tabla.columns]
    tabla = tabla.reindex(columns=cols_ordenadas, fill_value=0)

    # Agregar total por eje
    tabla["TOTAL"] = tabla.sum(axis=1)

    print(tabla.to_string())

    # --- 2. Vacíos ---
    print(f"\n🔴 VACÍOS (celdas con <{UMBRAL_VACIO} fuentes)")
    print("-" * 50)

    vacios = []
    for eje in EJES:
        for clima in climas_reales:
            n = tabla.loc[eje, clima] if eje in tabla.index and clima in tabla.columns else 0
            if n < UMBRAL_VACIO:
                vacios.append({"Eje": eje, "Clima": clima, "N_fuentes": n})
                print(f"  ⚠ {eje} × {clima}: {n} fuentes")

    if not vacios:
        print("  ✅ Sin vacíos — todas las celdas tienen ≥2 fuentes")

    # --- 3. % Origen Colombia ---
    print("\n🇨🇴 ORIGEN COLOMBIA")
    print("-" * 50)

    if "Origen_CO" in df.columns:
        n_co = len(df[df["Origen_CO"].str.lower() == "si"])
        pct = (n_co / n_total * 100) if n_total > 0 else 0
        meta = "✅ CUMPLE" if pct >= 60 else "⚠ BAJO META (60%)"
        print(f"  Fuentes CO: {n_co} de {n_total} ({pct:.0f}%) — {meta}")
    else:
        print("  ⚠ Columna 'Origen_CO' no encontrada")

    # --- 4. Distribución por tipo de fuente ---
    print("\n📁 DISTRIBUCIÓN POR TIPO DE FUENTE")
    print("-" * 50)

    if "Tipo_fuente" in df.columns:
        dist = df["Tipo_fuente"].value_counts()
        for tipo, n in dist.items():
            print(f"  {tipo}: {n}")
    else:
        print("  ⚠ Columna 'Tipo_fuente' no encontrada")

    # --- 5. Distribución por tipo de medida ---
    print("\n📐 DISTRIBUCIÓN POR TIPO DE MEDIDA")
    print("-" * 50)

    if "Medida" in df.columns:
        dist_medida = df["Medida"].value_counts()
        for tipo, n in dist_medida.items():
            print(f"  {tipo}: {n}")

    # --- 6. Cobertura Anexo 1 ---
    print("\n📋 COBERTURA ANEXO 1 (columna Medida_Anexo1_ref)")
    print("-" * 50)

    if "Medida_Anexo1_ref" in df.columns:
        con_ref = df["Medida_Anexo1_ref"].notna().sum()
        sin_ref = df["Medida_Anexo1_ref"].isna().sum()
        print(f"  Con referencia Anexo 1: {con_ref}")
        print(f"  Sin referencia (estrategias fuera del Anexo): {sin_ref}")

    # --- 7. Cobertura CEELA ---
    print("\n📋 COBERTURA CEELA (columna Criterio_CEELA_ref)")
    print("-" * 50)

    if "Criterio_CEELA_ref" in df.columns:
        con_ceela = df["Criterio_CEELA_ref"].notna().sum()
        sin_ceela = df["Criterio_CEELA_ref"].isna().sum()
        print(f"  Con referencia CEELA: {con_ceela}")
        print(f"  Sin referencia CEELA: {sin_ceela}")

    # --- Guardar ---
    # Reporte texto
    archivo_txt = os.path.join(SALIDA, f"cobertura_M1_{date.today()}.txt")
    with open(archivo_txt, "w", encoding="utf-8") as f:
        f.write(f"REPORTE DE COBERTURA M1 — {date.today()}\n")
        f.write(f"Total filas: {n_total}\n\n")
        f.write("TABLA CRUZADA Eje × Clima:\n")
        f.write(tabla.to_string())
        f.write(f"\n\nVacíos: {len(vacios)} celdas\n")
        for v in vacios:
            f.write(f"  {v['Eje']} × {v['Clima']}: {v['N_fuentes']} fuentes\n")

    # Tabla cruzada CSV
    archivo_csv = os.path.join(SALIDA, f"cobertura_M1_{date.today()}.csv")
    tabla.to_csv(archivo_csv, encoding="utf-8-sig")

    print(f"\n✅ Reporte guardado en: {archivo_txt}")
    print(f"✅ Tabla cruzada guardada en: {archivo_csv}")


if __name__ == "__main__":
    main()
