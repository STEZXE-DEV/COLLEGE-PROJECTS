from datetime import datetime
data_teraz=datetime.now()
wejscie = str(input("Podaj pesel: "))
pesel=[]
dlugosc_pesel = len(wejscie)
if not dlugosc_pesel==11 and not wejscie.isdigit():
    print("To nie jest wlasciwy numer pesel!")
    exit()
else:
    for i in wejscie:
        pesel.append(i)
    rok = int(pesel[0]+pesel[1])
    mies = int(pesel[2]+pesel[3])
    dzien = int(pesel[4]+pesel[5])
    if 1 <= mies <= 12:
        rok += 1900
    elif 21 <= mies <= 32:
        rok += 2000
        mies -= 20
    elif 41 <= mies <= 52:
        rok += 2100
        mies -= 40
    elif 61 <= mies <= 72:
        rok += 2200
        mies-= 60
    elif 81 <= mies <= 92:
        rok += 1800
        mies -= 80
    else:
        print("Nieprawidlowy miesiac w numerze PESEL")
    data_pesel = datetime(rok, mies, dzien)
    roznica = data_teraz - data_pesel
    if roznica.days//365>=18:
        print("Osoba pelnoletnia!")
    else:
        print("Osoba niepelnoletnia!")


