import pyinputplus as pyi

''' Zadanie 1 - Program, który wyznacza daną permutację z podanych "n" i "k". '''

#funkcja do obliczania silni
def silnia(x):  
    sil=1
    for i in range(1, x+1):
        sil*=i
    return sil
#print(silnia(5))

#funkcja do tworzenia tablicy z cyframi, które pózniej będą wykorzystywane do tworzenia permutacji
def ilosc_cyfr(x):  
    tab=[]
    for i in range(1, x+1):
        tab.append(i)
    return tab
#print(ilosc_cyfr(5))

#funkcja wybiera cyfry z listy i wstawia je do stringa
def wybieranie_cyfry(n, k, c, s):
    if len(c)==0: #gdy lista jest pusta zwraca wynik - stringa
        return s
    else:
        z=silnia(len(c)-1)  #(n-1)!
        p=(k-1)//z  # p daje indeks do listy z cyframi, to jest to samo co wzór "p=(k-1)/(n-1)!"
        s+= f"{c[p]}" #dopisanie cyfry do stringa
        c.pop(p) #usunięcie pobranej cyfry z listy
        k=k-p*z  # nowa wartość k
        return wybieranie_cyfry(n, k, c, s) #operacja rekurencyjna

strg=""
n=pyi.inputInt(prompt="Podaj ilość cyfr: (min - 3, max - 9): \n> ", min=3, max=9)
cyfry=ilosc_cyfr(n) #ilość cyfr jest uzależniona od n
k=pyi.inputInt(prompt="Podaj wartość permutacji:\n> ", min=1, max=silnia(n))
wynik=wybieranie_cyfry(n, k, cyfry, strg)
print(f"Permutacja o l.p. {k} ---> {wynik}")