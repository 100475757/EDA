import random as rd 

#Ejercicio 1: Tarjeta de Crédito
#Objetivo: ingresar y retirar el dinero de la cuenta, con una serie de condiciones.

class Credit_card:
  
    def __init__(self, name: str , id:int, balance = 0 , limit = 0 ):
        self.name = name
        self.id = id
        self.balance = balance
        self.limit = limit

    def charge(self, money:int):
        self.balance+=money
        if self.balance > self.limit:
            self.balance -=money
        else:
            self.balance == self.balance
    
    def make_deposit(self, money):
        self.balance-=money
        if self.balance < money:
            self.balance+=money
            print("No tienes suficinte saldo ")
        else:
            self.balance == self.balance

    
t1 = Credit_card("Paulo" , 345594309 , 0 , 3000)
t1.charge(2499)
t1.charge(600)
t1.make_deposit(400)
t1.make_deposit(4000)

print(t1.balance)




"-----------------------------------------------------------------------------------------------------------"
#Ejercicio 2: Polinomio
#Objetivo: Crear un polinomio y operar con el.

class polinomio:  #creates a new polynomial whose coefficients are the elements of the input list coef. The element at index 0 is the coefficient of term with degree 0 (constant term), the element at index 1 is the coefficient of term with degree 1, and so on.

    def __init__(self, coeff:list):
        self.coeff = coeff

    def  getDegree(self): # which returns the polynomial grade.
        grade = -1
        for i in range(len(self.coeff)):
            if len(self.coeff) == 0:
                print("No existen polinomios vacíos")
                return None
            
            grade += 1
        return  grade
    
    def getCoefficient(self , n): #which returns the coefficient of the term, which is squared to n. 
        if n > len(self.coeff) or n < 0:
            print("El grado del polinomio es menor al pedido")
            return None
       
        return self.coeff[n]

    def setCoefficient(self , n:int, newValue:int): #which modifies the coefficient of the term whose power is n by the value newValue. 
         if n > len(self.coeff) or n < 0:
            print("El grado del polinomio es menor al pedido")
            return 
    
         self.coeff[n] = newValue

    def evaluate(self , x): #which takes x as param and returns the value of the polynomial functions for this value.   
        pol = 0
        for i in range(len(self.coeff)):
            pol += self.coeff[i]*(x**i)

        return pol

    def __add__(self, p): #which returns the sum of the invoking polynomial and the polynomial p. The invoking polynomial must not be modified.
        """It returns a new polynomial which is the sum of the invoking polynomial (self)
        and q. This allows us to overwrite the operator + """
    #Create a new polynomial that is a copy of the polynomial with greater degree
        if self.getDegree()>=p.getDegree():
            sumPol=polinomio(self.coeff)
            #now, we have to add the coefficients from q
            for i in range(0,p.getDegree()+1):
                sumPol[i]=sumPol[i]+p[i]
            else:
                sumPol=polinomio(p.coeff)
                #now, we have to add the coefficients from self
                for i in range(0,self.getDegree()+1):
                    sumPol[i]=self[i]+sumPol[i]
                
            return sumPol

    def __str__(self):
        "It retuns a string representing the polynomial function"
        result=''

        i=self.getDegree()

        while i>0:
            term=self[i]
            if term==1:
                result += '+x'
            elif term==-1:
                result += '-x'
            elif term>1:
                result += '+' + str(term)+'x'
            elif term<-1:
                result += str(term)+'x'
            if term!=0 and i>1: 
                result += '^'+str(i) 
            i=i-1
       
        if self[0]>0:
            result += '+'+str(self[0])
        elif self[0]<0:
            result += str(self[0])


        if result[0]=='+':
            result=result[1:]
        return result

p1 = polinomio([1,4,7,9])
p2 = polinomio([4,6,9,2,3])
print(p1.getDegree())
print(p1.getCoefficient(3))            
p1.setCoefficient(2,100)
print(p1.evaluate(2))
print(p1.__add__(p2))







