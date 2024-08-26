class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        
        diff_1 = -1
        diff_2 = -1
        
        diff_count = 0
        
        for i in range(len(s1)):
            
            if s1[i] != s2[i]:
                
                diff_count += 1
                
                if diff_count == 1:
                    diff_1 = i
                    
                elif diff_count == 2:
                    diff_2 = i
                    
                else:
                    return False
                
                
        if diff_count == 2:
            
            lista = list(s1)
            
            lista[diff_1], lista[diff_2] = lista[diff_2], lista[diff_1]
            
            s1 = "".join(lista)
            
        return s1 == s2
        