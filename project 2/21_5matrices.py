def etiquetar(secuencia, posiciones_nucleotidos_cpg): # modelo oculto
    etiquetas = ['N'] * len(secuencia)  # a todas las posiciones asignarles la N para cambiar solo los qeu cumplan la condición (si esta esa posicion en la secuencia)
    for indice in posiciones_nucleotidos_cpg:
        etiquetas[indice] = 'C'  
    return etiquetas


def calcular_transiciones(etiquetas):
    transiciones = {'C': {'C': 0, 'N': 0}, 'N': {'C': 0, 'N': 0}} 
    for i in range(1, len(etiquetas)):
        estado_actual = etiquetas[i - 1]
        estado_siguiente = etiquetas[i]
        transiciones[estado_actual][estado_siguiente] += 1  
    return transiciones

def normalizar_transiciones(transiciones):
    for estado_actual, transiciones_desde_estado in transiciones.items():
        total_transiciones = sum(transiciones_desde_estado.values())
        for estado_siguiente in transiciones_desde_estado:
            transiciones[estado_actual][estado_siguiente] /= total_transiciones  
    return transiciones

def calcular_emisiones(secuencia, posiciones_nucleotidos_cpg, posiciones_nucleotidos_no_cpg):
    emisiones = {'C': {'A': 0, 'C': 0, 'G': 0, 'T': 0}, 'N': {'A': 0, 'C': 0, 'G': 0, 'T': 0}}

    for posicion in posiciones_nucleotidos_cpg:
        nucleotido = secuencia[posicion]

        if nucleotido not in {'A', 'C', 'G', 'T'}:
            continue
        estado_oculto = etiquetas[posicion]
        emisiones[estado_oculto][nucleotido] += 1

    for posicion in posiciones_nucleotidos_no_cpg:
        nucleotido = secuencia[posicion]

        if nucleotido not in {'A', 'C', 'G', 'T'}:
            continue
        estado_oculto = etiquetas[posicion]
        emisiones[estado_oculto][nucleotido] += 1

    return emisiones

def contar_cpg_islands(secuencia, longitud_region):
    contar_cpg = 0
    contar_no_cpg = 0
    cpg_islands = []
    no_cpg_islands = []

    total_region = len(secuencia) // longitud_region

    for i in range(0, len(secuencia), longitud_region):
        region = secuencia[i:i+longitud_region]
        cg_count = region.count("CG")
        if cg_count >= longitud_region // 5:
            cpg_islands.append((i, i+longitud_region, region))
        else:
            no_cpg_islands.append((i, i+longitud_region, region))

    return cpg_islands, no_cpg_islands

def obtener_posiciones_nucleotidos_cpg(posiciones_cpg):
    posiciones_nucleotidos = []

    for inicio, fin, region in posiciones_cpg:
        for i, nucleotido in enumerate(region):
            posicion_absoluta = inicio + i
            posiciones_nucleotidos.append(posicion_absoluta)

    return posiciones_nucleotidos

def obtener_posiciones_nucleotidos_no_cpg(posiciones_no_cpg):
    posiciones_nucleotidos = []

    for inicio, fin, region in posiciones_no_cpg:
        for i, nucleotido in enumerate(region):
            posicion_absoluta = inicio + i
            posiciones_nucleotidos.append(posicion_absoluta)

    return posiciones_nucleotidos

with open('./21.fasta', 'r') as file:
    secuencia = file.read()

longitud_region = 500
# ...

posiciones_cpg, posiciones_no_cpg = contar_cpg_islands(secuencia, longitud_region)

posiciones_nucleotidos_cpg = obtener_posiciones_nucleotidos_cpg(posiciones_cpg)
posiciones_nucleotidos_no_cpg = obtener_posiciones_nucleotidos_no_cpg(posiciones_no_cpg)

etiquetas = etiquetar(secuencia, posiciones_nucleotidos_cpg)

transiciones = calcular_transiciones(etiquetas)
transiciones_normalizadas = normalizar_transiciones(transiciones)

emisiones = calcular_emisiones(secuencia, posiciones_nucleotidos_cpg, posiciones_nucleotidos_no_cpg)


print("Posiciones de los nucleótidos en las CpG islands:")
print(posiciones_nucleotidos_cpg)

print("\nTransiciones sin normalizar:")
print(transiciones)
print("\nTransiciones normalizadas:")
print(transiciones_normalizadas)

print("\nEmisiones sin normalizar:")
print(emisiones)


print("\nEmisiones normalizadas:")
for estado_oculto, emisiones_por_estado in emisiones.items():
    total_emisiones = sum(emisiones_por_estado.values())

    for nucleotido in emisiones_por_estado:
        emisiones[estado_oculto][nucleotido] /= total_emisiones


print(emisiones)
