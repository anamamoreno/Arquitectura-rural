"""
Script para agregar filas de documentos NUEVAS a la Matriz de Estandares.
"""
import csv
import os

DOCS = os.path.join(os.path.dirname(__file__), "..", "docs")
MATRIZ = os.path.join(DOCS, "F0-Matriz_estandares_sostenibilidad.csv")

new_rows = [
    # Guia Sostenibilidad Mejoramientos MVCT - estrategias RURALES
    # Nuevas (no cubiertas aun en la matriz)
    ["GuiaMej-MVCT","GM-E2","Estufas eficientes para vivienda rural","Reemplazo de fogon abierto por estufa eficiente; reduccion PM2.5 y consumo de lena","criterio_ambiental","operacion","","P","","","ENUT 2024-25: 78.7% mujeres cocinan; estufa eficiente reduce tiempo y humo (Ley 2462 Fin 3)","","si","frio templado","S5","obligatorio","minimo","% reduccion PM2.5; kg lena/dia","Res.0534:A-EM-6; CEELA:C07; Ley.2462:L-F03"],
    ["GuiaMej-MVCT","GM-T3","Generacion de biogas domiciliario","Sistema de biodigestor para generacion de biogas a partir de residuos organicos y excretas animales","criterio_ambiental","operacion","","P","","","","","si","todos","S5","voluntario","na","m3 biogas/dia","CEELA:C07; C14"],
    ["GuiaMej-MVCT","GM-T4","Energia eolica a pequena escala","Microturbina eolica para vivienda rural en zonas con vientos sostenidos (Guajira; paramo; altiplano)","criterio_ambiental","operacion","","P","","","","","condicional","calido_seco frio","S5","voluntario","na","kWh/mes","CEELA:C14; Res.0534:A-EM-8"],
    ["GuiaMej-MVCT","GM-M2","Durabilidad y garantias de materiales","Especificar materiales con garantia de durabilidad documentada; reducir reposiciones prematuras","criterio_ambiental","diseno","","","","P","","","si","todos","S2 S3 S4","obligatorio","minimo","Anos de garantia; vida util estimada","Res.0534:A-M-1"],
    ["GuiaMej-MVCT","GM-S1","Mano de obra local en construccion rural","Priorizar contratacion de mano de obra del territorio para transferencia de conocimiento y economia local","criterio_social","construccion","","","","","","Economia local; empleo rural; saberes vernaculos","si","todos","na","obligatorio","minimo","% mano obra local","Ley.2462:L-E01; L-E05; L-F01"],
    ["GuiaMej-MVCT","GM-S2","Compromiso social del constructor","Constructor debe garantizar acompanamiento social; capacitacion a beneficiarios en uso y mantenimiento","criterio_social","construccion","","","","","Capacitacion diferencial por genero","Participacion comunitaria","si","todos","na","obligatorio","minimo","","CEELA:C01; C11; Ley.2462:L-F11"],
    ["GuiaMej-MVCT","GM-S3","Gestion comunitaria resiliente","Conformar y capacitar comite comunitario para mantenimiento y gestion de la vivienda y sus sistemas","criterio_social","operacion","","","","","Liderazgo de mujeres en gestion comunitaria","Participacion comunitaria; autonom.a","si","todos","na","obligatorio","minimo","","CEELA:C11; Ley.2462:L-F11; L-F12"],
    ["GuiaMej-MVCT","GM-A1","Proveeduria local de materiales","Priorizar materiales de origen regional (<300 km) para reducir huella de carbono del transporte","criterio_ambiental","diseno","","","","P","","Economia local","si","todos","S2 S3 S4","obligatorio","deseable","km origen; % materiales locales","Res.0534:A-E-1; A-M-1; CEELA:C03"],

    # PNVISR - Plan Nacional Vivienda Social Rural
    ["PNVISR","PNVISR-1","Enfoque diferencial en vivienda rural","Reconocimiento diferencial de condiciones sociales; culturales; etnicas y territoriales en diseno de VISR","criterio_social","diseno","T","T","T","T","Enfoque diferencial de genero obligatorio","Etnico; discapacidad; victimas conflicto; adulto mayor","si","todos","na","obligatorio","na","","Ley.2462:L-E04; L-E08; L-E12"],
    ["PNVISR","PNVISR-2","Vivienda rural integral; saludable y productiva","Vivienda como unidad que integra habitabilidad; salud; produccion agropecuaria y sostenibilidad","criterio_social","diseno","P","","","","Vivienda como espacio de trabajo productivo femenino","","si","todos","S3","obligatorio","na","","Ley.2462:L-E05; L-E10; L-F06; L-F09"],
    ["PNVISR","PNVISR-3","Acceso a agua potable y saneamiento basico rural","Garantizar acceso a agua y saneamiento en vivienda rural donde no existe infraestructura","criterio_ambiental","diseno","","","P","","Acceso agua reduce acarreo por mujeres","","si","todos","S5","obligatorio","minimo","l/hab/dia","RAS:RAS-1; RAS-2; Res.0194:MW-08; Ley.2462:L-F03"],
    ["PNVISR","PNVISR-4","Subsidio vivienda rural (hasta 70 SMLV + 20 transporte)","Res. 0536/2020: tope subsidio 70 SMLV; 20 SMLV adicionales para transporte en zonas dificil acceso","criterio_economico","diseno","T","T","T","T","","Priorizacion zonas dificil acceso","si","todos","na","obligatorio","na","SMLV","D1467:D1467-1"],

    # Anexo C - Documento de Parametrizacion SFVR
    ["ParamSFVR","PARAM-1","Analisis de asoleacion y orientacion para vivienda rural","Diagrama estereografico con latitud/longitud; radiacion solar directa/difusa; definicion de orientacion optima por clima","criterio_ambiental","diseno","P","","","","","","si","todos","S2 S3","obligatorio","minimo","Orientacion optima por clima","Res.0194:MP-01 a MP-04; Res.0534:S-CT-1"],
    ["ParamSFVR","PARAM-2","Proteccion solar en fachadas y cubiertas rurales","Elementos horizontales y verticales de fachada/cubierta para bloqueo de radiacion; definidos por clima","criterio_ambiental","diseno","P","","","","","","si","templado calido_seco calido_humedo","S3 S4","obligatorio","minimo","ASV; ASH","Res.0194:MP-02 a MP-04; Res.0534:S-CT-1; CEELA:C02"],
    ["ParamSFVR","PARAM-3","Iluminacion natural en vivienda rural","Proporciones de ventanas; claraboyas y repisas de luz para garantizar penetracion de luz natural y ahorro energetico","criterio_ambiental","diseno","P","C","","","","","si","todos","S3","obligatorio","minimo","FLD (%); proporcion ventana","Res.0194:MA-01; Res.0534:S-CL-1"],
    ["ParamSFVR","PARAM-4","Ventilacion natural cruzada en vivienda rural","Aprovechamiento de vientos dominantes; aberturas enfrentadas; efecto chimenea por clima","criterio_ambiental","diseno","P","","","","","","si","templado calido_seco calido_humedo","S3 S4","obligatorio","minimo","ACH; velocidad aire","Res.0194:MP-14; Res.0534:S-A-1; CEELA:C06"],

    # TdR Guia Rural CEELA 2026
    ["TdR-CEELA","TDR-1","Guia de obligatorio cumplimiento para contratistas VISR","La guia sera de obligatorio cumplimiento por el contratista en etapas de estructuracion y ejecucion de proyectos rurales MVCT","criterio_ambiental","todas","T","T","T","T","","","si","todos","todos","obligatorio","na","",""],
    ["TdR-CEELA","TDR-2","Al menos 2 sistemas constructivos por zona climatica","Identificar materiales; estrategias y complementos para minimo 2 sistemas constructivos por clima","criterio_ambiental","diseno","","","","P","","","si","todos","S2","obligatorio","minimo","2 sistemas x 4 climas = 8 minimo",""],

    # Estado Construccion Sostenible 2024 (CCCS)
    ["CCCS-2024","CCCS-1","Estado actual certificaciones sostenibles en CO","EDGE; CASA Colombia; LEED son las 3 certificaciones mas usadas en CO (2024). 93% constructores incorporan criterios ASG","criterio_economico","operacion","T","T","T","T","","","si","todos","na","voluntario","na","% empresas con ASG","Res.0534:A-M-1; EC-MADS:EC-4"],

    # Sentencia T-333/22
    ["ST333","ST333-1","Derecho a vivienda digna como derecho fundamental (jurisprudencia)","Corte Constitucional: vivienda digna incluye habitabilidad; disponibilidad de servicios; accesibilidad; adecuacion cultural","criterio_social","todas","T","T","T","T","Vivienda digna incluye perspectiva de genero","Accesibilidad; adecuacion cultural y etnica","si","todos","todos","obligatorio","na","","Ley.2462:L-E03; Res.0534:S-AC-1"],
]

# Read existing
with open(MATRIZ, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

for row in new_rows:
    rows.append(row)

# Write
with open(MATRIZ, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Filas anadidas: {len(new_rows)}")
print(f"Total filas en matriz: {len(rows)}")

from collections import Counter
refs = Counter(r[0] for r in rows)
print("\nPor referencia:")
for ref, n in refs.most_common():
    print(f"  {ref:15s} {n:3d}")
