liczba=int(input('Podaj liczbę: '))
kopia=liczba
while kopia>0:
    kopia-=1
    if kopia == 0:
        print(liczba)
    else:
        liczba*=kopia