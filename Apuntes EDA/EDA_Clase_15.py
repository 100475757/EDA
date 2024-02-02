#Grafos, recorridos, y otras implementaciones

from EDA_Clase_7 import DList

#Implemntación con matriz de adyacencia 
class Graph1:
    def __init__(self, vertices: list):  #Implementacion grafo no dirigido con aristas sin peso
        self._vertices = vertices
        self._N = len(vertices)
        #row = [0]*self._N    Creamos una fila con "n" ceros
        self._matrix = [[0]*self._N for i in range(self._N)]  #Creamos una matriz de "n" filas, de ceros 
    
    def _index(self, v):
        "Devuelve el índice del vértice v. Si v no existe, printea un error y devuelve -1"
        if v  and v in self._vertices:
            index = self._vertices.index(v)
        else:
            print(f"Error, el vértice {v} no existe")
            index = -1
        
        return index
    
    def addEdge(self,start,end):
        """gets two vertices and adds an edge from start to end."""
        #first, we get their indeces
        i,j=self._index(start),self._index(end)
        if i==-1 or j == -1:
            print('[addEdge]: {} does not exist!!!'.format(start))
            return
        #now, we modify its element in the matrix 
        self._matrix[i][j]= 1
        self._matrix[j][i] = 1
        print('[addEdge]: ({},{}) was added!!!'.format(start,end))
    
    def containEdge(self,start,end):
        """checks if the edge from start to end exists."""
        i,j=self._index(start),self._index(end)
        if i==-1 or j == -1:
            print('[addEdge]: {} does not exist!!!'.format(start))
            return False
        if self._matrix[i][j] == 1:
            return True
        
        #o tb return self._matrix[i][j]==1

    def removeEdge(self,start,end):
        """removes the edge from start to end. It must
        modify its corresponding element in the matrix to 0."""
        i,j=self._index(start),self._index(end)
        if i==-1 or j == -1:
            print('[addEdge]: {} does not exist!!!'.format(start))
            return False
        
        self._matrix[i][j] == 0
        self._matrix[j][i] == 0

    
    def __str__(self):
        """returns the matrix"""
        result=' '
        #the first row are the vertices
        for l in self._vertices:
            result+='  ' + l
        
        result+='\n'
    
        for i,row in enumerate(self._matrix):
            result+=self._vertices[i]+' ' +str(row)+'\n'
        
        return result
    

vertices=['A','B','C','D','E','F']
g=Graph1(vertices)
#Now, we add the edges
g.addEdge('A','B') #A->B
g.addEdge('B','C') #B->C
g.addEdge('C','E') #C->E
g.addEdge('D','B') #D->B
g.addEdge('E','D') #E->D
g.addEdge('E','F') #E->F
print('containEdge(A,E)=',g.containEdge('A','E'))
print('containEdge(D,B)=',g.containEdge('D','B'))
print(g)
g.removeEdge('E','D')
print(g)



#Implementación grafo dirigido y ponderado

class DyGraph:
    def __init__(self, vertices , dirigido = False):
        self._vertices = vertices
        self._dirigido = dirigido
        self._N = len(vertices)
        #row = [0]*self._N    Creamos una fila con "n" ceros
        self._matrix = [[0]*self._N for i in range(self._N)]  #Creamos una matriz de "n" filas, de ceros 
    
    def _index(self, v):
        "Devuelve el índice del vértice v. Si v no existe, printea un error y devuelve -1"
        if v  and v in self._vertices:
            index = self._vertices.index(v)
        else:
            print(f"Error, el vértice {v} no existe")
            index = -1
        
        return index
    
    def addEdge(self,start,end , w = 1):
        """gets two vertices and adds an edge from start to end."""
        #first, we get their indeces
        i,j=self._index(start),self._index(end)
        if i==-1 or j == -1:
            print('[addEdge]: {} does not exist!!!'.format(start))
            return
        #now, we modify its element in the matrix 
        self._matrix[i][j]= w
        if not self._dirigido: 
            self._matrix[j][i] = w
        print('[addEdge]: ({},{}) was added!!!'.format(start,end))
    
    def containEdge(self,start,end):
        """checks if the edge from start to end exists."""
        i,j=self._index(start),self._index(end)
        if i==-1 or j == -1 or i == 0 or j == 0:
            print('[addEdge]: {} does not exist!!!'.format(start))
            return False
        if self._matrix[i][j] != None:
            return True
        
        #o tb return self._matrix[i][j] != 0
    

    def removeEdge(self,start,end):
        """removes the edge from start to end. It must
        modify its corresponding element in the matrix to 0."""
        i,j=self._index(start),self._index(end)
        if i==-1 or j == -1:
            print('[addEdge]: {} does not exist!!!'.format(start))
            return False
        
        self._matrix[i][j] == 0
        if not self._dirigido:
            self._matrix[j][i] == 0
    

    def __str__(self):
        """returns the matrix"""
        result=' '
        #the first row are the vertices
        for l in self._vertices:
            result+='  ' + l
        
        result+='\n'
    
        for i,row in enumerate(self._matrix):
            result+=self._vertices[i]+' ' +str(row)+'\n'
        
        return result
    

