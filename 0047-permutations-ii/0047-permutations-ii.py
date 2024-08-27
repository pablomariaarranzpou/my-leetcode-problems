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
                    
                    # si el numero actual es igual al anterior y el anterior no lo he usado este tampoco
                    if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
            
                    actual.append(nums[i])
                    used[i] = True
                    _aux(actual, used)
                    used[i] = False
                    actual.pop(-1)
                   
        _aux([], [False] * len(nums))
                   
        return sol
        
        