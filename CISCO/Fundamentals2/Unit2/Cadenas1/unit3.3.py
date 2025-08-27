""""
2.3 Sección 3 – Métodos de Cadenas
"""
# Capitalize - First letter at mayus and the other to min
print('aBcD'.capitalize())

# Center - To fit in the middle
print('[' + 'middle'.center(10) + ']')
print('[' + 'middle'.center(10, '*') + ']')

# find()
"""
El método find() es similar al método index(), el cual ya conoces, busca una subcadena y devuelve el índice de la primera aparición de esta subcadena, pero:
 - Es más seguro, no genera un error para un argumento que contiene una subcadena inexistente (devuelve -1 en dicho caso).
 - Funciona solo con cadenas, no intentes aplicarlo a ninguna otra secuencia.
"""
print("Hola mundo".find('no')) # -1 Due it doesnt exist inside string
print("Hola mundo".find('do')) # 8


# isalnum() Compruba si tiene solo dígitos o caracteres
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# isdigit()
print('2332'.isdigit())
print("OnlyDigits32".isdigit())

# join() -- Para unir pero es algo especial
print(",".join(["omicron", "pi", "rho"]))

# lower() -- El método lower() genera una copia de una cadena, reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas, y devuelve la cadena como resultado. Nuevamente, la cadena original permanece intacta
print("ChangIng to LoWER".lower()) #changing to lower

#strip() -- Elimina los espacios en blanco iniciales y finales
print("  -- quitnaod epsacio --  ".strip())

#lstrip() -- Elimina los espacios iniciales o izquierda
print("   sin espacios iniciales".lstrip())
print("www.algo.com por ak".lstrip("w"))

# rstrip() -- Elimina los de la derecha
print("eliminando_desde_derecha.com".rstrip(".com"))
print("eliminando_desde_derecha.com     ".rstrip())


# replace()
print("Apple juice".replace("juice", ""))
print("This is it!".replace("is", "are", 2))

# rfind() -- Busca iniciando desde el final - right find
print("tau tau tau".rfind("ta", 3, 9))

# split() -- divide la cadena y crea una lista de todas las subcadenas detectadas separadas por espacios.
print("phi       chi\npsi".split())
print("phichi ta".split())

# swapcase() -- Cambia de mayus a minus y las de minus a mayus
print("Ta LoCa EsTa CoSa".swapcase())

# title() == la primera en mayuscula
print("Este si ta rifado!!".title())

# upper()
print("Este si ta rifado!!".upper())

"""
1. Algunos de los métodos que ofrecen las cadenas son:

capitalize(): cambia todas las letras de la cadena a mayúsculas.
center(): centra la cadena dentro de una longitud conocida.
count(): cuenta las ocurrencias de un carácter dado.
join(): une todos los elementos de una tupla/lista en una cadena.
lower(): convierte todas las letras de la cadena en minúsculas.
lstrip(): elimina los caracteres en blanco al principio de la cadena.
replace(): reemplaza una subcadena dada con otra.
rfind(): encuentra una subcadena comenzando por el final de la cadena.
rstrip(): elimina los caracteres en blanco al final de la cadena.
split(): divide la cadena en una subcadena usando un delimitador dado.
strip(): elimina los espacios en blanco iniciales y finales.
swapcase(): intercambia las mayúsculas y minúsculas de las letras.
title(): hace que la primera letra de cada palabra sea mayúscula.
upper(): convierte todas las letras de la cadena en mayúsculas.

2. El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):

endswith(): ¿La cadena termina con una subcadena determinada?
isalnum(): ¿La cadena consta solo de letras y dígitos?
isalpha(): ¿La cadena consta solo de letras?
islower(): ¿La cadena consta solo de letras minúsculas?
isspace(): ¿La cadena consta solo de espacios en blanco?
isupper(): ¿La cadena consta solo de letras mayúsculas?
startswith(): ¿La cadena consta solo de letras mayúsculas?

"""