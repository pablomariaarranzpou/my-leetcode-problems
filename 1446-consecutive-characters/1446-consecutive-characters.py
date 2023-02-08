class Solution:
    def maxPower(self, s: str) -> int:
        
        maxo = 1
        act_maxo = 1
        
        
        for i in range(len(s) - 1):
            
            if s[i] == s[i + 1]:
                act_maxo += 1
                
            else:
                
                if act_maxo > maxo:
                    maxo = act_maxo
                    
                act_maxo = 1
        if act_maxo > maxo:
            maxo = act_maxo
        
                           
        return maxo
            
            