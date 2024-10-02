class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        nums = sorted(nums)[::-1]
        
        if len(nums) == 1 or nums[1] != nums[0]:
            return nums[0]

        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i - 1] and nums[i + 1] != nums[i]:
                return nums[i]
                
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        return -1