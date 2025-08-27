"""
Comparisons
"""

s1 = '¿Dónde están las nieves de antaño?'
s2 = s1.split()
print(s2)
s3 = sorted(s2)
print(s3)
print(s3[1])

var = 1
assert var == 0

try:
  print("5"/0)
except ArithmeticError:
  print('arit')
except ZeroDivisionError:
  print('cero')
except:
  print('algo')