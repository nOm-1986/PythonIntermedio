#bloques = 1000
bloques = 2
numero_de_capas = 0
total_bloques = 0
anterior = 0
numero_siguiente = 0

while (bloques - total_bloques)  > numero_siguiente:
    numero_de_capas += 1
    numero_siguiente = anterior + 1
    total_bloques = total_bloques + numero_siguiente
    anterior = numero_siguiente
    print(f'Bloques usados: {total_bloques}... Capa actual: {numero_de_capas} ... Bloques restantes: {bloques - total_bloques}')
    
print('Numero de capas: ', numero_de_capas)

x = 1
x = x == x
print(x)

i = 0
while i <= 3 :
    i += 2
    print("*")

i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
        break
    print("*")

for i in range(1):
    print("#")
else:
    print('#')

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print('#')
    

var = 1
while var < 10:
    print("#")
    var = var << 1

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)

my_list = [1,2,3,4]
print(my_list[-3:-2])

vals = [0,1,2]
vals.insert(0,1)
del vals[1]
print(sum(vals))

nums = [1,2,3]
vals = nums[-1:-2]
print(vals)

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

my_list = [i for i in range(-1, 2)]
print(my_list)

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

my_list = [[0,1,2,3] for i in range(2)]
print(my_list[2][0])

