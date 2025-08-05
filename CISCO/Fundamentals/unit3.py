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