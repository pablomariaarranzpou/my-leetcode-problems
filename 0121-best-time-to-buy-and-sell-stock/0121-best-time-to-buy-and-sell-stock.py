class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        min_price = prices[0]
        max_prof = 0
        
        
        for i in range(1, len(prices)):
            
            min_price = min(min_price, prices[i])
            max_prof = max(max_prof, prices[i] - min_price)
            
        
        return max_prof
        
        