"""
Script Fase 2 + Fase 3: Enriquecer celdas existentes de la Matriz de Estándares
con datos de contextualización y verificación cruzada.
"""
import csv
import os

DOCS = os.path.join(os.path.dirname(__file__), "..", "docs")
MATRIZ = os.path.join(DOCS, "F0-Matriz_estandares_sostenibilidad.csv")

# Read
with open(MATRIZ, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

col_id = header.index("ID")
col_desc = header.index("Descripcion")
col_param = header.index("Parametro_indicador")
col_corresp = header.index("Correspondencia_cruzada")
col_obs = -1  # no hay columna observaciones, usamos Descripcion y Correspondencia

# --- FASE 2: Contextualización ---

enrichments = {
    # CONPES 3934 - metas de materiales
    "EC-2": {
        "desc_append": ". CONPES 3934: tasa reciclaje materiales construccion CO es solo 2% (meta potencial 50%); 2.28 kg materiales/USD PIB (2.8x mayor que OCDE)",
        "param_append": "; Meta: aumentar tasa reciclaje construccion de 2% a 50%",
    },
    "EC-1": {
        "desc_append": ". CONPES 3934: 91.5M ton materiales construccion/ano; 7.4M ton escombros (7%); necesidad de eco-diseno para reducir consumo",
    },
    "A-R-1": {
        "corresp_append": "; CONPES 3934 meta reciclaje materiales",
    },

    # PROURE Res. 41286/2016 - metas sector residencial
    "D1285-1": {
        "desc_append": ". PROURE 2017-2022: meta ahorro sector residencial 56.121 TJ (0.73% del total nacional)",
        "param_append": "; PROURE: 56.121 TJ ahorro residencial",
    },
    "MA-02": {
        "corresp_append": "; PROURE Res.41286/2016 meta residencial",
    },

    # NDC 2020 - meta edificaciones
    "A-EM-5": {
        "desc_append": ". NDC 2020: Colombia compromete reduccion 176 Mt CO2eq a 2030; sector vivienda incluido; edificaciones nuevas deben ser bajas en carbono",
        "param_append": "; NDC: 176 Mt CO2eq reduccion a 2030",
    },
    "L1931-1": {
        "desc_append": ". NDC 2020: reduccion 176 Mt CO2eq a 2030 todos los sectores incluyendo vivienda",
        "corresp_append": "; NDC 2020",
    },

    # Estrategia 2050 - edificaciones neto cero
    "A-EM-8": {
        "desc_append": ". E2050: 100% edificaciones nuevas Net Zero a partir de 2030; existentes Net Zero a 2050 (WorldGBC). 75% RCD aprovechables en peso total materiales",
        "param_append": "; E2050: 100% nuevas Net Zero 2030; 75% RCD aprovechable",
        "corresp_append": "; E2050 Estrategia Climatica LP",
    },
    "A-R-4": {
        "desc_append": ". E2050: meta 75% de RCD aprovechables en peso total de materiales usados en nuevas edificaciones",
        "param_append": "; E2050: 75% RCD aprovechable",
    },

    # Ley 1955/2019 PND - VIS sostenible
    "D1467-1": {
        "desc_append": ". PND 2018-2022 Ley 1955/2019 Art. 85: VIS debe cumplir estandares de calidad en diseno urbanistico; arquitectonico y de construccion sostenible",
        "corresp_append": "; Ley 1955/2019 Art.85",
    },

    # Res. 196/2020 UPME - procedimiento incentivos
    "L1715-1": {
        "desc_append": ". Res. 196/2020 UPME: establece requisitos y procedimiento para acceder a beneficios tributarios de eficiencia energetica (IVA y renta). Requiere certificacion UPME",
        "corresp_append": "; Res.196/2020 UPME procedimiento",
    },
    "L1819-1": {
        "corresp_append": "; Res.196/2020 UPME procedimiento acceso",
    },

    # --- FASE 3: Verificación cruzada ---

    # Decreto 3930/2010 - verificar agua
    "MW-06": {
        "corresp_append": "; Decreto 3930/2010 (vertimientos; control aguas residuales)",
    },
    "MW-07": {
        "corresp_append": "; Decreto 3930/2010 (vertimientos)",
    },
    "A-A-5": {
        "corresp_append": "; Decreto 3930/2010 (control vertimientos en obra)",
    },

    # Res. 0831/2020 - MRV emisiones
    "A-EM-1": {
        "corresp_append": "; Res.0831/2020 (MRV acciones mitigacion)",
    },

    # Ley 1333/2009 - sanciones ambientales
    "R0472-1": {
        "corresp_append": "; Ley 1333/2009 (procedimiento sancionatorio ambiental para incumplimiento)",
    },
    "D948-1": {
        "corresp_append": "; Ley 1333/2009 (sanciones por contaminacion atmosferica)",
    },

    # CONPES 3934 - verificar circularidad
    "A-M-1": {
        "corresp_append": "; CONPES 3934 (Crecimiento Verde 2030)",
    },
    "A-M-2": {
        "corresp_append": "; CONPES 3934; Estrategia Economia Circular MADS",
    },
}

count = 0
for row in rows:
    id_val = row[col_id].strip()
    if id_val in enrichments:
        e = enrichments[id_val]

        if "desc_append" in e:
            row[col_desc] = row[col_desc].rstrip() + e["desc_append"]
            count += 1

        if "param_append" in e:
            row[col_param] = row[col_param].rstrip() + e["param_append"]
            count += 1

        if "corresp_append" in e:
            row[col_corresp] = row[col_corresp].rstrip() + e["corresp_append"]
            count += 1

# Write
with open(MATRIZ, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Celdas enriquecidas: {count}")
print(f"Filas afectadas: {len(enrichments)}")
print(f"Total filas en matriz: {len(rows)}")
