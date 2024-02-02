import random as rd


# PILAS

class stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):  # equivalente a return len(self.items) == 0
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, other):
        self.items.append(other)

    def pop(self):
        if self.isEmpty():  # Equivalente a if len(self.items) == 0:
            print("La lista está vacía, no hay elementos")
        else:
            return self.items.pop()  # .pop elimina y devuelve el elemento de la ultima posicion

    def top(self):
        if self.isEmpty():  # Equivalente a if len(self.items) == 0:
            print("La lista está vacía, no hay elementos")
            return None
        else:
            return self.items[-1]

    def __len__(self):
        return len(self.items)

s = stack()
print(s)
for i in range(0, 6):
    s.push(rd.randint(0, 9))
print(s)
s.pop()
print(s)
print(s.top())
print(s.__len__())

"------------------------------------------------------------------------------------------------------------------"


# COLAS

class queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, other):
        self.items.append(other)

    def dequeue(self):
        if self.isEmpty():  # Equivalente a if len(self.items) == 0:
            print("La lista está vacía, no hay elementos")
            return None
        else:
            return self.items.pop(0)

    def front(self):
        if self.isEmpty():  # Equivalente a if len(self.items) == 0:
            print("La lista está vacía, no hay elementos")
            return None

        else:
            return self.items[0]
    
    def __len__(self):
        return len(self.items)

q = queue()

for i in range(0, 6):
    q.enqueue(rd.randint(0, 9))

print(q)
q.dequeue()
print(q)
print(q.front())

"--------------------------------------------------------------------------------------------------------------------"


# Palindromas palabras

def reverse(world):
    s = stack()
    string = ""
    for i in world:
        s.push(i)
    for i in range(len(s.items)):
        string += s.pop()


print(reverse("abcdefg"))


