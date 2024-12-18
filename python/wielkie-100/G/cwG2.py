import pyinputplus as p

#funkcja pobierająca dokładnie jeden znak od użytkownika
def pobierz_dane():
    inp=p.inputStr(prompt="Podaj znak: ", blockRegexes=[r"^..$"])
    return inp

#funkcja, która sprawdza czy wpisana została mała litera, w innym wypadku instrukcja funkcji się powtórzy
def glowna():
    while True:
        a=pobierz_dane()
        if a.islower():
            print(a)
            break

if __name__=="__main__":
    glowna()