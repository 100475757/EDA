#Implementación divide y vencerás 

import random as rd 
#Ejercicio examen final

def findMax(A: list):
    #Devuelve el mayor elemento de una lista, aplicando divide y vencerás

    #Caso base 
    if A == None or len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    #Divide
    m = len(A)//2
    #Dividimos la lista en dos mitades, para aplicar recursión en cada mitad
    parte1 = A[0:m]  #Esto va de 0 a m-1
    parte2 = A[m:]   #Esto va de m hasta el final
    max1 = findMax(parte1)
    max2 = findMax(parte2)

    #Vencer
    if max1 > max2:
        return max1
    else:
        return max2

#Otra forma de hacer el findMax
def findMax2(A: list):
    if A == None or len(A) == 0:
        return None
    
    return _findMax2(A, 0 , len(A)-1)

def _findMax2(A , start, end):
    if start == end:
        return A[start]
    
    else:
        m = len(A)//2
        max1 = _findMax2(A, start , m)
        max2 = _findMax2(A, m + 1, end)

        return max(max1, max2)
    

def findMin(A: list):
    #Devuelve el menor elemento de una lista, aplicando divide y vencerás
    #Caso base 
    if A == None or len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    #Divide 
    m = len(A)//2
    parte1 = A[0:m]   #Esto va de la pos 0 a la pos m-1
    parte2 = A[m:]
    min1 = findMin(parte1)
    min2 = findMin(parte2)

    #Vencer
    return min(min1, min2)

#Otra forma de hacer el findMin
def findMin2(A: list):
    if A == None or len(A) == 0:
        return None
    
    return _findMin2(A, 0 , len(A)-1)

def _findMin2(A , start, end):
    if start == end:
        return A[start]
    
    else:
        m = len(A)//2
        min1 = _findMin2(A, start , m)
        min2 = _findMin2(A, m + 1, end)

        return min(min1, min2)
    

def sumArray(A: list):
    #Función que aplicando el algoritmo de divide y vencerás suma los elementos de una lista
    #Caso base 
    if A == None or len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    #Divide
    m = len(A) //2
    parte1 = A[0:m]
    parte2 = A[m:]
    sum1 = sumArray(parte1)
    sum2 = sumArray(parte2)

    #Vence 
    result = sum1 + sum2
    return result 

#Otra forma de hacerlo
def sumArray2(A: list):
    if A == None or len(A) == 0:
        return None
    
    return _sumArray2(A, 0 , len(A)-1)

def _sumArray2(A, start, end):
    if start == end:
        return 2 * A[start]
    
    else:
        m = len(A) //2
        p1 = _sumArray2(A, start, m)
        p2 = _sumArray2(A, m+1 , end)
    
        return p1 + p2
    
#Función que devuelve el valor minimo y maximo de una lista

def findMinMax(A: list):
    if A == None or len(A) == 0:
        return None 
    if len(A) == 1:
        return A[0] , A[0]
    
    m = len(A) //2
    parte1 = A[0:m]
    parte2 = A[m:]

    mayor1 , menor1 = findMinMax(parte1)
    mayor2 , menor2 = findMinMax(parte2)
    return max(mayor1 , mayor2) , min(menor1 , menor2)

#Función que devuelve el nº par más pequeño de una lista

def findLowestEven(A: list):
    #Casos base
    if A == None or len(A) == 0:
        return None
    if len(A) == 1: 
        if A[0] % 2 == 0:
            return A[0]
        else: 
            return None
    
    #Divide
    m = len(A) //2
    p1 = A[0:m]
    p2 = A[m:]

    min_par_1 = findLowestEven(p1)
    min_par_2 = findLowestEven(p2)

    #Vence
    if min_par_1 != None and min_par_2 != None:
        return min(min_par_1 , min_par_2)
    
    if min_par_1 != None:
        return min_par_1
    
    if min_par_2 != None:
        return min_par_2
    
    else:
        return None

# #Función que devuelve el nº par e impar más pequeño de una lista
def findLowestEvenOdd(A: list):
    #Casos base
    if A == None or len(A) == 0:
        return None
    
    if len(A) == 1:
        if A[0] % 2 == 0:
            return A[0] , None
        else:
            return None, A[0]
    

    m = len(A) // 2
    p1 = A[0:m]
    p2 = A[m:]

    minEven1,minOdd1= findLowestEvenOdd(p1)
    minEven2,minOdd2=findLowestEvenOdd(p2)

    if minEven1!=None and minEven2!=None:
        minEven=min(minEven1,minEven2)
    elif minEven1==None and minEven2!=None:
        minEven=minEven2
    elif minEven2==None and minEven1!=None:
        minEven=minEven1
    else: #los dos son None
        minEven=None

    if minOdd1!=None and minOdd2!=None:
        minOdd=min(minOdd1,minOdd2)
    elif minOdd1==None and minOdd2!=None:
        minOdd=minOdd2
    elif minOdd2==None and minOdd1!=None:
        minOdd=minOdd1
    else: #los dos son None
        minOdd=None
    

    return minEven, minOdd
    

