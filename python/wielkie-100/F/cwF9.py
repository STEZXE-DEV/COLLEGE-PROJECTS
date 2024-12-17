import pyinputplus as p

a=p.inputStr(prompt="Podaj zdanie: ")

spacje=a.count(" ")
x=a.split(" ", spacje)

#<.reverse()> odwrócenie zawartości listy
x.reverse()
for i in x:
    print(i,end=" ")