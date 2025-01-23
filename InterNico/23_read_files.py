file = open("../archivos/names.txt")
print(file.readline())

def read():
    #number = list()
    with open("../archivos/numbers.txt", "r", encoding="utf-8") as f:
        number = [ int( x ) for x in f]
        # for line in f:
        #     number.append(int(line))
    print(number)


#open(ruta, 'r+') ---> Donde r+ es para dar permisos de lectura y escritura no sobre escribe el archivo a diferencia de w+
#open(ruta, 'w+') ---> Donde r+ es para dar permisos de lectura y escritura pero va a reescribir

def write():
    names = ['Fabian', 'Adrian', 'Leidy', 'María José', 'Karen','Fabiola', 'Alberto']
    with open('./archivos/names.txt', "w", encoding='utf-8') as f:
    # with open('./archivos/names.txt', "a", encoding='utf-8') as f: -> usando a de append
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()
    write() 


if __name__ == '__main__':
    run()