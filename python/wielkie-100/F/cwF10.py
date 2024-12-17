import pyinputplus as p

a=p.inputInt(prompt="Podaj liczbę całkowitą: ", lessThan=1000)

#deklaracja słownych zapisów liczb
jedn=['','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć']
nas=['','jedenaście','dwanaście','trzynaście','czternaście','piętnaście','szesnaście','siedemnaście','osiemnaście','dziewiętnaście']
dz=['','dziesięć','dwadzieścia','trzydzieści','czterdzieści','pięćdziesiąt','sześćdziesiąt','siedemdziesiąt','osiemdziesiąt','dziewięćdziesiąt']
setk=['','sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset']

#funkcja zamiany liczby na słowa
def liczba_na_slowa(liczba):
    
    #deklaracja listy, w której znajdować się będą słowa zapisu liczby
    zapis=[]

    if liczba < 0:
        #obsługa liczb ujemnych za pomocą rekurencji
        return "minus " + liczba_na_slowa(-liczba)
    if liczba == 0:
        return "zero"
    
    #obliczenie reszt
    reszta_s=liczba//100
    reszta_dz=liczba//10-(10*reszta_s)
    reszta_j=liczba-reszta_s*100-reszta_dz*10

    #obsługa liczb _11-_19 (szczególny przypadek)
    if reszta_dz==1 and reszta_j in range(1,10):
        if reszta_s!=0:
            zapis.append(setk[reszta_s])
        if reszta_dz!=0:
            zapis.append(nas[reszta_j])
    
    #obsługa pozostałych liczb
    else:
        if reszta_s!=0:
            zapis.append(setk[reszta_s])
        if reszta_dz!=0:
            zapis.append(dz[reszta_dz])
        zapis.append(jedn[reszta_j])
    
    #otrzymanie końcowego zapisu słownego liczby poprzez złączenie elementów listy <zapis>
    zapis_koncowy=' '.join(zapis)
    return zapis_koncowy

#funkcja wypisania liczby w postaci słownej na ekranie
def wypisz():   
    wynik=liczba_na_slowa(a)
    print(wynik)

if __name__=="__main__":
    wypisz()