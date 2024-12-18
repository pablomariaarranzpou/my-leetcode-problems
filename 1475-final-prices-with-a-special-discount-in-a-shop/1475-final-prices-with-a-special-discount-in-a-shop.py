class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        nueva = []
        
        for i in range(len(prices)):
            
            for j in range(i + 1, len(prices)):
                
                if prices[j] <= prices[i]:
                    nueva.append(prices[i] - prices[j]) 
                    break
                    
                elif j == len(prices) - 1:   
                    nueva.append(prices[i])     

        return nueva + [prices[-1]]
            
        