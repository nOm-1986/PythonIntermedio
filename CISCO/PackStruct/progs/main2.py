""""
Un archivo de Python llamado __init__.py se ejecuta implícitamente cuando un paquete 
que lo contiene está sujeto a importación y se utiliza para inicializar un paquete y/o 
sus subpaquetes (si los hay). El archivo puede estar vacío, pero no debe faltar.
"""
from sys import path

print(dir(path))
exit()

# Es Windows es mejor utilizar la ruta relativa
#path.append("d:\Development\PythonIntermedio\CISCO\PackStruct\packages")
path.append("d:\\Development\\PythonIntermedio\\CISCO\\PackStruct\\packages")


import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())


