# 4.6.1 = TIPOS DE SECUENCIAS Y MUTABILIDAD
important = """
Secuencia: Es un tipo de dato el cual es capaz de almacenar más de un valor
una secuencia es un tipo de dato que puede ser escaneado por el bucle for.
La segunda noción - la mutabilidad - es una propiedad de cualquier tipo de dato en Python que describe su disponibilidad para poder cambiar libremente durante la ejecución de un programa. Existen dos tipos de datos en Python: mutables e inmutables.
Los datos mutables pueden ser actualizados libremente en cualquier momento - a esta operación se le denomina "in situ".
In situ es una expresión en Latín que se traduce literalmente como en posición, en el lugar o momento. Por ejemplo, la siguiente instrucción modifica los datos "in situ":
"""

print(important)

# Tuples - Inmutables
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
tupla_1_elemento = (1, )
un_elemento_tupla = 1.,

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

# Diccionarios
dictionary = {'clave': 'valor', 'otro': 'esto es formato JSON'}
for key, value in dictionary.items():
  print(key, " --> ", value)

for key in dictionary.keys():
  print(key, " -- > ", dictionary[key])

for french in dictionary.values():
    print(french)

# Diccionarios osn colecciones indexadas de datos, mutables y desordenadas.
# Agregar
dictionary.update({'cambio': 'actualizado'})
print(dictionary)

# clear() -- Para eliminar todos los elementos de un diccionario se debe emplear el método clear():
# copy() == Para copiar un diccionario, emplea el método copy():

tuple_1 = (1, 2, 4, 8)