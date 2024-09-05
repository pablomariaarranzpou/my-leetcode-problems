class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
                              
        suma = mean * (len(rolls) + n) - sum(rolls)
        res = []
        
        if suma > 6 * n or suma < n:
            return res
        
        mean_d = suma // n 
        mod = suma % n
        
        res = [mean_d] * n
        
        for i in range(mod):
            
            res[i] += 1
        
        
        return res
    
    
    
    
                    
                    
        
                
                
        
        