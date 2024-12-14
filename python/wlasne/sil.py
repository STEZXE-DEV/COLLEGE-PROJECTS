
wybor = int(input("Podaj metode"))
x=int(input("Podaj liczbe: "))
a=x
for i in range(1, x+1):
    if i == a:
        print(x)
    else:
        x*=i