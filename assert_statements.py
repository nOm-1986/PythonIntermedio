""" Los errores en el código:
    con asserts
"""
def divisors(num):
    divisors = [ x for x in range(1, num + 1) if num % x == 0]
    return divisors
        

def run():
    num = input('Favor ingrese un número: ')
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un número"
    print(divisors(int(num)))
    print('Terminó mi programa')


if __name__ == '__main__':
    run()