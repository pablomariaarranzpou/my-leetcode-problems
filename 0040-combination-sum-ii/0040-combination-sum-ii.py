class Solution:
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(actual, last):
            
            if sum(actual) == target:
                res.append(actual[:])

            for i in range(last, len(candidates)):
                if i > last and candidates[i] == candidates[i - 1]:
                    continue
                if sum(actual) + candidates[i] <= target:
                    actual.append(candidates[i])
                    backtracking(actual, i + 1)
                    actual.pop()
                else:
                    break
        
        candidates.sort()
        res = []
        backtracking([], 0)
        
        return res
        
        
       
                
                