import pyinputplus as pyip
import time
import numpy as np
import matplotlib.pyplot as plt

def el_ciagu(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return el_ciagu(n - 2) + el_ciagu(n - 1)

def czas(n):
    start = time.process_time_ns()
    el_ciagu(n)
    return time.process_time_ns() - start  # Czas w nanosekundach

# Pobranie wartości n od użytkownika
n = pyip.inputInt(prompt='Podaj indeks liczby Fibonacciego: ', min=0, max=40)

# Obliczenie wartości liczby Fibonacciego dla n
fib_wynik = el_ciagu(n)
czas_wykonania=czas(n)/1e6
print(f"Liczba Fibonacciego dla n={n}: {fib_wynik}")
print(f"Czas wykonania: {czas_wykonania} (ms)")

# Tworzenie wykresu dla zakresu wartości n (od 0 do 40)
xpoints = np.array([x for x in range(0, n+1)])  # Ograniczamy do 40, bo czas rośnie wykładniczo
ypoints = np.array([czas(x)/1e6 for x in xpoints])  # dzielenie nanosekund (nano = 10^-9) przez 1e6 to konwersja na milisekundy

# Wykres
plt.figure(figsize=(10, 5))
plt.plot(xpoints, ypoints, linestyle='solid', color='b', label="Czas wykonania (ms)")  # Ciągła linia
plt.fill_between(xpoints, ypoints, color='r', alpha=0.9)  # Wypełnienie wykresu
plt.xlabel("n")
plt.ylabel("Czas (ms)")
plt.title("Czas obliczeń funkcji Fibonacciego (rekurencyjnie)")
plt.legend()
plt.show()
