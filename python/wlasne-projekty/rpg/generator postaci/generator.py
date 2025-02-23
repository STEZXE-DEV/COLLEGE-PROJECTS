import random as r 
import configparser as con
import os

config=con.ConfigParser()

sciezka_kodu=os.path.dirname(os.path.realpath(__file__))

def generuj_nazwe_pliku(nazwa="postać", rozszerzenie=".ini"):
    numer=1
    while True:
        if numer>10:
            print("Przekroczono maksymalną ilość postaci!")
            return False
        nazwa_pliku=f"{nazwa}{numer}{rozszerzenie}"
        if not os.path.exists(sciezka_kodu+"\\"+nazwa_pliku):
            return nazwa_pliku
        numer+=1
        

def generuj_wyglad_postaci(rasy):
    
    #kolory włosów
    kw=[
    "rudy",
    "jasny_blond",
    "ciemny_blond",
    "brązowy",
    "czarny"]
    
    #kolory oczu
    ko=[
    "zielony",
    "brązowy",
    "niebieski",
    "turkusowy",
    "szmaragdowy",
    "czarny"
    ]
    
    #odcienie skóry
    ks=[
    "blady",
    "jasny",
    "opalony",
    "ciemny",
    "czarny"]

    kolor_skory=r.choice(ks)

    if kolor_skory not in ("ciemny", "czarny"):
        kolor_wlosow=r.choice(kw)
    else:
        kw=["brązowy", "czarny"]
        kolor_wlosow=r.choice(kw)
    
    kolor_oczu=r.choice(ko)

    rasa=r.choice(rasy)

    #wybór płci
    while True:

        plec=input("Wybierz Płeć: (K/M)\n> ")

        if plec.upper() == "M":
            plec=0
            plec_slownie="Mężczyzna"
            wzrost=r.randint(150, 220)
            if wzrost<=165:
                rasa=r.choice(["Gnom", "Niziołek", "Krasnolud"])
            elif wzrost >=210:
                rasa="Gigant"
            return plec, plec_slownie, rasa, wzrost, kolor_oczu, kolor_wlosow, kolor_skory
        elif plec.upper() == "K":
            plec=1
            plec_slownie="Kobieta"
            wzrost=r.randint(135, 210)
            if wzrost<=145:
                rasa=r.choice(["Gnom", "Niziołek", "Krasnolud"])
            elif wzrost >=200:
                rasa="Gigant"
            return plec, plec_slownie, rasa, wzrost, kolor_oczu, kolor_wlosow, kolor_skory
        else:
            print("Niepoprawnie podana płeć!")


def wybierz_klase(klasy):
    
    while True:
        for k,v in klasy.items():
            print(f"{v}. {k}")
        inp=input("Podaj nazwę klasy z podanych: ")
        if inp.upper() in klasy or inp.lower() in klasy or inp.capitalize() in klasy:
            return inp.capitalize()
        else:
            print("Nieprawidłowo wybrana klasa!")

def kalkulator_statystyk_postaci(pl, rs, wz, kl):
    zdr=100
    atak=10
    obr=10
    int=10
    zwn=10
    scs=r.randint(0,5)
    if pl == 0:
        atak+=5
    elif pl == 1:
        int+=5
    
    return zdr,atak,obr,int,zwn,scs

def main():
    
    rasy=[
    "Człowiek",
    "Elf",
    "Krasnolud",
    "Niziołek",
    "Ork",
    "Leśny Elf",
    "Wysoki Elf",
    "Półelf",
    "Półork",
    "Goblin",
    "Troll",
    "Gnom",
    "Hobgoblin",
    "Ogr",
    "Gigant",
    "Drakonid",
    "Wilkołak",
    "Wampir",
    "Minotaur",
    "Satyr"
    ]

    wyglad=(plec,plec_slownie, rasa, wzrost, kolor_oczu, kolor_wlosow, kolor_skory)=generuj_wyglad_postaci(rasy)

    klasy = {
    "Wojownik":1,
    "Mag":2,
    "Zwiadowca":3,
    "Nekromanta":4,
    "Złodziej":5,
    "Paladyn":6
    }

    klasa=wybierz_klase(klasy)

    staty=(zdrowie, atak, obrona, inteligencja, zwinnosc, szczescie)=kalkulator_statystyk_postaci(plec, rasa, wzrost, klasa)
    
    config["Cechy Wygladu Postaci"]={
        "plec": plec_slownie,
        "rasa": rasa,
        "wzrost": wzrost,
        "kolor_oczu": kolor_oczu,
        "kolor_wlosow": kolor_wlosow,
        "odcien_skory": kolor_skory,    
    }
    config["Klasa Postaci"]={
        "nazwa_klasy": klasa,
    }
    config["Statystyki Postaci"]={
        "zdrowie": zdrowie,
        "sila_ataku": atak,
        "obrona": obrona,
        "inteligencja": inteligencja,
        "zwinnosc": zwinnosc,
        "szczescie": szczescie,
    }

    if generuj_nazwe_pliku() == False:
        exit()
    else:
        sciezka_pliku = sciezka_kodu+"\\"+generuj_nazwe_pliku()
        with open(sciezka_pliku,"w", encoding="utf-8") as plik:
            config.write(plik)
            print("Wygenerowano nową postać!")

if __name__=="__main__":
    print("Witaj w generatorze postaci RPG!")
    x=input("Czy chcesz wygenerować swoją postać? (max 10) TAK/NIE\n> ")
    if x.upper() in ("TAK","T","YES","Y"):
            main()
    else:
            print("Zakończono działanie programu.")
            exit()
    
    while True:
            y=input("Czy chcesz generować kolejną postać? (max 10 postaci) TAK/NIE\n> ")
            if y.upper() in ("TAK","T","YES","Y"):
                main()
            else:
                print("Zakończono działanie programu.")
                exit()

        