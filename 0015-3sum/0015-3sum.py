class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        n = len(nums)
        sol = []
        
        
        for i in range(n - 2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = n - 1
            
            
            while l < r:
                
                calc = nums[i] + nums[l] + nums[r]
                
                if calc > 0:
                    
                    r -= 1
                    
                elif calc < 0: 
                    l += 1
                    
                else:
                    sol.append([nums[i],nums[l], nums[r]])
                    
                    
                    l += 1
                    
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
                    r -= 1
                    
                    
        return sol
        
                    
                
                
        