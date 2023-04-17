class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        great = []
        max_candies = max(candies)
        
        for i in candies:
            if i + extraCandies >= max_candies:
                great.append(True)
            else:
                great.append(False)
                
        return great
            