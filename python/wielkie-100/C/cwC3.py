#import potrzebnych bibliotek i utworzenie aliasow <as>
import numpy as np
import pyinputplus as pyi
import math as m

#zmiennoprzecinkowa pojedynczej precyzji <numpy.float32>
pi=np.float32(m.pi) #deklaracja liczby pi z modulu math

#pobranie wejsc i konwersja na float32
a=pyi.inputFloat(prompt="Podaj wartosc a (w stopniach): \n")
a = np.float32(a)
b=pyi.inputFloat(prompt="Podaj wartosc b (w radianach): \n")
b = np.float32(b)

#wykonanie obliczen podanych w zadaniu
obl1=m.sin(m.radians(a))
obl2=m.cos(b)
obl3=m.cos(m.radians(a))+m.cos(b)
obl4=m.radians(a)
obl5=m.degrees(b)
wynik = [obl1,obl2,obl3,obl4,obl5] #lista z wynikami obliczen
dl=len(wynik) #dlugosc listy z wynikami

#wypisanie wynikow w petli for,
#ograniczone wyswietlanie liczby do czterech miejsc po przecinku <zmienna:.4f> f - liczba typu float
for i in range(0, dl):
    if i==3: #obliczenie IV
        print(f"Wynik {i+1}: {wynik[i]:.4f} radian/y/ow.")
    elif i==4: #obliczenie V
        print(f"Wynik {i+1}: {wynik[i]:.4f} stopni.")
    else: #reszta wynikow
        print(f"Wynik {i+1}: {wynik[i]:.4f}.")
