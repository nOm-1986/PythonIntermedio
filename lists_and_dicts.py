def run():
    my_list = [1, 'Hello', True, 4.5, 'Fabian']
    my_dict = {"firstname" : "Fabián", "lastname" : "Beltran"}

    super_list = [
        {"firstname" : "Fabián", "lastname" : "Beltran"},
        {"firstname" : "Maria", "lastname" : "Rivera"},
        {"firstname" : "Karen", "lastname" : "Agredo"},
        {"firstname" : "Zury", "lastname" : "Beleño"},
        {"firstname" : "Yuliza", "lastname" : "Mujica"}
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1,-2,0,1,2],
        "floating_nums": [1.1, 4.5, 6.43, 5.86]
    }

    for key,value in super_dict.items():
        print(key, " - ", value)


    print("\n===========================================\n")

    for a in super_list:
        for k,v in a.items():
            print(k, " - ", v)


    print("\n===========================================\n")

    for a in super_list:
        print(f'{a["firstname"]} {a["lastname"]}')


if __name__ == '__main__':
    run()