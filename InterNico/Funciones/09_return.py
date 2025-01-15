def find_volume(length:int = 1, width:int = 1, depth:int = 1):
    return length * width * depth

def with_multiples_returns(a,b,c):
    return a, b,c

vol1 = find_volume()
print(vol1)
vol2 = find_volume(width=3)
print(vol2)

print('+'*40)
res1,  res2, res3 = with_multiples_returns('a', 'b', 'c')
print(res1)
print(res2)
print(res3)