import pyinputplus as pyip



from decimal import *
getcontext().prec = 2
#przy czym ta precyzja odnosi się nie do ilości miejsc po przecinku, a do ogólnej liczby wszystkich miejsc dla tej liczby
a=Decimal(input('Podaj liczbę a: '))
b=Decimal(input('Podaj liczbę b: '))
c=Decimal(input('Podaj liczbę c: '))

print(a+b+c)
print(a**2+b**2+c**2)
print(a**3+b**3+c**3)
