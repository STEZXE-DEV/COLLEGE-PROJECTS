class Node:
    def __init__(self, parent, nazwa, cena, ilosc):
        self.ilosc = ilosc
        self.parent = parent
        self.nazwa = nazwa
        self.cena = cena
        self.right = None
        self.left = None

    def next(self):
        if self.right is not None:
            x = self.right
            while x.left is not None:
                x = x.left
            return x
        x = self
        while x.parent is not None and x == x.parent.right:
            x = x.parent
        return x.parent

    def prev(self):
        if self.left is not None:
            x = self.left
            while x.right is not None:
                x = x.right
            return x
        x = self
        while x.parent is not None and x == x.parent.left:
            x = x.parent
        return x.parent


class BST:
    def __init__(self, nazwa=None, cena=None, ilosc=None):
        self.root = None
        self.N = 0

    def _add(self, node, nazwa, cena, ilosc):
        if ilosc < node.ilosc:
            if node.left is None:
                node.left = Node(node, nazwa, cena, ilosc)
            else:
                self._add(node.left, nazwa, cena, ilosc)
        else:
            if node.right is None:
                node.right = Node(node, nazwa, cena, ilosc)
            else:
                self._add(node.right, nazwa, cena, ilosc)

    def add(self, nazwa, cena, ilosc):
        if self.root is None:
            self.root = Node(None, nazwa, cena, ilosc)
        else:
            self._add(self.root, nazwa, cena, ilosc)
        self.N += 1

    def findMin(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node

    def findMax(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node

    def findMedian(self):
        node = self.findMin()
        for i in range(self.N // 2):
            node = node.next()
        return node


akcje = []
with open("gielda.txt", 'rt') as f:
    for line in f.readlines():
        tokens = line.split()
        akcje.append((tokens[0], float(tokens[1]), int(tokens[2])))
f.close()

drzewo = BST()

for x in akcje:
    drzewo.add(x[0], x[1], x[2])

n = drzewo.findMax()
print(f"Akcje o najwyższym obrocie:")
for i in range(1, 6):
    if n is not None:
        print(f"{i}. {n.ilosc} {n.nazwa}")
        n = n.prev()
    else:
        break




