def sum_with_range(min:int, max: int ):
    sum = 0
    for x in range(min, max):
        sum += x
    print(sum)
    return sum

result = sum_with_range(1,20)
print(f'El resultado es: {result}')
result2 = sum_with_range(10,30)
print(f'El resultado es: {result2}')
