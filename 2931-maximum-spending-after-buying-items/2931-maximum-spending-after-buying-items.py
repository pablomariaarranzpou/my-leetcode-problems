class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        
        c = 0
        n = len(values)
        m = len(values[0])
        
        
        for d in range(1, n * m + 1):
            
            min_value = float('inf')
            min_shop = None
            act = []
            
            for i in range(len(values)):
                if values[i]:
                    if min_value > values[i][-1]:
                        min_shop = i
                        min_value = values[i][-1]
                        
                    
            c += values[min_shop].pop() * d
                
        return c
                        
                        
                
                        
                    
                
        