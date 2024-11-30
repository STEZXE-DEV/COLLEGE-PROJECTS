import pyinputplus as pyi
import math as m

#podanie liczby
a = pyi.inputFloat(prompt="Podaj liczbe: \n")
zao_w_d = m.floor(a) #<m.floor()> zaokragla liczbe w dol
zao_w_g = m.ceil(a) #<m.ceil() zaokragla liczbe w gore

#wypisanie zaokraglen 
#przyklady: (dla 3.45: floor: 3, ceil: 4) (dla -2.55: floor: -3, ceil: -2)
print(f"Zaokraglenie w dol: {zao_w_d}\nZaokraglenie w gore: {zao_w_g}")
