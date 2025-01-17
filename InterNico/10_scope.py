price = 100

def increment():
    global price
    price = 200
    return price

def remove():
    price: int = 320
    price = price - 10
    print(price)


print(price)
print(increment())
print(price)
remove()

