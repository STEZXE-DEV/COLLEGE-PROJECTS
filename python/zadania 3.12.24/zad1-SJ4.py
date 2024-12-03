def wylicz_element_ciagu(n):
    n0=0
    n1=1

    for i in range(1,wejscie+1):
        fib=n0+n1
        n0=n1
        print(f"{n0}", end=" ")
        n1=fib
    return fib
while True:
    wejscie=input("\nPodaj dlugosc ciagu fibonacciego: ")
    if wejscie.isdigit():
        wejscie=int(wejscie)
        if wejscie<=0:
            print(f"'{wejscie}' to nie jest prawidlowa liczba!")
        else:
            ciag_fib = wylicz_element_ciagu(wejscie)
    elif not wejscie.isdigit():
        print(f"'{wejscie}' to nie jest liczba dlugosci ciagu! Podaj liczbę dodatnia!")