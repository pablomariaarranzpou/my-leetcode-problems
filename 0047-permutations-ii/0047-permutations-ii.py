class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        n = len(nums)
        seen = set()
        
        
        def _aux(actual, used):
  
            
            if len(actual) == len(nums):
            
                tup = tuple(actual)
                if tup not in seen:
                    seen.add(tup)
                    sol.append(actual)
            
            else:
                for i in range(n):
                    if i not in used:
                        actual.append(nums[i])
                        used.add(i)
                        _aux(actual[:], used)
                        used.remove(i)
                        actual.pop(-1)
                    
        _aux([], set())
                   
        return sol
        
        