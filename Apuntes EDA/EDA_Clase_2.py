import random as rd

class vector:
    def __init__(self, dim: int):#método constructor que crea un vector con todas las coordenadas igual a 0 y de dimensión m.
        self.values = [0]*dim   #Creamos una lista con n 0´s, con n = NUMERO DE COORDENADAS 
        self.dim = dim

    def __len__(self):      
        return self.dim 
    
    def __str__(self): #devuelve un string representando el vector
        string = "("
        for value in self.values:
            string += str(value) + ","
        string = string[:-1]      #Elimino ls última coma, voy desde el inicio de la lista hasta el ultimo -1
        string +=")"
        return string           
    def __setitem__(self, i , newValue): #modifica la i ésima coordenada del vector al nuevo valor newValue.
        self.values[i] = newValue
        
    
    def __getitem__(self,i): #devuelve la i ésima coordenada del vector. Recuerda que la primera coordenada siempre debe estar representada por el índice 0.
        return self.values[i]

    def __add__(self,other): #devuelve un nuevo vector que es la suma del vector invocante (self) y del parámetro other.
       if self.dim != other.dim:
        print("¡Dimensiones distintas!")
       else:        #Necesario poner el else, pues sino la condicion de antes no tendría efecto
        result = vector(self.dim)
        for i in range(self.dim):
           result.__setitem__(i,self.values[i] + other.values[i]) #Tb lo puedo hacer con listas ->  result.values[i] = self.values[i] + other.values[i]
        return result 

    def dot(self,other): #devuelve el producto escalar de dos vectores.
        if self.dim != other.dim:
            print("¡Dimensiones distintas!")
        else:
         prodesc = 0      #Inicializamos a 0 
         for i in range(self.dim):
            prodesc += (self.values[i] * other.values[i])
         return prodesc

    def  __eq__(self,other): #devuelve True is los dos vectores son iguales, y False en otro caso.
         if self.dim != other.dim:
            return False
        
         else:
            for i in range(self.dim):
                if self.values[i] == other.values[i]:
                    return True
                else:
                    return False

    def norm(self): #Devuelve el módulo/norma de un vector. Nota: norma = (a**2 + b**2 + c**2 +...)**0.5
        norma = 0
        for i in range(self.dim):
            norma+=self.values[i]**2
        norma = norma**0.5
        return norma

    def cosine_distance(self,other): #devuelve la distancia del coseno entre los dos vectores.
         if self.dim != other.dim:
            print("¡Dimensiones distintas!")
         else:
            result = self.dot(other)/ (self.norm()* other.norm()) 
         
         return result


vec, v2 = vector(4),vector(4)
print(vec)
print(v2)
for i in range(len(vec)):
    vec.__setitem__(i, rd.randint(-9,10))
    v2.__setitem__(i, rd.randint(-9,10))
print(vec)
print(v2)
print(vec.__getitem__(3))
print(vec.__add__(v2))
print(vec.dot(v2))
print(vec.__eq__(v2))
print(vec.norm())
print(v2.norm())
print(vec.cosine_distance(v2))
