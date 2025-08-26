from platform import platform, machine, processor, system, version
from platform import architecture, python_implementation, python_version_tuple
import os

information_about_platform = """
El módulo platform permite acceder a los datos de la plataforma subyacente, es decir, hardware, SO e información
sobre la versión del intérprete.

1 - Una función llamada dir() puede mostrarte una lista de las entidades contenidas dentro de un módulo importado.
2 - El módulo math contiene más de 50 funciones para realizar operaciones matemáticas
3 - El módulo random agrupa más de 60 entidades diseñadas para ayudarte a usar números psudoaleatorios.
4 - El módulo platform contiene alrededor de 70 funciones que me ayudan a ver información del SO y hardware.


"""
# print(platform())
# print(platform(1))
# print(platform(0, 1))
# print(machine())
print(processor())
print(system())
print(version())
# print(architecture())
# print(python_implementation())
# for atr in python_version_tuple():
#   print(atr)

# dir(os)