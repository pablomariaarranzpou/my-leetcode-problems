class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k == 0:
            return nums
        
        n = len(nums)
        
        k = k % n
        
        if k == 0:
            return nums 

        nums[:] = nums[-k:] + nums[:-k]
        
        

        
        
            
        