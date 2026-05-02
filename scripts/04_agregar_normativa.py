"""
Script para agregar filas de normativa complementaria a la Matriz de Estándares.
"""
import csv
import os

DOCS = os.path.join(os.path.dirname(__file__), "..", "docs")
MATRIZ = os.path.join(DOCS, "F0-Matriz_estandares_sostenibilidad.csv")

new_rows = [
    # SUDS - Guia MVCT/DNP 2022
    ["SUDS-MVCT","SUDS-1","Captacion agua lluvia escala vivienda","Aprovechar agua lluvia captada en cubiertas para usos no potables: riego; aseo; descarga sanitarios","criterio_ambiental","diseno","","","P","","Reduce acarreo agua mujeres/ninas en rural","","si","todos","S4 S5","obligatorio","minimo","m3/ano captado","Res.0194:MW-08; Res.0534:A-A-3; CEELA:C12"],
    ["SUDS-MVCT","SUDS-2","Jardin de lluvia / jardin microcuenca","Depresion vegetada que recibe escorrentia; permite infiltracion y remocion contaminantes","criterio_ambiental","diseno","","","P","","","","si","calido_humedo templado","Exterior","obligatorio","minimo","m2 jardin / m2 impermeabilizado","Res.0534:A-SE-1"],
    ["SUDS-MVCT","SUDS-3","Pozo de infiltracion","Estructura subterranea para infiltrar agua lluvia al suelo; reduce escorrentia","criterio_ambiental","diseno","","","P","","","","si","todos","Exterior","obligatorio","minimo","m3 infiltrado","Res.0534:A-SE-1"],
    ["SUDS-MVCT","SUDS-4","Cisterna / aljibe de almacenamiento pluvial","Tanque sobre suelo o enterrado para almacenar agua lluvia; uso diferido","criterio_ambiental","diseno","","","P","","Reduce acarreo agua; disponible para mujer rural","","si","calido_seco todos","S5","obligatorio","minimo","m3 almacenamiento","Res.0194:MW-08; Ley.2462:L-F03"],
    ["SUDS-MVCT","SUDS-5","Techos verdes como SUDS","Cubierta verde que retiene agua lluvia; reduce escorrentia y efecto isla de calor","criterio_ambiental","diseno","P","","P","","","","condicional","todos","S4","obligatorio","deseable","% retencion; Valor U","Res.0194:MP-12; Res.0534:A-SE-1"],
    ["SUDS-MVCT","SUDS-6","Pavimentos permeables","Superficies que permiten infiltracion directa al suelo","criterio_ambiental","diseno","","","P","","","","condicional","todos","Exterior","obligatorio","deseable","% permeabilidad","Res.0534:A-SE-1"],

    # Economia Circular - MADS 2019
    ["EC-MADS","EC-1","Eco-diseno en productos y estructuras de construccion","Disenar usando menos materiales; modularidad; desensamblaje","criterio_ambiental","diseno","","","","P","","","si","todos","S2 S3","voluntario","na","% reduccion material","Res.0534:A-R-2; A-M-1"],
    ["EC-MADS","EC-2","Aprovechamiento de RCD en obra nueva","Incorporar material reciclado de demoliciones en nueva construccion (agregados; concreto reciclado)","criterio_ambiental","construccion","","","","P","","","si","todos","S1 S2","voluntario","na","% RCD aprovechado","Res.0534:A-R-1; A-R-4"],
    ["EC-MADS","EC-3","Simbiosis industrial en materiales de construccion","Uso de subproductos de otros sectores como insumo constructivo (escoria; cenizas; plastico PET)","criterio_ambiental","extraccion/manufactura","","","","P","","","si","todos","S2 S3","voluntario","na","% material alternativo","Res.0534:A-R-1"],
    ["EC-MADS","EC-4","Certificaciones de construccion sostenible","LEED; BREEAM; EDGE; CASA Colombia; Sello Ambiental Colombiano como verificadores","criterio_ambiental","operacion","T","T","T","T","","","condicional","todos","todos","voluntario","na","Tipo certificacion","Res.0534:A-M-1"],

    # Decreto 1285/2015
    ["D1285","D1285-1","Porcentajes obligatorios de ahorro agua y energia","Lineamiento base que dio origen a Res. 0549/2015 y luego a Res. 0194/2025","criterio_ambiental","operacion","","P","P","","","","si","todos","S5","obligatorio","minimo","% ahorro por clima y tipologia","Res.0194:Tablas 10-11"],

    # Decreto 1467/2019
    ["D1467","D1467-1","VIS debe cumplir estandares de construccion sostenible","Ley 1955/2019 Art. 85: VIS cumple estandares de calidad en diseno y construccion sostenible","criterio_ambiental","todas","T","T","T","T","","","si","todos","todos","obligatorio","na","","Res.0194; Res.0534"],

    # Decreto 1727/2021 - Ecobertura
    ["D1727","D1727-1","Subsidio adicional por sostenibilidad (Ecobertura)","Cobertura adicional 10 SMLV en tasa de interes para vivienda No VIS con criterios de sostenibilidad","criterio_economico","operacion","T","T","T","T","","","condicional","todos","na","voluntario","na","SMLV adicionales","Res.0534:E-CI-1"],

    # Ley 1715/2014
    ["L1715","L1715-1","Incentivos tributarios para FNCE en vivienda","Exclusion IVA y deduccion renta por inversion en energia solar FV; solar termica; eolica; biomasa","criterio_economico","operacion","","P","","","","","si","todos","S5","obligatorio","na","% deduccion renta; exclusion IVA","Res.0534:A-EM-8; CEELA:C14"],

    # Ley 373/1997
    ["L373","L373-1","Programa uso eficiente y ahorro del agua","Obliga a entidades a implementar programas de ahorro de agua; incluye captacion pluvial y reuso","criterio_ambiental","operacion","","","P","","Reduce acarreo agua en rural","","si","todos","S5","obligatorio","na","","Res.0194:MW-01 a MW-10; CEELA:C12"],

    # Ley 1931/2018
    ["L1931","L1931-1","Medidas de mitigacion y adaptacion en vivienda","Directrices para gestion cambio climatico en sector vivienda; PIGCCS y PIGCCT","criterio_ambiental","todas","T","T","T","T","","","si","todos","na","obligatorio","na","Meta reduccion GEI","Res.0534:A-EM-5; A-EM-8"],

    # Res. 0472/2017 + 1257/2021
    ["R0472","R0472-1","Gestion integral de Residuos de Construccion y Demolicion","Aplica a todas las personas que generen; recolecten; transporten; aprovechen y dispongan RCD","criterio_ambiental","construccion","","","","P","","","si","todos","na","obligatorio","minimo","% aprovechamiento RCD","Res.0534:A-R-4; A-R-6"],

    # Res. 0330/2017 RAS (criterios clave para rural)
    ["RAS","RAS-1","Sistemas de acueducto rural","Requisitos tecnicos para diseno; construccion y operacion de sistemas de agua potable rural","criterio_ambiental","diseno","","","P","","Acceso agua potable reduce acarreo mujeres","","si","todos","S5","obligatorio","minimo","l/hab/dia; presion minima","Res.0534:A-A-3; CEELA:C12"],
    ["RAS","RAS-2","Sistemas de alcantarillado y saneamiento rural","Requisitos tecnicos para tratamiento de aguas residuales en zona rural","criterio_ambiental","diseno","","","P","","","","si","todos","S5","obligatorio","minimo","DBO5; SST; remocion %","Res.0194:MW-06; MW-07"],
    ["RAS","RAS-3","Sistemas de manejo de aguas lluvias","Requisitos tecnicos para drenaje pluvial; incluye SUDS","criterio_ambiental","diseno","","","P","","","","si","todos","Exterior","obligatorio","minimo","Caudal diseno; periodo retorno","SUDS-MVCT:SUDS-1 a SUDS-6; Res.0534:A-SE-1"],

    # Res. 0541/1994
    ["R0541","R0541-1","Manejo de escombros y materiales de construccion","Regula cargue; descargue; transporte; almacenamiento y disposicion de escombros y materiales","criterio_ambiental","construccion","","","","C","","","si","todos","na","obligatorio","minimo","","Res.0534:A-R-4"],

    # Decreto 948/1995
    ["D948","D948-1","Control contaminacion atmosferica en obra","Mallas protectoras en construccion; control material particulado; prevencion emisiones","criterio_ambiental","construccion","","","","C","","","si","todos","na","obligatorio","minimo","","Res.0534:A-EM-7"],

    # Decreto 1443/2014 - SG-SST
    ["D1443","D1443-1","Sistema de Gestion de Seguridad y Salud en el Trabajo","Buenas practicas; materiales de calidad; prevencion accidentes y enfermedades en construccion","criterio_social","construccion","T","T","T","T","","Seguridad trabajadores rurales","si","todos","na","obligatorio","minimo","","Res.0534:S-H-2"],

    # Ley 1819/2016
    ["L1819","L1819-1","Beneficios tributarios FNCE y carbono neutro","Exclusion IVA en equipos y tecnologias con beneficio ambiental; no causacion impuesto carbono","criterio_economico","operacion","","P","","","","","si","todos","S5","obligatorio","na","% exclusion IVA","Res.0534:A-EM-8; CEELA:C14; L1715:L1715-1"],
]

# Read existing
with open(MATRIZ, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

# Append
for row in new_rows:
    rows.append(row)

# Write
with open(MATRIZ, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Filas anadidas: {len(new_rows)}")
print(f"Total filas en matriz: {len(rows)}")

# Count by reference
from collections import Counter
refs = Counter(r[0] for r in rows)
print("\nPor referencia:")
for ref, n in refs.most_common():
    print(f"  {ref:15s} {n:3d}")
