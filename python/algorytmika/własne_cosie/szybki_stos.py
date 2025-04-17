class Stos:
    def __init__(self):
        self.elements=[]
    
    def __repr__(self):
        return f"{self.elements}"
    
    def czy_pusty(self):
        return not self.elements
    
    def push(self, item):
        if type(item) == list: #jeżeli podany argument jest listą
            for i in item:
                self.elements.append(i)
        else: #jeżeli argument jest zwykłą wartością
            self.elements.append(item)

    def szczyt(self):
        return self.elements[len(self.elements)-1]
    
    def delete_last(self):
        return self.elements.pop()
    
    def calosc(self):
        strg=""
        for i in range(len(self.elements)): 
            if i == 0:
                strg+=f"{self.elements[i]}"
            else: strg+=f", {self.elements[i]}"
        return strg

    
lista=[1,6,7,3,9,12,4]

#operacje na stosie
stos = Stos()
stos.push(5)
stos.push(5)
stos.push(5)
stos.push(lista)

print(f"Elementy stosu: {stos.calosc()}")

print(f"Stos jest pusty?: {stos.czy_pusty()}")

print(f"Usunięto element: {stos.delete_last()}")

print(f"Elementy stosu: {stos.calosc()}")

print(f"Ostatni element stosu: {stos.szczyt()}")
