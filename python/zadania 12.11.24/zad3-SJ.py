
while True:
    a = int(input("Podaj pierwsza dlugosc:\n"))      
    b = int(input("Podaj druga dlugosc:\n"))
    c = int(input("Podaj trzecia dlugosc:\n"))
    if a<=0 or b<=0 or c<=0 or a>=b+c or b>=c+a or c>=a+b:
        print("====================================")
        print("NIE MOZNA UTWORZYC TROJKATA")
        print("====================================")
    else:
        print("====================================")
        print("MOZNA UTWORZYC TROJKAT")
        if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
            print("TROJKAT JEST PROSTOKATNY")
            print("====================================")
        else:
            print("TROJKAT NIE JEST PROSTOKATNY")
            print("====================================")