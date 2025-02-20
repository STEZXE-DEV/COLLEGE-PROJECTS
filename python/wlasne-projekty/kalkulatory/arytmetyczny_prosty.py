import pyinputplus as p
import math as m

opcje = {0:"EXIT", 1:"Dodawanie", 2:"Odejmowanie", 3:"Mnożenie", 4:"Dzielenie", 5:"Potęgowanie", 6:"Pierwiastkowanie (kwadratowe)"}
for k, v in opcje.items():
    print(f"{k} - {v}")

def pobierz_dane():
    inp1=p.inputInt(prompt="Wybierz działanie (cyfra): ", min=0, max=6)
    print(f"Wybrano: {opcje[inp1]}")
    if inp1==0:
        return 0,0,0
    elif inp1<4:
        inp2=p.inputInt(prompt="Podaj pierwszą liczbę: ")
        inp3=p.inputInt(prompt="Podaj drugą liczbę: ")
        return inp1,inp2,inp3
    elif inp1==4:
        inp2=p.inputInt(prompt="Podaj pierwszą liczbę: ")
        inp3=p.inputInt(prompt="Podaj drugą liczbę: ", greaterThan=0)
        return inp1,inp2,inp3
    elif inp1==5:
        inp2=p.inputInt(prompt="Podaj podstawe potęgi: ")
        inp3=p.inputInt(prompt="Podaj wykładnik potęgi: ", greaterThan=0)
        return inp1,inp2,inp3
    else:
        inp2=p.inputInt(prompt="Podaj liczbę: ")
        return inp1,inp2,None

def dodawanie(a,b):
    a+=b
    return a

def odejmowanie(a,b):
    a-=b
    return a

def mnozenie(a,b):
    a*=b
    return a

def mnozenie(a,b):
    a*=b
    return a

def dzielenie(a,b):
    a/=b
    return a

def potegowanie(a,b):
    a**=b
    return a

def pierwiastkowanie(a):
    a=m.sqrt(a)
    return a

def main():
    while True:
        wyb,l1,l2=pobierz_dane()
        match wyb:
            case 0:
                break
            case 1:
                wynik=dodawanie(l1,l2)
            case 2:
                wynik=odejmowanie(l1,l2)
            case 3:
                wynik=mnozenie(l1,l2)
            case 4:
                wynik=dzielenie(l1,l2)
            case 5:
                wynik=potegowanie(l1,l2)
            case 6:
                wynik=pierwiastkowanie(l1)
        print(f"Wynik: {wynik}")

if __name__=="__main__":
    main()