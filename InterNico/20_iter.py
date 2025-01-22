for i in range(1, 11):
    pass
    #print(i)

my_iter = iter(range(1,4))
print(my_iter)
#Para ir iterando utilizo next, ya que lo hemos convertido en algo iterable
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))