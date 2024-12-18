import pyinputplus as p

def pobierz_dane():
    inp = p.inputStr(prompt="Podaj ciąg znaków: ")
    return inp

def glowna():
    a = pobierz_dane()
    
    #moduł <.replace(old, new)> zamienia stary element łańcucha na nowy
    a=a.replace("r","w")
    print(a)

if __name__=="__main__":
    glowna()