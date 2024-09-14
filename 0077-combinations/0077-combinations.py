class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(act, last):
            
            if len(act) == k:
                res.append(act[:])
                
            else:  
                for i in range(last, n + 1, 1):
                    
                    act.append(i)
                    backtrack(act, i + 1)
                    act.pop()
                
        backtrack([], 1)
        
        return res
                
            
                
                
            
            
            
        
        
        
        
                    
                    