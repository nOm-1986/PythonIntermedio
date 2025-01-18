numbers = list(x for x in range(1, 21))

new_numbers = list(filter(lambda x: x % 3 == 0, numbers))
print(new_numbers)