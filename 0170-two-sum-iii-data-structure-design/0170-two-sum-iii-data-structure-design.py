class TwoSum:

    def __init__(self):
        self.dict = {}
        

    def add(self, number: int) -> None:
        
        if number not in self.dict:
            self.dict[number] = 1     
        else:
            self.dict[number] += 1

    def find(self, value: int) -> bool:
        
        for i in self.dict:
            
            diff = value - i 
            
            if diff in self.dict:
                
                if diff == i and self.dict[i] == 1:
                    continue
                return True
                
                
            
            
                
            
        return False
            
            
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)