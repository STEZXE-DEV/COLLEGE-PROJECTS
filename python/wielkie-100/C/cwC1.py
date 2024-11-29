import pyinputplus as pyi
#pobranie 3 wartosci zmiennoprzecinkowych podwojnej precyzji (w pythonie jest to float)
a = pyi.inputFloat(prompt="Podaj pierwsza liczbe: \n")
b = pyi.inputFloat(prompt="Podaj druga liczbe: \n")
c = pyi.inputFloat(prompt="Podaj trzecia liczbe: \n")

#wykonanie zadanych obliczen
obl1=a+b+c
obl2=a**2+b**2+c**2
obl3=a**3+b**3+c**3

#wypisanie wynikow obliczen
print(f"Wynik nr.1: {obl1}\nWynik nr.2: {obl2}\nWynik nr.3: {obl3}\n")