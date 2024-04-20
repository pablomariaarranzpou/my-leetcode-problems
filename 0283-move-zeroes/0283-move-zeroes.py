class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        for i in nums:
            
            if i == 0:
                nums.remove(i)
                nums.append(0)
                
        return nums
                
        