#Implementación basada en listas de adyacencia
class AdjacentVertex:
    """This class allows us to represent a tuple with an adjacent vertex
    and the weight associated (by default 1, for non-unweighted graphs)"""
    def __init__(self,vertex,weight=None):
        self._vertex=vertex
        self._weight=weight
    
    def __str__(self):
        if self._weight!=None:
            return '('+str(self._vertex)+','+str(self._weight)+')'
        else:
            return str(self._vertex)

class Graph2():
    """This implementation is based on adjacency lists."""
    def __init__(self,vertices: list,directed=True):
        """This constructor gets an array saving the vertices. The class has the
        following attributes:
        _vertices: is a Python list to save the vertices
        _adjacents: a Python list of doubly linked list. 
        Given a vertex v, it has an index in _vertices, for example, i. 
        Then, its list of adjacent vertex is saved into _adjacents[i], which is a 
        doubly linked list saving objects of the AdjacentVertex class.  
        """
        self._vertices =vertices
        self._adjacents=[]
        self._N = len(vertices)
        for v in self._vertices:
            self._adjacents.append(DList())

        self._directed=directed
        
    def addVertex(self,v):
        self._vertices.append(v)
        self._adjacents.append(DList())
        self._N +=1


    def _index(self,v):
        if v and v in self._vertices:
            index=self._vertices.index(v)
        else:
            index=-1
        return index

     
    def addEdge(self, start, end, weight=None):
        """This function adds the edge (start,end). First, it must check if the 
        vertices exist."""
        i,j=self._index(start),self._index(end)
        if i==-1:
            print('[addEdge]: {} does not exist!!!'.format(start))
            return
        if j==-1:
            print('[addEdge]: {} does not exist!!!'.format(end))
            return

        self._adjacents[i].addLast(AdjacentVertex(end,weight))
        if self._directed==False:
            self._adjacents[j].addLast(AdjacentVertex(start,weight))

        
                
    def containsEdge(self, start, end):
        """This function adds the edge (start,end). First, it must check if the 
        vertices exist."""
        i,j=self._index(start),self._index(end)
        if i==-1:
            print('[containsEdge]: {} does not exist!!!'.format(start))
            return 0
        if j==-1:
            print('[containsEdge]: {} does not exist!!!'.format(end))
            return 0
        for k in range(len(self._adjacents[i])):
            adj=self._adjacents[i].getAt(k)   
            if adj._vertex==end:
                if adj._weight==None:
                    return 1
                else:
                    return adj._weight

        return 0


    def removeEdge(self, start, end):
        """This function adds the edge (start,end). First, it must check if the 
        vertices exist."""
        i,j=self._index(start),self._index(end)
        if i==-1:
            print('[removeEdge]: {} does not exist!!!'.format(start))
            return 
        if j==-1:
            print('[removeEdge]: {} does not exist!!!'.format(end))
            return 

        for k in range(len(self._adjacents[i])):
            adj=self._adjacents[i].getAt(k)   
            if adj._vertex==end:
                self._adjacents[i].removeAt(k)
                break

        if not self._directed:
            for k in range(len(self._adjacents[j])):
                adj=self._adjacents[j].getAt(k)   
                if adj._vertex==start:
                    self._adjacents[j].removeAt(k)
                    break

        
    def __str__(self):
        result=''
        for i,v in enumerate(self._vertices):
            result+='\n'+str(v)+': '+str(self._adjacents[i])
        return result


#we use this dictionary to represent the vertices with numbers:
labels=[0,1,2,3,4]
g=Graph2(labels,False)
print(g)

