class Solution:
    def minSteps(self, n: int) -> int:
        
        memo = {}
        if n == 1:
            return 0
        
        def recuersive(a_count, copied):
            
            if a_count == n:
                return 0
            
            if a_count > n:
                return float('inf')
            
            if (a_count, copied) in memo:
                return memo[(a_count, copied)]
            
            pasting = 1 + recuersive(a_count + copied, copied)
            copi_paste = 2 + recuersive(a_count * 2, a_count)
            
            mini = min(pasting, copi_paste)
            
            memo[(a_count, copied)] = mini
            
            return mini
                
            
        
        return 1 + recuersive(1,1)
        