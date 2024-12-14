import pyinputplus as p
import math as m
inp = p.inputFloat(prompt="Podaj liczbę zmiennoprzecinkową: ")

#funkcja licząca wartość bezwzględną
def my_abs(a): 
    abs=a**2
    abs=m.sqrt(abs)
    return abs

wynik = my_abs(inp)
print(f"Wartość bezwzględna z '{inp}' wynosi: {wynik}")