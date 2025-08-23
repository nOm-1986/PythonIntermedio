import module


"""
Cuando los modulos son importados, la inicialización solo se realiza
la primera vez. Python recuerda los módulos iportados y omite silenciosamente
todas las importaciones posteriores.

-- Cuando se ejeucta un archivo directamente, su variable __name__ se establece en __main__
-- Cuando un archivo se importa como un módulo, su variable __name__ se establece con el nombre del archivo excluyendo el .py 

Cuando importo un módulo tambien puedo acceder a sus variables.

Esto se hace anteponiendo al nombre de la variable _ (un guión bajo) o __ (dos guiones bajos), pero recuerda, es solo un acuerdo. Los usuarios de tu módulo pueden obedecerlo o no.

"""
import sys
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

for p in sys.path:
  print(p)