class Node:
    def __init__(self, data):
        self.data=data #Node value
        self.next=None #default None

    def __repr__(self):
        return "Node({:d})".format(self.data)
            

class Linkedlist:
    def __init__(self, node=None):
        self.head = node
    
    def __repr__(self):
        strl= "Lista: {:d}\n".format(self.size())
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
        else:
            self.head, node.next = node, self.head

    def size(self):
        count = 0
        cursor = self.head
        while cursor is not None:
            count += 1
            cursor = cursor.next
        return count

    

    def insert(self, node, data_to_insert):
        data_to_insert.next=node.next
        node.next=data_to_insert

    def find(self, item):
        poczatek=self.head
        while poczatek!=None and poczatek.data!=item:
            poczatek=poczatek.next
        return poczatek


x=Linkedlist()
t=x.is_empty()
print(t)
x.add(5)

dti=Node(25)
x.insert(x.head, dti)
print(x)
y=x.find(35)
print(y)
