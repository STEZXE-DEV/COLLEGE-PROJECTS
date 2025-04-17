class Queue:
    def __init__(self, rozmiar):
        self.table = [None] * rozmiar
        self.head = 0
        self.tail = 0
        self.size = 0
        self.rozmiar = rozmiar

    def queue_size(self):
        return self.size

    def push(self, N):
        if self.size < self.rozmiar:
            self.table[self.tail] = N
            self.tail = (self.tail + 1) % self.rozmiar
            self.size += 1
        else:
            raise RuntimeError("Queue full")

    def pop(self):
        if self.size > 0:
            x = self.table[self.head]
            self.table[self.head] = None
            self.head = (self.head + 1) % self.rozmiar
            self.size -= 1
            return x
        else:
            raise RuntimeError("Queue empty")

    def __repr__(self):
        return f"Queue size: {self.size}, Table: {self.table}"

x = Queue(10)
print(x)

x.push(1)
x.push(2)
x.push(3)
x.push(4)
print(x)

print("Popped:", x.pop())
print(x)

x.push(5)
x.push(6)
print(x)
