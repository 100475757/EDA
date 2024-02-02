#Listas simplemente enlazadas con  head y tail (SList)

import random as rd

class SNode:
    def __init__(self , e , next = None):
        self.elem = e 
        self.next = next

class SList:
    def __init__(self):
        self._head = None  #Iincializamos como None, como si estuviera vacía
        self._tail = None
        self._size = 0 
        
    def __str__(self):
        result = "["
        result += str(self._head.elem)  + "," 
        current =  self._head.next     #Creo una variable que me diga en que caja estoy 
        while current != None:
            result += str(current.elem) + ","
            current = current.next
        result = result[:-1]
        result += "]"
        return result 
    
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0

    def addFirst(self,e):
        newNode = SNode(e, self._head)
        self._head = newNode
        if self._size== 0:
            self._tail = newNode
        self._size += 1

    def removeFirst(self): #Elimino el primer elemento 
        if self.isEmpty():
            print("No puedo eliminar elementos de una lista vacía")
        else:
            if self._size == 1:
                self._tail = None
            self._head = self._head.next   # Quito la conexion, es decir convierto en la cabeza al siguiente nodo y se elimina automaticamente 
            self._size -= 1

    def addLast(self, e):
        newNode = SNode(e)
        if self._size == 0:
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.next = newNode
            self._tail = newNode
        self._size += 1

    def removeLast(self): #Completar para los casos de 1 elemento y 0 elementos.
        if self._size ==0:
            print("Lista vacía. No se puede ejecutar removeLast")
        elif self._size == 1:
            self._head = None
            self._tail = None
            self._size = 0
        else:
            current = self._head 
            while current.next.next:
                current = current.next
            current.next = None
            self._tail = current
            self._size -= 1

    def insertAt(self, index, e):
        if index == 0:
            self.addFirst(e)
        elif index == self._size:
            self.addLast(e) 
        else:
            newNode = SNode(e)
            current = self._head
            for i in range(index-1):  #index-1 pq sino me paso, me tengo que quedar en el anterior a index
                current = current.next
            newNode.next = current.next
            current.next = newNode
            self._size += 1
    
    def removeAt(self, index): #devuelve y borra el elemento de la posición index de la lista. 
        result = None
        if self.isEmpty():
            print("No puedo eliminar elementos de una lita vacía")
        elif index > self._size:
                print("El índice es mayor que el tamaño de la lista")
        elif index == 0:
            result = self.removeFirst()
        elif index == self._size-1:
            result = self.removeLast()
        else:
            current = self._head
            for i in range(index-1):
                current = current.next
            result = current.next.elem
            current.next = current.next.next            
            self._size -=1     
        
        return result

    def getAt(self, index): #devuelve el elemento en la posición index de la lista.
        result = None
        current = self._head
        if self.isEmpty():
            print("No puedo devolver elementos de una lita vacía")
        elif index > self._size:
                print("El índice es mayor que el tamaño de la lista")
        elif index == 0:
            result = current.elem            
        else:
            for i in range(index):
                current = current.next
            result = current.elem     

        return result


# Ejercicios propuestos acerca de listas simplemente enlazadas

    def remove(self, e): #método que recibe un elemento, e, y borra la primera ocurrencia de e en la lista (es decir, elimina el primer nodo que contiene a e). La función modifica la lista y no devuelve nada. Si el elemento no existe en la lista, la función debe informar que no existe.
        prev = None
        current = self._head
        found = False #Utilizamos las llamadas banderas
        while not found and current : #current != None
            if current.elem==e:
                #remove node
                if prev == None:
                    #it is the first node
                    self._head = self._head.next
                    if self._head == None:
                        self._tail = None
                else:
                    #it's not the first node
                    prev.next = current.next
                    if current.next == None:
                        #current was the last node
                        self._tail = prev

                self._size -=1
                found=True
            else:
                prev=current
                current=current.next
                
        if not found:
            print(e, ' does not exist!!!')
        
    def removeAll(self, e): #función que recibe un elemento, e, y borra todas las ocurrencias de e en la lista (es decir, elimina todos los nodos que contienen a e). La función modifica la lista y no devuelve nada. Si el elemento no existe en la lista, la función debe informar que no existe.
        """This solution does not not use any function of the SList class"""
        prev = None
        current = self._head
        while current : #current != None
            if current.elem == e:
                #remove node
                if prev == None:
                    #it is the first node
                    self._head = self._head.next
                    if self._head == None:
                        self._tail = None
                else:
                    #it's not the first node
                    prev.next = current.next
                    if current.next == None:
                        #nodeIt was the last node
                        self._tail = prev
                self._size -=1
            else:
                prev = current
            current = current.next
            
    def getAtRev(self, index): #función que recibe un índice, index, y devuelve el elemento en la posición index empezando por el final.
        """This solution is based on the function getAt"""
        result=None
        n=self._size
        if index>=0 and index<n:
            i=0
            current=self._head
            while index<n-1-i:
                current=current.next
                i+=1
                
            result=current.elem
            
        else:
            print(index,' wrong!!!')
        return result          

    def getMiddle(self): #función que devuelve el elemento que está en la mitad de la lista. Si la lista tiene un número par de elementos, la función devolverá el elemento en la posición len(l)//2 +1.
        current = self._head
        while self._size != 0:
            if self._size % 2 == 0:
                for i in range(self._size//2):
                    current = current.next
            else:
                for i in range((self._size-1)//2):
                    current = current.next
            
            return current.elem

    def count(self, e): #: función que recibe un elemento, e, y devuelve el número de veces que ocurre en la lista. Si el elemento no existe en la lista, la función devuelve 0.
        current = self._head  
        contador = 0
        while current:
            if current.elem == e:
                contador += 1
            current = current.next
        return contador             #Contemplamos todos los casos


    """def isPalindrome(self): #función que comprueba si los elementos contenidos en la lista forman una palabra palíndroma (por ejemplo, radar, aba, abba, abcba). Si es palíndroma devuelve True, y en otro caso, False.
        current = self._head 
        prev = None
        while current == self._tail:"""
    
    """Sea SList la implementación de lista enlazada (una versión
    simplificada con los métodos necesarios para inicializar una lista con elementos).
    Completa la función moveLastToFront, que reciba un entero k, y que como
    resultado mueve los últimos k elementos de la lista al principio de la lista. A
    """

    def moveLastToFront(self, k:int):
        if k > 0 and k < self._size:
            current = self._head
            while current.next:
                current = current.next
            for i in range(self._size - k):
                current.next = self._head
                self._head = self._head.next
                current = current.next
            
            current.next = None


s = SList()
for i in range(5):
    s.addLast(i)
print(s)
s.moveLastToFront(2)
print(s)






s = SList()
for i in range(5):
    s.addFirst(i)
s.removeFirst()
print(s)
s.addLast(9)
print(s)
s.removeLast()
print(s)
s.removeFirst()
print(s)
for i in range(8):
    s.addLast(1)
print(s)
print(s.count(1))
s.remove(2)
print(s)
s.removeAt(1)
print(s)
s.addFirst(56)
s.removeAll(1)
print(s)
for i in range(5):
    s.addLast(rd.randint(0,9))
print(s)
print(s.getAt(4))
print(s.getAtRev(3))
for i in range(3):
    s.addLast(rd.randint(0,9))
print(s)
print(s.getMiddle())