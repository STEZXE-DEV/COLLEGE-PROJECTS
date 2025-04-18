import pyinputplus as pyi

''' Zadanie 3 - Program, który wyznacza kolejną w kolejności permutację z podanej permutacji. '''

#funkcja do obliczania silni
def silnia(x):  
    sil=1
    for i in range(1, x+1):
        sil*=i
    return sil

#funkcja do tworzenia tablicy z cyframi, które pózniej będą wykorzystywane do tworzenia permutacji
def ilosc_cyfr(x):  
    tab=[]
    for i in range(1, x+1):
        tab.append(i)
    return tab

#funkcja znajduje element w tablicy i go usuwa, a zwraca indeks tego elementu
def znajdz(tab, szukany):
    for i in range(0, len(tab)):
        if szukany==tab[i]:
            tab.remove(szukany)
            return i

k=pyi.inputInt(prompt="Podaj zapis permutacji:\n> ", min=1, max=987654321, blockRegexes=[r"0"])
if k==987654321:
    print("Podano ostatnią możliwą permutację niepowtarzających się liczb od 1 do 9!")
    exit()
lista_obecnej_permutacji=[]

#tworzy listę z cyframi permutacji
for i in str(k):
    lista_obecnej_permutacji.append(int(i))

print(f"Lista cyfr podanej permutacji w kolejności: {lista_obecnej_permutacji}")

#<cyfry> - lista cyfr, które występują w permutacji, ułożone w rosnącej kolejności (prawdopodobnie można było tu zastosować także lista_obecnej_permutacji.sort())
cyfry=ilosc_cyfr(len(lista_obecnej_permutacji)) #jednakże tak zapisana zmienna pozwala na pózniejszą walidację poprawności inputa
print(f"Lista dozwolonych cyfr w permutacji: {cyfry}")

#<wartosc_cyfr=1>, dlatego że jeśli nie zachodzi żadna zmiana w permutacji daje ona wartość 0, a powinniśmy numerować od 1
wartosc_cyfr=1

for i in lista_obecnej_permutacji:
    z=znajdz(cyfry, i)

    #jeśli funkcja <znajdz()> zwraca None to oznacza nieprawidłowy zapis permutacji
    if z==None:
        print("======== Źle podany zapis permutacji! ========")
        exit()
        break

    #po działaniu funkcji <znajdz()> z listy <cyfry> znika znaleziony element więc funkcja <silnia()> przyjmuje argument n-1
    z*=silnia(len(cyfry)) 
    wartosc_cyfr+=z
    
print(f"L.p. dla podanego zapisu permutacji ---> {wartosc_cyfr}")

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
k=wartosc_cyfr+1
n=len(lista_obecnej_permutacji)
cyfry=ilosc_cyfr(n) #ilość cyfr jest uzależniona od n
wynik=wybieranie_cyfry(n, k, cyfry, strg)
print(f"Permutacja o l.p. {k} (następna) ---> {wynik}")