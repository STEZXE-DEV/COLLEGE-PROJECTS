import pyinputplus as p

#pobranie zapisu słownego liczby
def pobierz_dane():
    inp=p.inputStr(prompt="Podaj liczbę słownie: ")
    return inp


#słownik zapisów słownych i ich wartości liczbowych
slowa={"minus":0,"zero":0,"jeden":1,"dwa":2,"trzy":3,"cztery":4,"pięć":5,"sześć":6,"siedem":7,"osiem":8,"dziewięć":9,
       "dziesięć":10,"jedenaście":11,"dwanaście":12,"trzynaście":13,"czternaście":14,"piętnaście":15,"szesnaście":16,"siedemnaście":17,"osiemnaście":18,"dziewiętnaście":19,
       "dwadzieścia":20,"trzydzieści":30,"czterdzieści":40,"pięćdziesiąt":50,"sześćdziesiąt":60,"siedemdziesiąt":70,"osiemdziesiąt":80,"dziewięćdziesiąt":90,
       "sto":100,"dwieście":200,"trzysta":300,"czterysta":400,"pięćset":500,"sześćset":600,"siedemset":700,"osiemset":800,"dziewięćset":900}

#funkcja, przyjmuje jako argument input użytkownika, a zwraca liczbę
def slowa_na_liczbe(a):
    spacje=a.count(" ")
    zapis=a.split(" ", spacje)  
    wartosc=0

    #jeśli dane słowo wystąpi dwa lub więcej razy w zapisie to każde powielenie zostanie zignorowane i nie wpłynie na wartość
    for i in zapis:
        if zapis.count(i)>1:
            zapis.remove(i)
    
    #rozpatrzenie przypadku kiedy liczba w zapisie słownym jest ujemna
    if zapis[0]=="minus":
        for i in zapis:
            if i in slowa.keys():
                wartosc-=slowa[i] #końcowa wartość jest obliczana poprzez odejmowanie wartości odpowiadającej słowu w słowniku
            
            #odporność kodu na niepowołane powielenie spacji
            elif i=="": 
                continue

            #odporność kodu na podanie niepoprawnego słowa
            else:
                print(f"Nie znaleziono liczby \"{i}\"")
                exit()
                break
    
    #przypadek liczby dodatniej
    else:
        for i in zapis:
            if i in slowa.keys():
                wartosc+=slowa[i] #końcowa wartość jest obliczana poprzez dodawanie wartości odpowiadającej słowu w słowniku
            elif i=="":
                continue
            else:
                print(f"Nie znaleziono liczby \"{i}\"")
                exit()
                break
    return wartosc

#funkcja wypisująca na ekranie ostateczną wartość liczbową liczby (zapis za pomocą cyfr)
def wypisz():
    a=pobierz_dane()
    wynik=slowa_na_liczbe(a)
    print(f"Wartość liczbowa: {wynik}")

if __name__=="__main__":
    wypisz()