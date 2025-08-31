"""
Generadores:
Es un fragmento de código capaz de producir valores e iterar sobre los mismos.
Ejemplo: range(5) -> es un generador y a la vez un iterador

Qué es un iterador?
El protocolo iterador es una forma en que un objeto debe comportarse para ajustarse a las 
reglas impuestas por el contexto de las sentencias for e in. Un objeto conforme a estas 
reglas se llama iterador.
Debe proporcinar
->  __iter__() === El cual devuelve el objeto en si y que se invoca una vez.
-> __next__() === El cual devuelve el siguiente valor de la seria deseada.
Este es invocado por las sentencias for / in para pasar a la siguiente iteración; si no hay más
valores a proporcinar, el método deberá generar la excepción StopIteration.


"""
class Fib:
  def __init__(self, nn):
    print("__init__")
    self.__n = nn
    self.__i = 0
    self.__p1 = self.__p2 = 1

  def __iter__(self):
    print("__iter__")
    return self

  def __next__(self):
    print("__next__")		
    self.__i += 1
    if self.__i > self.__n:
      raise StopIteration
    if self.__i in [1, 2]:
      return 1
    ret = self.__p1 + self.__p2
    self.__p1, self.__p2 = self.__p2, ret
    return ret


for i in Fib(10):
  print(i)

class MiIterador:
  def __init__(self, lista: int):
    print("__init__")
    self.__lista = lista
    self.__contador = 0
    self.__sumatoria = 0
  
  def __iter__(self):
    print("__iter__")
    return self
  
  def __next__(self):
    print("next")
    self.__contador += 1
    x = [x for x in range(self.__lista)]
    if self.__contador > self.__lista: 
      raise StopIteration
    self.__sumatoria = self.__sumatoria + x[self.__contador -1]
    return self.__sumatoria
  
for i in MiIterador(5):
  print(i)

""""
yield --- Un hermano más inteligente que return  XD
YIELD convierte la función en un generador esto le permite proporcionar el valor de la expresión
especificada después de la palabra clave reservada yield, pero no pierde el estado de la función.
Todos los valores de las variables estan congelados
"""

def fun(n):
  for i in range(1,n+1):
    yield i

for v in fun(5):
    print(v)


# Primeras potencias de n
def powers_of_2(n):
  power = 1
  for i in range(n):
    yield power
    power *= 2

for v in powers_of_2(8):
  print(v)

def powers_of_2(n):
  power = 1
  for i in range(n):
    yield power
    power *= 2

t = [x for x in powers_of_2(5)]
print(t)