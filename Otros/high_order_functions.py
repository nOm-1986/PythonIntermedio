""" Funciones de orden superior.
    Son funciones que reciben como parametro a otra función y hacen algo con ella.
    Existen 3 funciones de orden superior que puedes encontrar en muchos lenguajes:
    Filter, Map, Reduce.
"""
from functools import reduce


def saludo(funct):
    funct()

def hola():
    print('Hola')

def adios():
    print('Adios')

saludo(hola)
saludo(adios)

my_list = [1,4,5,6,9,13,12,19,21]
odd = list(filter(lambda x: x%2 !=0, my_list))
print(odd)


my_list2 = [1,2,3,4,5]
squares = list(map(lambda x: x**2, my_list2))
print(squares)


my_list3 = [2,2,2,2,2]
my_list4 = [1,2,3,4,5]
all_multiplied = reduce(lambda a,b: a*b, my_list4)
print(all_multiplied)