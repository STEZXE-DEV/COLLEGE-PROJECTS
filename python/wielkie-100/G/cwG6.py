import pyinputplus as p


#funkcja pobierająca input w systemie dziesiętnym będący liczbą całkowitą nieujemną

def pobierz_dane():
    inp=p.inputInt(prompt="Podaj liczbę w sys. dziesiętnym: ", min=0)
    return inp


#funkcja, która dokonuje odbicia lustrzanego liczby w sys. dz.,
#a następnie weryfikuje czy liczby (stringi) są sobie równe,
#zwraca uzyskaną liczbę lustrzaną lub <"Nie istnieje!">

def dziesietna_liczba_lustrzana(a):
    x=[]
    for i in str(a):
        x.append(i)
    x.reverse()
    b=int(''.join(x))
    if a==b:
        return b
    else:
        return "Nie istnieje!"


#funkcja, która dokonuje odbicia lustrzanego liczby w sys. bin.,
#a następnie weryfikuje czy liczby (stringi) są sobie równe,
#zwraca uzyskaną liczbę lustrzaną lub <"Nie istnieje!">

def binarna_liczba_lustrzana(a):
    x=[]
    for i in a:
        x.append(i)
    x.reverse()
    y=''.join(x)
    if y==a:
        return y
    else:
        return "Nie istnieje!"


#funkcja, która dokonuje odbicia lustrzanego liczby w sys. hex.,
#a następnie weryfikuje czy liczby (stringi) są sobie równe,
#zwraca uzyskaną liczbę lustrzaną lub <"Nie istnieje!">

def heksadecymalna_liczba_lustrzana(a):
    x=[]
    for i in a:
        x.append(i)
    x.reverse()
    y=''.join(x)
    if y==a:
        return y
    else:
        return "Nie istnieje!"


#funkcja, która wypisuje na ekranie liczbę podaną i jej liczbę lustrzaną dla każdego obsługiwanego systemu

def wyswietl():

    liczba_dz=pobierz_dane()
    mirror_dz=dziesietna_liczba_lustrzana(liczba_dz)

    liczba_bin=bin(liczba_dz)
    mirror_bin=binarna_liczba_lustrzana(liczba_bin[2:])

    liczba_hex=hex(liczba_dz)
    mirror_hex=heksadecymalna_liczba_lustrzana(liczba_hex[2:])

    print(f"Podana liczba: {liczba_dz} | Liczba lustrzana: {mirror_dz}")
    print(f"Podana liczba w sys. bin.: {liczba_bin[2:]} | Liczba do niej lustrzana: {mirror_bin}")
    print(f"Podana liczba w sys. hex.: {liczba_hex[2:]} | Liczba do niej lustrzana: {mirror_hex}")
    
if __name__=="__main__":
    wyswietl()