#Implementa una función basada en divide y vencerás que devuelva una lista con los strings que tengan longitud
#menor o igual a 2

def getWordsLenght2(words: list):
    #Caso base 
    if words == None or len(words) == 0:
        return None
    
    if len(words) == 1:
        w = words[0]
        if len(w) <= 2:
            return words
        else: 
            return []
    
    m = len(words) // 2
    p1 = words[0:m]
    p2 = words[m:]

    w1_lenght2 = getWordsLenght2(p1)
    w2_lenght2 = getWordsLenght2(p2)

    return w1_lenght2 + w2_lenght2

"""Implementa una función basada en divide y 
vencerás que **sume los elementos múltiplos de 5 **en una array."""

def sumMultiply5(A: list):
    #Casos base 
    if A == None or len(A) == 0:
        return None
    if len(A) == 1:
        if A[0] % 5 == 0:
            return A[0]
        else:
            return None    #Tb puedo poner aquí 0 y me ahorro las condiciones del "vencer"
    
    #Divide
    m = len(A) //2
    p1 = A[0:m]
    p2 = A[m:]
    sum_1 = sumMultiply5(p1)
    sum_2 = sumMultiply5(p2)

    #Vencer
    if sum_1 != None and sum_2 != None:
        return sum_1 + sum_2
    if sum_1 and sum_2 == None:
        return sum_1
    if sum_1 == None and sum_2:
        return sum_2

"""## Binary search
Given a **sorted list** and a number, x, return True if x is found, False otherwise.
"""
def binarySearch(A: list , x):
    #Casos base 
    if A == None or len(A) == 0 or x not in A:
        return False
    if len(A) == 1:
        if x == A[0]:
            return True 
        else: 
            return False
    
    m = len(A) //2
    p1 = A[0:m]
    p2 = A[m:]
    search_1 = binarySearch(p1 , x)
    search_2 = binarySearch(p2 , x)

    return search_1 or search_2

"""Implementa una función que reciba un **array  ordenado de enteros** A y un valor x, y 
**devuelva el índice de x en el array A**. Si x no existe, la función devuelve -1. 
No está permitido aplicar slicing (es decir, expresiones del tipo A[0:m] o A[m:]) ni crear sublistas auxiliares."""

def binarySearch2(A: list, x: int):
    #Casos base 
    if len(A) == 0 or A == None or x not in A:
        return -1
    
    return _binarySearch(A, x , 0 , len(A)-1)

def _binarySearch(A , x , start , end):
    m = len(A) //2 
    if x == A[m]:
        return m
    if x < A[m]:
        return  _binarySearch(A, x , start , m-1)
    
    if x > A[m]:
        return  _binarySearch(A, x , m+1 , end)



"""Implementa una función basada en divide y vencerás 
que reciba una lista de strings y que devuelva la **palabra con mayor longitud**. """

def longestword(words: list):
    #Casos base 
    if words == None or len(words) == 0:
        return None
    if len(words)==1:
        return words[0]
    
    #Divide
    m = len(words) //2
    p1 = words[0:m]
    p2 = words[m:]

    longest1 = longestword(p1)
    longest2 = longestword(p2)

    #Vencer
    if longest1==None and longest2==None:
        return None
    elif longest1==None:
        return longest2
    elif longest2==None:
        return longest1
    else:
        if len(longest1)>=len(longest2):
            return longest1
        else:
            return longest2

"""Algoritmo MergeSort"""

def merge(lista1,lista2):
    #lsita1 y lista2 están ordenadas!!!
    #devolver la lista ordenada
    result=[]
    i=0 #lista 1
    j=0 #lista 2

    while i<len(lista1) and j<len(lista2):
        if lista1[i]<=lista2[j]:
            result.append(lista1[i])
            i+=1
        else: #lista1[i]>lista2[j]
            result.append(lista2[j])
            j+=1

    while i<len(lista1):
        result.append(lista1[i])
        i+=1

    while j<len(lista2):
        result.append(lista2[j])
        j+=1

    return result

def mergesort(A: list):
    #Ordena una lista de python
    #Caso base 
    if A == None or len(A) == 0:
        return None
    if len(A) == 1:
        return A
    
    #Divide
    m = len(A)//2
    parte1 = A[0:m]  #Esto va de 0 a m-1
    parte2 = A[m:]
    sort1 = mergesort(parte1)
    sort2 = mergesort(parte2)

    A = merge(sort1, sort2)

    return A


## Quicksort

