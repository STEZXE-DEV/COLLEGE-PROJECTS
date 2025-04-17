
def wstaw(l, s, k):
    for i in range(s+k, len(l), k):
        wartosc = l[i]
        indeks =i
        while indeks >= k and l[indeks-k]>wartosc:
            l[indeks]=l[indeks-k]
            indeks=indeks-k
        l[indeks]=wartosc

def sort_shell(lista):
    krok = len(lista)//2
    while krok>0:
        for i in range(0, krok):
            wstaw(lista, i, krok)
        krok//=2

lista = [1,2,333,444,5,5,6,67,7,1,88]
sort_shell(lista)
print(lista)