waga = int(input("Podaj wage w kg: "))
wzrost = int(input("Podaj wzrost w cm: "))
wzrost_m = wzrost/100
bmi = waga/(wzrost_m**2)
value =""
if bmi<16:
    value="wyglodzenie"
elif 16<=bmi<=16.99:
    value="wychudzenie"
elif 17<=bmi<=18.49:
    value="niedowaga"
elif 18.5<=bmi<=24.99:
    value="wartosc prawidlowa"
elif 25<=bmi<=29.99:
    value="nadwaga"
elif 30<=bmi<=34.99:
    value="I st. otylosci"
elif 35<=bmi<=39.99:
    value="II st. otylosci"
elif bmi>40:
    value="otylosc skrajna"

print(value)