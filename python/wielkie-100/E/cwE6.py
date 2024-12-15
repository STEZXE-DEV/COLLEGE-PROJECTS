import pyinputplus as p
a = p.inputInt(prompt="Podaj liczbę: ")
a=str(a)
tab=[]
if a.isdigit():
    for i in a:
        tab.append(int(i))
    a=int(a)
    suma=sum(tab)
    if suma%3==0 and a>1000:
        a/=2
        print(a)