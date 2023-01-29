class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        min_p = prices[0]
        max_p = 0

        for i in range(1, len(prices)):

            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)

        return max_p