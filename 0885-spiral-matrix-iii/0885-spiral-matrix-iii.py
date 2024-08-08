import math
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        
        radio = 0
        max_radio = max(max(rows - rStart, rStart), max(cStart, cols - cStart))
        
        i = rStart
        j = cStart
        path = []
        
        visited = set()
        
        while radio <= max_radio:
            
        
            path.append([i, j])
            
            print(i + 1, rStart + radio)        
            while i + 1 < rStart + radio + 1:
                # abajo sumamos una row 
                path.append([i + 1, j])
                i += 1
            
            print(j - 1, cStart - radio) 
            while j - 1 > cStart - radio - 1:
                
                # izquierda restamos una columna
                path.append([i, j - 1])
                j -= 1
                    
            while i - 1 > rStart - radio - 1:
                # arriba restamos una row
                path.append([i - 1, j])
                i -= 1
                     
            while j + 1 < cStart + radio + 1:
                
                # derecha sumamos una col
                path.append([i, j + 1])
                j += 1
                    
            j += 1
            radio += 1
            
        final = []
        for edge in path:
            
            if edge[0] >= 0 and edge[1] >= 0 and edge[0] < rows and edge[1] < cols and edge not in final:
                final.append(edge)
            
        return final
                
                
            
                
                
        
            
            
            
                
                
        