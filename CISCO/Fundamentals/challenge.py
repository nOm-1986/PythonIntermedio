#bloques = 1000
bloques = 2
numero_de_capas = 0
total_bloques = 0
anterior = 0
numero_siguiente = 0

while (bloques - total_bloques)  > numero_siguiente:
    numero_de_capas += 1
    numero_siguiente = anterior + 1
    total_bloques = total_bloques + numero_siguiente
    anterior = numero_siguiente
    print(f'Bloques usados: {total_bloques}... Capa actual: {numero_de_capas} ... Bloques restantes: {bloques - total_bloques}')
    
print('Numero de capas: ', numero_de_capas)