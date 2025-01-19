import functools

numbers = [x for x in range(1, 5)]

def accum(counter, item):
    print('Counter =>',counter)
    print('Item =>', item)
    return counter + item

result1 = functools.reduce(lambda counter, item: counter + item, numbers)
result2 = functools.reduce(accum, numbers)
print(f'Resultado 1:  {result1}')
print(f'Resultado 2:  {result2}')

