# 01 -- Sabiendo que una función llamada fun() reside en un módulo llamado mod
# y que fue importado usando la siguiente sentencia: R: fun()
"""
from mod import fun
  fun()
"""


# 02 -- Qué resultado aparecerá después de ejecutar el siguiente fragmento de código?
import math
print(dir(math))


# 03 -- El código bytecode compilado de Python se almacena en archivos con la extensión: R: pyc


# 04 -- Suponiendo que los siguientes 3 archivos ... cab
"""
archivo a.py
print("a", end="")

archivo b.py
print("b", end="")

archivo c.py
print("c", end="")
import a
import b

Respuesta: cab

"""


# 05 -- Cuál será la salida del siguiente código, ubicado en el archivo p.py?
print(__name__)


# 06 -- from a.b import c --- R: la entidad c del módulo b del paquete a


# 07 -- Si hay más de un bloque except: después de un try:, podemos decir que: --- R: No más de un bloque except será ejecutado.


# 08 -- 
try:
  raise Exception
except BaseException:
  print("a")
except Exception:
  print("b")
except:
  print("c")


# 09 -- La siguiente línea de código:
# for line in open('text.txt', 'rt'): ----> R: es válida porque open devuelve un objeto iterable

# 10 -- Cuál es el resultado esperado del siguiente fragmento de código? R: El except: debe ser el último por lo tanto da un error de Sintaxis
# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")



# 11 -- La siguiente sentencia: assert var != 0 ===> R: Detendrá el programa cuando var == 0


# 12 -- El siguiente código: ==== R: Imprimirá 2
x = "\\\\"
print(len(x))


# 13 --El siguiente código: ==== R: Con tres causa un error. SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
#x = "\\\"
print(len(x))


# 14 -- El siguiente código: ==== R: Imprimirá r
print(chr(ord('p')+ 2))


# 15 -- print(float("1.3")) ==== R Imprimirá 1.3
print(float("1.3"))

# 16 -- Si el constructor de la clase se declara de la siguiente manera: Cuál de las asignaciones es inválida?
# R: object = Class(1,2)
class Class:
  def __init__(self, val=0):
    pass
object = Class(1,2)
print(object)

# 17 -- Cuál es el resultado esperado del siguiente código? === R: 3
class A:
  def __init__(self, v=2):
    self.v = v
  
  def set(self, v=1):
    self.v += v
    return self.v

a = A()
b = a
b.set()
print(b.v)
print(a.v)


# 18 -- Cuál es el resultado esperado del siguiente código? === R: False. Como no se ha inicializado no tiene aún el atributo
class A:
  A = 1
  def __init__(self):
    self.a = 0

print(hasattr(A, 'a'))


# 19 -- Cuál es el resultado esperado del siguiente código? === R: False pues A no es subclase de C, es alcontrario
class A:
  pass
class B(A):
  pass
class C(B):
  pass

print(issubclass(A, C))


# 20 -- El flujo o stream sys.stderr normalmente se asocia con: === R: es un error normalmente se asocia con: la pantalla?


# 21 -- Cual sera el resultado esperado al ejecutar el siguiente código? === R: El código generará una excepción AttributeError
class A:
  def __init__(self, v):
    self.__a = v + 1

a = A(0)
print(a.__a)




# 22 -- Cual sera el resultado esperado al ejecutar el siguiente código? === R: El código generará una excepción
class A:
  def __init__(self):
    pass
  
a = A(1)
print(hasattr(a, 'A'))


# 23 -- R: El código imprimirá b
class A:
  def a(self):
    print('a')


class B:
  def a(self):
    print('b')


class C(B,A):
  def c(self):
    self.a()

o = C()
o.c()


# 24 --El código imprimirá 3
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))


# 25 -- Cual es el resultado esperado al ejecutar el siguiente código? === R: Imprimirá ++++++
def fun(n):
  s = '+'
  for i in range(n):
    s += s
    yield s

for x in fun(2):
    print(x, end='')

# 26 -- Cuál es el resultado esperado al ejecutar el siguiente código? === R: El código imprimirá 'abc'
class I:
  def __init__(self):
      self.s = 'abc'
      self.i = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.i == len(self.s):
      raise StopIteration
    v = self.s[self.i]
    self.i += 1
    return v


for x in I():
  print(x, end='')



# 27 -- Cuál es el resultado esperado al ejecutar el siguiente código? === R: ***
def o(p):
  def q():
    return '*' * p
  return q

r = o(1)
s = o(2)
print(r() + s())


# 28 -- Si s es un stream abierto en modo lectura, la siguiente línea: q = s.read(1) === R Leerá un carácter del stream


# 29 -- Suponiendo que la invocación open() se ha realizado correctamente, el siguiente fragmento de código: === R: leerá el archivo linea por linea
for x in open('file', 'rt'):
  print(x)


# 30 -- Si deseas llenar un arreglo de bytes con datos leídos de un stream, puedes usar: === R: El método readinto()


# 31 -- Cuál de los siguientes comandos usarías para verificar la versión de pip? === R: pip3 --version ------- pip --version


# 32 -- Cuál comando pip usarías para desinstalar un paquete previamente instalado? === R: pip uninstall nombre_del_paquete


# 33 -- R: foo = map(lambda num: num**2, numbers) 
numbers = [0, 2, 7, 9, 10]
resultado = map(lambda x: x ** 2, numbers)
print(list(resultado))

# 34 -- R: foo = list(filter(lambda x: x % 2, numbers))
print()
numbers = [i*i for i in range(5)]
print(numbers)
foo = list(filter(lambda x: x % 2, numbers))
print(foo)

# 35 -- R ===
import random


# 36 -- R: El código imprimirá la ruta al directorio creado
import os

os.mkdir('pictures')
os.chdir('pictures')
print(os.getcwd())


# 37 -- Qué información se puede leer usando la función uname proporcinada por el módulo os?
# R:Identificador de hardware
# R: Nombre del sistema operativo

import os

print(os.uname())


# 38 -- R: 11:27:22
from datetime import datetime
datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)
print(datetime_1 - datetime_2)

# 39 -- 28 days, 22:00:00
from datetime import timedelta

delta = timedelta(weeks = 1, days = 7, hours = 11)
print(delta * 2)



# 40 --
import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(3))




