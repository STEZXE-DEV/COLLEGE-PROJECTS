def is_valid_binary_number(postac_bin1, postac_bin2, error, error_alert):
    for i in postac_bin1:
        if i not in ('1', '0'):
            error+=1
            error_alert.append("Pierwsza liczba to nie liczba w postaci binarnej!!!")
            break
        
    for i in postac_bin2:
        if i not in ('1', '0'):
            error+=1
            error_alert.append("Druga liczba to nie liczba w postaci binarnej!!!")
            break
    return error, error_alert

def binary_sum(postac_bin1, postac_bin2):
    suma_bin=[]
    postac_dec1=[]
    postac_dec2=[]
    zakres1=len(postac_bin1)
    zakres2=len(postac_bin2)
    for i in postac_bin1:
        postac_dec1.append(int(i)*2**(zakres1-1))
        zakres1-=1
    for k in postac_bin2:
        postac_dec2.append(int(k)*2**(zakres2-1))
        zakres2-=1
    suma_dec=sum(postac_dec1)+sum(postac_dec2)
    while True:
        reszta=suma_dec%2
        suma_bin.append(reszta)
        suma_dec//=2
        if suma_dec==0:
            break
    suma_bin.reverse()
    return suma_bin

def main():
    while True:
        error=0
        error_alert=[]
        error_alert2=[]
        liczba1=str(input("\nPodaj pierwsza liczbe binarna: \n"))
        liczba2=str(input("Podaj druga liczbe binarna: \n"))
        if liczba1 == "exit" or liczba2 == "exit":
            print("Zakonczono program!")
            break
        elif not (liczba1.isdigit() and liczba2.isdigit()):
            error+=1
            error_alert2.append("TO NIE JEST LICZBA!!!")   
        postac_bin1=list(liczba1)
        postac_bin2=list(liczba2)
        error, error_alert=is_valid_binary_number(liczba1, liczba2, error, error_alert)
        error_alert_all=error_alert+error_alert2
        if error>0:
            print("========================ERROR========================")
            print(f"Ilosc napotkanych bledow: {error}")
            for i in error_alert_all:
                print(i, end='\n')
            print("========================ERROR========================\n")
            break
        else:
            suma=binary_sum(postac_bin1, postac_bin2)
            print("============WYNIK_BIN============")
            for y in suma:
                print(f"{y}", end='')
            print("\n=================================\n")
while True:
    if __name__=='__main__':
        main()