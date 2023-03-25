class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        nums.sort(reverse=True)
        
        for i in range(len(nums)):
            
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
            
        return nums
        