while True:
    print("<<<<<<   NAPISZ exit BY ZAKONCZYC PROGRAM  >>>>>>>")
    liczba = str(input("Podaj liczbe w postaci osemkowej: \n"))
    if liczba=="exit":
        break
    postac_oct = list(liczba)
    error=0
    error_alert=[]
    dlugosc=len(postac_oct)
    wynik=[]
    if dlugosc>32:
        error+=1
        error_alert.append("PRZEKROCZONO ZAKRES WYSWIETLANYCH ZNAKOW!!!")
        for i in postac_oct:
            if i.isdigit():
                if int(i) == 8 or int(i) == 9:
                    error+=1
                    error_alert.append("TO NIE JEST LICZBA W POSTACI OSEMKOWEJ!!!")
                    break
            else:
                error+=1
                error_alert.append("TO NIE JEST LICZBA!!!")
                break
    elif dlugosc<=32:
        for i in postac_oct:
            if i.isdigit():
                if int(i) == 8 or int(i) == 9:
                    error+=1
                    error_alert.append("TO NIE JEST LICZBA W POSTACI OSEMKOWEJ!!!")
                else:
                    liczba_dec=int(i)*8**(dlugosc-1)
                    wynik.append(int(liczba_dec))
                    dlugosc-=1
                    if dlugosc==0:
                        break
            else:
                error+=1
                error_alert.append("TO NIE JEST LICZBA!!!")
                break
    if error>0:
        print("\n======================ERROR====================")
        print(f"Liczba napotkanych bledow: {error}")
        print("==================ERROR_ALERT==================")
        for k in error_alert:
            print(k,sep='\n')
        print("======================ERROR====================\n")
    elif error==0:
        suma=str(sum(wynik))
        zakres=len(suma)
        print("\n=================WYNIK_DEC===============")
        print(sum(wynik))
        print(f"Zakres wyswietlanych znakow: {zakres}")
        print("=========================================")