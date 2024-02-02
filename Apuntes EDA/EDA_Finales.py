#Ejercicios de examenes finales 

#Problema 2 -> 4 de Junio de 2020

import sys
class Graph():
    def __init__(self,labels):
        """uses a dictionary to represent the graph"""
        self.vertices={}
        for v in labels:
            self.vertices[v]=[]
       
    def addEdge(self, start, end):
        """adds an edge from start to end"""
        if start not in self.vertices.keys():
            return
        if end not in self.vertices.keys():
            return
        self.vertices[start].append(end)

    def minDistance(self, distances, visited): 
        """This functions returns the vertex (index) with the mininum distance. We 
        only consider the set of vertices that have not been visited"""
        # Initilaize minimum distance for next node 
        min = sys.maxsize 

        #returns the vertex with minimum distance from the non-visited vertices
        for i in self.vertices: 
            if distances[i] <= min and visited[i] == False: 
                min = distances[i] 
                min_index = i 
    
        return min_index 
    
    def dijkstra(self, origin): 
        """"This function takes a vertex v and calculates its mininum path 
        to the rest of vertices by using the Dijkstra algoritm"""  
        
        #we use a Python list of boolean to save those nodes that have already been visited  
        # Mark all the vertices as not visited 
        visited={}
        for v in self.vertices.keys():
            visited[v]=False

        #this list will save the previous vertex 
        previous={}
        for v in self.vertices.keys():
            previous[v]=-1

        #This array will save the accumulate distance from v to each node
        distances={}
        for v in self.vertices.keys():
            distances[v]=sys.maxsize

        #The distance from v to itself is 0
        distances[origin] = 0
        
        for n in range(len(self.vertices)): 
            # Pick the vertex with the minimum distance vertex.
            # u is always equal to v in first iteration 
            u = self.minDistance(distances, visited) 
            # Put the minimum distance vertex in the shotest path tree
            visited[u] = True
            
            # Update distance value of the u's adjacent vertices only if the current  
            # distance is greater than new distance and the vertex in not in the shotest path tree 
            for i in self.vertices[u]:
                if visited[i]==False and distances[i]>distances[u]+1:
                    distances[i]=distances[u]+1   
                    previous[i]=u       
                
        #finally, we print the minimum path from v to the other vertices

        #self.printSolution(distances,previous,origin)
        return distances,previous
    


    #Ejercicio final 

    def minimumpath(self, start, end):
        """returns a list containing the minimum path from start to end"""
        distances,previous=self.dijkstra(start)
        minimum_path=[]
        if start==end:
            #print('start == end ')
            pass
        elif distances[end]==sys.maxsize:
            #print("There is not path from ",start,' to ',end)
            pass
        else: 
            prev=previous[end]
            while prev!=-1:
                minimum_path.insert(0,prev)
                prev=previous[prev]
                
            minimum_path.append(end)  

        return minimum_path


class Person():
    
    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number

        
    def __eq__(self,other):
        if other==None:
            return False
        
        return self.name==other.name and self.phone_number==other.phone_number
        
    def __str__(self):
        
        str_person = "Name: {}; Phone number: {}".format(self.name,self.phone_number)
        return str_person

    def __hash__(self):
        #print('The hash is:')
        return hash((self.name, self.phone_number))

class Contacts():
    
    def __init__(self):
        #vertices
        self.vertices={}
        
    def addPerson(self,person):
        self.vertices[person]=[]
    
    def __str__(self):
        result=''
        for p in self.vertices.keys():
            result+=str(p)+':\n'
            for friend in self.vertices[p]:
                result+='\t'+str(friend)
            result+='\n'
            
        return result
        
    def addConnection(self,person1,person2):
        #print('new connection:',point1,point2)
        if person1 not in self.vertices.keys():
            print(str(person1) + ' does not exist!!!')
            return
        if person2 not in self.vertices.keys():
            print(str(person2) + ' does not exist!!!')
            return
            
        self.vertices[person1].append(person2)
        self.vertices[person2].append(person1)
    
    def areConnected(self,person1,person2):
        if person1 not in self.vertices.keys():
            print(str(person1) + ' does not exist!!!')
            return
        if person2 not in self.vertices.keys():
            print(str(person2) + ' does not exist!!!')
            return
            

        return person2 in self.vertices[person1]
    
    def minDistance(self, distances, visited): 
        """This functions returns the vertex (index) with the mininum distance. We 
        only consider the set of vertices that have not been visited"""
        # Initilaize minimum distance for next node 
        min = sys.maxsize 

        #returns the vertex with minimum distance from the non-visited vertices
        for i in self.vertices: 
            if distances[i] <= min and visited[i] == False: 
                min = distances[i] 
                min_index = i 
    
        return min_index 

    def dijkstra(self, origin): 
        """"This function takes a vertex v and calculates its mininum path 
        to the rest of vertices by using the Dijkstra algoritm"""  
        
        #we use a Python list of boolean to save those nodes that have already been visited  
        # Mark all the vertices as not visited 
        visited={}
        for v in self.vertices.keys():
            visited[v]=False

        #this list will save the previous vertex 
        previous={}
        for v in self.vertices.keys():
            previous[v]=-1

        #This array will save the accumulate distance from v to each node
        distances={}
        for v in self.vertices.keys():
            distances[v]=sys.maxsize

        #The distance from v to itself is 0
        distances[origin] = 0
        
        for n in range(len(self.vertices)): 
            # Pick the vertex with the minimum distance vertex.
            # u is always equal to v in first iteration 
            u = self.minDistance(distances, visited) 
            # Put the minimum distance vertex in the shotest path tree
            visited[u] = True
            
            # Update distance value of the u's adjacent vertices only if the current  
            # distance is greater than new distance and the vertex in not in the shotest path tree 
            for i in self.vertices[u]:
                if visited[i]==False and distances[i]>distances[u]+1:
                    distances[i]=distances[u]+1   
                    previous[i]=u       
                
        #finally, we print the minimum path from v to the other vertices

        #self.printSolution(distances,previous,origin)
        return distances,previous
    
    def getSuggestions(self, person: Person , minimumJumps: int)->list:
        distances,previous=self.dijkstra(person)
        result=[]
        for v in distances.keys():
            if distances[v]<sys.maxsize and distances[v]>=minimumJumps:
                result.append(v)

        return result



    

