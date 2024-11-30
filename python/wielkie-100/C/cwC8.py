import pyinputplus as pyi
import math as m

#slownik z wartoscia pozniejszego wejscia i odpowiadajacej mu nazwie figury
typy = {1:'trojkat prostokatny', 2:'trojkat rownoramienny', 3:'prostokat', 4:'pieciakat foremny'}
print("Jakiej figury pole chcesz obliczyc?")

#petla for wypisujaca klucz i wartosc dla kazdego elementu w slowniku
for key, value in typy.items():
    print(f"{key} - {value}")

#pobranie wejscia ze zbioru {1,2,3,4}
wejscie = pyi.inputInt(prompt="Wybierz odpowiedznia cyfre: ", min=1, max=4)

#sprawdzenie zmiennej 'wejscie'
match wejscie:
    case 1: #przypadek kiedy wejscie == 1
        a = pyi.inputFloat(prompt="Podaj dl. podstawy trojkata: ", greaterThan=0)
        h = pyi.inputFloat(prompt="Podaj dl. wysokosci trojkata: ", greaterThan=0)
        wynik = (a*h)/2
    case 2: #przypadek kiedy wejscie == 2
        a = pyi.inputFloat(prompt="Podaj dl. podstawy trojkata: ", greaterThan=0)
        b = pyi.iinputFloat(prompt="Podaj dl. ramienia trojkata: ", greaterThan=0)
        h = m.sqrt(-((a/2)**2)+b**2)
        wynik = (a*h)/2
    case 3: #przypadek kiedy wejscie == 3
        a = pyi.inputFloat(prompt="Podaj dl. boku a: ", greaterThan=0)
        b = pyi.inputFloat(prompt="Podaj dl. boku b: ", greaterThan=0)
        wynik = a*b
    case 4: #przypadek kiedy wejscie == 4
        r = pyi.inputFloat(prompt="Podaj dl. promienia okregu opisanego na pieciokacie: ", greaterThan=0)
        wynik = 5/4*r**2*m.sin((2*m.pi)/5)

#wypisanie nazwy ze slownika 'typy' zgodnie z podanym 'wejscie', <.upper()> - zmienia litery na WIELKIE
print(f"\n{typy[wejscie].upper()}\nPole wynosi: {wynik}\n")