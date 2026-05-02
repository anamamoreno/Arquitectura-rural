"""
Script para agregar notas de valor agregado rural a las filas sin notas.
Enfoque: implicación rural + conexión género + vacíos normativos.
"""
import csv
import os

DOCS = os.path.join(os.path.dirname(__file__), "..", "docs")
MATRIZ = os.path.join(DOCS, "F0-Matriz_estandares_sostenibilidad.csv")

# Notas por ID — solo donde hay valor agregado para contexto rural
notas_rurales = {
    # === Res. 0194 — Medidas pasivas ===
    "MP-01": "En vivienda rural de un piso la RVP debe equilibrar luz natural vs. ganancia solar segun clima. En calido humedo priorizar ventanas amplias con proteccion; en frio reducir area vidriada para conservar calor",
    "MP-02": "Aleros perimetrales >80 cm son la estrategia vernacula mas comun en vivienda rural colombiana (Caribe; Pacifico; eje cafetero). Bajo costo; alta efectividad; facil de construir con mano de obra local",
    "MP-03": "Celosias y lamas verticales en fachadas oeste son criticas en calido seco rural (Guajira; Tatacoa). Materiales locales: guadua; bahareque; madera",
    "MP-04": "Combinacion alero + celosia es patron vernaculo del eje cafetero (bahareque con corredor perimetral). Patrimonio PCC UNESCO",
    "MP-05": "Vidrios especiales tienen costo alto para VIS rural (presupuesto 70 SMLV). Alternativa: reducir area vidriada + usar proteccion solar externa",
    "MP-08": "En vivienda rural la cubierta es el elemento con mayor ganancia solar. Aislamiento con materiales locales: paja comprimida (frio); palma (calido humedo); teja de barro (templado)",
    "MP-09": "Muros de tapia (>40 cm) y adobe tienen Valor U naturalmente bajo por su masa termica. En frio andino son la solucion vernacula de aislamiento sin costo adicional",
    "MP-10": "Pintura blanca exterior es la medida mas costo-efectiva para vivienda rural en calido seco y humedo. SRI alto con inversion minima",
    "MP-11": "Cubiertas de zinc sin pintura reflectiva son inhabitables en calido (hasta 70 dB lluvia + 50°C radiacion). Pintura blanca o sobrecubierta de yotojoro (wayuu) reducen hasta 80% la temperatura",
    "MP-12": "Cubierta verde requiere losa — no aplica directamente a vivienda rural con cubierta liviana. Alternativa rural: sobrecubierta vegetal sobre estructura liviana",
    "MP-13": "Inercia termica es la estrategia dominante en vivienda rural andina. Tapia pisada y adobe estabilizan ±3°C la oscilacion diurna. ENUT 2024-25: mujeres pasan 8h53min/dia en vivienda rural — el confort termico las impacta directamente",
    "MP-14": "Ventilacion cruzada es la estrategia bioclimatica mas importante en calido humedo y seco rural. Palafito del Pacifico usa ventilacion inferior; bahareque caribe usa aberturas opuestas. Critico para calidad del aire en cocinas con lena",
    "MP-15": "Night flush funciona en calido seco rural donde la oscilacion termica diurna es >10°C (Tatacoa; Chicamocha; Guajira). Requiere masa termica + aberturas operables",

    # === Res. 0194 — Medidas activas ===
    "MA-01": "Iluminacion natural es critica en vivienda rural donde el acceso a energia electrica puede ser limitado (ZNI). ENUT 2024-25: cocina y zona de lavado requieren iluminacion adecuada para las 2h03min/dia que mujeres dedican a suministro de alimentos",
    "MA-02": "LED >90 lm/W es la unica tecnologia viable en vivienda rural con panel solar (bajo consumo). Reemplaza velas y mecheros en ZNI. RETILAP 2024 obligatorio",
    "MA-10": "Calentador solar es viable en frio y templado rural. Reduce consumo de lena/gas para agua caliente. Incentivo tributario Ley 1715/2014 (exclusion IVA)",
    "MA-11": "Enfriamiento evaporativo funciona en calido seco rural (Guajira; Tatacoa) donde la humedad es baja. Bajo costo; no requiere electricidad si es pasivo (panel humedo)",

    # === Res. 0194 — Medidas agua ===
    "MW-01": "Aparatos de bajo consumo reducen demanda en vivienda rural con acueducto limitado o captacion pluvial. Cada litro ahorrado = menos acarreo",
    "MW-02": "Grifo de cierre automatico + aireador: inversion pequena; ahorro significativo en rural donde cada litro cuenta",
    "MW-03": "Ducha de bajo flujo (<8 l/min) reduce demanda de agua calentada con lena o solar — ahorro energetico + hidrico",
    "MW-05": "Inodoro doble descarga (<4.5 l) es la medida de agua con mejor costo-beneficio para VIS rural",
    "MW-06": "Tratamiento aguas grises en rural: humedal artificial o trampa de grasa + campo de infiltracion. No requiere energia",
    "MW-07": "Aguas negras en rural sin alcantarillado: biodigestor o pozo septico mejorado. RAS Res. 0330/2017 aplica",
    "MW-08": "ENUT 2024-25: 70% mujeres participan en limpieza/mantenimiento que incluye acarreo agua en rural; 8h53min/dia trabajo no remunerado. Captacion pluvial elimina acarreo y libera tiempo. Ley 2462 Fin 3",
    "MW-09": "Paisajismo con vegetacion nativa: sin riego adicional; contribuye a biodiversidad; sombra natural. Especialmente util en calido seco rural",

    # === Res. 0534 — Criterios clave para rural ===
    "A-E-1": "Energia embebida en materiales rurales: tapia (GWP ~0.08 kg CO2eq/kg) vs. bloque concreto (~0.12) vs. ladrillo (~0.22). Materiales locales tienen menor energia embebida por menor transporte (<100 km)",
    "A-E-2": "En vivienda rural el consumo energetico proyectado es bajo (sin HVAC); el enfoque debe ser maximizar estrategias pasivas antes que activas. Diseno bioclimatico es mas critico que eficiencia de equipos",
    "A-M-1": "En rural los materiales con atributos de sostenibilidad son frecuentemente los vernaculos: tierra (tapia; adobe; BTC); guadua; madera local. La certificacion formal (ACV; EPD) no existe para estos — documentar como patrimonio constructivo",
    "A-R-1": "Circularidad en rural: la vivienda de tapia al demolerse vuelve a ser tierra; la guadua se reutiliza; el bahareque se reconstruye. Los sistemas vernaculos SON circulares por naturaleza",
    "A-R-2": "Diseno modular en rural: sistemas de entramado liviano (guadua; madera) permiten ampliacion futura sin reforzar estructura. PNVISR define vivienda progresiva",
    "A-EM-8": "FNCE en rural: panel solar FV es la opcion principal en ZNI. E2050: 100% edificaciones nuevas Net Zero a 2030. Ley 1715/2014: exclusion IVA para equipos renovables",
    "A-FL-1": "Madera responsable en rural: verificar SUNL; LOF. En eje cafetero la guadua tiene NTC 5301. FSC/PEFC deseable pero poco disponible en zonas rurales remotas",
    "S-CT-1": "Confort termico en vivienda rural: analisis bioclimatico debe considerar que la vivienda ES el lugar de trabajo (cocina; procesamiento; artesania). ENUT: mujeres rurales 8h53min/dia en la vivienda",
    "S-A-1": "Calidad del aire interior en rural: el problema NO es HVAC sino humo de cocina a lena. 78.7% mujeres cocinan (ENUT 2024-25); exposicion a PM2.5 es diferencial por genero. Estufa eficiente es medida de salud + genero",
    "S-H-1": "Materiales no toxicos en rural: verificar pinturas (VOC); evitar asbesto en cubiertas (fibrocemento viejo); preferir materiales naturales (tierra; cal; madera sin tratamiento quimico)",
    "S-AC-1": "Accesibilidad en vivienda rural: alta proporcion de adultos mayores por migracion juvenil urbana. NTC 6047; Ley 361/1997; Sentencia T-333/22 (vivienda digna incluye adecuacion cultural)",

    # === CEELA ===
    "C02": "Control radiacion solar en rural: aleros; corredores perimetrales; arborizacion son estrategias vernaculas de bajo costo. Conecta con proteccion solar de mujeres y ninos en zonas productivas exteriores",
    "C03": "Energia incorporada: priorizar materiales locales (<300 km CASA Colombia). Tapia; adobe; guadua tienen menor energia embebida que cemento; acero; vidrio",
    "C04": "Aislamiento termico en rural frio: muros gruesos de tapia/adobe; cubierta con paja; piso aislado del suelo. Alternativas naturales al poliuretano",
    "C06": "Ventilacion natural: en rural es la UNICA estrategia de climatizacion disponible (sin HVAC). Disenar para vientos dominantes locales es obligatorio",
    "C12": "Gestion agua en rural: captacion pluvial + bajo consumo + reuso. En calido seco la captacion es critica; en calido humedo la evacuacion es critica. ENUT: acarreo agua impacta mujeres/ninas",
    "C14": "Autogeneracion renovable: panel solar FV es la solucion dominante en ZNI rural. Microeolica en Guajira y paramo. Biogas donde hay produccion animal",

    # === Economia Circular ===
    "EC-1": "Eco-diseno rural: la vivienda progresiva con entramado liviano (guadua/madera) permite ampliaciones sin demoler. Menor generacion de RCD vs. mamposteria convencional",
    "EC-2": "Aprovechamiento RCD en rural: escombros de demolicion pueden usarse como relleno; agregados reciclados para sobrecimiento. CONPES 3934: solo 2% de RCD se recicla en CO",

    # === SUDS ===
    "SUDS-1": "Captacion pluvial a escala vivienda rural: canales + tanque + filtro basico. Dimensionar segun precipitacion por clima (>8000 mm/ano Pacifico vs. <300 mm Guajira). Impacto genero: elimina acarreo agua",
    "SUDS-4": "Cisterna/aljibe: solucion ancestral colombiana (Caribe; Santanderes). Almacenamiento subterraneo mantiene agua fresca. Complementa captacion pluvial en estacion seca",

    # === Parametrizacion ===
    "PARAM-1": "Orientacion vivienda rural segun clima: en frio maximizar fachada norte (ganancia solar); en calido minimizar fachada oeste (evitar sobrecalentamiento vespertino). Diagrama estereografico por latitud/longitud del sitio",
    "PARAM-2": "Proteccion solar en rural: aleros (horizontal); celosias guadua/madera (vertical); corredores perimetrales (combinada). Soluciones vernaculas de bajo costo",
    "PARAM-3": "Iluminacion natural rural: ventanas altas producen mas lux que bajas de misma area. Claraboyas en cocina mejoran condiciones de trabajo domestico (ENUT: 2h03min/dia suministro alimentos). RETILAP 2024 obligatorio",
    "PARAM-4": "Ventilacion cruzada rural: aberturas enfrentadas orientadas a vientos dominantes. En Pacifico: ventilacion inferior (palafito); en Caribe: ventilacion alta (efecto chimenea). Critico para evacuacion humo cocina a lena",
}

# Read
with open(MATRIZ, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

for i, row in enumerate(rows):
    if len(row) < len(header):
        rows[i] = row + [''] * (len(header) - len(row))
    elif len(row) > len(header):
        rows[i] = row[:len(header)]

col_notas = header.index("Notas")
col_id = header.index("ID")

count_new = 0
count_append = 0
for row in rows:
    id_val = row[col_id].strip()
    if id_val in notas_rurales:
        existing = row[col_notas].strip()
        if existing:
            row[col_notas] = existing + " | RURAL: " + notas_rurales[id_val]
            count_append += 1
        else:
            row[col_notas] = notas_rurales[id_val]
            count_new += 1

with open(MATRIZ, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

con = sum(1 for r in rows if r[col_notas].strip())
sin = len(rows) - con
print(f"Notas nuevas agregadas: {count_new}")
print(f"Notas existentes ampliadas: {count_append}")
print(f"Total con Notas ahora: {con} de {len(rows)} ({con*100//len(rows)}%)")
print(f"Sin Notas: {sin} ({sin*100//len(rows)}%)")
