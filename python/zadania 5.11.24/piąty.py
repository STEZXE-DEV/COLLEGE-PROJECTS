
while True:
    print("\n===========OBLICZANIE SREDNIEJ PREDKOSCI=========\n")
    decyzja = input("Czas w: godziny czy minuty\n")
    if decyzja=="godziny":
        droga = float(input("Podaj odległosc w KM pokonanej trasy\n"))
        czas = float(input("Podaj czas w godzinach w jakim ta trasa zostala pokonana\n"))
        avgV = droga/czas
        print("Średnia predkosc wynosi: ",avgV,"km/h")
    elif decyzja=="minuty":
        droga = float(input("Podaj odległosc w KM pokonanej trasy\n"))
        czas = int(input("Podaj czas w minutach w jakim ta trasa zostala pokonana\n"))
        avgV = droga/(czas/60)
        print("Średnia predkosc wynosi: ",avgV,"km/h")
    else:
        print("Wybierz: godziny lub minuty")