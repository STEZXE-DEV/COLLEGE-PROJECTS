import pyinputplus as p

'''Symbol Newtona to oznaczenie współczynnika Newtona, używanego w matematyce, głównie w kombinatoryce.
   Zapisuje się go w postaci symbolu Newtona (symbolu dwumianowego), czyli „n nad k”,
   co oznacza liczbę sposobów wybrania k elementów z n-elementowego zbioru bez uwzględniania kolejności.'''

#funkcja obliczająca silnię.
def silnia(x):
    sil=1
    for i in range(1, x+1):
        sil*=i
    return sil

#funkcja pobierająca wartości n i k.
def pobierz_dane():
    n=p.inputInt(prompt="Podaj n:\n> ", min=0)
    k=p.inputInt(prompt="Podaj k:\n> ", min=0)
    if k>n:
        print(f"Nie można wybrać {k} elementów z {n}, liczba takich kombinacji wynosi 0!")
        exit()
    else:
        return n,k

#funkcja obliczająca symbol Newtona wedle wzoru   
def oblicz_dwumian(n,k):
    l=silnia(n) #licznik
    m=silnia(k)*silnia(n-k) #mianownik
    return l/m
    
n,k = pobierz_dane()
wynik = int(oblicz_dwumian(n,k))
print(f"Dwumian Newtona {n} nad {k} wynosi ---> {wynik}")