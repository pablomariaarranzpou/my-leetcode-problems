class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        cols = len(matrix[0])
        rows = len(matrix)
        visited = set()
        
        i, j, r, v = 0, 0, 0, 0
        
        res = []
        
        while r < min(rows, cols):
            
            if (i, j) not in visited:
                res.append(matrix[i][j])
                visited.add((i,j))
        
            while j + 1 < cols - r:
                j += 1
                if (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i,j))
                    
                    

            while i + 1 < rows - r:
                i += 1
                if (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i,j))

            while j - 1 >= r:
                j -= 1
                if (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i,j))
                

                
            while i - 1 >= r + 1:
                i -= 1
                if (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i,j))

            
            j += 1
            r += 1
            
        return res
              