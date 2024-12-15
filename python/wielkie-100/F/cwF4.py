import pyinputplus as p

a=p.inputStr(prompt='Podaj słowo: ')
b=[]
for i in a:
    b.append(i)
b.reverse()

#złączenie elementów listy odbywa się za pomocą modułu "separator".join(list)
b=''.join(b)

if a==b:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")
