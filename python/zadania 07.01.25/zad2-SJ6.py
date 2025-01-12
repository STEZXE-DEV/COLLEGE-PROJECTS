import pyinputplus as p

def pobierz_dane():
    inp1 = p.inputInt(prompt="1 - Konwersja m/s na km/h\n2 - Konwersja km/h na m/s\n", min=1, max=2)
    return inp1
def konwersja_ms_na_kmh():
    inp2=p.inputFloat(prompt="Podaj prędkość w m/s: ")
    wzor=inp2/(1000/3600)
    format=str(inp2)+" m/s"
    return format,str(wzor)+" km/h"

def konwersja_kmh_na_ms():
    inp2=p.inputFloat(prompt="Podaj prędkość w km/h: ")
    wzor=inp2*1000/3600
    format=str(inp2)+" km/h"
    return format,str(wzor)+" m/s"

a=pobierz_dane()
match a:
    case 1:
        x,wynik=konwersja_ms_na_kmh()
    case 2:
        x,wynik=konwersja_kmh_na_ms()
print(f"{x} to {wynik}.")