class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        prev = prices[0]
        for i in range(1, len(prices)): 
            diff = prices[i] - prev
            if diff > 0:
                prof += diff  
            prev = prices[i]
        return prof 