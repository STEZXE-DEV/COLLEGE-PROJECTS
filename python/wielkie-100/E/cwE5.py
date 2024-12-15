import pyinputplus as p

#funkcja tworząca listę podanych w inpucie liczb od najwiekszej do najmniejszej
def najwieksza_liczba(a,b,c,d,e):
    wynik=[a,b,c,d,e]
    wynik.sort() #sortowanie listy wartościami od najmniejszej do największej
    wynik.reverse() #odwrócenie listy indeksami "od tyłu" co daje wartości w liście uporządkowane od najwiekszej
    return wynik

#funkcja wyznaczająca największą parzystą wartość z listy, jeśli takiej nie ma zwraca znak '-'
def najwieksza_parzysta(a):
    for i in a:
        if i%2==0: #jeżeli warunek natrafi w liście na liczbę parzystą, zakańcza pętlę i zwraca wartość tej liczby
            b=i
            break
        else: #jeżeli nie natrafi na żadną parzystą to zwraca '-'
            b='-'
    return b

#funkcja główna z inputami, przypisaniem wyników działań funkcji oraz wypisaniem na ekranie
def main():
    a1 = p.inputInt(prompt="Podaj pierwszą liczbę: ")
    a2 = p.inputInt(prompt="Podaj drugą liczbę: ")
    a3 = p.inputInt(prompt="Podaj trzecią liczbę: ")
    a4 = p.inputInt(prompt="Podaj czwartą liczbę: ")
    a5 = p.inputInt(prompt="Podaj piątą liczbę: ")
    naj=najwieksza_liczba(a1,a2,a3,a4,a5)
    naj_pa=najwieksza_parzysta(naj)
    print(f"Największa liczba parzysta z podanych liczb: {naj_pa}")

if __name__=='__main__':
    main()