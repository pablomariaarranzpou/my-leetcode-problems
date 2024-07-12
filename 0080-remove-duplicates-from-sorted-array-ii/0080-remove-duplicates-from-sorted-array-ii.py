class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i=0
        
        while i < len(nums) - 2:
            
            if(nums[i] == nums[i+1]):
                
                if nums[i+1] == nums[i+2]:
                    nums.remove(nums[i + 1])
                    continue
            
            
            i+=1