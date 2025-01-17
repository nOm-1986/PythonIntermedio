def increment(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

# 2 + func(2 +1)
result = high_ord_func(2, increment)
print(result)