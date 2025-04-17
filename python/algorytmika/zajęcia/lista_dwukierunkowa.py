class Node:
    def __init__(self, data):
        self.data=data 
        self.next=None
        self.prev = None

    def __repr__(self):
        return "Node({:d})".format(self.data)
            

class Linkedlist:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
    
    def __repr__(self):
        strl= "Lista {:d} elementów\n ".format(self.size())
        poczatek=self.head
        while poczatek!=None:
            strl+="{:d}, ".format(poczatek.data)
            poczatek=poczatek.next
        return strl


    def is_empty(self):
        return self.head is None

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.head, node.next = node, self.head
            node.next.prev = node

    def size(self):
        count = 0
        cursor = self.head
        while cursor is not None:
            count += 1
            cursor = cursor.next
        return count

    

    def insert(self, node, data_to_insert):
        data_to_insert.next = node.next
        data_to_insert.prev = node
        if node.next:
            node.next.prev = data_to_insert
        node.next = data_to_insert

    def find(self, item):
        poczatek=self.head
        while poczatek!=None and poczatek.data!=item:
            poczatek=poczatek.next
        return poczatek
    def rfind(self, item):
        koniec=self.tail
        while koniec!= None and koniec.data != item:
            koniec=koniec.prev
        return koniec
    
    def delete(self, N:Node):
        if N.prev!=None:
            N.prev.next=N.next
        else:
            self.head=N.next
        if N.next!=None:
            N.next.prev=N.prev
        else:
            self.tail=N.prev
        N.next = N.prev = None

    def merge(self, other_list):
        N = other_list.head
        while N!=None:
            if self.find(N.data)==None: 
                self.add((N.data))
            N = N.next

    def append(self, item):
        n = Node(item)
        self.tail.next = n
        n.prev = self.tail
        self.tail = n
        


x=Linkedlist()
t=x.is_empty()
print(t)
x.add(5)
x.add(7)
t=x.find(5)
x.delete(t)
dti=Node(25)
x.insert(x.head, dti)
print(x)
# y=x.find(35)
# print(y)
z=Linkedlist()
z.add(5)
z.add(7)
z.add(8)
z.add(11)
z.add(43)
print(z)
x.merge(z)
print(f"Lista po złączeniu: {x}")