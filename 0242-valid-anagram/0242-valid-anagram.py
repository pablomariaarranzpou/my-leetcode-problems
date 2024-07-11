class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n = len(s)
        if n != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)
        
        for i in range(len(s)):
            
            if s[i] != t[i]:
                return False
        
            
        return True