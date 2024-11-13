while True:
    liczba = int(input("\nPodaj liczbe w systemie dziesietnym:\n")) #max:32bit
    zakres = 0
    wynik=[]
    if liczba<0:
        print("\nLICZBY UJEMNE SA NIEOBSLUGIWANE!")
    else:
        while True:
            reszta=liczba%2
            wynik.append(int(reszta))
            liczba/=2
            zakres+=1
            if int(liczba)==0:
                break
        if zakres<=32:
            print("\nZakres wyswietlania:",zakres,"bit(y/ow).")
            print("\n==============WYNIK=============")
            wynik.reverse()
            for j in wynik:
                print(j, end='')
            print("\n================================")
        else:
            print("\n====================================")
            print("ZBYT DUZY ZAKRES WYSWIETLANIA!!!")   
            print("====================================\n")