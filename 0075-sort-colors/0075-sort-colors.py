class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        r, w = 0, 0
        
            
        for i in nums:
            
            if i == 0:
                r += 1
            elif i == 1:
                w += 1
            

                
        nums[:r] = [0] * r
        
        nums[r:w+r] = [1] * w
        
        nums[w+r:] = [2] * (len(nums) - w - r)
        
            
            
        