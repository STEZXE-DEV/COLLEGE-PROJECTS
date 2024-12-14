def silnia(s):
    if s<=1:
        return 1
    else:
        return s*silnia(s-1)

s=int(input("Podaj liczbe: "))
wynik = silnia(s)
print(wynik)