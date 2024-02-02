#TEMA 4. Recursión

def factorial(n): #Factorial: n*(n-1)(n-2)......3*2*1
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(6))

def multSum(a,b):
    result = 0
    if b == 1:
        result = a
    else:
        result = a + multSum(a, b-1)
    return result

print(multSum(5,4))

def SumList(L):
    result = 0
    if len(L) == 1:
        result = L[0]
    else:
        result = L[0] + SumList(L[1:])  #RECORDAR ESTE OPERADOR!!!
    return result 

def invLista(L):  #Método de listas auxiliares
    if len(L) == 1:
        return L
    else:
        return invLista(L[1:]) + [L[0]]
    
    
def sumBin(L):
    if len(L) == 1:
        return L[0]
    
    L1 = L[:len(L)//2]
    L2 = L[len(L)//2:]
    return sumBin(L1) + sumBin(L2)

L = [1,2,3,4,5,6,7,8,9,10]
print(SumList(L))
print(invLista(L))
print(sumBin(L))

    