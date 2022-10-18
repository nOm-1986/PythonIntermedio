"""Working with string functions in python - There are 47 in total.
    Looking for and count functions.
"""

def group_looking_for_and_count(my_string):
    #Looking for an occurrence
    print(my_string.find('u', 4))
    #looking for an occurrence using comprehensions
    inicio = 0
    list_index = list()

    while True:
        var = my_string.find('a', inicio)
        if var == -1:
            break
        else:
            inicio = var+1
            list_index.append(var)

    print(list_index)


def using_find(letter_to_find, my_string = 'Una palabra', inicio = 0):
    '''Devuelve el índice mínimo donde se encuetre la cadena sub en cad1.
        Recibe opcinalmente el parámetro inicio y fin. Por defecto inicio = 0.
    '''
    print(my_string.find(letter_to_find, inicio))


def using_rfind(letter, my_string):
    #Devuelve el indice máximo donde se encuetre la cadena
    print(my_string.rfind(letter))


def using_index(letter_to_find, my_string = 'Una palabra', inicio = 0):
    print(my_string.index(letter_to_find))


if __name__ == '__main__':
    my_string = 'Unaplabralarga'
    print(my_string.count('a'))
    group_looking_for_and_count(my_string)
    using_find('rac', 'Una oración algo larga')
    using_rfind('a', 'Una oración algo larga')
    using_index('ra', 'Una oración algo larga')
