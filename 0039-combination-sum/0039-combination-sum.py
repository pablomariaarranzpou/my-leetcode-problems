class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        seen = set()
        self.auxiliar_function(0, [], candidates, target, results)
        return results
        
       
    def auxiliar_function(self, suma, lista, candidates, target, results):
        
        
        if suma == target:
            sort = sorted(lista)
            if sorted(sort) not in results:
                results.append(sort)
            return
        
        else:
            
            for candidate in candidates:
                
                if suma + candidate <= target:
                    
                    lista_2 = lista.copy()
                    lista_2.append(candidate)
                    
                    suma += candidate
                    
                    self.auxiliar_function(suma, lista_2, candidates, target, results)
                    
                    suma -= candidate
                    
                    
                    
                    
                    
                
                
                
        
        