### 1) Quicksort con pivote en la posición central del array
def quicksort(A):
    _quicksort(A,0,len(A)-1)
    
    
def _quicksort(A, left, right):
    i = left
    j = right
    
    m=(left + right) // 2
    
    p = A[m] # pivot element in the middle
    
    while i <= j:
        while A[i] < p: 
          i += 1

        #estoy en un i cuyo valor es mayor que p

        while A[j] > p: 
          j -= 1

        #llego un j cuyo valor es menor que p

        if i <= j: # swap 
            if i < j:
                A[i], A[j] = A[j], A[i]

            i += 1
            j -= 1

    if left < j: # sort left list
        _quicksort(A, left, j)
    if i < right: # sort right list
        _quicksort(A, i, right)



def getIndices(data,x):
  """returns the list of indices for x in data"""
  if data==None or len(data)==0:
    return []

  return _getIndices(data,x,0,len(data)-1,[])

def _getIndices(data,x,left,right,indices):
   if left<=right:
     mid = (left + right) // 2
    
     _getIndices(data,x,left,mid-1,indices)

     if data[mid]==x:
        indices.append(mid)
    
     _getIndices(data,x,mid+1,right,indices)
  
   return indices

#Pregunta examne final
"""Implementa una función recursiva are_adjacent que reciba una
cadena de texto, w, y dos caracteres, c1 y c2, y comprueba si c1 aparece inmediatamente
antes que c2 en w. En ese caso devuelve True, y en cualquier otro caso devuelve False."""

"""Tu función debe cumplir las siguientes reglas:
- No puede usar bucles ni listas auxiliares. Aunque sí está permitido aplicar slicing
sobre las listas. En otras palabras, sí está permitido utilizar expresiones como: w[0],
w[1:], etc.
- No está permitido el uso del operador in. Tampoco puedes utilizar métodos como
find, index, startswith o endswith.
- Sin embargo, sí está permitido usar el método len()."""
def are_adjacent(w: str , c1: str , c2: str) -> bool:
    #Caso base 
    if w == None or len(w) < 2:
        return False
    
    if len(w) == 2:
        if w[0] == c1 and w[1] == c2:
            return True 
        else:
            return False
    
    if c1 != w[0]:
        return are_adjacent(w[0:] , c1 , c2)

    if c2 == w[1]:
        return True
    
    
    return are_adjacent(w[2:] , c1 , c2)  


#Escribe una función en Python llamada `contar_inversiones` que tome como 
# argumento una lista de enteros llamada `nums` y devuelva el número total de inversiones 
# en la lista. Una inversión ocurre cuando hay un par de elementos `nums[i]` y `nums[j]` 
# tal que `i < j` pero `nums[i] > nums[j]`. Utiliza el enfoque de "divide y vencerás" para dividir 
# la lista en subproblemas más pequeños y combinar las soluciones para obtener el número total de inversiones.

def contar_inversiones(nums: list) -> int:
    #Caso base 
    if nums == None or len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 0
    
    #Divide
    m = len(nums) //2
    p1 = nums[0:m]
    p2 = nums[m:]
    inv1 = contar_inversiones(p1)
    inv2 = contar_inversiones(p2)

    #Vencer
    inv = inv1 + inv2
    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i] > p2[j]:
                inv += 1
    return inv

# Encuentra los  pares de elementos en una lista de enteros cuya suma 
# sea igual a un valor dado, utilizando el algoritmo de divide y vencerás.

def findPair(nums: list , x: int):
    #Caso base 
    if nums == None or len(nums) == 0:
        return None
    if len(nums) == 1:
        return None
    
    #Divide
    m = len(nums) //2
    p1 = nums[0:m]
    p2 = nums[m:]
    pair1 = findPair(p1 , x)
    pair2 = findPair(p2 , x)

    #Vencer
    if pair1 != None and pair2 != None:
        return pair1 + pair2
    if pair1 and pair2 == None:
        return pair1
    if pair1 == None and pair2:
        return pair2

    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i] + p2[j] == x:
                return p1[i] , p2[j]
    return None





    



nums = [5,4,6,3,7,2,8,1,9,0]
print(findPair(nums , 9))
print(contar_inversiones(nums))
"""
            
words = ["Me" , "gustas" , "natural" , "yo", "ya" , "no" , "se" , "estar" , "sin" , "ti"]
lista = []
for i in range(10):
    lista.append(rd.randint(0,30))

lista.append(5)
print(lista)
print(findMax(lista))
print(findMin(lista))
print(sumArray(lista))
print(findMinMax(lista))
print(findLowestEven(lista))
print(getWordsLenght2(words))
print(findLowestEvenOdd(lista))
print(sumMultiply5(lista))
print(binarySearch(lista , 20))
print(longestword(words))
print(getIndices(lista , 5))
print(are_adjacent(words , "Me" , "gustas"))"""





