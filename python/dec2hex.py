while True:    
    liczba = int(input("\nPodaj liczbe w systemie dziesiętnym\n"))
    postac_hex=[]
    hex={10: "A",11: "B",12: "C",13: "D",14: "E",15: "F"}
    zakres=0
    if liczba<0:
            print("\nLICZBY UJEMNE SA NIEOBSLUGIWANE!")
    else:
        print("\n============WYNIK_HEX============")
        while True:
            if zakres<=32:
                reszta=int(liczba)%16
                if reszta<10:
                    postac_hex.append(reszta)
                    postac_hex.reverse()
                    liczba/=16
                    zakres+=1
                    if int(liczba)==0:
                        break
                elif reszta in hex.keys():
                    reszta_poczatkowa=reszta
                    reszta=hex[reszta_poczatkowa]
                    postac_hex.append(reszta)
                    postac_hex.reverse()
                    liczba/=16
                    zakres+=1
                    if int(liczba)==0:
                        break
            else:
                print("Przekroczono zakres wyswietlania!")
                break
    
    if zakres<=32:
        for i in postac_hex:
            print(i,end='')
        print("\n=================================\n")
        print(f"Wyswietlane znaki: {zakres}")
    else:
        print("ERROR - Liczba jest zbyt duza!")
        print("=================================")