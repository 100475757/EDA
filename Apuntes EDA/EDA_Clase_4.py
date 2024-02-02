# Probelema: Detecta expresiones aritméticas correctas o incorrectas con "()".
# Emplear para ello pilas

class stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):  # equivalente a return len(self.items) == 0
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, other):
        self.items.append(other)

    def pop(self):
        if self.isEmpty():  # Equivalente a if len(self.items) == 0:
            print("La lista está vacía, no hay elementos")
        else:
            return self.items.pop()  # .pop elimina y devuelve el elemento de la ultima posicion

    def top(self):
        if self.isEmpty():  # Equivalente a if len(self.items) == 0:
            print("La lista está vacía, no hay elementos")
            return None
        else:
            return self.items[-1]

    def __len__(self):
        return len(self.items)

def balanced(exp: str): #La expresion es un string
    s = stack()
    for i in exp:  #Llenamos toda la pila con los parentesis de apertura "(" y por cada ")" eliminamos uno de entrada, con el objetivo de vaciar la pila, lo que indica que la expresion es correcta
        if i == "(":
            s.push(i)
        elif i == ")":
            if s.isEmpty():  #No hace falta poner else, pq si entro en el if no leo el resto de condiciones.
                return False
            s.pop()
        return s.isEmpty() #Si es true la expresion es correcta, pues significa que se nos han ido los parentesis, luego la expresion es correcta
        

"---------------------------------------------------------------------------------------------------------------------"
#Problema 2 – Josephus problem.

class queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, other):
        self.items.append(other)

    def dequeue(self):
        if self.isEmpty():  # Equivalente a if len(self.items) == 0:
            print("La lista está vacía, no hay elementos")
            return None
        else:
            return self.items.pop(0)

    def front(self):
        if self.isEmpty():  # Equivalente a if len(self.items) == 0:
            print("La lista está vacía, no hay elementos")
            return None

        else:
            return self.items[0]

    def __len__(self):
        return len(self.items)

def josephus(n, step): #n= nº de soldados , step= nº de veces que salto
    q = queue()
    for i in range(1,n+1): #pq el range acaba en el anterior a n+1, es decir en n.
        q.enqueue(i)

    while len(q)>1:
        for i in range(step-1):
            q.enqueue(q.dequeue()) #Encolo lo que desencolo, es decir los soldados que no mueren
        q.dequeue()
    return q


print(josephus(40,7))
    
