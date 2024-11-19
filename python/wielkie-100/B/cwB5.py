#pobranie wejscia od uzytkownika
wejscie = input("Podaj wlasciwosci: <grubosc_linii>, <numer_warstwy>: <x0> <y0> <x1> <y1>,<nazwa_linii> \n")
#podzial inputa funkcja split
wynik_wejscia=wejscie.split(", ", 1)
#deklaracja grubosci linii w typie float
grubosc_linii=float(wynik_wejscia[0])
#kolejny podzial
wynik_wejscia=wynik_wejscia[1].split(": ", 1)
#deklaracja numeru warstwy
numer_warstwy=int(wynik_wejscia[0])
#podzial na 3 elementy ktore sa oddzielone od siebie spacja
wynik_wejscia=wynik_wejscia[1].split(" ", 3)
#deklaracja x0,x1,y0
x0=int(wynik_wejscia[0])
y0=int(wynik_wejscia[1])
x1=float(wynik_wejscia[2])
#kolejny podzial ze wzgledu na to, ze po y1 wystepuje przecinek a po nim nazwa linii
wynik_wejscia=wynik_wejscia[3].split(",", 1)
#deklaracja y1
y1=float(wynik_wejscia[0])
#deklaracja nazwy linii
nazwa_linii=wynik_wejscia[1]
#deklaracja tablic z wynikami - wyjscie1 i wyjscie2
wyjscie1=[nazwa_linii, grubosc_linii, numer_warstwy]
wyjscie2=[x0,y0,x1,y1]
#wypisanie wynikow zgodnie z zasadami podanymi w zadaniu
print(f"Linia\t\t:{wyjscie1[0]}") #odwolanie do elementu tablicy poprzez tablica[indeks elementu]
print(f"Grubosc linii\t:{wyjscie1[1]}")
print(f"Numer warstwy   :{wyjscie1[2]}")
print(f"P1=({wyjscie2[0]},{wyjscie2[1]}) ", end='')
print(f"P2=({wyjscie2[2]},{wyjscie2[3]})")
