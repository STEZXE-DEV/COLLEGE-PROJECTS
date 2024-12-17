a=input('Podaj słowo: ')
b=[]
for i in a:
    b.append(i)
b.reverse()
b=''.join(b)

if a==b:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")
