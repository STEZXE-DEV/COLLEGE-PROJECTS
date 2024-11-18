kolor = input("Podaj trzy kolory w formacie <nazwa>,<nazwa>,<nazwa>: \n") #wejscie
kolory=[] #definicja listy kolory
kolory.extend(kolor.split(",")) #rozszerzenie listy o wejscie (zdefiniowane ze zmienne sa rodzdielone znakiem ",")
for i in range(1,4): #funkcja for
    print(f"Kolor{i}: {kolory[i-1]}", end='') #wypisanie koloru z listy wraz z indeksowaniem 
    if not i==3: #jesli nie jest to ostatni element listy to stawiany jest przecinek
        print(",", end='\n')
    else: #w innym wypadku brak przecinka
        print("" ,end="\n")