import math
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        
        radio = 0
        max_radio = max(max(rows - rStart, rStart), max(cStart, cols - cStart))
        
        i = rStart
        j = cStart
        path = []
        
        while radio <= max_radio:
            
            if j < cols and i < rows and i >= 0 and j >= 0:
                path.append([i, j])
                    
            while i + 1 < rStart + radio + 1:
                # abajo sumamos una row 
                if j < cols and i + 1 < rows and i + 1 >= 0 and j >= 0:
                    path.append([i + 1, j])
                i += 1
             
            while j - 1 > cStart - radio - 1:
                
                # izquierda restamos una columna
                if j - 1 < cols and i < rows and i >= 0 and j - 1>= 0:
                    path.append([i, j - 1])
                j -= 1
                    
            while i - 1 > rStart - radio - 1:
                # arriba restamos una row
                
                if j < cols and i - 1 < rows and i - 1 >= 0 and j >= 0:
                    path.append([i - 1, j])
                i -= 1
                     
            while j + 1 < cStart + radio + 1:
                
                # derecha sumamos una col
                
                if j + 1 < cols and i < rows and i >= 0 and j + 1 >= 0:
                    path.append([i, j + 1])
                j += 1
                    
            j += 1
            radio += 1
            
        return path
                
            
                
                
        
            
            
            
                
                
        