class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowed  = set(list(allowed))
        c = 0

        for word in words:
            error = False      
            for char in word:
                       
                if char not in allowed:
                    error = True
                    break
                       
            if not error:
                c += 1
                       
        return c
        