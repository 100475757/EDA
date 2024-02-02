#Problemas de recursión

def sumList(L):
    return (_sumList(L,0))

def _sumList(L,index):
    if index == len(L) - 1:
        return L[index]
    return L[index] +_sumList(L,index+1)

def maxlist(L):
    return (_maxList(L,0))

def _maxList(L,index):
    if index == len(L)-1:
        return L[index], index

    return max(L[index],_maxList(L,index))

def ordered(L):
    if len(L) ==1:
        return True
    if L[0] <L[1]:
        return False
    return ordered(L[1:])

def reverse(word):
    result = ""
    if len(word) == 0:
        return result 
    result = result + word[-1] + reverse(word[:1])

L = [1,7,8,4,6]
print(sumList(L))    
print(L)
