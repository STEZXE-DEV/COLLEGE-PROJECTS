def sprawdz_liczbe(wejscie):
    lista=[]
    for i in range(1, wejscie):
        lista.append(wejscie%i)
    if lista.count(0) == 1:
        wynik='liczba PIERWSZA!'
        return wynik
    else:
        wynik='NIE jest liczba PIERWSZA!'
        return wynik

while True:
    wejscie=str(input("Podaj liczbe (wyjdz by zakonczyc): "))
    if wejscie == 'wyjdz':
        break
    elif wejscie.isdigit():
        if int(wejscie)>1:
            wejscie=int(wejscie)
            wynik=sprawdz_liczbe(wejscie)
            print(f"'{wejscie}' to {wynik}")
        else:
            print("To NIE jest liczba PIERWSZA!")