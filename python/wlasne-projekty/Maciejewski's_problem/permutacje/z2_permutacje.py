import pyinputplus as pyi

''' Zadanie 2 - Program, który wyznacza kolejność podanej permutacji. '''

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
lista_obecnej_permutacji=[]

#tworzy listę z cyframi permutacji
for i in str(k):
    lista_obecnej_permutacji.append(int(i))

print(f"Lista cyfr permutacji w podanej kolejności: {lista_obecnej_permutacji}")

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