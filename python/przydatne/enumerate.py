a=input("Podaj szukany element\n> ") #a - szukana
print()

lista=["jeden","dwa","trzy","cztery","pięć"]

for i in enumerate(lista): #dla każdego elementu i
    print(i) #zwraca ktrotkę (indeks, wartość)

for i,v in enumerate(lista): #i - indeks, v - wartość
    if v == a: #jeśli wartość == szukana
        print(f"\nIndeks szukanej wartości w liście: {i}") #zwraca indeks
