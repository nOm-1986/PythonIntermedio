# Review - Notes - Summary About Module 2 CISCO Fundamentals I.

# Int - We can uses int with 10base, 8base (Octal) and 16base(hexadecimal)

# Octal - we can use 0O or 0o is not case sensitive
print(0o123, 0O123, sep=' -- ') # 83
print() # 83

# Hexadecimal 0x - 0X cero ex
print(0x123, 0X123, sep=' ** ')

# Exponentials
print(3E8)

#Booleans
print(True > False)
print(True < False)

print('"Estoy\n"\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"')


# Module 2.3 -- Operators

# Exponencia **
print(2**3)

# Multiplier
print(2*3)

# Division
print(8 / 2)
print(8 / 2.)
print(8. / 2)
print(8. / 2.)

# División Entera - El resultado carece de la parte fraccionaria, está ausente (para los enteros), o siempre es igual a cero (para los flotantes); esto significa que los resultados siempre son redondeados;
# Esto es muy importante: el redondeo siempre va hacia abajo.
print(8 // 2)
print(8 // 2.)
print(8. // 2)
print(8. // 2.)

# Modules % - residuo que queda de la división entera.
print(14 % 4)
print(12 % 4.5)

#
print(-4 - 4)
print(4. - 8)
print(-1.1)

# El resultado muestra claramente que el operador de exponenciación utiliza enlazado del lado derecho.
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))

print(2 * 3 % 5)
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

a = 6
b = 3
a /= 2 * b
print(a)

ciclo = True

while ciclo:
  salirPrograma = input('Para salir ingrese 1. Continuar de enter')
  if salirPrograma == '1':
    print('Finalizando...')
    break

  x = float(input("Ingresa el valor para x: "))
  y = (1 / (x + (1 / (x + (1 / (x + (1 / x)) )))))
  print("y =", y)

# Posibles preguntas

# Caracteres de escape que hace \n, \t, \\, \'
# El siginifcado del parametro de palabra clave o que hace el argumento palabra clave: se debe especificar el argumento con su valor, van al final
# Algo de exponenciales 12.20E8
print(20.12E8)
print(20.12*(10**8))
print(1 // (2 * 3))
x = 1
y = 2
z = x
x = y
y = z
print(x, y)

x = 11
y = 4
x = x % y
print(x)
x = x % y
print(x)
y = y % x
print(y)

z = y = x = 1
print(x, y, z, sep='*')

x = 1/2+3//3+4**2
print(x)

