def contar_cpg_islands(secuencia, longitud_region):
    contar_cpg = 0
    contar_no_cpg = 0
    cpg_islands = []
    no_cpg_islands = []

    total_region = len(secuencia) // longitud_region

    for i in range(0, len(secuencia), longitud_region):
        region = secuencia[i:i+longitud_region]
        cg_count = region.count("CG")
        if cg_count >= longitud_region // 10:
            cpg_islands.append((i, i+longitud_region, region))
            contar_cpg += 1
        else:
            no_cpg_islands.append((i, i+longitud_region, region))
            contar_no_cpg += 1

    return contar_cpg, cpg_islands, contar_no_cpg, no_cpg_islands

with open('./21.fasta', 'r') as file:
    secuencia = file.read()

longitud_region = 500  
contar_cpg, cpg_islands, contar_no_cpg, no_cpg_islands = contar_cpg_islands(secuencia, longitud_region)

# Imprimir el número de islas CpG y no CpG
'''
print("Number of CpG islands found in 21 chromosome 10%:", contar_cpg)
print("Number of non CpG islands found in 21 chromosome 10%:", contar_no_cpg)
'''
print("Positions of CpG islands in 21 chromosome 10%:", cpg_islands)
print("Positions of non CpG islands in 21 chromosome 10%:", no_cpg_islands)

