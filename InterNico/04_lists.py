numbers = []
for element in range(1, 11):
    numbers.append(element)
print(numbers)

numbers_v2 = [x for x in range(1, 11)]
print(numbers_v2)

even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print(even_numbers)