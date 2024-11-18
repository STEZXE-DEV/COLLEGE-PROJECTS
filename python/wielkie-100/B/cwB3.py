a = int(input("Podaj liczbe calkowita: \n")) #wejscie liczby calkowitej
b = float(input("Podaj liczbe zmiennoprzecinkowa: \n")) #wejscie liczby zmiennoprzecinkowej
c = float(input("Podaj liczbe zmiennoprzecinkowa: \n")) #wejscie liczby zmiennoprzecinkowej
liczby = [] #deklaracja listy
liczby.extend([a,b,c]) #rozszerzenie listy o wiele elementow
suma = sum(liczby) #suma liczb
print() #odstep miedzy wynikami
for i in liczby:
    print(i) #funkcja for wypisuje kazdy element listy "liczby"
print(suma) #wypisanie sumy liczb