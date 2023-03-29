class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        m = [1, 1, 1, 1, 1]
        
        for i in range(2, n + 1):
            m[4] = sum(m[:5])
            m[3] = sum(m[:4])
            m[2] = sum(m[:3])
            m[1] = sum(m[:2])
            
        return sum(m)
            
            