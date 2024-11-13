while True:
    liczba = str(input("Podaj liczbe w systemie binarnym.\n"))
    print("=====================WYNIK========================")
    if int(liczba)==0:
        print('Podana liczba w systemie dziesietnym wynosi: 0\n==================================================\n')
    elif int(liczba)<0:
        print("Liczba nie moze byc ujemna!!!\n==================================================\n")
    else:
        lista_bin = list(liczba)
        lista_dec=[]
        for x in lista_bin:
            if int(x)==1 or int(x)==0:
                zakres = len(liczba)
                zakres_poczatkowy = zakres
                if zakres<=32:
                    for i in lista_bin:
                        wynik=int(i)*(2**(zakres-1))
                        zakres-=1
                        lista_dec.append(wynik)
                else:
                    print("Przekroczono zakres 32bit!!!\n==================================================\n")
                    break
                postac_dec=sum(lista_dec[0:zakres_poczatkowy])
                if postac_dec==0:
                    print()
                else:
                    print("Podana liczba w systemie dziesietnym wynosi:",postac_dec,"\n==================================================\n")
                    break
            else:
                print("To nie jest liczba w postaci binarnej!!!\n==================================================\n")
                break
        
       