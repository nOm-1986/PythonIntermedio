"""    Métodos disponibles: """

def run():
    lst1 = [1, True, 'hola mundo', 3.1416, 1, False]
    a = [1,2,3,4]
    b = [5,6,7,8,2]

    #lst1.append(valor) -- Añade valor al final de la lista. 
    lst1.append(2) # [1, True, 'hola mundo', 3.1416, 2]
    print(lst1)

    #.clear() -- elimina todos los elementos de lst1. Es equivalente a del lst[:]
    #lst1.clear() #[]
    #print(lst1)
    
    #.copy() -- devuelve una copia superficial
    copia = lst1.copy()
    print(copia)

    #.count(valor) -- cuenta el número de veces que el elemento aparece en la lista
    # importante saber que True se considera 1, False 0
    print(lst1.count(1)) #3
    print(lst1.count(0)) #1

    #.extend(iter) -- extiende la lista lst1 añadiendo todos los elementos del iterable iter1.
    a.extend(b)
    print(a)

    #.index(elem,[, inicio[, final]]) -- Devuelve el índice de la posición que ocupa el elemento dentro de la lista
    print(a.index(2)) #
    print(a.index(2,3)) # indice del elemento 2 contado desde la posicion 3

    #.insert(pos, elem) -- inserta elem en la posición anterior definida por el índice pos.
    a.insert(0,20)
    print(a)

    #.pop([pos]) -- elimina y devuelve el elemento de la posición definida por pos. El parámetro es opcional y, si se omite, se devuelve y elimina el último elemento de la lista.
    a.pop(4)
    a.pop()

    #.remove(elem) -- elimina la primera ocurrencia de elem en las lista. Si no existe una ocurrencia eleva un ValueError
    a.remove(2)

    #.reverse() -- invierte el orden de los elementos de la lista(no genera una lista nueva, sino que lo hace en la misma - reverse in place)
    a.reverse()

    #.sort(key=None, reverse=False) -- ordena la lista en el sitio. En el parámetro key se puede añadir una funcion que se utilice para ordenar, yu el parámetro reverse se utiliza para que el orden sea inverso o no.
    #key es por lo general una función anónima lambda
    a.sort()
    print(a)
    lst1.sort(key=lambda x: str(x))
    print(lst1)


if __name__ == '__main__':
    run()
