import pyinputplus as pyi
import math as m

def wysokosc_g_cz_sciany():
    a = pyi.inputFloat(prompt="Podaj pierwsza zmierzona dlugosc: ", greaterThan=0)
    #b = pyi.inputFloat(prompt="Podaj druga zmierzona dlugosc: ", greaterThan=0)
    c = pyi.inputFloat(prompt="Podaj kat odchylenia dalmierza od poziomu: ", min=0, max=180)

    wynik = a*m.sin(m.radians(c))
    return wynik

def wysokosc_d_cz_sciany():
    #a = pyi.inputFloat(prompt="Podaj pierwsza zmierzona dlugosc: ", greaterThan=0)
    b = pyi.inputFloat(prompt="Podaj druga zmierzona dlugosc: ", greaterThan=0)
    c = pyi.inputFloat(prompt="Podaj kat odchylenia dalmierza od poziomu: ", min=0, max=180)
    
    wynik = b*m.sin(m.radians(c))
    return wynik

def dlugosc_sufitu():
    a = pyi.inputFloat(prompt="Podaj pierwsza zmierzona dlugosc: ", greaterThan=0)
    b = pyi.inputFloat(prompt="Podaj druga zmierzona dlugosc: ", greaterThan=0)
    c = pyi.inputFloat(prompt="Podaj kat odchylenia dalmierza od poziomu: ", min=0, max=180)
    a*=m.cos(m.radians(c))
    b*=m.cos(m.radians(c))
    wynik = m.fabs(a-b)
    return wynik

def main():
    typy = {1:'wysokosc gornej czesci sciany' , 2:'wysokosc dolnej czesci sciany', 3:'dlugosc sufitu'}
    print("Wybierz jedna z podanych opcji: ")
    for key, value in typy.items():
        print(f"{key} - {value}")
    typ = pyi.inputInt(prompt="Podaj odpowiednia cyfre: ", min=1, max=3)
    match typ:
        case 1:
            wynik = wysokosc_g_cz_sciany()
        case 2:
            wynik = wysokosc_d_cz_sciany()
        case 3:
            wynik = dlugosc_sufitu()
    print(f"Wykonano obliczenie: {typy[typ].upper()}\nWartosc obliczenia wynosi: {wynik}")

if __name__=='__main__':
    main()