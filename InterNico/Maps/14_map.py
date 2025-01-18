numbers = [x for x in range(1, 20)]
numbers_v2 = []

numbers_v2 = list(map(lambda x : x * 2, numbers))
print(numbers_v2)
print('++' * 30)
# Iterando 2 listas de distinta longitud
numbers_1 = [x for x in range(1, 5)]
numbers_2 = [x for x in range(1, 4)]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)


numbers = [1, 2, 3, 4]
response = list(map(lambda x: x*2, numbers))
print(response)