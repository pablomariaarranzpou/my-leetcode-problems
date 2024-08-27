class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        
        c = 0
        n = len(values)
        m = len(values[0])
        
        pq = []
        
        for i in range(len(values)):
            for j in range(len(values[0])):
                
                heappush(pq, (values[i][j], i))
        
        for d in range(1, n * m + 1):
            
            val, shop = heappop(pq)
                 
            c += values[shop].pop() * d
                
        return c
                        
                        
                
                        
                    
                
        