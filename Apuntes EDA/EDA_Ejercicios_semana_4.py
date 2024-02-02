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
   
    def removeAt(self, index):
        if index==0:
            self.removeFirst()
       
        else:
            current = self._head
            for i in range(index-1):
                current = current.next
            current.next=current.next.next
            current.next.prev=current
            self._size-=1

    def removeAll(self, e):
        current=self._head
        index=0
        while current:
            if current.elem==e:
                current=current.next
                self.removeAt(index)
                
            else:
                current=current.next
                index+=1

    def remove(self, e): 
        """método que recibe un elemento, e, 
        y borra la primera ocurrencia de e en la lista (es decir, elimina el primer nodo que contiene a e). 
        La función modifica la lista y no devuelve nada. Si el elmento no existe en la lista debemos informar de ello"""
        prev=None
        current=self._head
        found=False
        while not found and current : #current!=None
            if current.elem==e:
                #remove node
                if prev==None:
                    #it is the first node
                    self._head=self._head.next
                    if self._head==None:
                        self._tail=None
                    else:
                        self._head.prev=None
                else:
                    #it's not the first node
                    prev.next=current.next
                    if current.next==None:
                        #nodeIt was the last node
                        self._tail=prev
                    else:
                        current.next.prev=prev

                self._size -=1
                found=True
            else:
                prev=current
                current=current.next
                
        if not found:
            print(e, ' does not exist!!!')

    def getAtRev(self, index): 
        """función que recibe un índice, index, y devuelve el elemento en la
            posición index empezando por el final"""
        result=None
        n=len(self)
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
    def getAtEff(self,index): 
        """versión eficiente de la función getAt, teniendo en cuenta si el index
        es menor o mayor que la mitad de la lista, para comenzar la búsqueda por el
        principio o por el final de la lista."""
        if index<0 or index>=len(self):
          print('error: index out of range')
          return None
        if index <= len(self)//2:
          print(index, len(self), 'searching from the beginning')
          return self.getAt(index)
        else:
          print(index,'searching from the tail')

          aux=self._tail
          i=len(self)-1
          result=None
          while aux!=None and result==None:
            if i==index:
              result=aux.elem
            aux=aux.prev
            i-=1

          return result

    


            
    
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
print("Primer elem:" , d._head.elem , "Último elem:" , d._tail.elem , "Tamaño:" , d._size )
d.remove(6)
print(d)
