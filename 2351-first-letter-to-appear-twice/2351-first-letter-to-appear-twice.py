class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        
        conj = set()
        
        for char in s:
            
            if char in conj:
                
                return char
            
            conj.add(char)
            
            
            
            
        