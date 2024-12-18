class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        nueva = []
        n = len(prices)
        
        for i in range(n):
            
            pos = prices[i]
            for j in range(i + 1, n):
                
                
                if prices[j] <= pos:
                    nueva.append(pos - prices[j]) 
                    break
                    
                elif j == n - 1:   
                    nueva.append(pos)     

        return nueva + [prices[-1]]
            
        