""" Los errores en el código:
    * - Cuando python nos avisa que nos equivocamos:
            Devuelve un traceback
            -SyntaxError: Cuando escribimos mal el nombre de una función. - Detiene el programa, no se ejecuta.
            -Exception: Suceden en un puton del programa que quiebra toda la lógica. Lo hace en una línea específica.
                -KeyboardInterrupt: pulsamos ctrl + c interrumpiendo el proceso en consola.
                -KeyError: Cuando intentamos acceder a una llave en un diccionario y esta no existe.
                -IndexError: Cuando trabajamos con listas y un indice en esa lista no existe.
                -FileNotFoundError: Intentamos abrir un archivo que no existe
                -ZeroDivisionError: Intentamos dividir un número entre cero
                -ImportError: Cuando intentamos importar algun módulo y hay algún error en el módulo y algo falla.
        -Consultar los tipos de excepciones que maneja python
            

    * - Cuando python no nos avisa:
            Haciendo debbugin
"""
def divisors(num):
    try:
        if num < 0:
            raise ValueError('Ingresa un número positivo')
        divisors = [ x for x in range(1, num + 1) if num % x == 0]
        return divisors
        
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input('Favor ingrese un número: '))
        print(divisors(num))
        print('Terminó mi programa')

    except ValueError:
        print('Debes ingresar un número')

if __name__ == '__main__':
    run()