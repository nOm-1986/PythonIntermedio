"""    Métodos disponibles: """

def run():
    lst1 = [1, True, 'hola mundo', 3.1416]

    #lst1.append(valor) -- Añade valor al final de la lista. 
    lst1.append(2) # [1, True, 'hola mundo', 3.1416, 2]
    print(lst1)

    #.clear() – elimina todos los elementos de lst1. Es equivalente a del lst[:]
    #lst1.clear() #[]
    #print(lst1)
    
    #.copy() – devuelve una copia superficial
    copia = lst1.copy()
    print(copia)

    #.count(valor)

if __name__ == '__main__':
    run()
