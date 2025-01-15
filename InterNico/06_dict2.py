import random

coutries = ['col', 'mex', 'bol', 'pe', 've']
population_v2 = { country: random.randint(1, 100) for country in coutries}
print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population > 70}
result2 = { country: population for (country, population) in population_v2.items() if 'o' in country}
print(result)
print(result2)

print('='*40)
text = 'Hola, soy Fabian'
unique = { c: c.upper() for c in text if c in 'aeiou'}
print(unique)