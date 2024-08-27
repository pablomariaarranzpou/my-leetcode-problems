class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        
        c = 0
        n = len(values)
        m = len(values[0])
        
        values_a = []
        for value in values:
            values_a += value
            
        values_a = sorted(values_a)
        
        for d in range(1, n * m + 1):
            
            c += values_a[d - 1] * d
                
        return c
                        
                        
                
                        
                    
                
        