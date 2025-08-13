def message(number):
    print("Ingresa un número:", number)
 
number = 1234
message(1)
print(number)

# Parámetros posicionales - a normal function with arguments.
def introduction(first_name, last_name):
    print(f'Hello, my name is {first_name} {last_name}')

introduction('Jose', 'Beltran')

# Paso de argumentos de palabra clave
introduction(last_name='Meza', first_name='Fabian')

# Funciones parametrizadas - valores predefidos
def defined_parameters(si_es_nulo=True):
    if si_es_nulo:
        print('Con el valor por defecto: ', si_es_nulo)
    else:
        print(f'You sent an argument: ', si_es_nulo)

defined_parameters()
#defined_parameters('Sending string')

# 2. Puedes pasar argumentos a una función utilizando las siguientes técnicas:
#paso de argumentos posicionales en la cual el orden de los parámetros es relevante (Ejemplo 1)
#paso de argumentos con palabras clave en la cual el orden de los argumentos es irrelevante (Ejemplo 2)
#una mezcla de argumentos posicionales y con palabras clave (Ejemplo 3).
# NOTA: Es importante recordar que primero se especifican los argumentos posicionales y después los de palabras clave. Es por esa razón que si se intenta ejecutar el siguiente código:

def add_numbers(a, c, b=2):
#def add_numbers(a, b=2, c):
  print(a + b + c)

add_numbers(a=1, c=3)
#Syntax error.

# Global variables
def my_function():
  global var
  var = 2
  print("¿Conozco a aquella variable?", var)

var = 1
my_function()
print(var)

# Esta parte es cierta para valores escalares
# Esto también significa que una función recibe el valor del argumento, no el argumento en sí. Esto es cierto para los valores escalares.
# Que pasa con las listas, son pasadas como valor o como referencia?

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(weight = lb_to_kg(175), height = ft_and_inch_to_m(10, 7)))

