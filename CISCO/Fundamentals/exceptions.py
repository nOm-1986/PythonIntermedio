excepciones_comunes = """ 
ZeroDivisionError
Hacer una operación de división por cero o no se puede distinguir de cero. 

ValueError
Manejar valores que pueden usarse de manera inapropiada en algún contexto. En general, esta excepción se genera cuando una función (como int() o float()) recibe un argumento de un tipo adecuado, pero su valor es inaceptable.

TypeError
Trata de igresar un valor en una variable que no es de ese tipo. Ejemplo un indice con flotante[0.5]

AttributeError
Error de atributo

SyntaxError
Cuando se viola la gramática de python.
"""

try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')
except:
  print('Ha sucedido algo extraño, ¡lo siento!')

