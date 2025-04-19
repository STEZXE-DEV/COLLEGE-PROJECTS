import customtkinter as ctk
import random as r
import os
import pygame as pyg
import threading
from mutagen.mp3 import MP3

# Ścieżka folderów w jakich znajduje się kod
sciezka_kodu = os.path.dirname(os.path.realpath(__file__))

# Funkcja mierząca czas trwania pliku dźwiękowego w formacie MP3
def dlugosc_trwania_mp3():
    mp3 = MP3(sciezka_mp3)
    return int(mp3.info.length*1000) #zwraca wartość długości pliku w milisekundach

# Funkcja zamykająca główne okno programu
def zakoncz_program():
    okno_aplikacji.destroy()

# Funkcja losująca wartość całkowitą
def losuj():
    return r.randint(1, 5)

# Funkcja wyświetla wynik losowania na ekranie, ukrywa przycisk losowania, wypisuje komunikat o odtwarzanym pliku
def wyswietl_los():
    global los #global pozawala na dostęp do zmiennej w innych funkcjach
    global przycisk_losowania
    los = losuj()
    przycisk_losowania.pack_forget()
    przycisk_zamkniecia.pack(pady=110)
    wynik_losowania.configure(okno_aplikacji, text=str(los), font=("Helvetica", 100))
    komunikat.configure(okno_aplikacji, text=f"Odtwarzanie dźwięku - nagranie{los}.mp3...", font=("Helvetica", 30))
    odtworz_dzwiek()

# Funkcja przywraca widoczność przycisku losowania, który ukrywany jest w <wyswietl_los()>
def pokaz_przycisk_losowania():
    przycisk_losowania.pack(before=przycisk_zamkniecia,side="top", padx=10, pady=10)
    przycisk_zamkniecia.pack(pady=50)

# Zestaw funkcji do otwarzania dźwięku
def odtworz_dzwiek():
    def odtwarzanie():
        global sciezka_mp3
        sciezka_mp3 = f"{sciezka_kodu}\\nagranie{los}.mp3"
        if os.path.exists(sciezka_mp3): # Sprawdzenie czy plik audio (MP3) istnieje
            pyg.mixer.init()
            pyg.mixer.music.load(sciezka_mp3)
            pyg.mixer.music.play()
            komunikat.after(dlugosc_trwania_mp3(), wyczysc_komunikat) # Po zakończeniu trwania pliku MP3 komunikat znika
            komunikat.after(dlugosc_trwania_mp3(), pokaz_przycisk_losowania) # Po zakończeniu trwania pliku MP3 przywrócona zostaje widoczność przycisku losowania
        else: 
            komunikat.configure(text=f"Nie znaleziono pliku!", font=("Helvetica", 30)) # Jeżeli plik audio (MP3) nie istnieje, to zostanie wypisany komunikat
    # Threading zapobiega zamrożeniu ("zawieszeniu się") GUI w czasie odtwarzania pliku audio (MP3)   
    threading.Thread(target=odtwarzanie, daemon=True).start()

# Funkcja, która czyści komunikat z jego zawartości
def wyczysc_komunikat():
    komunikat.configure(text=f"", font=("Helvetica", 30))

# Ustawienie motywu ciemnego
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue") #domyślny kolor dla elementów

okno_aplikacji = ctk.CTk() #okno
okno_aplikacji.geometry("1920x1080") #rozdzielczość okna w pixelach
okno_aplikacji.title("Maszyna losująca!") #tytuł okna
okno_aplikacji.attributes("-fullscreen", True) #pełny ekran

# Ustawienia etykiet
wynik_losowania = ctk.CTkLabel(okno_aplikacji, text="Kliknij \"Losuj!\" by wylosować!", font=("Helvetica", 60))
wynik_losowania.pack(side="top", pady=150)

komunikat = ctk.CTkLabel(okno_aplikacji, text=" ", font=("Helvetica", 30))
komunikat.pack(side="top", pady=150)

# Ustawienia przycisków
przycisk_losowania = ctk.CTkButton(okno_aplikacji, text="Losuj!", command=wyswietl_los, font=("Arial", 40, "bold"), height=100, width=350)
przycisk_losowania.pack(side="top", padx=10, pady=10)

przycisk_zamkniecia = ctk.CTkButton(okno_aplikacji, text="Zakończ", command=zakoncz_program, fg_color="#eb0e0e", hover_color="#732525", font=("Arial", 37, "bold"), height=100, width=350)
przycisk_zamkniecia.pack(side="top", padx=10, pady=50)

# Uruchomienie okna
okno_aplikacji.mainloop()