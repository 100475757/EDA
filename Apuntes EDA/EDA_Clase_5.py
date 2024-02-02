#Listas simplemente enlazadas con head (SList)

class SNode:
    def __init__(self , e , next = None):
        self.elem = e 
        self.next = next

class SList:
    def __init__(self):
        self._head = None  #Iincializamos como None, como si estuviera vacía
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

    def push(self,e):
        newNode = SNode(e, self._head)
        self._head = newNode
        self._size += 1

    def pop(self): #Elimino el primer elemento 
        if self.isEmpty():
            print("No puedo eliminafr elementos de una lista vacía")
        
        self._head = self._head.next   # Quito la conexion, es decir convierto en la cabeza al siguiente nodo y se elimina automaticamente 
        self._size -= 1

    def addLast(self, e):
        newNode = SNode(e)
        current= self._head
        if self.isEmpty():
            self.push(e)
        else:
            while current.next != None:
                current = current.next
            current.next = newNode
        self._size += 1

    def removeLast(self): #Completar para los casos de 1 elemento y 0 elementos.
        if self._size ==1:
            self._head = None
        elif self._size == 0:
            self._head = None
        else:
            current = self._head
            while current.next.next != None:
                current = current.next
            current.next = None
            self._size -= 1



s = SList()
for i in range(5):
    s.push(i)
s.pop()
print(s)
s.addLast(9)
print(s)
s.removeLast()
print(s)
s.push(5)
print(s)
