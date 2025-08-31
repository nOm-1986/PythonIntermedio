class Classy:
  varia = 1
  def __init__(self):
    self.var = 2

  def visible(self):
    print("visible")

  def __hidden(self):
    print("oculto")


obj = Classy()
obj.visible()

try:
  obj.__hidden()
except:
  print("fallido")

obj._Classy__hidden()

print(Classy.__dict__)
print("------------" * 10)
print(obj.__dict__)

print("------------" * 10)
# type
print(Classy.__name__)
print(type(obj).__name__)

"""
Como sabes, cualquier módulo llamado __main__ en realidad no es un módulo, sino es el archivo actualmente en ejecución.

Nota: una clase sin superclases explícitas apunta a object (una clase de Python predefinida) como su antecesor directo.
Todas las clases (pero no los objetos) contienen una propiedad llamada __name__, que almacena el nombre de la clase. 
Además, una propiedad llamada __module__ almacena el nombre del módulo en el que se ha declarado la clase, 
mientras que la propiedad llamada __bases__ es una tupla que contiene las superclases de una clase.

"""
print(Classy.__module__)
