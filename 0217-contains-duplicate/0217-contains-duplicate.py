class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        
        if len(nums) < 2:
            return False
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
            
        if nums[-1] == nums[-2]:
                return True    
        
        return False