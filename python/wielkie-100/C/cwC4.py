import pyinputplus as pyi
import math as m

#podanie wejsc a,b,c przez uzytkownika
a = pyi.inputFloat(prompt="Podaj dlugosc pierwszego boku: \n", greaterThan=0)
b = pyi.inputFloat(prompt="Podaj dlugosc drugiego boku: \n", greaterThan=0)
c = pyi.inputFloat(prompt="Podaj dlugosc trzeciego boku: \n", greaterThan=0)

#warunek sprawdza czy z podanych wartosci mozna utworzyc trojkat
if a<b+c and b<c+a and c<a+b: 

    #<m.acos()> podaje wynik w radianach
    cos_a=m.acos((b**2+c**2-a**2)/(2*b*c)) 
    cos_b=m.acos((a**2+c**2-b**2)/(2*a*c))
    cos_c=m.acos((a**2+b**2-c**2)/(2*a*b))
    wynik=[cos_a,cos_b,cos_c]
    dl = len(wynik)
    for i in range(0, dl):

        #<m.degrees()> zamienia radiany na stopnie
        print(f"{i+1}. Kat w radianach: {wynik[i]}, Kat w stopniach: {m.degrees(wynik[i])}") 
else:
    print("To nie jest trojkat!\n")