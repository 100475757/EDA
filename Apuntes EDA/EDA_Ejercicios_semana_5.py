#Problemas de recursión 

def sumN(n):
    #Caso base 
    if n == 0:
        return 0
    else: #Caso recursivo
        return sumN(n-1) + n

def factorial(n):
    #Caso base
    if n == 0: 
        return 1
    else: #Caso recursivo
        return factorial(n-1)*n

def potencia(a , n):
    #Caso base
    if n == 0:
        return 1
    else: #Caso recursivo 
        return potencia(a , n-1)*a

def mult(a,b):
    #Caso base
    if a < 0 or b < 0:
        return None
    if a == 0 or b == 0:
        return 0
    else: #Caso recursivo
        return mult(a , b-1) + a

def sum_list(data: list)-> int:
    #Caso base
    if data == None:
        return None
    if len(data) == 1:
        return 0
    else: #Caso recursivo 
        return data[0] + sum_list(data[1:])

def max_elem(data: list) -> int:
    #Caso base
    if data == None:
        return None
    if len(data) == 0:
        return data[0]
    else: #Caso recursivo
        return max(data[0], max_elem(data[1:]))

def isPalindrome(string: str) -> bool:
    #Caso base
    if string == None:
        return False
    if len(string) <= 1:
        return True
    else: #Caso recursivo
        return string[0] == string[-1] and isPalindrome(string[1:-1])
    
def isSorted(array: list)-> bool:
    #Caso base
    if array is None:
        return False
    if len(array) <=1:
        return True
    else: #Caso recursivo
        return array[0]<=array[1] and isSorted(array[1:])

def binary_search(array: list , a: int) -> bool:
    #Caso base
    if not isSorted(array):
        return False
    if len(array) == 0:
        return False
    else: #Caso recursivo
        return array[0] == a or binary_search(array[1:] , a)

def binary_search2(input_list: list, x: int) -> bool:
    """returns the index of x in input_list (which must be sorted)
    It does not use slicing"""
    if input_list is None or not isinstance(input_list, list) or not isinstance(x, int):
        return False
    
    if not isSorted(input_list):
        return False

    return _binary_search(input_list, x, 0, len(input_list) - 1)


def _binary_search(input_list: list, x: int, start: int, end: int) -> bool:
    """returns True if x exist into data, False eoc.
    O(log n), O"""
    if start <= end:
        m = (start + end) // 2
        if x == input_list[m]:
            return True
        elif x < input_list[m]:
            return _binary_search(input_list, x, start, m - 1)
        else:
            return _binary_search(input_list, x, m + 1, end)
    else:
        return False


def reverse(array: list) -> list:
    #Caso base 
    if array is None:
        return None
    if len(array) <= 1:
        return array
    else: #Caso recursivo
        aux = array.pop(0)
        reverse(array)
        array.append(aux)

def num_digits(x: int)-> int:
    #Caso base 
    if x < 0 or x != int:
        return 0
    if x < 10:
        return 1
    #Caso recursivo
    else:
        return 1 + num_digits(x//10)

def fibo(n: int) -> int:
    #Caso base
    if n < 0:
        return None
    if n <= 1:
        return n
    else: #Caso recursivo
        return fibo(n-1) + fibo(n-2)

def mult_rusa(a: int , b: int) -> int:
    #Caso base 
    if a != int or b != int or a < 0 or b < 0:
        return None
    if b == 1:
        return a
    if a == 1: 
        return b
    if a % 2 == 0: #Caso recursivo
        return mult_rusa(a // 2 , b * 2)
    else:
        return b + mult_rusa(a // 2 , b * 2)

def mcd(a: int , b: int) -> int:
    #Caso base
     if a != int or b != int or a < 0 or b < 0:
        return None
     if a > b: #Caso recursivo
         return mcd(b , a % b)
     else: 
         return mcd(a , a % b)

def num_vocales(string: str) -> int:
    if string is None or len(string) == 0:
        return 0

    first_char = string[0].lower()

    if first_char in ['a', 'e', 'i', 'o', 'u']:
        return 1 + num_vocales(string[1:])
    else:
        return num_vocales(string[1:])
    

values = [0,1,2,3,4,5,6]
print(isSorted(values))
print(binary_search(values , 9))
        


    

