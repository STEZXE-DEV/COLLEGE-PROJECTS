a=int(input("Podaj liczbę: "))
metody={1:"binarny", 2:"ósemkowy", 3:"szesnastkowy"}
for k,v in metody.items():
    print(f"{k} - {v}")
metoda=int(input("Podaj numer systemu z listy: "))
if metoda in metody.keys():
    match metoda:
        case 1:
            print(f"Wybrano System {metody[metoda].capitalize()},\nPodana liczba w tym systemie wynosi: {bin(a)[2:]}")
        case 2:
            print(f"Wybrano System {metody[metoda].capitalize()},\nPodana liczba w tym systemie wynosi: {oct(a)[2:]}")
        case 3:
            print(f"Wybrano System {metody[metoda].capitalize()},\nPodana liczba w tym systemie wynosi: {hex(a)[2:]}")