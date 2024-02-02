class complex:
    
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __str__(self):
        return(f"{self.Re} + {self.Im}i")

    def sum(self,Z):         #Z es el resultado de la suma de Z1 Y Z2
        result = complex(0,0)
        result.Re = self.Re+Z.Re
        result.Im = self.Im+Z.Im
        return result 
        
    def rest(self,Z):
        result = complex(0,0)
        result.Re = self.Re-Z.Re
        result.Im = self.Im-Z.Im
        return result  

    def mult(self,Z):
        result = complex(0,0)
        resultado = (self.Re*Z.Re - self.Im*Z.Im) + (self.Re*Z.Im + self.Im*Z.Re)
        return (f"{resultado} + i")

    def div(self,Z):
        result = complex(0,0)
        result.Re = self.Re / Z.Re
        result.Im = self.Im / Z.Im - 0.0
        return result 


Z1 = complex(2,3)
Z2 = complex(4,1) 
print(Z1)
print(Z1.sum(Z2))
print(Z1.rest(Z2))
print(Z1.mult(Z2))
print(Z1.div(Z2))