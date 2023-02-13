class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd = (high-low) // 2
        if high % 2 == 1 or low % 2 == 1:
            odd += 1  
        return odd