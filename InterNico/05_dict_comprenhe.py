import random
dict1 = {x:x*2 for x in range(1,11)}
print(dict1)

print("+"*40)
coutries = ['col', 'mex', 'bol', 'pe', 've']
population = {x: random.randint(200, 500) for x in coutries}
print(population)

print("+"*40)
names = ['nico', 'fabo', 'majo']
ages = ['23', '38', '5']
unionZip = list(zip(names, ages))
print(unionZip)