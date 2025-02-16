import pyinputplus as p
a = p.inputInt("Podaj pierwszą liczbę: ", greaterThan=0)
b = p.inputInt("Podaj drugą liczbę: ", greaterThan=0)
while True:
    if a==b:
        print(f"NWD wynosi: {a}")
        break
    elif a>b:
        a-=b
    elif a<b:
        b-=a