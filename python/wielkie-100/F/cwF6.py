import pyinputplus as p

a = p.inputStr(prompt="Podaj tekst: ")

#czy całość stringa jest w standardzie ASCII (0-127)
ascii=all(ord(i) < 128 for i in a)
if ascii==True:
    print("Wszystkie znaki należą do znaków ASCII.")
else:
    print("nie wszystkie znaki należą do znaków ASCII.")

#czy całość stringa jest alfanumeryczna (aA-zZ, 0-9)
if a.isalnum():
    print("Wszystkie znaki są alfanumeryczne.")
else:
    print("Nie wszystkie znaki są alfanumeryczne.")

#czy całość stringa tworzy liczbę
if a.isdigit():
    print("Znaki tworzą liczbę.")
else:
    print("Znaki nie tworzą liczby.")