class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        numbers = s.split(" ")
        listafinal = []
        
        
        for i in numbers:

            if i.isdigit():
                listafinal.append(int(i))
                                  
                                  
        for i in range(0, len(listafinal) - 1):
            if(listafinal[i] >= listafinal[i+1]):
                return False
            
        return True
                
        
        