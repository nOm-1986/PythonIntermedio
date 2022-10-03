def run():
    clist = [a**2 for a in range(1,101)]
    print(clist, "Mensaje")

    clist2 = [a**2 for a in range(1,101) if a % 3 != 0]
    print(clist2, "Dif")

if __name__ == '__main__':
    run()