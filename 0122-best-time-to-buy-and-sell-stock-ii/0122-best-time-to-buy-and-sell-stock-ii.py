class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        last_sold = 0
        prof = 0
        
        for i in range(1, len(prices)):
            petit = min(prices[last_sold:i])
            if petit < prices[i]:
                last_sold = i
                prof += prices[i] - petit
            
        return prof
            
            
        