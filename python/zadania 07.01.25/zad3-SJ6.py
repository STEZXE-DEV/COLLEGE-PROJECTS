import pyinputplus as p

litery = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 
    'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 
    'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 
    'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

keywordy=[" YOU ", " YOUR ", " AND ", " IS ", " ARE ", " THAT ", " THIS ", " THE ", " HOW ", " HE ", " SHE ", " IT ", " LIKE ", " WHICH ", " WITH ", " FOR ", " WAS ", " WERE ", " HAVE "]

def pobierz_dane_do_szyfrowania():
    inp1=p.inputStr(prompt="Podaj wiadomość: ")
    inp2=p.inputInt(prompt="Podaj klucz: ", min=1, max=25)
    return inp1.upper(),inp2

def pobierz_dane_do_deszyfrowania():
    inp1=p.inputStr(prompt="Podaj zaszyfrowaną wiadomość: ")
    return inp1.upper()

def szyfrowanie(a, b):
    x=[]
    y=[]
    for i in a:
        if i==" ":
            x.append(i)
        if i.upper() in litery.keys():
            x.append((litery[i]+b)%26)
    for i in x:
        if i==" ":
            y.append(i)
        if i in litery.values():
            for k,v in litery.items():
                if i==v:
                    y.append(k)
                
    return ''.join(y).lower()

def deszyfrowanie(a):
    x=[]
    y=[]
    for j in range(1,26):
        for i in a:
            if i==" ":
                x.append(i)
            if i in litery.keys():
                x.append((litery[i]-j)%26)
        x.append(",")
    for i in x:
        if i == " " or i == ",":
            y.append(i)
        for k,v in litery.items():
            if i == v:
                y.append(k)
    y.pop()
    tekst=''.join(y)
    wyniki=tekst.split(",")
    return wyniki

def wybrana_wiadomosc():
    inp=p.inputInt(prompt="Wybierz numer wiadomości: ", min=1, max=25)
    return inp

wybor=p.inputInt(prompt="1 - Szyfrowanie wiadomości\n2 - Deszyfrowanie wiadomości\nPodaj cyfrę wyboru: ", min=1, max=2)

match wybor:
    case 1:
        wiad,klucz=pobierz_dane_do_szyfrowania()
        wynik=szyfrowanie(wiad, klucz)
        print(f"Zaszyfrowana wiadomość: {wynik}")
    case 2:
        wiad=pobierz_dane_do_deszyfrowania()
        wynik=deszyfrowanie(wiad)
        j=1
        for i in wynik:
            if any(x in i for x in keywordy):
                print("\nZnaleziono keyworda!")
                print(f"Klucz {j}. Wiadomość: {i.lower()}")
                break
            else:
                j+=1
        if j>25:
            print("\nNie znaleziono keyworda!")
            j=1
            for i in wynik:
                print(f"Klucz {j}. Wiadomość: {i.lower()}")
                j+=1
            j=1
            num=wybrana_wiadomosc()
            for i in wynik:
                if num==j:
                    print(f"Rozszyforwana wiadomość: {i.lower()}, Klucz = {j}")
                    break
                else:
                    j+=1