class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        if len(chalk) == 1:
            return 0
        
       
        n = len(chalk)
        sum_chalks = 0
        
        for i in range(n): 
            sum_chalks += chalk[i]
            
            if k < sum_chalks:
                break
        
        k = k % sum_chalks
        
        i = 0
        while chalk[i % n] <= k:
            k -= chalk[i % n]
            i += 1
            
        return i % n
        