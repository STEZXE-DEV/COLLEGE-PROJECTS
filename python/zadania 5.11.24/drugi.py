while True:
    liczba2 = int(input("Podaj liczbe (sprawdzanie parzystosci)\n"))
    reszta = liczba2%2
    if reszta==int(0):
        print("Liczba jest parzysta.")
    else:
        print("Liczba jest nieparzysta.")