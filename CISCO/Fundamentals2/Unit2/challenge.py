#1 El entrar al bloque try: implica que: R - Algunas instrucciones de este bloque no se ejecuten
#2 El bloque except sin nombre: : R - debe ser el último
#3 La excepción base en Python se llama: R - BaseException
#4 La siguiente sentencia: assert var == 0 ---- R detendrá el programa cuando var!=0
#5 Cuál es el resultado esperado del siguiente código? === R - Algo
""""
try:
  print("5"/0)
except ArithmeticError:
  print('arit')
except ZeroDivisionError:
  print('cero')
except:
  print('algo')
"""

#6 Cuales de las siguiente son excepciones integradas concretas de Python: R - IndexError, ImportError

#7 ASCII es: R - American Code Standard for Information Interchange

#8 UTF-8 es: R - Una forma de codificar puntos de código Unicode

#9 UNICODE es un estandar: como ASCII, pero más expansivo

#10 x = '\'' print(len(x)):  R - 1

#11 print(ord('c') - ord('a')): R - 2

#12 print(chr(ord('z') - 2)): R - x

#13 print(3 * 'abc' + 'xyz'): R - abcabcabcxyz

#14 print('Mike' > 'Mikey'): R - False

#15 print(float('1, 3')): R - Genera una excepción ValueError


print(ord('c') - ord('a'))
print(chr(ord('z') - 2))
print(3 * 'abc' + 'xyz')
print('Mike' > 'Mikey')
print(float('1, 3'))