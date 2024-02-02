from EDA_Clase_6 import SList
from EDA_Clase_6 import SNode
import random as rd

class SList2(SList,SNode):
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
        if self.isEmpty():
            print("Error: list is Empty")
        else:
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
        if self.isEmpty():
            print("Error: list is Empty")
        else:
            current = self._head  
            contador = 0
            while current:  #current!= None
                if current.elem == e:
                    contador += 1
                current = current.next
            return contador             #Contemplamos todos los casos
        
    def isPalindrome(self): 
        """función que comprueba si los elementos contenidos en la lista
            forman una palabra palíndroma (por ejemplo, radar, aba, abba, abcba). Si es
            palíndroma devuelve True, y en otro caso, False."""
        m=len(self)//2
        if m>0:
            for i in range(m+1):
                if self.getAt(i)!=self.getAtRev(i):
                    return False
                
        return True

    def isSorted(self): 
        """función que comprueba si la lista está ordenada de forma ascendente (en
            este caso devuelve True). En caso contrario, debe devolver False."""
        ordenada = False 
        current = self._head 
        nodeIt = current.next
        i = 0
        while nodeIt != None and self._size> 0:
            if current.elem <= nodeIt.elem:
                current = nodeIt
                nodeIt = nodeIt.next
                i += 1
            else: 
                current = nodeIt
                nodeIt = nodeIt.next
                    
        if i == self._size -1:
            ordenada = True
        else: 
            ordenada = False
        
        return ordenada
        
    def removeDuplicates(self): 
        """función que borra los elementos duplicados en una lista (no
        tiene que estar ordenada). La función modifica la lista, no devuelve nada."""
        current =self._head
        while current:
            prev= current
            nodeIt=current.next

            e=current.elem
            while nodeIt:
                if e==nodeIt.elem:
                    prev.next=nodeIt.next
                    if nodeIt.next==None:
                        self._tail=prev
                    self._size-=1
                else:    
                    prev=nodeIt

                nodeIt=nodeIt.next
                
            current=current.next
    
    def swapPairwise(self): 
        """función que intercambia los elementos que ocupan posiciones
            contiguas. La función modifica la lista, no devuelve nada"""
        if self._size > 1:
            current=self._head
            nodeIt=current.next
            while current and nodeIt:
                #swap elements
                current.elem,nodeIt.elem=nodeIt.elem,current.elem
                current=nodeIt.next
                if current:
                    nodeIt=current.next

    def moveLast(self): 
        """función que mueve el último elemento al principio de la lista, sin usar
        ninguna de las funciones de la clase SList. La función modifica la lista, no devuelve
        nada."""
        current = self._head
        nodeIt = current.next
        while nodeIt.next and self._size > 0:
            current = nodeIt
            nodeIt = nodeIt.next
        nodeIt.next = self._head
        self._head = nodeIt
        current.next = None         

    """def intersection(self,l2): 
        función que recibe una lista l2 y devuelve una nueva lista que
        contenga la intersección de ambas listas, la invocante y l2. Como precondición, se
        exige que ambas listas están ordenadas de forma ascendente.
        output=SList2()
        if self.isSorted() and l2.isSorted():
            current1=self._head
            current2=l2._head
            
            while current1:
                while current2 and current2.elem<current1.elem:
                    current2=current2.next
                if current2!=None and current2.elem==current1.elem:
                    output.addLast(current1.elem)
                current1=current1.next
        
        return output"""
    
    def segregateOddEven(self): 
        """función que modifica la lista invocante para que todos los
        elementos pares aparezcan antes que los elementos impares. La función debe
        respetar el orden de los elementos pares y el orden de los elementos impares."""
        if self._size>1:
            evens=SList2()
            odds=SList2()
            current=self._head
            while current:
                e=current.elem
                if e%2==0:
                    evens.addLast(e)
                else:
                    odds.addLast(e)
                    
                current=current.next
                
            if evens.isEmpty():
                self._head=odds._head
                self._tail=odds._tail
            elif odds.isEmpty():
                self._head=evens._head
                self._tail=evens._tail
            else:
                self._head=evens._head
                evens._tail.next=odds._head
                self._tail=odds._tail
        

        

l = SList2()
l2 = SList2()
for i in range(3):
    l.addLast(rd.randint(0,9))
for i in range(6):
    l.addLast(rd.randint(0,9))
print(l)
print(l.isSorted())
l.removeDuplicates()
print(l)
l.swapPairwise()
print(l)
l.moveLast()
print(l)
#print(l2)
#print(l.intersection(l2))
l.segregateOddEven()
print(l)



