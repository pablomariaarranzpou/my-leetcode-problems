class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        self.auxiliar_function(0, [], candidates, target, results, 0)
        return results
        
    def auxiliar_function(self, suma, lista, candidates, target, results, start):
        if suma == target:
            results.append(lista.copy())
            return
        
        for i in range(start, len(candidates)):
            candidate = candidates[i]
            if suma + candidate > target:
                break
            
            lista.append(candidate)
            self.auxiliar_function(suma + candidate, lista, candidates, target, results, i) 
            lista.pop()
                    
                    
                    
                
                
                
        
        