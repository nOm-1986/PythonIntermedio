''''
LAMBDA
Una función lambda es una función sin nombre (también puedes llamarla una función anónima).
'''

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(a, sqr(a),sep=' -- ',end=" - ")
    print(pwr(a, two()))

