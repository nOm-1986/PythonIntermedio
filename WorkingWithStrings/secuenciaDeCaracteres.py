"""
    Utilizando las comillas en python
"""

def run():
    a = "Esto es una frase 'corta' usando comillas simples"
    b = 'Esto es una frease "corta" usando cimillas dobles'
    c = 'Fase simple convertida en párrafo\n \
        Haciendo uso del carácter \\ para separar las frases'
    d = '''En esta frase se usan comillas 'simples' y "dobles" dentro de la frase '''
    e = """Tambien puedo utilizar las 
        comillas dobles "comillas" 
        o simples 'simples' 
        con espaciado """
    print(e)

def evaluacionCadenaVacia():
    print(bool('') == False, """--> evaluación: bool('') == False """)
    print(bool("") == False, """--> evaluación: bool("") == False """)
    print(bool("""""") == False, """--> evaluación: bool(""" """) == False """)
    print(bool('''''') == False, """--> evaluación: bool('''''') == False """)



if __name__ == '__main__':
    #run()
    evaluacionCadenaVacia()