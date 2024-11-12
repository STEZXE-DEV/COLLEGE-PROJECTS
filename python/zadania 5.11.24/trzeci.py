while True:
    zakres1 = int(input("Podaj liczbe poczatku zakresu\n"))
    zakres2 = int(input("Podaj liczbe konca zakresu\n"))
    print("\n==========WYNIKI===PARZYSTE===========")
    for i in range(zakres1, zakres2):
        if i%2==int(0):
            print(i)
    print("==========WYNIKI===NIEPARZYSTE===========")
    for i in range(zakres1, zakres2):
        if i%2==int(1):
            print(i)