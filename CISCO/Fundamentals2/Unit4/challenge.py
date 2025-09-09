# 01 -- Qué palabra clave reservada usarías para definir una función anónima? --- lambda
# 02 -- Seleccione 2: a. La función lambda puede aceptar cualquier número de argumentos -- b. La función lambda puede evaluar sólo una expresión
# 03 -- foo = tuple(map(lambda x: x**x, my_list))
# 04 -- Que fragmento insertarías para que el programa genere el siguiente resultado (lista)?: [2,3,4,5,6]: 
  # R 04 - foo = list(filter(lambda x:L x-0 and x-1, my_tuple))
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result = list(filter(lambda x: x-0 and x-1, my_tuple))
print(result)
res2 = list(filter(lambda x: x==0 and x==1, my_tuple))
print(res2)
'''
  1. filter(function, iterable)

  Recorre my_tuple elemento por elemento.

  Aplica la función lambda x: x-0 and x-1.

  Conserva solo los elementos donde esa expresión devuelve True.

  2. La lambda: lambda x: x-0 and x-1

  x - 0 → es simplemente x.

  x - 1 → es x - 1.

  La operación es x and (x-1).

  En Python, and no devuelve siempre True o False, devuelve el último valor evaluado:

  Si x es 0, entonces x-0 = 0 → eso es False → la lambda da 0.

  Si x es 1, entonces x-0 = 1 (True), pero x-1 = 0 (False) → devuelve 0.

  Para cualquier otro valor (2, 3, … o negativos excepto 0 y 1), la expresión devuelve un número distinto de cero → considerado True.
'''

# 05 -- Cuál es el resultado esperado de ejecutar el siguiente código? -- R: ace
def I():
  s = 'abcdef'
  for c in s[::2]:
    yield c

for x in I():
  print(x, end='')


# 06 -- Cuál es el resultado esperado de ejecutar el siguiente código: -- Imprimirá ++++++
def fun(n):
  s = '+'
  for i in range(n):
    s += s
    yield s

for x in fun(2):
    print(x, end='');


# 07 --  Cuál es el resultado esperado de ejecutar el siguiente código:
def o(p):
  def q():
    return '*' * p
  return q

r = o(1)
s = o(2)
print(r() + s())



# 08 -- Cuáles de los sig... R: 'r+', 'r'


# 09 -- errno.EEXIST --- R: Archivo existente. En Python, errno.EEXIST es un código de error simbólico que se utiliza para indicar que se intentó crear un archivo o directorio que ya existe


# 10 -- Cuál es el resultado esperado de ejecutar el siguiente código:
b = bytearray(3)
print(b)


# 11 -- Cual es el resultado esperado del siguiente código?: R -- la ruta al directorio pictures
import os

os.mkdir('pictures')
os.chdir('pictures')
os.mkdir('thumbnails')
os.chdir('thumbnails')
os.mkdir('tmp')
os.chdir('../')

print(os.getcwd())




# 12 -- Cuál es el resultado esperado del siguiente código?: R -- ['large', 'small', 'medium']
import os

os.mkdir('thumbnails')
os.chdir('thumbnails')

sizes = ['small', 'medium', 'large']

for size in sizes:
    os.mkdir(size)

print(os.listdir())



# 13 -- Cuál es el resultado esperado del siguiente código?: R -- 345 days, 0:00:00
from datetime import date

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2)




# 14 -- Cuál es el resultado esperado del siguiente código?: R -- 19/November/27 11:27:22
from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))



# 15 -- Qué programa producirá la siguiente salida?:  R -- print(calendar.weekheader(2))
# Mo Tu We Th Fr Sa Su
import calendar
print(calendar.weekheader(2))

# 16 -- Cuál es el resultado esperado del siguiente código?: R --
import calendar
c = calendar.Calendar()

for weekday in c.iterweekdays():
  print(weekday, end=' ')

