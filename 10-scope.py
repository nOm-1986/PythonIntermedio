#Variable de alcance Global.
price: int = 100;

def increment():
    #print(price)
    price: int = 200
    price = price + 10
    print(price)


print(price)
increment()