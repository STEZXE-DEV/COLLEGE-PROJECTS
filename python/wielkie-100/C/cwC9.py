import pyinputplus as pyi
import math as m

#funkcja pobierajaca n - ilosc katow figury foremnej, r - dlugosc promienia okregu opisanego
def pobierz_dane():
    n = pyi.inputInt(prompt="Podaj ilosc katow n-kata foremnego: ", min=3)
    r = pyi.inputFloat(prompt=f"Podaj dlugosc promienia okregu opisanego na {n}-kacie: ", greaterThan=0)
    return n,r

#funkcja obliczajaca pole
def oblicz_pole(n,r):
    wzor = 1/2*r**2*n*m.sin(m.radians(360/n))
    return wzor

#funkcja glowna
def main():
    n,r=pobierz_dane()
    wynik = oblicz_pole(n,r)
    print(f"Pole {n}-kata foremnego wynosi: {wynik:.3f}")

#warunek sprawdza czy kod jest uruchamiany bezposrednio
if __name__ == "__main__":
    main()