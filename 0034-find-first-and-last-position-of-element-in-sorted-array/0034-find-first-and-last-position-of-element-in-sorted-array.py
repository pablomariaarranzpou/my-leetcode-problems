class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        set_n = set(nums)
        if target not in set_n:
            return [-1, -1]
        
        
        
        return [nums.index(target), len(nums) - nums[::-1].index(target) - 1]
        