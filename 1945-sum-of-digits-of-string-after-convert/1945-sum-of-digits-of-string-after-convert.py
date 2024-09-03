class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        number = ""
        
        for i in s:
            
            number += str(ord(i) - ord('a') + 1)
            
        j = 0
        while j < k:
            
            suma = 0
            for i in list(number):
                
                suma += int(i)
                
            number = str(suma)
            j += 1
            
        return suma
                          
                          
        
            
        
        