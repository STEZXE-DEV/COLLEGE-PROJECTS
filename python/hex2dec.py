while True:
    liczba = str(input("======> Podaj liczbe w postaci szestnastkowej: <======\n")).upper()
    zakres = len(liczba)
    hexa={"A": 10,"B": 11,"C": 12,"D": 13,"E": 14,"F": 15}
    postac_dec=[]
    wynik=[]
    error=0
    postac_poczatkowa=list(liczba)
    if zakres<=32:
        for i in postac_poczatkowa:
            if i in hexa.keys():
                wartosc=hexa[i]
                postac_dec.append(wartosc)
            elif i.isdigit():
                postac_dec.append(int(i)) 
            else:
                print("\n====================ERROR======================")
                print("\nTo nie jest liczba w systemie szesnastkowym!!!\n")
                error=1
                break         
        dlugosc=len(postac_dec)
        for k in postac_dec:
            wynik.append(k*16**(dlugosc-1))
            dlugosc-=1
            if dlugosc==0:
                break
    else:
        print("\n=============================\n")
        print("Przekroczono zakres znaków!!!")
        print("\n=============================\n")
        break
    if error==0:
        print("\n========WYNIK_DEC==========")
        print(sum(wynik))
        print("Zakres znaków:", zakres)
        print("===========================\n")
    else:
        print("====================ERROR======================\n")