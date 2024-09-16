class TwoSum:

    def __init__(self):
        self.list = []
        

    def add(self, number: int) -> None:
        
        self.list.append(number)
        

    def find(self, value: int) -> bool:
        
        hashmap = {}
        
        for i in range(len(self.list)):
            
            num = self.list[i]
            
            target = value - num
            
           
            
            if target in hashmap:
                return True
            
                
            
            hashmap[num] = 1
            
        return False
            
            
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)