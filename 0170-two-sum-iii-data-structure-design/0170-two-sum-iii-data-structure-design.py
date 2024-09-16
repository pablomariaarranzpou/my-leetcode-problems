class TwoSum:

    def __init__(self):
        self.list = []
        

    def add(self, number: int) -> None:
        
        self.list.append(number)
        self.list.sort()
        

    def find(self, value: int) -> bool:
        
        i = 0
        j = len(self.list) - 1
        
        while i < j:
            
            calc = self.list[i] + self.list[j]
            
            if calc == value:
                return True
            
            elif calc < value:
                i += 1
                
            else:
                j -= 1
                
                
        return False
            
            
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)