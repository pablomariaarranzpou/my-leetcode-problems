class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        first, second = 0, 0
        currSum = 0
        mini = float('inf')
        
        for first in range(len(nums)):
            
            currSum += nums[first]
            
            while  currSum >= target:
                mini = min(mini, first - second + 1)
                currSum -= nums[second]
                second += 1
            
            
        return 0 if mini == float('inf') else mini
        