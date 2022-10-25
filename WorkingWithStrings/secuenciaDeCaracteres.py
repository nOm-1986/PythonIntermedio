"""
    Utilizando las comillas en python
"""

def run():
    a = "Esto es una frase 'corta' usando comillas simples"
    b = 'Esto es una frease "corta" usando comillas dobles'
    c = 'Frase simple convertida en párrafo\n \
        Haciendo uso del carácter \\ para separar las frases'
    d = '''En esta frase se usan comillas 'simples' y "dobles" dentro de la frase '''
    e = """Tambien puedo utilizar las 
        comillas dobles "comillas" 
        o simples 'simples' 
        con espaciado """
    f = '''
     ____  _        _  _____ ________ 
    |  _ \| |      / \|_   _|__  |_ _|
    | |_) | |     / _ \ | |   / / | | 
    |  __/| |___ / ___ \| |  / /_ | | 
    |_|   |_____/_/   \_|_| /____|___|
    '''
    print(f)

def evaluacionCadenaVacia():
    print(bool('') == False, """--> evaluación: bool('') == False """)
    print(bool("") == False, """--> evaluación: bool("") == False """)
    print(bool("""""") == False, """--> evaluación: bool(""" """) == False """)
    print(bool('''''') == False, """--> evaluación: bool('''''') == False """)



if __name__ == '__main__':
    run()
    #evaluacionCadenaVacia()