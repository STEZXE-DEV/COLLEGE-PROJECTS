import pyinputplus as p

a=p.inputInt(prompt="Podaj liczbę: ", min=0)

#funkcja <chr(wartość)> oczekuje całkowitej wartośći liczbowej, zwraca odpowiadający tej wartości znak
#dla wartośći: 0-127 ASCII, 128-255 extended ASCII (m.in. znaki diakrytyczne), 256+ UNICODE
b=chr(a)

if a<=255:
   print(f"Znak w ASCII: {b} Dec: {a} Hex: {hex(a)[2:]}") 
elif a>255:
   print(f"Znak w ASCII: {b} Dec: {a} Hex: {hex(a)[2:]}") 