import math

def wylicz_pierwiastki(a,b,delta):
    b1 = -b-math.sqrt(delta)/(2*a)
    b2 = -b+math.sqrt(delta)/(2*a)
    return (b1, b2)

def wylicz_delte(a,b,c):
    d=b*b-4*a*c
    return d

def oblicz_m_zerowe(a,b,c):

    #funkcja jest uzywana do obliczania pierwiastkow rownania kwadratowego
    #przyjmuje 3 parametry a,b,c bedace wspolczynnikami rowanania

    delta = wylicz_delte(a,b,c)

    if delta>0:
        x1, x2 = wylicz_pierwiastki(a,b,delta)
        return (2,x1,x2)
    if delta==0:
        x1,_ = wylicz_pierwiastki(a,b,delta)
        return (1,x1,0)
    if delta<0:
        return (0,None,None)
    
a = 1
b = 1
c = 1
a = int(input("Podaj A"))
b = int(input("Podaj B"))
c = int(input("Podaj C"))
ilosc_m_zerowych,x1,x2=oblicz_m_zerowe(a,b,c)

if ilosc_m_zerowych > 0:
    print(x1)
if ilosc_m_zerowych > 1:
    print(x2)
else:
    print("brak miejsc zerowych")


    

