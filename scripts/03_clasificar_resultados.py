"""
Script 3: Clasificación semi-automática de resultados
=====================================================
Lee el CSV de resultados de OpenAlex (script 01) y clasifica cada artículo
por eje de sostenibilidad y clima usando el título y conceptos.

Clasificación por REGLAS (sin API de IA) — rápida y gratuita.
Para clasificación más precisa con IA, ver la función clasificar_con_ia().

Uso:
    python 03_clasificar_resultados.py resultados/openalex_2026-04-23.csv

Salida:
    resultados/clasificados_YYYY-MM-DD.csv (con columnas Eje y Clima añadidas)
"""

import pandas as pd
import sys
import os
from datetime import date

# --- REGLAS DE CLASIFICACIÓN ---

# Palabras clave por eje
REGLAS_EJE = {
    "E1": [
        "bioclimatic", "passive", "ventilation", "thermal comfort", "shading",
        "solar orientation", "thermal mass", "night flush", "natural cooling",
        "daylight", "cross ventilation", "bioclimático", "pasivo", "ventilación",
        "confort térmico", "sombra", "inercia térmica", "alero", "orientación solar",
        "vernacular", "vernácula", "bahareque", "tapia", "palafito", "adobe",
    ],
    "E2": [
        "energy efficiency", "photovoltaic", "solar panel", "LED", "lighting",
        "cookstove", "biomass stove", "renewable energy", "off-grid", "micro-hydro",
        "wind turbine", "biogas", "eficiencia energética", "fotovoltaic", "estufa",
        "cocina mejorada", "iluminación", "energía renovable", "biogás",
    ],
    "E3": [
        "rainwater", "water harvesting", "greywater", "water efficiency",
        "water saving", "low-flow", "constructed wetland", "sanitation",
        "captación", "agua lluvia", "aguas grises", "eficiencia hídrica",
        "saneamiento", "bajo consumo", "humedal", "aljibe", "jagüey",
    ],
    "E4": [
        "sustainable material", "embodied energy", "life cycle", "LCA",
        "bamboo", "guadua", "rammed earth", "compressed earth", "recycled",
        "low carbon", "material sostenible", "ciclo de vida", "energía incorporada",
        "tierra comprimida", "reciclado", "huella de carbono", "GWP",
        "madera certificada", "certified timber",
    ],
}

# Palabras clave por clima
REGLAS_CLIMA = {
    "calido_humedo": [
        "hot humid", "tropical humid", "equatorial", "pacific", "caribbean",
        "amazon", "rainfall", "cálido húmedo", "pacífico", "caribe", "chocó",
        "amazonía", "urabá", "buenaventura", "quibdó",
    ],
    "calido_seco": [
        "hot arid", "hot dry", "semi-arid", "arid", "savanna", "desert",
        "cálido seco", "semiárido", "árido", "guajira", "tatacoa", "llanos",
        "chicamocha", "sabana",
    ],
    "templado": [
        "temperate", "subtropical highland", "coffee", "mild", "moderate",
        "templado", "eje cafetero", "medellín", "ibagué", "popayán",
        "antioquia", "caldas", "risaralda", "quindío",
    ],
    "frio": [
        "cold", "highland", "high altitude", "páramo", "altiplano", "alpine",
        "frío", "boyacá", "cundinamarca", "nariño", "pasto", "tunja",
        "bogotá", "sumapaz", "altoandino",
    ],
}


def clasificar_eje(texto: str) -> str:
    """Clasifica un texto en el eje de sostenibilidad más probable."""
    texto_lower = texto.lower()
    scores = {}

    for eje, keywords in REGLAS_EJE.items():
        score = sum(1 for kw in keywords if kw.lower() in texto_lower)
        scores[eje] = score

    max_score = max(scores.values())
    if max_score == 0:
        return ""

    # Devolver el eje con mayor score; si hay empate, devolver todos
    ejes = [e for e, s in scores.items() if s == max_score]
    return "; ".join(ejes)


def clasificar_clima(texto: str) -> str:
    """Clasifica un texto en el clima más probable."""
    texto_lower = texto.lower()
    scores = {}

    for clima, keywords in REGLAS_CLIMA.items():
        score = sum(1 for kw in keywords if kw.lower() in texto_lower)
        scores[clima] = score

    max_score = max(scores.values())
    if max_score == 0:
        return "todos"

    climas = [c for c, s in scores.items() if s == max_score]
    return "; ".join(climas)


def main():
    # Leer archivo de entrada
    if len(sys.argv) < 2:
        # Buscar el más reciente en resultados/
        salida_dir = os.path.join(os.path.dirname(__file__), "..", "resultados")
        archivos = [f for f in os.listdir(salida_dir) if f.startswith("openalex_") and f.endswith(".csv")]
        if not archivos:
            print("⚠ No se encontraron archivos de OpenAlex. Ejecute primero 01_busqueda_openalex.py")
            return
        archivo = os.path.join(salida_dir, sorted(archivos)[-1])
    else:
        archivo = sys.argv[1]

    print(f"📂 Leyendo: {archivo}")
    df = pd.read_csv(archivo, encoding="utf-8-sig")
    n = len(df)
    print(f"   {n} registros")

    # Construir texto para clasificar (título + conceptos)
    df["_texto_clasificar"] = (
        df["titulo"].fillna("") + " " +
        df["conceptos"].fillna("") + " " +
        df["revista_fuente"].fillna("")
    )

    # Clasificar
    print("\n🔄 Clasificando por eje y clima...")
    df["eje_sugerido"] = df["_texto_clasificar"].apply(clasificar_eje)
    df["clima_sugerido"] = df["_texto_clasificar"].apply(clasificar_clima)

    # Limpiar columna auxiliar
    df = df.drop(columns=["_texto_clasificar"])

    # Estadísticas
    print("\n📊 DISTRIBUCIÓN POR EJE SUGERIDO")
    print("-" * 40)
    for eje in ["E1", "E2", "E3", "E4"]:
        n_eje = df["eje_sugerido"].str.contains(eje, na=False).sum()
        print(f"  {eje}: {n_eje} artículos")

    sin_eje = (df["eje_sugerido"] == "").sum()
    print(f"  Sin clasificar: {sin_eje}")

    print("\n📊 DISTRIBUCIÓN POR CLIMA SUGERIDO")
    print("-" * 40)
    for clima in ["frio", "templado", "calido_seco", "calido_humedo", "todos"]:
        n_clima = df["clima_sugerido"].str.contains(clima, na=False).sum()
        print(f"  {clima}: {n_clima} artículos")

    # Colombianos
    n_co = (df["origen_CO"] == "si").sum()
    pct_co = (n_co / n * 100) if n > 0 else 0
    print(f"\n🇨🇴 Origen Colombia: {n_co} ({pct_co:.0f}%)")

    # Guardar
    salida_dir = os.path.join(os.path.dirname(__file__), "..", "resultados")
    archivo_salida = os.path.join(salida_dir, f"clasificados_{date.today()}.csv")
    df.to_csv(archivo_salida, index=False, encoding="utf-8-sig")
    print(f"\n✅ Clasificados guardados en: {archivo_salida}")

    print("\n⚠ IMPORTANTE: la clasificación es SUGERIDA por reglas de palabras clave.")
    print("  Revisar manualmente antes de incorporar a M1.")
    print("  Los artículos 'sin clasificar' requieren lectura humana del resumen.")


if __name__ == "__main__":
    main()
