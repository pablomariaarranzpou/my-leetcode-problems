class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        sol = []
        visited = set()
        
        for i in range(len(nums)):
            
            left = i + 1
            
            right = len(nums) - 1
            
            while left < right:
                
                if nums[i] + nums[left] + nums[right] > 0:
                    
                    right -= 1
                    
                elif nums[i] + nums[left] + nums[right] < 0:
                    
                    left += 1
                    
                else:
                    if((nums[i], nums[left], nums[right]) not in visited):
                        visited.add((nums[i], nums[left], nums[right]))
                        sol.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    
        return sol
                    