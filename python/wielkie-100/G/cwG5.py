import pyinputplus as p

#pobranie liczby całkowitej
def pobierz_dane():
    inp=p.inputInt(prompt="Podaj liczbę: ")
    return inp

#obliczenie sumy cyfr za wykorzystaniem listy
def suma_cyfr(a):
    x=[]
    for i in str(a):
        x.append(int(i))
    z=sum(x)
    return z

#wypisanie wyniku
def glowna():
    a=pobierz_dane()
    suma=suma_cyfr(a)
    print(f"Suma cyfr: {suma}")

if __name__=="__main__":
    glowna()