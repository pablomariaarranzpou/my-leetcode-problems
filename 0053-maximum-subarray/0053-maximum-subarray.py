class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            if nums[i - 1] + nums[i] > nums[i]:
                nums[i] = nums[i - 1] + nums[i]
            
        return max(nums)
            