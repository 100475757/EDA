#Complejidad temporal 
import time
import math


def sumN(n): #Función q suma los numeros naturales hasta desde 1 hasta "n".
    st = time.time()
    result = 0
    for i in range(1,n+1):
        result+=i
    et = time.time()
    pt = et-st
    return result, pt

print(sumN(1000000))
    
