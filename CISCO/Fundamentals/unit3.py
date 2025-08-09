n = int(input('Ingrese un valor'))
#Ternary operator
print('Mayor o igual a 100') if n >= 100 else print('Menor a 100')

# A compacted way to use if else:
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = 120200
# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2

# Max is a built_in function to get the biggest number
largest_number = max(number1, number2, number3)

# Min the same as Max
minius_number = min(number1, number2, number3)


largest_number = -999999999
# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)

print(0 == False)

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

user_number = int(input('Ingresa un número: '))
condition = True

while condition:
    if user_number == secret_number: 
        print("¡Bien hecho, muggle! Eres libre ahora.")
        condition = False
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
        user_number = int(input('Ingresa un número: '))


# 3.2.8 Break and continue
print("""
Estas en el juego del traga vocales .....
Ingresa una palabra y el sistema se encagará de eliminar las vocales.
""")

user_word = input('Ingrese -1 para salir o una palabra para quitarle las vocales: ')

while user_word != '-1':
    
    user_word = user_word.upper()
    
    for letter in user_word:
        if letter in 'AEIOU': continue
        print(letter)
        
    user_word = input('Ingrese -1 para salir o una palabra para quitarle las vocales: ')
    if user_word == '-1':
        continue
print('Esta hecho!!!!')


# 3.2.12
# While using else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
# imprimira 5

for i in range(5):
    print(i)
else:
    print("else:", i)


bloques = 6
numero_de_capas = 0
bloques_usados = 1

while bloques > 0:
    if  bloques - bloques_usados > 0:
        bloques = bloques - bloques_usados
        numero_de_capas =+ 1
        bloques_usados =+ 1 
    else: break
print('Numero de capas: ', numero_de_capas)

# Working with lists
l = [x for x in range(1, 21)]
print(l)

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)


var_1 = 1
var_2 = 3
var_1, var_2 = var_2, var_1


my_list = [8, 10, 6, 2, 4]  # lista a ordenar
 
for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]