#Now, we add the edges
g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
print(g)

print()
print('g.containsEdge({},{})={}'.format(0,1,g.containsEdge(0,1)))
print('g.containsEdge({},{})={}'.format(1,0,g.containsEdge(1,0)))
print('g.containsEdge({},{})={}'.format(3,1,g.containsEdge(3,1)))
print('g.containsEdge({},{})={}'.format(0,2,g.containsEdge(0,2)))
print(g)
g.removeEdge(2,3)
print(g)

    
#we use this dictionary to represent the vertices with numbers:
labels=[0,1,2,3,4]
g=Graph2(labels,False)

#Now, we add the edges
g.addEdge(0,1,3)
g.addEdge(0,3,7)
g.addEdge(0,4,8)
g.addEdge(1,2,1)
g.addEdge(1,3,4)
g.addEdge(2,3,2)
g.addEdge(3,4,3)
print(g)
print()
print('g.containsEdge({},{})={}'.format(0,1,g.containsEdge(0,1)))
print('g.containsEdge({},{})={}'.format(1,0,g.containsEdge(1,0)))
print('g.containsEdge({},{})={}'.format(3,1,g.containsEdge(3,1)))
print('g.containsEdge({},{})={}'.format(0,2,g.containsEdge(0,2)))
print(g)
print()
print('after removing (2,3):')
g.removeEdge(2,3)
print(g)

labels=['A','B','C','D','E']
g=Graph2(labels)
#Now, we add the edges
g.addEdge('A','C',12) 
g.addEdge('A','D',60)
g.addEdge('B','A',10) 
g.addEdge('C','B',20)
g.addEdge('C','D',32) 
g.addEdge('E','A',7) 
print(g)
print()
print("g.containsEdge('C','B')", g.containsEdge('C','B'))
print(g.containsEdge('B','C'))


g.removeEdge('C','B')
print('after removing (C,E)')
print(g)
    

#Implementación basada en diccionarios 

class AdjacentVertex:
    """This class allows us to represent a tuple with an adjacent vertex
    and the weight associated (by default 1, for non-unweighted graphs)"""
    def __init__(self,vertex,weight=None):
        self._vertex=vertex
        self._weight=weight
    
    def __str__(self):
        if self._weight!=None:
            return '('+str(self._vertex)+','+str(self._weight)+')'
        else:
            return str(self._vertex)



class Graph3():
    def __init__(self, vertices , directed=True):
        """We use a dictionary to represent the graph
        the dictionary's keys are the vertices
        The value associated for a given key will be the list of their neighbours.
        Initially, the list of neighbours is empty"""
        self._vertices={}
        for v in vertices:
            self._vertices[v]=[]
        self._directed=directed
    
    def addEdge(self, start, end, weight=None):
        if start not in self._vertices.keys():
            print(start,' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end,' does not exist!')
            return
        
        #adds to the end of the list of neigbours for start
        self._vertices[start].append(AdjacentVertex(end,weight))

        if self._directed==False:
            #adds to the end of the list of neigbours for end
            self._vertices[end].append(AdjacentVertex(start,weight))

    def containsEdge(self, start, end):
        if start not in self._vertices.keys():
            print(start,' does not exist!')
            return 0
        if end not in self._vertices.keys():
            print(end,' does not exist!')
            return 0

        #we search the AdjacentVertex whose v is end
        for adj in self._vertices[start]:
            if adj._vertex==end:
                if adj._weight!=None:
                    return adj._weight
                else:
                    return 1 #unweighted graphs
        return 0  #does not exist

    def removeEdge(self,start,end):
        if start not in self._vertices.keys():
            print(start,' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end,' does not exist!')
            return

        #we must look for the adjacent AdjacentVertex (neighbour)  whose vertex is end, and then remove it
        for adj in self._vertices[start]:
            if adj._vertex==end:
                self._vertices[start].remove(adj)
        if self._directed==False:
            #we must also look for the AdjacentVertex (neighbour)  whose vertex is end, and then remove it
            for adj in self._vertices[end]:
                if adj._vertex==start:
                    self._vertices[end].remove(adj)
  
    def __str__(self):
        result=''
        for v in self._vertices:
            result+='\n'+str(v)+':'
            for adj in self._vertices[v]:
                result+=str(adj)+"  "
        return result

    

    








