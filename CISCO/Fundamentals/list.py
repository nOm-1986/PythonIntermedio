# A life inside lists
list_1 = [x for x in range(1, 11)]
list_2 = list_1
print(list_1, list_2, sep=" --- ")
list_2.pop(0)
print(list_1, list_2, sep=" --- ")

# El nombre de una lista es el nombre de una ubicación de memoria donde se almacena
# lista_1 = D00000  Si igualo otra lista esta tambien apunta al mismo espacio en memoria.
# La asignación: list_2 = list_1 copia el nombre del arreglo no su contenido. 
# En efecto, los dos nombres (list_1 y list_2) identifican la misma ubicación en la memoria de la computadora. 
# Modificar uno de ellos afecta al otro, y viceversa.

# SOLUCIÓN

list_3 = [x for x in range(1, 20) if x % 2 == 0]
# Slicing list ===== my_list[inicio:fin]
list_2 = list_1[:]
list_4 = list_3[1:-1]
print(list_3, list_4)

# More about DEL instruction
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
del my_list[:]
print(my_list)
del my_list
print(my_list)

# 3.6.4 -- in y not in to work with List in python
# Python have two powerfull operators that let you to check if a list have a value inside it.
# elem in my_list --- elem not in my_list

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

# Some simple programs
my_list = [12,4,54,6,7,809,4,122,1,3,54,6,7,8,9,23]
largest = my_list[0]

for i in range(1, len(my_list)):
  if my_list[i] > largest:
    largest = my_list[i]
print(largest)

# Using for i in my_list
my_list = [12,4,54,6,7,809,4,1222,1,3,54,6,7,8,9,23]
largest = my_list[0]
#for i in my_list:
for i in my_list[1:]: # para se más optimo no comparo el primero ya se que son iguales.
  if i > largest:
    largest = i
print(largest)


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
  if number in drawn:
    hits += 1

print(hits)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
uniq_list = []
for number in my_list:   
    if number not in uniq_list:
        uniq_list.append(number)
print("La lista con elementos únicos:")
print(uniq_list)
