import customtkinter as ctk
import random as r

def zakoncz_program():
    okno_aplikacji.destroy()

def losuj():
    return r.randint(1, 100)

def wyswietl_los():
    global los
    los = losuj()
    wynik_losowania.configure(okno_aplikacji, text=str(los), font=("Helvetica", 100))

# Ustawienie motywu ciemnego
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue") #domyślny kolor dla elementów

okno_aplikacji = ctk.CTk() #okno
okno_aplikacji.geometry("1920x1080") #rozdzielczość okna w pixelach
okno_aplikacji.title("Maszyna losująca!") #tytuł okna
okno_aplikacji.attributes("-fullscreen", True) #pełny ekran

wynik_losowania = ctk.CTkLabel(okno_aplikacji, text="Kliknij \"Losuj!\" by wylosować!", font=("Helvetica", 60))
wynik_losowania.pack(expand=True)

komunikat = ctk.CTkLabel(okno_aplikacji, text=" ", font=("Helvetica", 30))
komunikat.pack(side="top", pady=150)

przycisk_losowania = ctk.CTkButton(okno_aplikacji, text="Losuj!", command=wyswietl_los, font=("Arial", 40, "bold"), height=100, width=350)
przycisk_losowania.pack(side="top", padx=10, pady=10)

przycisk_zamkniecia = ctk.CTkButton(okno_aplikacji, text="Zakończ", command=zakoncz_program, fg_color="#eb0e0e", hover_color="#732525", font=("Arial", 37, "bold"), height=100, width=350)
przycisk_zamkniecia.pack(side="top", padx=10, pady=50)

# Uruchomienie okna
okno_aplikacji.mainloop()