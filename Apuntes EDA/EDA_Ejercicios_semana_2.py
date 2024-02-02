# Ejercicio 1: Crear una cola doblemente enlazada, es decir una cola que pueda añadir o eliminar elementos que estan al principio(head) o al final(tail) de la misma.

import random as rd 

class deque:
    def __init__(self): #creates an empty double-ended queue.
        self.items = []

    def __str__(self): # Devuelvo la cola de manera legible para comprobar las pruebas
        return str(self.items)    

    def isEmpty(self):  #checks if the deque is empty.
        return len(self.items) == 0

    def addLast(self,elem): #adds the elements at the end of the deque
        self.items.append(elem)

    def addFirst(self,elem): #: adds the element at the beginning of the deque
        if self.isEmpty():
            self.items.append(elem)
        else:
            self.items.insert(0 , elem)
 
    def removeFirst(self): #: returns and removes the first element of the deque
        if self.isEmpty():
            raise SyntaxError("No puedes eliminar elementos de una lista vacía")
        else:
            return self.items.pop(0)

    def removeLast(self): #: returns and removes the last element of the deque.
        if self.isEmpty():
            raise SyntaxError("No puedes eliminar elementos de una lista vacía")
        else:
            return self.items.pop()

    def __len__(self): #: returns the numbers of element in the deque.
        return len(self.items)

d = deque()
for i in range(0,6):
    d.addFirst(rd.randint(0,9))
print(d)
d.addFirst(8)
d.addLast(5)
print(d)
print(d.isEmpty())
d.removeFirst()
d.removeLast()
print(d)
print(d.__len__())

"---------------------------------------------------------------------------------------------------------------"
#Ejercicio 2: Printer queue: 
"""The class, PrinterQueue, must implement the following operations:
● addRequest: takes a request as input and adds it to the set of requests.
● printWork: gets the first request and shows its data (id and name file) by
console (it only simulates the imprension of the request) . The request has
to be removed from the set of requests.
● getNumRequest(): returns the total number of requests.
● showAll(): shows all the requests that have have been not printed.
● printAll(): print all the requests.
Include the needed instructions to test all the methods explained above."""

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

class Request:
    def __init__(self, id , name):
        self.id = id
        self.name = name 
    
    def __str__(self):
        return (f"Id: {self.id} , Name: {self.name}")

class PrinterQueue:
    def __init__(self):
        self.q = queue()
        
    def addRequest(self, request): # takes a request as input and adds it to the set of requests.
        self.q.enqueue(request)

    def printWork(self): #gets the first request and shows its data (id and name file) by console (it only simulates the imprension of the request).The request has to be removed from the set of requests.
        if self.q.isEmpty():
         print('There is no work to print')
         return 
        r=self.q.dequeue()
        print("printing...",r)
    
    def getNumRequest(self): #returns the total number of requests.
         return len(self.q)

    def showAll(self): #shows all the requests that have have been not printed.
        for r in self.q.items:
            print(r)
    
    def printAll(self): #print all the requests.
        while not self.q.isEmpty():
            self.printWork()


p = PrinterQueue()
p.addRequest(Request("293939","Unit2.pdf"))
p.addRequest(Request("111","Unit1.pdf"))
p.addRequest(Request("333","Unit3.pdf"))
p.showAll()
