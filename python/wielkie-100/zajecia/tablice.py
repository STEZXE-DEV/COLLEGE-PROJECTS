#tablica w pythonie jest nazywana listą
python_table = [] #definicja listy w pythonie

#dopisanie elementu <5> na koniec listy
python_table.append(5)

#pierwszy element listy ma indeks 0
python_table[0] 

#wstawienie na podany indeks <0> elementu <23>
python_table.insert(0, 23) #[23,5]

#zastapienie elementu o indeksie <0> elementem <12>
python_table[0] = 12 #[12,5]

#usuwanie elementu <5> z listy
python_table.remove(5) #[12]

#utworzenie listy z określoną liczba elementow - 12 (od 0 do 11)
python_table=[i for i in range(12)]

#utworzenie listy dwuwymiarowej
python_table2=[[i,i*2] for i in range(12)]
print(python_table)
print(python_table2[5][1])

#wyciągniecie zakresu elementow z listy (table slicing)
x=python_table[3:5]
y=python_table[3:]
z=python_table[:3]
print(x)
print(y)
print(z)

#liczba razy ile element o wartosci <4> wystąpił w liście
print(python_table.count(4))

#czyszczenie zawartosci listy
python_table2.clear()
print(python_table2)

#
# s = [str[x] for x in python_table]
# print("<>".join(s))
# print(s)

s = [1,2,3]
s1 = (1,2,3,4) #krotka
s2 = (*s1,5)
print(s2)

def funkcja(a,b,c):
    pass
p1 = (3,4,5)
funkcja(*p1)

#map(inaczej słownik) - kontener obsługi danych, jest asocjacją gdzie mamy klucz i wartość, które stanowią parę 
python_dict = {
    "John":23,
    "Heinz":11,
    "Jan":8,
    "Ho":124
}
