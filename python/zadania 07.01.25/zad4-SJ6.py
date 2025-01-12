import pyinputplus as p
import random as r

znaki_sp=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/", "~"]
cyfry=[]
litery=[]
w_litery=[]

for i in range(48,58):
    cyfry.append(chr(i))
for i in range(97,123):
    litery.append(chr(i))
for i in litery:
    w_litery.append(i.upper())
def pobierz_dane():
    wybory=[]
    opcje=['T', 'N']
    inp1=p.inputInt(prompt="Podaj długość hasła (8-21 znaków): ", min=8, max=21)
    inp2=p.inputChoice(opcje, prompt="Czy hasło ma zawierać znaki specjalne (T/N): ") #4
    inp3=p.inputChoice(opcje, prompt="Czy hasło ma zawierać cyfry (T/N): ")           #2
    inp4=p.inputChoice(opcje, prompt="Czy hasło ma zawierać wielkie litery (T/N): ")  #1
    inputy1=[inp2,inp3,inp4]
    inputy2=[]
    for i in inputy1:
        if i.upper() == 'T':
            inputy2.append("1")
        elif i.upper() == 'N':
            inputy2.append("0")
    return inp1,''.join(inputy2)

dl, wlasciwosci=pobierz_dane()
wlasciwosci=int(wlasciwosci, 2)
#print("wlasciwosci", wlasciwosci)

def generowanie_hasla():
    haslo=[]
    match wlasciwosci:
        case 0: #tylko litery
            for i in range (0, dl):
                haslo.append(r.choice(litery))
            r.shuffle(haslo)
            return haslo,dl,0,0,0
        case 1: #litery + wielkie litery
            ilosc_l=r.randint(1, dl-1)
            ilosc_wl=dl-ilosc_l
            for i in range (0, ilosc_l):
                haslo.append(r.choice(litery))
            for i in range (0, ilosc_wl):
                haslo.append(r.choice(w_litery))
            r.shuffle(haslo)
            return haslo,ilosc_l,ilosc_wl,0,0
        case 2: #litery + cyfry
            ilosc_l=r.randint(1, dl-1)
            ilosc_c=dl-ilosc_l
            for i in range (0, ilosc_l):
                haslo.append(r.choice(litery))
            for i in range (0, ilosc_c):
                haslo.append(r.choice(cyfry))
            r.shuffle(haslo)
            return haslo,ilosc_l,0,ilosc_c,0
        case 3: #litery + wielkie litery + cyfry
            ilosc_l=r.randint(1, dl-1)
            mozliwa_ilosc_wl=dl-ilosc_l
            ilosc_wl=r.randint(1, mozliwa_ilosc_wl)
            ilosc_c=mozliwa_ilosc_wl-ilosc_wl
            for i in range (0, ilosc_l):
                haslo.append(r.choice(litery))
            for i in range (0, ilosc_wl):
                haslo.append(r.choice(w_litery))
            for i in range (0, ilosc_c):
                haslo.append(r.choice(cyfry))
            r.shuffle(haslo)
            #print(ilosc_l, ilosc_wl, ilosc_c)
            return haslo,ilosc_l,ilosc_wl,ilosc_c,0
        case 4: #litery + znaki specjalne
            ilosc_l=r.randint(1, dl-1)
            ilosc_zs=dl-ilosc_l
            for i in range (0, ilosc_l):
                haslo.append(r.choice(litery))
            for i in range (0, ilosc_zs):
                haslo.append(r.choice(znaki_sp))
            r.shuffle(haslo)
            return haslo,ilosc_l,0,0,ilosc_zs
        case 5: #litery + wielkie litery + znaki specjalne
            ilosc_l=r.randint(1, dl-1)
            mozliwa_ilosc_wl=dl-ilosc_l
            ilosc_wl=r.randint(1, mozliwa_ilosc_wl)
            ilosc_zs=mozliwa_ilosc_wl-ilosc_wl
            for i in range (0, ilosc_l):
                haslo.append(r.choice(litery))
            for i in range (0, ilosc_wl):
                haslo.append(r.choice(w_litery))
            for i in range (0, ilosc_zs):
                haslo.append(r.choice(znaki_sp))
            #print(ilosc_l, ilosc_wl, ilosc_zs)
            r.shuffle(haslo)
            return haslo,ilosc_l,ilosc_wl,0,ilosc_zs
        case 6: #litery + cyfry + znaki specjalne
            ilosc_l=r.randint(1, dl-1)
            mozliwa_ilosc_c=dl-ilosc_l
            ilosc_c=r.randint(1, mozliwa_ilosc_c)
            ilosc_zs=mozliwa_ilosc_c-ilosc_c
            for i in range (0, ilosc_l):
                haslo.append(r.choice(litery))
            for i in range (0, ilosc_c):
                haslo.append(r.choice(cyfry))
            for i in range (0, ilosc_zs):
                haslo.append(r.choice(znaki_sp))
            r.shuffle(haslo)
            return haslo,ilosc_l,0,ilosc_c,ilosc_zs
        case 7: #litery + wielkie litery + cyfry + znaki specjalne
            ilosc_l=r.randint(1, dl-1)
            mozliwa_ilosc_wl=dl-ilosc_l
            ilosc_wl=r.randint(1, mozliwa_ilosc_wl)
            mozliwa_ilosc_c=mozliwa_ilosc_wl-ilosc_wl
            ilosc_c=r.randint(1, mozliwa_ilosc_c)
            ilosc_zs=mozliwa_ilosc_c-ilosc_c
            for i in range (0, ilosc_l):
                haslo.append(r.choice(litery))
            for i in range (0, ilosc_wl):
                haslo.append(r.choice(w_litery))
            for i in range (0, ilosc_c):
                haslo.append(r.choice(cyfry))
            for i in range (0, ilosc_zs):
                haslo.append(r.choice(znaki_sp))
            r.shuffle(haslo)
            return haslo,ilosc_l,ilosc_wl,ilosc_c,ilosc_zs


haslo,l,wl,c,zs=generowanie_hasla()
print(f"\nWygenerowane hasło: {''.join(haslo)}\n")
print(f"Ilość małych liter: {l}\nIlość wielkich liter: {wl}\nIlość cyfr: {c}\nIlość znaków specjalnych: {zs}")
