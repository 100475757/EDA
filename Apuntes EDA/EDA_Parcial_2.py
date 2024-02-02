#Ejercicios segundo parcial EDA, Árboles

class Node: 
    def __init__(self,elem,left=None,right=None,parent=None):
        self.elem=elem
        self.left=left
        self.right=right
        self.parent=parent

class MyBST:

    def __init__(self):
        self.root = None

    def depth(self,node):
            if node==None or node.parent==None:
                return 0
            
            return 1 + self.depth(node.parent)

    def find(self,x):
        """Returns True if x exists into the True, eoc False"""
        return self._find(self.root,x)

    def _find(self,node,x):
        """Returns the node whose elem is x. 
        If this does not exist, it returns None"""
        if node==None:
            return None
        if node.elem==x:
            return node
        if node.elem:
            return self._find(node.right,x)    
        
    def insert(self,x):
        """inserts a new node, with element x, into the tree"""
        if self.root==None:
            self.root=Node(x)
        else:
            self._insertNode(self.root,x)


    def _insertNode(self,node,x):
        """método recursivo"""
        if node.elem==x:
            #print('Error: la clave ya existe. No permitimos duplicados')
            return 

        if x<node.elem:

            if node.left==None:
                #ya he encontrado su sitio
                newNode=Node(x)
                newNode.parent=node
                node.left=newNode
            else:
                self._insertNode(node.left,x)

        else: #x>node.elem

            if node.right==None:
                #ya he encontrado la posición
                newNode=Node(x)
                newNode.parent=node
                node.right=newNode
            else:
                 self._insertNode(node.right,x)
        

    def draw(self):
      """Function to draw the tree"""
      self._draw('',self.root,False)
      print()
      
    def _draw(self,prefix, node, isLeft):
        if node:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + ("|-- ") + str(node.elem))
            self._draw(prefix + "     ", node.left, True)
    
    #1º Ejercicio:
    def getNonLeaves(self):
        """Devuelve una lista de Python con
        los elementos de los nodos que no son hojas. La lista debe estar ordenada de forma
        descendente (de mayor a menor)."""
        lista = []
        self._getNonLeaves(self.root , lista)
        return lista
    
    def _getNonLeaves(self , node , lst):
        #Función recursiva
        if node:
            self._getNonLeaves(node.right,lst)
            if node.left or node.right:
                lst.append(node.elem)
            self._getNonLeaves(node.left,lst)
    
    #2º Ejercicio:
    def checkCousins(self,x,y):
        """returns True if x and y are cousins, and False eoc"""
        nodeX=self.find(x)
        nodeY=self.find(y)
        if nodeX==None or nodeY==None:
            return False

        depthX=self.depth(nodeX)
        depthY=self.depth(nodeY)

        if depthX!=depthY:
            return False

        if nodeX.parent==nodeY.parent:
            return False

        if nodeX.parent.parent!=nodeY.parent.parent:
            return False

        return True

    #3º Ejercicio
    def lwc(self,a,b):
        """returns the lowest common ancestor of a and b"""
        nodeA=self.find(a)
        if nodeA==None:
            return None
        
        nodeB=self.find(b)
        if nodeB==None:
            return None

        return self._lwc(self.root,nodeA,nodeB)

    def _lwc(self,node,nodeA,nodeB):
        if node==None:
            return None

        if nodeA.elem<node.elem and nodeB.elem<node.elem:
            return self._lwc(node.left,nodeA,nodeB)
        
        if nodeA.elem>node.elem and nodeB.elem>node.elem:
            return self._lwc(node.right,nodeA,nodeB)

        return node.elem





        

"---------------------------------------------------------------------------------------------------------------------"
values=[25,20,36,10,22,30,40,5,12,28,38,48]
tree=MyBST()
for x in values:
    tree.insert(x)
tree.draw()
print('getNonLeaves()',tree.getNonLeaves())

values=[25,20,36,10,22,30,40,5,12,28,38,48]
tree=MyBST()
for x in values:
    tree.insert(x)

tree.draw()

print('5 and 15 are cousins?:',tree.checkCousins(5,15)) #False, 15 does not exist
print('5 and 22 are cousins?:',tree.checkCousins(5,22)) #False, have diferent levels
print('5 and 22 are cousins?:',tree.checkCousins(5,22)) #False, have diferent levels
print('36 and 48 are cousins?:',tree.checkCousins(36,48)) #False, have diferent levels
print('5 and 12 are cousins?:',tree.checkCousins(5,12)) #False, are siblings
print('20 and 36 are cousins?:',tree.checkCousins(20,36)) #False, are siblings
print('10 and 22 are cousins?:',tree.checkCousins(10,22)) #False, are siblings
print('5 and 28 are cousins?:',tree.checkCousins(5,28)) #False, same level, their parents are not siblings
print('12 and 28 are cousins?:',tree.checkCousins(12,28)) #False, same level, their parents are not siblings
print('10 and 30 are cousins?:',tree.checkCousins(10,30)) #True, are cousins
print('10 and 40 are cousins?:',tree.checkCousins(10,30)) #True, are cousins
print('22 and 30 are cousins?:',tree.checkCousins(22,30)) #True, are cousins
print('22 and 40 are cousins?:',tree.checkCousins(22,40)) #True, are cousins
print('28 and 38 are cousins?:',tree.checkCousins(28,38)) #True, are cousins
print('28 and 48 are cousins?:',tree.checkCousins(28,48)) #True, are cousins






