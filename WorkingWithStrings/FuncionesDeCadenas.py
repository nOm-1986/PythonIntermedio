import datetime


def stringsToChars():
    a, b, c, d, e = 23, 3.45, 2-3j, 8.56e+12, 1
    print(str(a), str(b), str(c), str(d), str(e))


def dateToChar():
    something = str(datetime.datetime(2022, 5,8, 5, 35))
    print(type(something), something)

def strings_to_numbers():
    '''Python lets us transform characters in numbers corresponding to Unicode table using the ord function. 
    '''
    my_var = ''.join([chr(x+1) for x in range(200)])
    print(my_var)

    my_var2 = ' '.join([chr(x+9812) for x in range(12)])
    print(my_var2)


if __name__ == '__main__':
    #stringsToChars()
    #dateToChar()
    strings_to_numbers()
