import random as r 
import configparser as con
import os

config=con.ConfigParser()

sciezka_kodu=os.path.dirname(os.path.realpath(__file__))

def generuj_nazwe_pliku(nazwa="wygląd_postaci", rozszerzenie=".ini"):
    numer=1
    while True:
        if numer>10:
            print("Przekroczono maksymalną ilość postaci!")
            return False
        nazwa_pliku=f"{nazwa}{numer}{rozszerzenie}"
        if not os.path.exists(sciezka_kodu+"\\"+nazwa_pliku):
            return nazwa_pliku
        numer+=1
        

def generuj_wyglad_postaci():
    
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
    
    #rodzaje ras
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

    kolor_skory=r.choice(ks)

    if kolor_skory not in ("ciemny", "czarny"):
        kolor_wlosow=r.choice(kw)
    else:
        kw=["brązowy", "czarny"]
        kolor_wlosow=r.choice(kw)
    
    kolor_oczu=r.choice(ko)

    rasa=r.choice(rasy)

    plec=r.randint(0,1)

    if plec < 1:
        plec_slownie="Mężczyzna"
        wzrost=r.randint(150, 220)
        if wzrost<=165:
            rasa=r.choice(["Gnom", "Niziołek", "Krasnolud"])
        elif wzrost >=210:
            rasa="Gigant"
    else:
        plec_slownie="Kobieta"
        wzrost=r.randint(135, 210)
        if wzrost<=145:
            rasa=r.choice(["Gnom", "Niziołek", "Krasnolud"])
        elif wzrost >=200:
            rasa="Gigant"
    return plec_slownie, rasa, wzrost, kolor_oczu, kolor_wlosow, kolor_skory

def main():
    
    plec_slownie, rasa, wzrost, kolor_oczu, kolor_wlosow, kolor_skory=generuj_wyglad_postaci()

    config["Cechy Postaci"]={
        "płeć": plec_slownie,
        "rasa": rasa,
        "wzrost": wzrost,
        "kolor_oczu": kolor_oczu,
        "kolor_włosów": kolor_wlosow,
        "odcień_skóry": kolor_skory,    
    }
    if generuj_nazwe_pliku() == False:
        exit()
    else:
        sciezka_pliku = sciezka_kodu+"\\"+generuj_nazwe_pliku()
        with open(sciezka_pliku,"w", encoding="utf-8") as plik:
            config.write(plik)
            print("Wygenerowano nową postać!")

if __name__=="__main__":
    while True:
        print("Witaj w generatorze postaci RPG!")
        x=input("Czy chcesz wygenerować swoją postać? (max 10) TAK/NIE\n> ")
        if x.upper() in ("TAK","T","YES","Y"):
            main()
        else:
            print("Zakończono działanie programu.")
            exit()