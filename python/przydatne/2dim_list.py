#jedno z zadań na egzaminie z podstaw programowania

tabela=[[0 for i in range(0,9)] for i in range(0,9)] #lista dwuwymiarowa 10x10 elementów
z=1
for i in range(0,9):
    tabela[4][i]=z
for i in range(0,9):
    tabela[i][4]=z

#wyświetlenie tabelki
for i in tabela:
    for j in i:
        print(f"{j}", end=" ")
    print(" ")