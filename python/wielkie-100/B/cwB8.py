import pyinputplus as pyi
#podanie daty (podstawowy format to yy/mm/dd h/m/s) np. 2024/11/29 16:04:49
data = pyi.inputDatetime(prompt="Podaj date w formacie (yy/mm/dd) wraz z godzina (h/m/s): \n") 
#podanie wartosci staloprzecinkowej(Int) z zakresu <min> 1000 i <max> 1005
wartosc1 = pyi.inputInt(prompt="Podaj wartosc z zakresu [1000, 1005]: \n", min=1000, max=1005) 
#podanie wartosci zmiennoprzecinkowej wiekszej niz <greatherThan> 4.2
wartosc2 = pyi.inputFloat(prompt="Podaj wartosc wieksza niz 4.2: \n", greaterThan=4.2) 
#podanie wartosci z dostepnych w menu red, green lub blue
kolor = pyi.inputMenu(['red', 'green', 'blue'], prompt="Wybierz kolor z dostepnych na liscie: \n") 
#podanie wartosci w typie BOOL (TRUE/FALSE) 
w_bool = pyi.inputBool(prompt="True/False: \n") 
#wypisanie wszystkich inputow 
print(f"Podana data i godzina: {data}\nWartosc z zakresu [1000,1005]: {wartosc1}\nWartosc wieksza niz 4.2: {wartosc2}\nKolor z listy: {kolor}\nWartosc BOOL: {w_bool}")
