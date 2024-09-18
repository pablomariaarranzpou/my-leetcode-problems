class Solution:
    def makePalindrome(self, s: str) -> bool:
        
        
        i = 0
        j = len(s) - 1
        c = 0
        
        while i < j:
            
            if s[i] != s[j]:
                c += 1
                
            i += 1
            j -= 1
            
        return c <= 2
        
        
        