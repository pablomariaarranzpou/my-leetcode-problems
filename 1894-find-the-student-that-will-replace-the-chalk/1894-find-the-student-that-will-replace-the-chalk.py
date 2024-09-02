class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        if len(chalk) == 1:
            return 0
        
        i = 0
        n = len(chalk)
        sum_chalk = sum(chalk)
        
        while sum_chalk <= k:
            k -= sum_chalk
            
        while chalk[i % n] <= k:
            k -= chalk[i % n]
            i += 1
            
        return i % n
        
       
        