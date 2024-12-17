import pyinputplus as p

a=p.inputStr(prompt="Podaj zdanie: ")

#zliczenie ilości spacji w inpucie
spacje=a.count(" ")

#lista podzielonych słów znakiem spacji, ilość podzielen to ilość spacji
x=a.split(" ", spacje)

#wypisanie każdego elementu
for i in x:
    #[::-1] odwraca element listy
    print(i[::-1], end=" ")