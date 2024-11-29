import pyinputplus as pyi
#pobeanie wejscia typu INT
a = pyi.inputInt(prompt="Podaj pierwsza liczbe: \n")
b = pyi.inputInt(prompt="Podaj druga liczbe: \n")

#obliczenia podane w zadaniu
obl1 = a/b
obl2 = a//b
obl3 = b/a
obl4 = b//a

#lista z wynikami obliczen
wynik = [obl1,obl2,obl3,obl4]

#warunek: a i b nie moga wynosic zero
if a!=0 and b!=0:

#wypisanie wynikow obliczen (kazdy w osobnej linii)
    for i in wynik:
        print(f"Wynik: {i}")

#postepowanie gdy warunek nie zostanie spelniony
elif a == 0:
    print("Pierwsza liczba jest zerem!")
elif b == 0:
    print("Druga liczba jest zerem!")