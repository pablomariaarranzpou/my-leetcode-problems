class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        closest = float("inf")
        nums = sorted(nums)
        
        for i in range(len(nums)-2):
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                
                suma = nums[i] + nums[j] + nums[k]
                
                if abs(suma - target) < abs(closest - target):
                    closest = suma
                    
                if suma > target:
                    k -= 1
                    
                elif suma < target:
                    j += 1
                    
                else:
                    return suma
                
        return closest
        
        
        