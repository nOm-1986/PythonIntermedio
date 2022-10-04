""" Qué significa lambda?
    Son funciones anónimas, pueden ser utilizadas como argumentos para otras funciones
    o almacenadas en simples variables.
    Estas funciones pueden ser utilizadas como argumento dentro de otras.
    Pueden tener varios argumentos, pero solo una línea de código.
    lambda argumentos: expresión
"""

f_x3 = lambda x: x * 3
print(f_x3(10))
print(f_x3(14))
print(f_x3(16))
print(f_x3(20))

palindrome = lambda string: string == string[::-1]
print(palindrome('ojo'))
print(palindrome('no es'))
