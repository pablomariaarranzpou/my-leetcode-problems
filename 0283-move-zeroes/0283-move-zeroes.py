class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        i = len(nums) - 1
        
        while i >= 0:
            
            if nums[i] == 0 and i != len(nums) - 1:
                
                if nums[i + 1] != 0:
                    
                    tmp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = tmp
                    i += 1
                    continue
            i -= 1
        
        return nums
                
        