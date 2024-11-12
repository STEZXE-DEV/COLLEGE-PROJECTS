while True:
    liczba = int(input("Podaj liczbe:\n"))
    ilosc = 0
    for i in range(0,1001):  #zero jest wielokrotnością
        if liczba*i<1001:
            print(i+1,liczba*i, sep='. ')
            ilosc+=1
    print("Dla liczby", liczba,"jest", ilosc, "wielokrotnosci do 1000")