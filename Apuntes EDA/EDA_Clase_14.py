# Árboles Binarios de Búsqueda

from EDA_Clase_13 import Node
from EDA_Clase_13 import BinaryTree

class BSTNode(Node):
    def __init__(self, key, elem, left = None, right = None , parent = None):
        self.key = key
        super(BSTNode, self).__init__(elem, left, right, parent)

class BinarySearchTree(BinaryTree):
    def search(self, key): # Devuelve True si la "key" existe, Fale en otro caso
        return self._search(self._root , key)
    
    def _search(self , node, key):
        #Caso base
        if node == None: #Caso base en el que no existe la key
            return False
        if node.key == key: #Caso base en el que si existe la key
            return True    
        #Caso recursivo
        if key < node.key:
            return self._search(node.left , key)
        else: #key > node.key
            return self._search(node.right, key)
    
    def searchIte(self, key): #Solución iterativa (como en listas)
        node = self._root
        while node: #node != None
            if node.key == key: 
                return True
            if key < node.key:
                node = node.left
            else: #key > node.key
                node = node.right 
        
        return False
    
    def insert(self, key, elem): #Añade un nuevo nodo con key == key y elemento elem
        if self._root == None:
            self._root = BSTNode(key, elem)
        else:
            self._insert(self._root, key , elem)
    
    def _insert(self, node, key , elem):
        #Caso base
        if node.key == key:
            print("Error, no se permiten claves duplicadas")
        #Casos recursivos
        if key < node.key:
            if node.left == None:    #no tiene hijo izqdo
                newNode = BSTNode(key, elem)
                newNode.parent = node
                node.left = newNode
            else:
                self._insert(node.left , key , elem)
        if key > node.key:
            if node.right == None:   #no tiene hijo dcho     
                newNode = BSTNode(key,elem)    
                newNode.parent = node 
                node.right = newNode
            else:
                self._insert(node.right , key , elem)
    
    def find(self, key): #Devuleve el nodo cuya key es "key"
        return self._find(self._root , key)
    
    def _find(self , node, key):
        #Caso base
        if node == None: #Caso base en el que no existe la key
            return None
        if node.key == key: #Caso base en el que si existe la key
            return node   
        #Caso recursivo
        if key < node.key:
            return self._find(node.left , key)
        else: #key > node.key
            return self._find(node.right, key)
    
    def remove(self, key): #Busca y elimina el nodo cuya key es "key"
        node = self.find(key)
        if node == None:
            print(key, "no existe ese nodo")
            return None
        self._remove(node)

    def _remove(self, node):
        """Funcion recursiva para eliminar el nodo.
        Tres posibles casos:
        1) es un nodo hoja
        2) el nodo solo tiene un hijo (izqdo o dcho)
        3) el nodo tiene dos hijos (izqdo y dcho)"""
        #Primer caso
        if node.left == None and node.right == None:
            if node.parent:   #el nodo no es la raíz
                if node.key < node.parent.key:
                    node.parent.left = None
                else: #node.key > node.parent.key
                    node.parent.right = None
                node.parent = None
            else:              #El nodo hoja es la raíz, pues no tiene padre
                self._root == None
            return node
        #Segundo caso
        elif (node.left != None and node.right == None) or (node.left == None and node.right != None):
            if node.parent:
                if node.left:
                    if node is node.parent.left:
                        node.parent.left = node.left
                        node.left.parent = node.parent
                    if node is node.parent.right:
                        node.parent.right = node.left
                        node.left.parent = node.parent
                else:   #node.right != None:
                    if node is node.parent.left:
                        node.parent.left = node.right
                        node.right.parent = node.parent
                    if node is node.parent.right:
                        node.parent.right = node.right
                        node.righ.parent = node.parent
            else:      #Quiero borrar la raíz 
                if node.left: 
                    self._root = node.left
                else:
                    self._root = node.right
                node.parent = None
            return node
        
        else:
            # Case 3: node.left!=None and node.right!=None
            # we search the bigger node from its left child
            pred = node.left
            # we replace elem with the elem of the predecessor
            while pred.right:
                pred = pred.right
            node.key = pred.key
            node.elem = pred.elem
            self._remove(pred)

            """successor = node.right
               while succesor.left:
                    succesor= succesor.left         #Otra forma de hacer el remove, en el caso de que el nodo tenga dos hijos
                node.key = succesor.key
                node.elem = succesor.elem
                self._remove(succesor)"""

        return node

    #Ejercicio de examen final, 
    #implementa un método checkCousins(a,b), que toma dos
    #elementos a y b, y devuelve True si sus nodos son primos, y False en otro caso.
    def checkCousins(self, a , b):
        nodeX = self.find(a)
        nodeY = self.find(b)
        if nodeX is None or nodeY is None:
            return False
        
        depthX=self.depth(nodeX)
        depthY=self.depth(nodeY)

        if depthX!=depthY:
            return False
        
        if nodeX.parent == nodeY.parent:
            return False
        
        if nodeX.parent.parent != nodeY.parent.parent:
            return False
        

        return True

if __name__ == "__main__":
    print('hola')
    aux = BinarySearchTree()
    for x in [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]:
        aux.insert(x , x)
        # aux.draw()

    aux.draw()
    print("after remove 80 (a leaf)")
    aux.remove(80)
    aux.draw()
    print()

    tree = BinarySearchTree()
    for x in [18, 11, 23, 5, 15, 20, 24, 9, 15, 22, 21, 6, 8, 7]:
        tree.insert(x, x)
    tree.draw()
    print('size:', tree.size())
    print('height:', tree.height())

    tree.remove(18)
    print("after remove 18 (root), replaced with its successor 20")
    tree.draw()

    tree.remove(7)
    print("after remove 7 (a leaf)")
    tree.draw()

    tree.remove(8)
    print("after remove 8 (a leaf)")
    tree.draw()

    tree.remove(5)
    print("after remove 5 (only a child), replaced with its child: 9")
    tree.draw()

    tree.remove(9)
    print("after remove 9 (only a child), replaced with its left child: 6")
    tree.draw()

    tree.remove(11)
    print("after remove 11 (two children), replaced with its successor: 15")
    tree.draw()

    tree.remove(20)
    print("after remove 20 (root), two children, replaced with its successor: 21")
    tree.draw()

    tree.remove(15)
    print("after remove 15 (only left child) -> 6")
    tree.draw()

    tree.remove(6)
    print("after remove 6 (a leaf)")
    tree.draw()

    tree.remove(8)
    print("after remove 8 (does not exist)")
    tree.draw()

    tree.remove(24)
    print("after remove 24 (a leaf)")
    tree.draw()
    print()

    for x in [5, 10, 15, 20]:
        tree.insert(x, x)
    print("after insert 5,10,15,20")
    tree.draw()

    tree.remove(23)
    print("after remove 23, only a left child -> 22")
    tree.draw()

    # remove a root, with only the left child
    tree.remove(22)
    print("after remove 22 (a leaf)")
    tree.draw()
    # remove a root, with only the right child
    print("after remove 5 (only a right child) ->10")
    tree.remove(5)
    tree.draw()

    print("after remove 21 (root with only a left child) -> 10")
    tree.remove(21)
    tree.draw()
            

                









        
        







