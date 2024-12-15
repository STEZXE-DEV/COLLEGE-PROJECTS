import math as m
import pyinputplus as p

#funkcja wyliczająca miejsca zerowe i zwracająca wynik w postaci krotki
def miejsca_zerowe(a,b,c):
    delta = b**2-4*a*c
    if delta>0:
        x1 = (-b+m.sqrt(delta))/2*a
        x2 = (-b-m.sqrt(delta))/2*a
        wynik=(2,x1,x2)
    elif delta==0:
        x0 = (-b/2*a)
        wynik=(1,x0, None)
    else:
        wynik=(0, None, None)
    return wynik

#funkcja, która modyfikuje krotkę uzyskana w funkcji <miejsca_zerowe> w celu łatwiejszego poźniejszego wyświetlania
def liczba_miejsc_zerowych(a,b,c):
    match a:
        case 0:
            return 'brak miejsc zerowych', #znak ',' jest wymagany, w razie jego braku string jest rozkładany jako jeden znak/litera jako jeden element krotki
        case 1:
            return 'jedno miejsce zerowe', b
        case 2:
            return 'dwa miejsca zerowe', b, c

#główna funkcja, która pobiera inputy, korzysta z funkcji i wypisuje na ekranie
def main():      
    a = p.inputFloat(prompt="Podaj współczynnik a równania kwadratowego: " )
    b = p.inputFloat(prompt="Podaj współczynnik b równania kwadratowego: " )
    c = p.inputFloat(prompt="Podaj współczynnik c równania kwadratowego: " )
    wynik=miejsca_zerowe(a,b,c)
    wynik2=liczba_miejsc_zerowych(*wynik)
    print(f"y = ({a})x2 + ({b})x + ({c})")
    for i in range(0, len(wynik2)):
        if i == 0:
            print(f"Ilość miejsc zerowych: {wynik2[i].upper()}")
        else:
            print(f"Miejsce zerowe: {wynik2[i]}")

if __name__ == '__main__':
    main()