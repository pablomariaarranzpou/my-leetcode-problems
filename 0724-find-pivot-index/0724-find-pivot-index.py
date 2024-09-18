class Solution:
    def pivotIndex(self, nums: List[int]) -> int:


        left = 0
        
        sumaTot = sum(nums)
        
        
        
        for i in range(len(nums)):
            
            sumaTot -= nums[i]
            
            if left == sumaTot:
                return i
            
            left += nums[i]
            
        return -1
        