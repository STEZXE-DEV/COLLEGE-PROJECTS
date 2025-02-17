import pyinputplus as p
import time as t

z=1
print("Nawiguje do: mieszkanie Wojtka")

while True:

    if z!=0 and z%5==0:
        b = p.inputChoice(["Tak", "Nie"], prompt=f"{z}. Czy widzisz Azkaban?\n")
        if b.upper() == "TAK":
            print("Dotarłeś do celu, tylko trzeba Wojtka poinformować!")
            break
        else:
            z+=1
    a = p.inputChoice(["Tak", "Nie"], prompt=f"{z}. Czy jesteś w Krakowie?\n")
    if a.upper() == "TAK":
        print("Idź prosto!")
        z+=1
    elif a.upper() == "NIE":
        print("Wyszedłeś z Krakowa, ZAWRACAJ DO KRAKOWA!")
    t.sleep(5)
    