class MyCircularDeque:

    def __init__(self, k: int):
        
        self.k = k
        self.lista = []
        

    def insertFront(self, value: int) -> bool:
        if len(self.lista) + 1 <= self.k:
            self.lista = [value] + self.lista
            return True
        else:
            
            return False
        
        

    def insertLast(self, value: int) -> bool:
        
        if len(self.lista) + 1 <= self.k:
            
            self.lista.append(value)
            return True
        
        else:
            
            return False
        
        
        

    def deleteFront(self) -> bool:
        
        if len(self.lista) - 1 >= 0:
            self.lista = self.lista[1:]
            return True
        else:
            
            return False
        

    def deleteLast(self) -> bool:
        if len(self.lista) - 1 >= 0:
            self.lista.pop()
            return True
        else:
            
            return False
        

    def getFront(self) -> int:
        if self.lista:
            return self.lista[0]
        else:
            return -1
        

    def getRear(self) -> int:
        
        if self.lista:
            return self.lista[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        
        if self.lista:
            return False
        else:
            return True
        

    def isFull(self) -> bool:
        
        return len(self.lista) == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()