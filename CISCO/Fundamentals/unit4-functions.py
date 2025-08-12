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
