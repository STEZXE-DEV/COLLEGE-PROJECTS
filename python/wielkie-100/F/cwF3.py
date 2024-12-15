import pyinputplus as p

a = p.inputStr(prompt='Podaj tekst: ')

# moduł .find('słowo') odnajduje w łańcuchu znaków słowo i zwraca jego pozycję indeksu (od 0)
# jeśli nie znajdzie słowa zwraca wartość -1
a = a.find('jest')

if a>=0:
    print(f"Znaleziono słowo \"jest\" na indkesie {a}")
else:
    print(f"Nie znaleziono słowa \"jest\"")