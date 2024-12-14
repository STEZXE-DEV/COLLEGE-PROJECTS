#rekurencja to funkcja, która wywołuje sama siebie (w pierwotnej postaci tworzy pętlę nieskonczoną, dlatego trzeba zastosować warunek)
#ograniczona jest o maksymalną ilość rekurencji
# def FunckcjaRekurencyjna():
#     if (warunek):
#         return 2*FunckcjaRekurencyjna()
#     return 1

def Silnia(n):
    if n==1:
        return 1
    else:
        return n*(Silnia(n-1))
    
n=int(input())
wynik=Silnia(n)
print(wynik)
