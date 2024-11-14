while True:   
    liczba = str(input("\nPodaj liczbe w systemie dziesietnym [DEC]:\n"))
    if liczba.isdigit():
        zakres=len(str(liczba))
        liczba=int(liczba)
        dlugosc=0
        postac_oct=[]
        if zakres>=32:
            print("\n===================ERROR====================")
            print("Przekroczono zakres mozliwych do wyswietlenia znakow!!!")
            print("===================ERROR====================\n")
            break
        elif zakres<=32:
            while True:
                reszta=liczba%8
                if int(liczba)==8 or int(liczba)==9:
                    if reszta==0:
                        reszta=10
                        postac_oct.append(reszta)
                        break
                    elif reszta==1:
                        reszta=11
                        postac_oct.append(reszta)
                        break
                else:
                    postac_oct.append(reszta)
                    liczba//=8
                    dlugosc+=1
                    if int(liczba)==0:
                        break
        postac_oct.reverse()        
        print("\n=================WYNIK_OCT=================")
        for i in postac_oct:
            print(i, end='')
        print("\nZakres wyswietlanych znakow:", dlugosc)
        print("===========================================")
    else:
        print("\n===================ERROR====================")
        print("TO NIE JEST LICZBA!!!")
        print("===================ERROR====================\n")  


