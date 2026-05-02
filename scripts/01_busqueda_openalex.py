"""
Script 1: Búsqueda automática en OpenAlex
==========================================
Ejecuta ecuaciones de búsqueda en OpenAlex (API gratuita, sin credenciales)
y guarda resultados como CSV listo para revisar.

OpenAlex indexa ~250 millones de trabajos académicos incluyendo Scopus,
PubMed, Crossref, SciELO, Redalyc y repositorios institucionales.

Uso:
    python 01_busqueda_openalex.py

Salida:
    resultados/openalex_YYYY-MM-DD.csv
"""

import requests
import pandas as pd
from datetime import date
import os
import time

# --- CONFIGURACIÓN ---

# Carpeta de salida
SALIDA = os.path.join(os.path.dirname(__file__), "..", "resultados")
os.makedirs(SALIDA, exist_ok=True)

# Correo para API cortesía (OpenAlex pide un email para priorizar requests)
EMAIL = "anamariamorenob@gmail.com"

# Ecuaciones de búsqueda adaptadas a OpenAlex
# OpenAlex usa búsqueda por conceptos + filtros, no booleanas puras
# Cada entrada: (id_busqueda, términos, filtro_clima_region, filtro_año)

BUSQUEDAS = [
    # E1 — Bioclimática pasiva
    ("E1-C1", "bioclimatic design rural housing tropical humid", "Colombia OR Pacific OR Caribbean", 2015),
    ("E1-C2", "passive cooling thermal mass rural housing arid", "Colombia OR Guajira OR Tatacoa", 2015),
    ("E1-C3", "bioclimatic design rural housing temperate Andean", "Colombia OR coffee region", 2015),
    ("E1-C4", "passive heating thermal insulation rural housing highland", "Colombia OR Andes OR paramo", 2015),

    # E2 — Eficiencia energética activa
    ("E2-C1", "energy efficiency photovoltaic rural housing tropical", "Colombia OR off-grid", 2015),
    ("E2-C2", "solar energy rural housing arid semi-arid", "Colombia OR Guajira", 2015),
    ("E2-C3", "energy efficiency improved cookstove rural", "Colombia OR Andean", 2015),
    ("E2-C4", "efficient heating biomass stove solar thermal highland", "Colombia OR Andes", 2015),

    # E3 — Eficiencia hídrica
    ("E3-C1", "rainwater harvesting rural housing tropical humid", "Colombia OR Latin America", 2015),
    ("E3-C2", "rainwater harvesting water storage arid rural", "Colombia OR Guajira OR fog harvesting", 2015),
    ("E3-C3", "rainwater harvesting greywater rural temperate", "Colombia OR Andean", 2015),
    ("E3-C4", "water management rural housing highland cold", "Colombia OR Andes OR paramo", 2015),

    # E4 — Materiales sostenibles
    ("E4-ALL", "sustainable materials rural housing bamboo rammed earth adobe", "Colombia OR Latin America", 2015),
    ("E4-VER", "bahareque guadua tapia vernacular architecture", "Colombia", 2000),

    # E5 — Metodologías
    ("E5-ALL", "site analysis hygrothermal simulation rural housing tropical", "Colombia OR Latin America", 2015),
]

# Máximo de resultados por búsqueda
MAX_RESULTADOS = 50


