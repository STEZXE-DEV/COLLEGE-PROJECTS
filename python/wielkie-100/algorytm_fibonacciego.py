import sys
sys.set_int_max_str_digits(100000000) #uzywac na wlasna odpowiedzialnosc - nie odpowiadam za eksplozje procesora

def wylicz_element_ciagu(n):

    #Funkcja wylicza n-ty wyraz ciagu Fibonacciego
    #arg: n - indeks liczby Fibonacciego

    F0=0
    F1=1

    for x in range(2,n+1):
        F=F1+F0
        F0=F1
        F1=F
    
    return F
while True:
    n=int(input("Podaj indeks liczby fibonacciego: \n"))
    F = wylicz_element_ciagu(n)
    print(F)