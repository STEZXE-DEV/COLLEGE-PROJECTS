import pyinputplus as p

def pobierz_dane():
    inp1 = p.inputInt(prompt="1 - Konwersja stopni Celsjusza na Fahrenheita\n2 - Konwersja stopni Fahrenheita na Celsjusza\n", min=1, max=2)
    return inp1
def konwersja_stopni_C_na_F():
    inp2=p.inputFloat(prompt="Podaj wartość w stopniach Celsjusza: ")
    wzor=inp2*9/5+32
    format=str(inp2)+"°C"
    return format,str(wzor)+"°F"

def konwersja_stopni_F_na_C():
    inp2=p.inputFloat(prompt="Podaj warstość w stopniach Fahrenheita: ")
    wzor=(inp2-32)*5/9
    format=str(inp2)+"°F"
    return format,str(wzor)+"°C"

a=pobierz_dane()
match a:
    case 1:
        x,wynik=konwersja_stopni_C_na_F()
    case 2:
        x,wynik=konwersja_stopni_F_na_C()
print(f"{x} to {wynik}.")