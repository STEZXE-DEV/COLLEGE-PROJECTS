import pyinputplus as p

a = p.inputStr(prompt="Podaj tekst: ")
print(a[2:5]) #od 3 znaku do 5
print(a[2:]) #od 3 znaku do końca
print(a[:7]) #do 7 znaku