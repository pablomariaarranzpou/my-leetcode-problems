class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        
        
        i = 0
        j = len(nums) - 1
        c = 0
        
        while i < j:
            
            calc = nums[i] + nums[j]
            
            if calc == k:
                c += 1
                i += 1
                j -= 1
                
            elif calc < k:
                i+= 1
                
            else:
                j -= 1
                
        return c      
        