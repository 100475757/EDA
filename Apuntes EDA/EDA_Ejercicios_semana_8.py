# Ejercicios de grafos 

# Final ordinaria 23 de junio de 2021

class MyGraph:
    def __init__(self, n):
        #Crea una grafo con n vértices (0,1,2....., n-1)
        self.vertices = {}
        for i in range(n):
            self.vertices[i] = []
    
    def addConection(self,i , j):
        if i not in self.vertices.keys():
            return 
        if j not in self.vertices.keys():
            return 
        
        self.vertices[i].append(j)
    
    def isStronglyConn(self):
        for i in self.vertices.keys():
            if len(self.depthnode(i)) != len(self.vertices):
                return False
        return True
    
    def depthnode(self, vertex):
        L = []
        return self._depthnode(vertex, L)
    
    def _depthnode(self, vertex, visited, L):
        visited.append(vertex)
        for i in self.vertices[vertex]:
            if i not in visited:
                self._depthnode(i , visited)
        
        return visited
    

G = MyGraph(6)
print(G.vertices)
G.addConection(1,2)
G.addConection(2,3)
G.addConection(3,1)
G.addConection(3,4)



        
    

