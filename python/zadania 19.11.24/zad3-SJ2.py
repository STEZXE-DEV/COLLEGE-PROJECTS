def nwd(a, b): 
    while b!=0:
        poczatkowe_a = a
        a = b
        b = poczatkowe_a%b
    return a

def nww(a, b):
    NWD=nwd(a,b)
    wynik=a*b//NWD
    return wynik

a = int(input("Podaj pierwszą liczbę: \n"))
b = int(input("Podaj drugą liczbę: \n"))
c = int(input("Podaj trzecią liczbę: \n"))

liczby = [a, b, c]
liczby.sort(reverse=True) # ustawienie listy wartosciami od najwiekszej do najmniejszej
maks = liczby[0]
srodek = liczby[1]
min = liczby[2]
NWW = nww(nww(min, srodek), maks)
print(f"NWW tych liczb wynosi: {NWW}")
