import pyinputplus as pip #as - tworzy alias dla importowanej funkcji
#deklaracja wejscia
wejscie = pip.inputStr(prompt="Podaj nazwe towaru i ilosc sztuk w formacie: <nazwa_towaru> <ilosc_sztuk>\n", blank=False) 
#przypisanie dla dwoch zmiennych, gdyz rsplit() dzieli tekst podany w wejsciu od konca na dwa elementy
nazwa_towaru, ilosc_sztuk=wejscie.rsplit(" ", 1)
#wypisanie zmiennych zgodnie z zadanym formatowaniem nazwa na 30 znakach a ilosc na 4 znakach
print(f"Towar1: {nazwa_towaru:30s} szt.{int(ilosc_sztuk):4d}")