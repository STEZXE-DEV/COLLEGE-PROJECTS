a=15
b=17.5
c=-10**20
#formatowanie str.format()
print("{:5d}".format(a)) #d liczba calkowita (np. int)
print("{:7f}".format(b)) #liczba zmiennoprzecinkowa (np. float)
print("{:7.3f}".format(b)) #7- ilosc pol, .3 - ilosc pol po przecinku
print("{:e}".format(c)) #formatowanie naukowe
print("{:g}".format(c)) #formatowanie naturalne