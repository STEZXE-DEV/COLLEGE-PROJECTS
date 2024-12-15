ala=5.4
ola=2
lista=["Ala", "ma", 4, "koty"]
print(str(ala))
print(str(ola))

#konwersja każdego elementu listy na str
for i in range(0, len(lista)):
    a=str(lista[i])
    lista.insert(i, a)
    del lista[i+1]

#złączenie elementów listy
print(' '.join(lista))