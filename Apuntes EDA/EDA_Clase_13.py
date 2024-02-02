#Aqui empezamos con grafos y arboles 

import queue


class Node:
    def __init__(self, e: object, node_left: 'Node' = None, node_right: 'Node' = None , node_parent: "Node" = None) -> None:
            self.elem = e    #guarda el elemento
            self.left = node_left  #referencia a su hijo izqdo
            self.right = node_right  #referencia a su hijo dcho
            self.parent = node_parent ##referencia a su padre

    def __eq__(self, other: 'Node') -> bool:
        """checks if two nodes (subtrees) are equal o not"""
        return other is not None and self.elem == other.elem and self.left == other.left and self.right == other.right

    def __str__(self):
        return str(self.elem)

class BinaryTree: 
    def __init__(self): #Crea un árbol binario vacío 
        self._root = None
    
    def size(self): #Devuelve el nº de nodes
        return self._size(self._root)
    
    def _size(self, node): #Devuelve el tamaño del subárbol del nodo "node"
        #Caso base
        if node == None:
             return 0
         #Caso recursivo
        return self._size(node.left) + self._size(node.right) + 1
    
    def depth(self, node): #Devuelve la profuncidad del nodo "node", es decir la distancia desde la raiz hasta dicho nodo.
        #Caso base
        if node.parent == None: #El nodo "node" es la raiz
            return 0
        #Caso recursivo 
        return self.depth(node.parent) + 1   #Profundiada de un nodo = Profundidad de su nodo padre + 1 
    
    def height(self): #Devuelve la longitud del arbol
        return self._height(self._root)
    
    def _height(self, node): #Devuelve la longitud del nodo "node"
        #Caso base
        if node == None: #Si no hay nodo la longitud del nodo == -1
            return -1
        #Caso recursivo
        return max(self._height(node.left), self._height(node.right)) + 1
    
    def preorder(self): #Devuelve el recorrido preorder (root, left , right) del árbol
        return self._preorder(self._root)
    
    def _preorder(self, node): #Devuelve el recorrido preorder (root, left , right) de un nodo
        #Caso base
        if node == None:
            pass
        #Caso recursivo 
        else: #node != None
            print(node.elem)
            self._preorder(node.left)
            self._preorder(node.right)
    
    def postorder(self):  #Devuelve el recorrido preorder (left, right , root) del árbol
        return self._postorder(self._root)

    def _postorder(self, node): #Devuelve el recorrido preorder (left, right , root) de un nodo
        #Caso base
        if node == None: 
            pass
        #Caso recursivo 
        else:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.elem)

    def inorder(self):  #Devuelve el recorrido preorder (left, root, right) del árbol
        return self._inorder(self._root)

    def _inorder(self, node): #Devuelve el recorrido preorder (left, root, right) de un nodo
        #Caso base
        if node == None: 
            pass
        #Caso recursivo 
        else:
            self._inorder(node.left)
            print(node.elem)
            self._inorder(node.right)
    
    def levelorder(self): #Devuelve el reocrrido por niveles del árbol
        #Caso base
        if self._root == None:
            print("El árbol está vacío")
        else:
            q = queue()
            q.put(self._root)
            while q.isEmpty() == False:
                node = q.get()
                print(node.elem)
                if node.left: #node.left != None
                    q.put(node.left)
                if node.right: #node.right != None
                    q.put(node.right)
    
    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n\n')

    def _draw(self, prefix: str, node: Node, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)


if __name__ == '__main__':
    tree = BinaryTree()

    newNode = Node(2)
    left = Node(3, newNode, None)

    right = Node(9)

    right.left = Node(8)
    right.right = Node(20)
    rrNode = right.right
    rrNode.right = Node(30)

    root = Node(5, left, right)

    tree._root = root
    tree.draw()

    print('Size of the tree:', tree.size())
    print('Height of the tree:', tree.height())
    print('root of the tree:',  tree._height(root))

    tree.preorder()
    tree.postorder()
    tree.inorder()
    print('depth of root:', tree.depth(root))
    print('depth of root.left:', tree.depth(left))
    print('depth of root.right:', tree.depth(right))

    print('depth of root.right.left:', tree.depth(right.left))
    print('depth of root.right.right.right:', tree.depth(rrNode.right), rrNode.right.elem)




    
        


