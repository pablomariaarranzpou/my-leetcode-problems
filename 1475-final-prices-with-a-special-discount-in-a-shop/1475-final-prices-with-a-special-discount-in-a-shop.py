class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        n = len(prices)
        
        for i in range(n):
            
            pos = prices[i]
            for j in range(i + 1, n):
                
                if prices[j] <= pos:
                    prices[i] -= prices[j]
                    break
        

        return prices
            
        