"""
Los objetos de Python, cuando se crean, están dotados de un pequeño conjunto 
de propiedades y métodos predefinidos. Cada objeto los tiene, los quieras o no. 
Uno de ellos es una variable llamada __dict__ (es un diccionario).

__dict__ => Muestra todas las propiedades(variables) del objeto
"""

class ExampleClass:
  def __init__(self, val = 1):
      self.__first = val
      #self.first = val

  def set_second(self, val):
      self.__second = val
      #self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__) # {'first': 1}
print(example_object_2.__dict__) # {'first': 2, 'second': 3}
print(example_object_3.__dict__) # {'first': 4, 'third': 5}

""""
Como se ve el tercer objeto puede crear una propiedad third que fue creada en marcha
esto es permitido pero tenga en cuenta que:
NOTA: EL MODIFICAR UNA VARIABLE DE INSTANCIA DE CUALQUIER OBJETO NO TIENE IMPACTO
EN TODOS LOS OBJETOS RESTANTES. LAS VARIABLES DE INSTANCIA ESTÁN PERFECTAMENTE
AISLADAS UNAS DE OTRAS.
"""
print('--'*10)
print(example_object_1._ExampleClass__first)


print("Variables de Clases")
class ExampleClass:
  counter = 0
  def __init__(self, val = 1):
    self.__first = val
    ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

print('--'*10)
print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)