import pyinputplus as pyi
import math as m

#funkcja obliczajaca objetosc stozka
def oblicz_stozek():
    r = pyi.inputFloat(prompt="Podaj promien podstawy stozka: ", greaterThan=0)
    h = pyi.inputFloat(prompt="Podaj wysokosc stozka: ", greaterThan=0)
    return 1/3*m.pi*m.pow(r,2)*h

#funkcja obliczajaca objetosc ostroslupa czworokatnego
def oblicz_ostr_czwrk():
    a = pyi.inputFloat(prompt="Podaj dlugosc boku ostroslupa czworokatnego: ", greaterThan=0)
    h = pyi.inputFloat(prompt="Podaj wysokosc ostroslupa czworokatnego: ", greaterThan=0)
    return 1/3*m.pow(a,2)*h

#funkcja obliczajaca objetosc graniastoslupa o podstawie 5-kata foremnego
def oblicz_gran_piecktny_praw():
    a = pyi.inputFloat(prompt="Podaj dlugosc boku podstawy: ", greaterThan=0)
    h = pyi.inputFloat(prompt="Podaj wysokosc gran. o pods. 5-kata forem.: ", greaterThan=0)
    return (1/4*m.sqrt(25+10*m.sqrt(5)))*m.pow(a,2)*h

#funkcja obliczajaca objetosc osmioscianu foremnego
def oblicz_osmioscian():
    r = pyi.inputFloat(prompt="Podaj promien okregu opisanego na osmioscianie: ", greaterThan=0)
    return m.sqrt(2)/3*m.pow(r,3)

#glowna funkcja
def main():
    print("Wybierz jedna z podanych opcji: ")
    typy = {1:'stozek', 2:'ostroslup czworokatny', 3:'graniastoslup prawidlowy pieciakatny', 4:'osmioscian foremny'}
    for key, value in typy.items():
        print(f"{key} - {value}")
    typ = pyi.inputInt(prompt="Podaj odpowiednia cyfre: ", min=1, max=4)
    
    #sprawdzenie podanej wartosci w inpucie 'typ' i przypisanie wynikow dzialania poszczegolnych funkcji
    match typ:
        case 1:
            wynik = oblicz_stozek()
        case 2:
            wynik = oblicz_ostr_czwrk()
        case 3:
            wynik = oblicz_gran_piecktny_praw()
        case 4:
            wynik = oblicz_osmioscian()

    #wypisanie nazwy ze slownika wraz z wyliczona objetoscia
    print(f"{typy[typ].upper()}\nObjetosc: {wynik:.3f}")

#sprawdzenie czy uruchomiono kod bezposrednio
if __name__=="__main__":
    main()