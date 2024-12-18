import pyinputplus as p

def pobierz_dane():
    inp=p.inputInt(prompt="Podaj liczbę: " )
    return inp

def czy_liczba_pierwsza(a):
    #jeśli ilośc zer w liście wynosi 2 to znaczy, że liczba dzieli się przez 1 i samą siebie co oznacza, że jest liczbą pierwszą
    if a == 2:
        return "jest"
    else:
        return "nie jest"

def glowna():
    N=pobierz_dane()
    x=[]
    for i in range(1, N+1):
        x.append(N%i)
    #ilość zer w liście z resztami z dzielenia
    y=x.count(0)
    wynik=czy_liczba_pierwsza(y)
    print(f"Liczba {wynik} liczbą pierwszą!")

if __name__=="__main__":
    glowna()