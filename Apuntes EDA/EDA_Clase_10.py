
#Clase unittest

import unittest


def divisionE(a,b): #Division entera, divide y devuekve en nº entero (función suelo)
    if b == 0:
        print("No se puede dividir por 0")
        return "x"
    else:
        return a//b

class Test(unittest.TestCase):
    def test_01(self):
        self.assertEqual(divisionE(8,4),2, "Fallo, resultado distinto del esperado 8/4")
    
    def test_02(self):
        self.assertEqual(divisionE(9,4),2, "Fallo, resultado distinto del esperado 9/4")
    
    def test_03(self):
        self.assertEqual(divisionE(8,0),"x", "Fallo, resultado distinto del esperado al dividir por 0")

#Comentar para usarlo en spyder
unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Descomenar para usarlo en Spyder
#if __name__ == '__main__':
    #unittest.main()

"--------------------------------------------------------------------------------------------"
from EDA_Clase_7 import DList

class DList2(DList):
    def removeDuplicate(self):
        current = self._head
        while current:
            current1 = current.next
            while current1:
                if current.elem == current1.elem:
                    current1.prev.next = current1.next
                    if current1.next:
                        current1.next.prev = current1.prev
                    else:
                        self._tail = current1
                    self._size -= 1
                current1 = current1.next
            current = current.next

d = [0,1,4,5,6,2,3,3,3,2,3,1,1,1,2,3]
D = DList2()
for i in d:
    D.addLast(i)
print(D)
D.removeDuplicate()
print(D)


