import math as m
import pyinputplus as pyi

#pobranie wejsc
a = pyi.inputFloat(prompt="Podaj liczbe a: \n")
b = pyi.inputFloat(prompt="Podaj liczbe b: \n")

#warunek: liczba logarytmowana nie moze byc rowna 0 lub ujemna (dot. obliczen 1 i 2)
if a>0:
    o1 = m.log10(a) #<math.log10()> - logarytm o podstawie 10
    o2 = m.log2(a) #<math.log2()> - logarytm o podstawie 2
else:
    o1 = "Blad logarytmu!"
    o2 = "Blad logarytmu!"
o3 = m.pow(a, b) #<math.pow(a, b)> - a do potegi b (to samo co a**b)
o4 = m.pow(m.e, b) #<math.e> - liczba Eulera w module math

#<math.pow> nie jest idealne do obliczania pierwiastkow
if a>0 and b>0:
    o5 = m.pow(b, 1/a)
elif a>0  and b==0:
    o5 = m.pow(b, 1/a)
else:
    o5 = "Blad <math.pow>!"

#round() zaokraglenie do najblizeszej calkowitej
o6 = round(a)

#<math.trunc()> - obciecie czesci ulamkowej (pozostawia tylko czesc calkowita liczby)
o7 = m.trunc(a+b)

#<math.fabs()> - wartosc bezwzgledna z liczby
o8 = m.fabs(a)

#tablica z wynikami
wynik = [o1, o2, o3, o4, o5, o6, o7, o8]
dl=len(wynik) #dlugosc tablicy z wynikami

#wypisanie wynikow wraz z ich indeksacja (numeracja linii)
for i in range(0, dl):
    print(f"Dzialanie nr. {i+1}: {wynik[i]}")