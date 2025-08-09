my_list = [8, 10, 6, 2, 4]  # lista a ordenar

for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
  if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.
  #print(my_list)


my_list = [8, 10, 6, 2, 4]

swapp = True

while swapp:
  swapp = False
  for i in range(len(my_list) - 1):
    print(my_list)
    if my_list[i] > my_list[i + 1]:
      swapp = True
      my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