def buscar_openalex(terminos: str, region: str, desde_año: int) -> list:
    """Ejecuta una búsqueda en OpenAlex y devuelve lista de resultados."""

    # Construir query
    search_query = f"{terminos} {region}"

    url = "https://api.openalex.org/works"
    params = {
        "search": search_query,
        "filter": f"from_publication_date:{desde_año}-01-01",
        "per_page": MAX_RESULTADOS,
        "sort": "relevance_score:desc",
        "mailto": EMAIL
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except Exception as e:
        print(f"  !! Error: {e}")
        return []


def extraer_datos(work: dict) -> dict:
    """Extrae los campos relevantes de un resultado de OpenAlex."""

    # Autores
    autores = "; ".join([
        a.get("author", {}).get("display_name", "?")
        for a in work.get("authorships", [])[:5]
    ])

    # Fuente (revista/repo)
    source = work.get("primary_location", {})
    if source:
        source_name = source.get("source", {}).get("display_name", "") if source.get("source") else ""
    else:
        source_name = ""

    # Conceptos/temas
    conceptos = "; ".join([
        c.get("display_name", "")
        for c in work.get("concepts", [])[:8]
    ])

    # País de instituciones
    paises = set()
    for a in work.get("authorships", []):
        for inst in a.get("institutions", []):
            cc = inst.get("country_code", "")
            if cc:
                paises.add(cc)

    origen_co = "si" if "CO" in paises else "no"

    return {
        "openalex_id": work.get("id", ""),
        "doi": work.get("doi", ""),
        "titulo": work.get("title", ""),
        "autores": autores,
        "año": work.get("publication_year", ""),
        "revista_fuente": source_name,
        "tipo": work.get("type", ""),
        "idioma": work.get("language", ""),
        "citaciones": work.get("cited_by_count", 0),
        "acceso_abierto": work.get("open_access", {}).get("is_oa", False),
        "url_pdf": work.get("open_access", {}).get("oa_url", ""),
        "resumen": (work.get("abstract_inverted_index") or "ver OpenAlex"),
        "conceptos": conceptos,
        "paises_instituciones": "; ".join(sorted(paises)),
        "origen_CO": origen_co,
    }


def main():
    print("=" * 60)
    print("BÚSQUEDA AUTOMÁTICA EN OPENALEX")
    print(f"Fecha: {date.today()}")
    print(f"Ecuaciones a ejecutar: {len(BUSQUEDAS)}")
    print("=" * 60)

    todos = []
    registro = []

    for id_busq, terminos, region, desde in BUSQUEDAS:
        print(f"\n>>> {id_busq}: {terminos[:60]}...")
        resultados = buscar_openalex(terminos, region, desde)
        n_brutos = len(resultados)
        print(f"   -> {n_brutos} resultados")

        for r in resultados:
            datos = extraer_datos(r)
            datos["id_busqueda"] = id_busq
            todos.append(datos)

        registro.append({
            "id_busqueda": id_busq,
            "terminos": terminos,
            "region": region,
            "desde_año": desde,
            "n_resultados": n_brutos,
            "fecha": str(date.today())
        })

        time.sleep(0.5)  # Cortesía con la API

    # Guardar resultados
    df = pd.DataFrame(todos)

    # Deduplicar por DOI
    n_antes = len(df)
    df = df.drop_duplicates(subset=["doi"], keep="first")
    n_despues = len(df)
    print(f"\nTotal: {n_antes} brutos -> {n_despues} unicos (deduplicados por DOI)")

    # Contar colombianos
    n_co = len(df[df["origen_CO"] == "si"])
    pct_co = (n_co / n_despues * 100) if n_despues > 0 else 0
    print(f"Origen Colombia: {n_co} ({pct_co:.0f}%)")

    # Guardar
    archivo = os.path.join(SALIDA, f"openalex_{date.today()}.csv")
    df.to_csv(archivo, index=False, encoding="utf-8-sig")
    print(f"\nOK: Resultados guardados en: {archivo}")

    # Guardar registro de búsquedas
    df_reg = pd.DataFrame(registro)
    archivo_reg = os.path.join(SALIDA, f"registro_openalex_{date.today()}.csv")
    df_reg.to_csv(archivo_reg, index=False, encoding="utf-8-sig")
    print(f"OK: Registro guardado en: {archivo_reg}")

    # Resumen por búsqueda
    print("\n" + "=" * 60)
    print("RESUMEN POR BÚSQUEDA")
    print("=" * 60)
    for _, row in df_reg.iterrows():
        print(f"  {row['id_busqueda']:8s} → {row['n_resultados']:3d} resultados")


if __name__ == "__main__":
    main()
