#Implementación recorrido en amplitud (bfs) y en profundidad (dfs)

from EDA_Clase_15 import Graph3

class Graph2(Graph3):

    def bfs(self):
        """Visitamos todos los vértices por niveles"""
        print('bfs traversal:')
        # Mark all the vertices as not visited 
        visited={}
        for v in self._vertices.keys():
            visited[v]=False

        for v in self._vertices.keys():
            if visited[v]==False:
                self._bfs(v,visited)

    # Function to print a BFS of graph 
    def _bfs(self, v,visited): 
        """This functions obtains the BFS traversal from the vertex 
        whose index is indexV."""
        
        # Create a queue for BFS. It will save the indices of vertices to visit
        queue = [] 
        #mark the source vertex as visited 
        visited[v] = True
        # and enqueue it 
        queue.append(v)
        
        while queue: 
            # Dequeue an index from queue and print its corresponding vertex(label)
            s = queue.pop(0) 
            #print (s, end = " ") 
            #we print the vertex, so we need to get its label
            print (s, end = " ")  
            # Get all adjacent vertices of the dequeued index. 
            # If an adjacent vertex has not been visited, 
            # then mark it visited and enqueue it 
            for adj in self._vertices[s]: 
                if visited[adj._vertex] == False: 
                    queue.append(adj._vertex) 
                    visited[adj._vertex] = True

  # The function to do DFS traversal. It uses 
  # recursive _dfs() 
    def dfs(self): 
        """This function prints all vertices of the graph by the DFS traversal."""
        
        print('dfs traversal:')
        # Mark all the vertices as not visited 
        visited={}  #valor booleano 
        for v in self._vertices.keys():
            visited[v]=False

        for v in  self._vertices.keys():
            if visited[v]==False:
                self._dfs(v, visited)
        print() 

    def _dfs(self, v, visited): 
        """This funcion prints the DFS traversal from the vertex whose index is indexV"""
        # Mark the current node as visited and print it 
        visited[v] = True
        #print(v, end = ' ') 
        #Instead of printing the index, we have to print its label
        print(v,end=' ')
        # Recur for all the vertices  adjacent to this vertex 
        for adj in self._vertices[v]: 
            if visited[adj._vertex] == False: 
                self._dfs(adj._vertex, visited)


#we use this dictionary to represent the vertices with numbers:
if __name__ == '__main__':

    labels=['A','B','C','D','E']

    g=Graph2(labels)

    #Now, we add the edges
    g.addEdge('A','C',12) #A->(12)C
    g.addEdge('A','D',60) #A->(60)D
    g.addEdge('B','A',10) #B->(10)A
    g.addEdge('C','B',20) #C->(20)B
    g.addEdge('C','D',32) #C->(32)D
    g.addEdge('E','A',7)  #E->(7)A

    print(g)
    print()

    g.bfs()
    print()

    label='C'
    # Mark all the vertices as not visited 
    visited={}
    for v in labels:
        visited[v]=False

    print('bfs traversal from ', label)
    #we have to pass the index of the vertex 
    g._bfs(label,visited)
    print()

    label='E'
    visited={}
    for v in labels:
        visited[v]=False
    print('bfs traversal from ', label)
    #we have to pass the index of the vertex 
    g._bfs(label,visited)


    labels=['A','B','C','D','E']
    g=Graph2(labels,False)
    g.addEdge('A','B') # A:0, B:1
    g.addEdge('A','C') # A:0, C:2
    g.addEdge('A','E') # A:0, E:5
    g.addEdge('B','D') # B:1, D:4
    g.addEdge('B','E') # C:2, B:1
    #g.addEdge('A','H',8)

    print(g)

    print('bfs traversal from A (A is the first vertex):')
    g.bfs()
    print()
    label='E'
    visited={}
    for v in labels:
        visited[v]=False
    print('bfs traversal from ', label)
    #we have to pass the index of the vertex 
    g._bfs(label,visited)

    """## Depth First Search


    """
    #we use this dictionary to represent the vertices with numbers:
    labels=['A','B','C','D','E']

    g=Graph2(labels)

    #Now, we add the edges
    g.addEdge('A','C',12) #A->(12)C
    g.addEdge('A','D',60) #A->(60)D
    g.addEdge('B','A',10) #B->(10)A
    g.addEdge('C','B',20) #C->(20)B
    g.addEdge('C','D',32) #C->(32)D
    g.addEdge('E','A',7)  #E->(7)A

    print(g)
    print()

    g.dfs()
    print()

    visited={}
    for v in labels:
        visited[v]=False
    print('dfs traversal from B')
    g._dfs('B',visited)