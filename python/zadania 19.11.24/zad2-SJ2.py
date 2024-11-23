import math
while True:
    odpowiedz1 = input("Pole jakiej figury chcesz obliczyc wybierz z podanych kolo/kwadrat/trapez/trojkat: \n")
    match odpowiedz1.lower():
        case "kolo":
            promien = int(input("Podaj promien kola: \n"))
            print(f"Pole kola wynosi: {math.pi*promien**2}")
        case "kwadrat":
            a = int(input("Podaj dlugosc boku kwadratu: \n"))
            print(f"Pole kwadratu wynosi: {a**2}")
        case "trapez":
            a = int(input("Podaj dlugosc pierwszej podstawy trapezu: \n"))
            b = int(input("Podaj dlugosc drugiej podstawy trapezu: \n"))
            h = int(input("Podaj dlugosc wysokosci trapezu: \n "))
            print(f"Pole trapezu wynosi: {((a+b)*h)/2}")
        case "trojkat":
            a = int(input("Podaj dlugosc podstawy trojkata: \n"))
            h = int(input("Podaj dlugosc wysokosci trojkata: \n"))
            print(f"Pole trojkata wynosi: {a*h/2}")
    odpowiedz2=input("Czy chcesz kontynuowac? (tak/nie) \n")
    if odpowiedz2=='tak':
        continue
    elif odpowiedz2=='nie':
        print("Zakonczono program!")
        break
    else:
        print("ERROR - nieprawidlowa odpowiedz na pytanie!")
        break
