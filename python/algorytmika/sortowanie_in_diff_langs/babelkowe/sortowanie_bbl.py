import random as r

def bubbleSort(alist):
    x = True
    z = 1
    while x:
        x = False
        for i in range(len(alist) - z):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                x = True
        z += 1 


lista = [1,2,333,444,5,5,6,67,7,3,88]
lista2 = [1,2,333,444,5,5,6,67,7,3,88]
print(bubbleSort(lista)) #jeśli nie wystąpi dyrektywa return to zwraca None
bubbleSort(lista2) #wywołanie funkcji
print(lista2)