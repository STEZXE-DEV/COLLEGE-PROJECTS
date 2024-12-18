import pyinputplus as p

def pobierz_dane():
    inp=p.inputInt(prompt="Podaj ilość liczb ciągu do wygenerowania: ")
    return inp

def glowna():
    N=pobierz_dane()
    N0=0
    N1=1
    for i in range(0, N-1):
        #dla pierwszego wyrazu ciągu zostaje wypisane 0
        if i==0:
           print(0, end=" ") 
        fib=N0+N1
        N0=N1
        print(f"{N0}", end=" ")
        N1=fib
            

if __name__=="__main__":
    glowna()