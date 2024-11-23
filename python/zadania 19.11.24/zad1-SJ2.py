while True:
    podstawa = int(input("Podaj dlugosc podstawy: "))
    wysokosc = int(input("Podaj dlugosc wysokosci: "))
    pole=podstawa*wysokosc/2
    print(pole)
    pytanie=str(input("Czy chcesz analizowac kolejny trojkat? (wpisz tak/nie): "))
    if pytanie=='nie':
        print("Zakonczono program!")
        break
    elif pytanie=='tak':
        continue
    else:
        print("ERROR - nieprawidlowa odpowiedz na pytanie")
        break