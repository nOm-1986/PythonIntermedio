my_list = [1, 2]

for v in range(2):
  my_list.insert(-1, my_list[v])
  print(my_list)


# ==========================
def func_1(a):
  return None

def func_2(a):
  return func_1(a) * func_1(a)

print(func_2(2))


# ===========================
print(1//2)

# ===========================
def func(a,b):
  return b ** a

print(func(b=2, 2))


# ===========================
z = 0
y = 10
x = y < z and z > y or y < z and z < y
print(x)

# Laca feo papa, crear una variable print sobre escribe el metodo print xD
# print = 200
# print(print)

my_list = [x * x for x in range(5)]
print(my_list)
def fun(lst):
  del lst[lst[2]]
  return lst
print(fun(my_list))


# ====================================
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)

# ===================================
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

# ==================================
def fun(x):
  if x % 2 == 0:
    return 1
  else:
    return 2

print(fun(fun(2)))

# ==================================
nums = [1, 2, 3]
vals = nums
del vals[:]

print(vals)
print(nums)

# ==================================
x = 3
y = 2
x = x % y
x = x % y
y = y % x
print(y)

#=======================
print('a', 'b', 'c', sep='sep')

# =======================
x = 1 // 5 + 1 / 5
print(x)

# =====================================
x = 2.0
y = 4.0
print(y ** (1/x))

# ====================================
lst = [i for i in range(-1, -2)]
print(lst)


#  ==================================
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)

print(fun(0, 3))

# ==============================
# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")

# ==================================
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

dd = {"1": "0", "0": "1"}
for x in dd.vals():
    print(x, end="")

# ===================================
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

# ========================
lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

# ==============================
try:
  print(5/0)
  #break
except (ValueError, ZeroDivisionError):
  print("Mala suerte...")
except TypeError, ZeroDivisionError, ValueError:
   print('pailas')
except:
  print("Lo siento, algo salió mal...")

# ============
foo = (1, 2, 3)
foo.index(0)

# ==========================
print(Hola mundo)















