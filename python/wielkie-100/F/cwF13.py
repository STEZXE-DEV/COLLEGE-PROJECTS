import pyinputplus as p

def pobierz_dane():
    inp=p.inputStr(prompt="Podaj łańcuch znaków: ")
    return inp

def glowna():
    a=pobierz_dane()
    #liczenie wystąpienia podanego elementu w stringu
    b=a.count("pa")
    print(b)

if __name__=="__main__":
    glowna()