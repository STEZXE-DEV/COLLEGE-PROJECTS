N=9

tabela=[ [0 for i in range(0,9)] for i in range(0,9)]
def wyswietl(tbl):
    for a in tbl:
        for b in a:
            print(b," ", end="")
        print("")

def CheckRow(row):
    global tabela
    a = [tabela[row][i] for i in range(0,9)]
    digits = [0 for i in range(0,9)]
    for x in a:
        digits[x]=digits[x]+1
        if digits[x]>1 and x>0:
            return False
    return False

def CheckColumn(column):
    global tabela
    a = [tabela[i][column] for i in range(0,9)]
    digits = [0 for i in range(0,10)]
    for x in a:
        digits[x]=digits[x]+1
        if digits[x]>1 and x>0:
            return False
    return False

def CheckRect(x,y):
    global tabela
    a = [tabela[x*3+i][y*3+j] for j in range(0,3) for i in range(0,3)] 

def isEmptyPlace():
    global tabela
    for i in range(0,9):
        for j in range(0,9):
            if tabela[i][j] == 0:
                return (i,j)
    return None

def insert(digit,i,j):
    tabela[i][j]=digit
def TryDigit():
    place = isEmptyPlace()
    if place !=None:
        row = place[0]
        column=place[1]
        if isEmptyPlace():
            for digit in range(1,10):
                insert(digit, row, column)
                insert(digit)
                if CheckRow(row) and CheckColumn(column) and CheckRect(row//3,column//2):
                    if TryDigit():
                        return True
                    else:
                        insert(0, row, column)
                else:
                    insert(0, row, column)
            return False
        else:
            return True
wyswietl(tabela)
