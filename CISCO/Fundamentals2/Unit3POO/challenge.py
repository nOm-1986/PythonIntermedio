# 1 - Una estructura de datos descrita con LIFO es en realidad --- R: Una pila
# 2 - object = Class()
# 3 - A.__init__(self).
# 4 - El código generará una excepción AttributeError

#5 - Cual será la salida del siguiente código? ==== R - 2
class A:
  def __init__(self, v = 1):
    self.v = v

  def set(self, v):
    self.v = v
    return v
a = A()
print(a.set(a.v + 1))


# 6 R: 3
class B:
  A = 1
  X = 0
  def __init__(self, v = 0):
    self.Y = v
    B.X += v

a = B()
b = B(1)
c = B(2)
print(c.X)



# 7 --- Cuál será la salida del siguiente código? -=-- R:  TRUE
class ClaseA:
  A = 1
print(hasattr(ClaseA, 'A'))


# 8 -- resultado de ejecutar -- R: Generar un error, esta pasando 2 argumentos
class A:
  def __init__(self):
    pass

a = A(1)
print(hasattr(a, 'A'))


# 9 -- Cual será el resultado de ejecutar el siguiente código? -- Imprimirá b
class A:
  def __str__(self):
    return 'a'

class B(A):
  def __str__(self):
    return 'b'

class C(B):
  pass

o = C()
print(o)

#10- Resultado --- R: True C es subclase de A
print(issubclass(C, A))
  

#11 - R: imprimirá b
class A:
  def a(self):
    print('a')


class B:
  def a(self):
    print('b')


class C(B,A):
  def c(self):
    self.a()


o = C()
o.c()


# 12 --- Resultado: imprimirá a
class A:
  def __str__(self):
    return 'a'


class B:
  def __str__(self):
    return 'b'
  
class D:
  def __str__(self):
    return 'DDD'

class C(A, B):
  pass

o = C()
print(o) # Imprime a pues al heredar de B y ya estar el metodo __str__ ignora el último


# 13 === Imprimirá 1
class A:
  v = 2

class B(A):
  v = 1

class C(B):
  pass

o = C()
print(o.v)

# 14 --- R: bcac
def f(x):
  try:
    x = x / x
  except:
    print("a",end='')
  else:
    print("b",end='')
  finally:
    print("c",end='')

f(1)
f(0)

# 15 ----- imprimirá 3
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))


# 16 ----- imprimirá ex
class Ex(Exception):
  def __init__(self, msg):
      Exception.__init__(self, msg + msg)
      self.args = (msg,)


try:
  raise Ex('ex')
except Ex as e:
  print(e)
except Exception as e:
  print(e)

# 17 -- imprimirá abc
class I:
  def __init__(self):
    self.s = 'abc'
    self.i = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.i == len(self.s):
      raise StopIteration
    v = self.s[self.i]
    self.i += 1
    return v


for x in I():
  print(x,end='')





