import pyinputplus as p

#pobranie cyfry od użytkownika
inp = p.inputInt(prompt="Podaj cyfre: ", min=0, max=9) 

#definicja słownika z cyframi
cyfry = {1:"jeden", 2:"dwa",3:"trzy",4:"czterY",5:"pięć",6:"sześć",7:"siedem",8:"osiem",9:"dziewięć",0:"Hubert"}

if inp in cyfry.keys(): #sprawdzenie czy input znajduje się w kluczach słownika <cyfry>
    
    #moduł .capitalize() zamienia pierwszy znak na .upper() resztę na .lower()
    print(f"{cyfry[inp].capitalize()}")