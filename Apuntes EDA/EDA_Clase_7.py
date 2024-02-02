#Listas doblemente enlazadas


import random as rd

class DNode:
    def __init__(self , e , next = None , prev = None):
        self.elem = e 
        self.next = next
        self._prev = prev

class DList:
    def __init__(self):
        self._head = None  #Iincializamos como None, como si estuviera vacía
        self._tail = None
        self._size = 0 
    
    def __str__(self):
        result = "["
        if self._size == 0:
            result = "[]"
        else:
            result += str(self._head.elem)  + "," 
            current =  self._head.next     #Creo una variable que me diga en que caja estoy 
            while current != None:
                result += str(current.elem) + ","
                current = current.next
            result = result[:-1]
            result += "]"
        return result 
    
    def isEmpty(self):
        return self._size == 0

    def addFirst(self,e):
        newNode = DNode(e, self._head , self._tail)
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            newNode.next = self._head
            self._head.prev =newNode
            self._head = newNode
        
        self._size += 1 

    def removeFirst(self):  #Para quitar un nodo, hay que eliminar las conexiones que van a el no sus conexiones con otros.
        if self.isEmpty():
            print("No puedo eliminar elemnetos de una lista vacía")
        else:
            self._head = self._head.next 
            if self._size >1:
                self._head.prev = None
            else:
                self._tail = None
            self._size -= 1

    def addLast(self , e):
      newNode = DNode(e)
      newNode.prev = self._tail
      if not self.isEmpty():
         self._tail.next = newNode
      else:
        self._head = newNode
      self._tail = newNode
      self._size += 1

    def insertAt(self, index , e):
        newNode = DNode(e)
        current = self._head
        for i in range(index-1):
            current = current.next
        newNode.prev = current 
        newNode.next = current.next
        current.next.prev = newNode
        current.next = newNode
        self._size += 1      


d = DList()
print(d)
d.addFirst(5)
print(d)
d.addFirst(7)
for i in range(5):
    d.addFirst(rd.randint(0,9))

print(d)
d.removeFirst()
print(d)
d.addLast(4)
print(d)
print("Primer elem:" , d._head.elem , "Último elem:" , d._tail.elem , "Tamaño:" , d._size )
