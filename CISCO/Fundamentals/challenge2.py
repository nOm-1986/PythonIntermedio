def f(x):
  if x == 0:
    return 0
  return x + f(x - 1)

print(f(3))

def fun(x):
  x += 1
  return x

x = 2
x = fun(x + 1)
print(x)

# +++++++++++++++++++++++++++++++++
dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])

# =====================================
def func_1(a):
  return a ** a

def func_2(a):
  return func_1(a) * func_1(a)

print(func_2(2))


# =====================================

def fun(x):
  if x % 2 == 0: return 1
  else: return

print(fun(fun(2)) + 1)

# =====================================
def fun(x):
  global y
  y = x * x
  return y

fun(2)
print(y)

# =====================================
def any():
  print(var + 1, end='')

var = 1
any()
print(var)

# ======================================
my_tuple = (1, 2, 4, 8)
#del my_tuple[0]
#print(my_tuple)
my_tuple[1] = my_tuple[1] = my_tuple[0]
print(my_tuple)


# ===============================
# Error my_list fue sobre escrito como función
my_list =  ['Mary', 'had', 'a', 'little', 'lamb']

def my_list(my_list):
  del my_list[3]
  my_list[3] = 'ram'

print(my_list(my_list))

# =======================================
def fun(x, y, z):
  return x + 2 * y + 3 * z

print(fun(0, z=1, y=3))

# ====================================

def fun(inp=2, out=3):
  return inp * out

print(fun(out=2))

# ===================================
dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
  v = dictionary[v]

print(v)


# ===================
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

# try -- catch
try:
  print('Con un error de sintaxis que sigue...')
  print('Error intencional')
except:
  print('Manejando el error...')


# ==============================================
try:
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")




