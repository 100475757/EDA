from EDA_Clase_14 import BSTNode
from EDA_Clase_14 import BinarySearchTree

class BST2(BinarySearchTree):
    def minimum(self):  
        """Implementa una función (iterativa o recursiva) que devuelva el elemento más 
          pequeño del árbol. ¿Cuál es su complejidad temporal? """
        #Solución iterativa , complejidad O(log(n))
        if self._root == None:
            print("Error, el árbol está vacío")
        
        node = self._root
        while node.left: 
            node = node.left
        return node.elem
    
    #Solución recursiva, misma complejidad
    def minimum_rec(self):
        return self._minimum_rec(self._root)
    
    def _minimum_rec(self, node):
        if node == None:
            return None
        elif node.left == None:  #nodo más pequeño
            return node.elem
        else:
            return self._minimum_rec(node.left)
        
    def maximum(self): 
        """Implementa una función (iterativa o recursiva) que devuelva el elemento
            mayor del árbol. ¿Cuál es su complejidad temporal?"""
        #Solución iterativa, complejidad O(log(n))
        if self._root == None:
            print("Error, el árbol está vacío")

        node = self._root
        while node.right:
            node = node.right
        return node.elem

    def maximum_rec(self):
        #Solución recursiva , misma complejidad
        return self._maximum_rec(self._root)
    
    def _maximum_rec(self, node):
        if node == None:
            return None
        elif node.right == None:    #nodo más grande
            return node.elem
        else:
            return self._maximum_rec(node.right)
    
    def sum(self): 
        """Implementa una función recursiva que sume todos los elementos del árbol
            y devuelva su resultado. ¿Cuál es su complejidad temporal?"""
        #Complejidad O(n) , ya que hay que recorrer todos los nodos para sumarlos
        return self._sum(self._root)
    def _sum(self, node):
        #Caso base
        if node == None:
            return 0
        #Casos recursivos 
        elif node.left and node.right == None:          #Los dos elifs son opcionales, no son necesarios, con el else se cumple igual
            return node.elem + self._sum(node.left)
        elif node.right and node.left == None:
            return node.elem + self._sum(node.right)
        else:
            return node.elem + self._sum(node.right) + self._sum(node.left)
    
    def prints10(self):
        """Implementa una función recursiva que imprima los elementos de los nodos
            cuyos abuelos tienen un elemento múltiplo de 10. ¿Cuál es su complejidad
            temporal?"""
        #Complejidad O(n)
        return self._prints10(self._root)
    
    def _prints10(self , node: "BSTNode" , parent: "BSTNode" , grand: "BSTNode"):
        if node:  #node != None
            self._prints10(node.left , node , parent)
            if grand and grand.elem % 10 == 0:
                print("node.elem = " , node.elem)
            self._prints10(node.right , node , parent)

    def _maximum_node(self , node):
        """Implementa una función iterativa que reciba un nodo, node. La función debe
            encontrar y devolver el nodo cuyo elemento sea el mayor en el subárbol
            node. """
        if node:
            while node.right:
                node = node.right
            return node
    
    def _remove(self, node , elem):
        """La función _remove(node), cuando el nodo a eliminar tiene dos subárboles
        izquierdo y derecho, busca el sucesor del nodo y reemplaza el elemento del
        nodo a eliminar por el elemento del sucesor. Implementa una nueva versión
        de _remove(node), donde en lugar de buscar y reemplazar por el sucesor,
        se busque y se reemplace por el predecesor (es decir, el nodo mayor del
        subárbol izquierdo)"""
        if node is None:
                return None
        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # elem == node.elem
            if node.left is None and node.right is None:
                # node is a leave
                node = None
            elif node.left is None:  # only has the right child
                return node.right
            elif node.right is None:  # only has the left child
                return node.left
            else:  # elem == node.elem
                predecessor = self._maximum_node(node.left)
                print('predecessor: ', predecessor.elem)
                node.elem = predecessor.elem
                node.left = self._remove(node.left, predecessor.elem)

        return node
    
    def fe_size(self , elem):
        """El factor de equilibrio basado en el tamaño de un nodo se define como el
        valor absoluto de la diferencia del tamaño de su subárbol izquierdo y el
        tamaño de su subárbol derecho.Implementa una función que reciba un nodo
        y calcule su factor de equilibrio basado en tamaño."""
        #Dado un elemento "elem" devuelve el factor balanceado de ese nodo
        node = self.search(elem)
        return self._fe_size(node)

    def _fe_size(self , node):
        if node:
             left =self._size(node.left)
             right = self._size(node.right)
             if left - right < 0:
                 return (left - right) * -1
             else:
                 return left-right
        else:
            return 0
        
    def fe_height(self):
        """ Implementa una función que reciba un nodo y calcule su factor de equilibrio
            basado en altura. El factor de equilibrio basado en la altura de un nodo se
            define como el valor absoluto de la diferencia de la altura de su subárbol
            derecho y la altura de su subárbol izquierdo"""

        self._fe_height(self._root)
    
    def _fe_height(self , node):
        if node:
            left = self._size(node.left)
            right = self._size(node.right)
            if right -left < 0:
                return (right - left) * -1
            else:
                return right - left
        else:
            return 0
    
    def is_balanced_size(self):
        """Implementa una función que compruebe si el árbol está balanceado en
        tamaño o no. Un ABB está equilibrado en tamaño si todos sus nodos tienen
        un factor de equilibrio basado en tamaño menor o igual que 1."""

        return self._is_balanced_size(self._root)
    
    def _is_balanced_size(self , node):
        if node:
            return self._fe_size(node) <=1 and \
            self. _is_balanced_size(node.left) and \
            self. _is_balanced_size(node.right)
        else:
            return True
        
    def is_balanced_height(self):
        """Implementa una función que compruebe si el árbol está balanceado en
            altura (AVL) o no. Un ABB es AVL, es decir, está equilibrado en altura,
            cuando todos sus nodos tienen un factor de equilibrio basado en altura
            menor o igual que 1."""
        return self._is_balanced_height(self._root)
    
    def _is_balanced_height(self , node):
        if node:
            return self._fe_height(node) <= 1 and \
            self._is_balanced_height(node.left) and \
            self._is_balanced_height(node.right)
        
        else:
            return True
    
    def get_count(self, low , high):
        return self._get_count(self._root , low , high)
    
    def _get_count(self, node  , low , high):
        if low > high:
            low , high = high , low
        
        if node:
            if node.elem >= low and node.elem <= high:
                return 1 + self._get_count(node.left , low , high) + self._get_count(node.right , low , high)
        
            else:
                return  self._get_count(node.left , low , high) + self._get_count(node.right , low , high)
        
        return 0
    
    def sumnodeleave(self):
        return self._sumnodeleave(self._root)
    
    def _sumnodeleave(self , node):
        if node:
            if node.left is None and node.right is None:
                return node.elem
            else:
                return self._sumnodeleave(node.left) + self._sumnodeleave(node.right)
        else:
            return 0
        
        
    
tree3 = BST2()
for i in range(1, 11):
    tree3.insert(i , i)

print(tree3.sumnodeleave())
print(tree3.get_count(2, 5))