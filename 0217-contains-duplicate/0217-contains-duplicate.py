class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        s_nums = set(nums)
        
        if len(nums) == len(s_nums):
            return False
        else:
            return True
        
        