def sprawdz_litery(wejscie, wejscie2):
    lista=[]
    for i in wejscie:
        lista.append(i)
    return lista.count(wejscie2)


wejscie=input("Podaj zdanie: ")
wejscie2=input("Podaj litere: ")
wynik = sprawdz_litery(wejscie, wejscie2)
print(f"{wynik}")

