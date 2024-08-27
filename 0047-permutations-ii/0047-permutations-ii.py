class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        nums = sorted(nums)
        n = len(nums)
        seen = set()
        
        
        def _aux(actual, used):
  
            
            if len(actual) == len(nums):
                sol.append(actual[:])
            
            else:
                for i in range(n):
                    
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    
                    if not used[i]:
                        actual.append(nums[i])
                        used[i] = True
                        _aux(actual, used)
                        used[i] = False
                        actual.pop(-1)
                   
        _aux([], [False] * len(nums))
                   
        return sol
        
        