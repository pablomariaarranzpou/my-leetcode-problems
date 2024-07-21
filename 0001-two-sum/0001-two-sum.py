class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_s = set(nums)
        
        for i in range(len(nums)):
            opt = target - nums[i]
            if(opt in nums_s):
                if nums.index(opt) != i:
                    return [nums.index(opt), i]
            
  