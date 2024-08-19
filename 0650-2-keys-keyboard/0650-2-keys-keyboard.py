class Solution:
    def minSteps(self, n: int) -> int:
        
        
        if n == 1:
            return 0
        
        def recuersive(a_count, copied):
            
            if a_count == n:
                return 0
            
            if a_count > n:
                return float('inf')
            
            
            
            pasting = 1 + recuersive(a_count + copied, copied)
            copi_paste = 2 + recuersive(a_count * 2, a_count)
            
            
            return min(pasting, copi_paste)
        
        return 1 + recuersive(1,1)
        