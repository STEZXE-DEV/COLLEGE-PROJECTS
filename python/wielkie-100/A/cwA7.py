a=88
b=25
#Dzieki [2:] wypisane zostaja wartosci poza dwoma pierwszymi znakami,
#przez co zostaje pominiety prefix i otrzymujemy wlasciwa wartosc.
print(f"{hex(a)[2:]} {hex(b)[2:]}") #hex = hexadecymalne/sys. szesnastkowy
print(f"{oct(a)[2:]} {oct(b)[2:]}") #oct = octadecymalne/sys. osemkowy
print(f"{bin(a)[2:]} {bin(b)[2:]}") #bin = binarne/sys. binarny