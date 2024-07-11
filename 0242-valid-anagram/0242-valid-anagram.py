class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        for i in s:
            t = t.replace(i,'',1)
        return len(t) == 0