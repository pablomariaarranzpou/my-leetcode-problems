class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        
        def isMagic(matrix):
            
            visited = set()
            for i in range(3):
                for j in range(3):
                    
                    num = matrix[i][j]
    
                    if  0 < num < 10 and num not in visited:
                        visited.add(num)
                        
                    else:
                        return False        
            
            suma_r1 = sum(matrix[0])
            suma_r2 = sum(matrix[1])
            
            if suma_r1 != suma_r2:
                return False
            
            suma_r3 = sum(matrix[2])
            
            if suma_r3 != suma_r2:
                return False
            
            suma_col1 = matrix[0][0] + matrix[1][0] + matrix[2][0]
            
            if suma_col1 != suma_r2:
                return False
            
            suma_col2 = matrix[0][1] + matrix[1][1] + matrix[2][1]
            
            if suma_col2 != suma_r2:
                return False
            
            suma_col3 = matrix[0][2] + matrix[1][2] + matrix[2][2]
            
            if suma_col3 != suma_r2:
                return False
            
            suma_d1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
            
            if suma_d1 != suma_r2:
                return False
            suma_d2 = matrix[0][2] + matrix[1][1] + matrix[2][0]
            
            if suma_d2 != suma_r2:
                return False

            return True
               
            
        total = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                
                matrix = []
                for a in range(i, i + 3):
                    row = []
                    for b in range(j, j + 3):
                        row.append(grid[a][b])
                    matrix.append(row)
                
                if isMagic(matrix):
                    total += 1
                    
        return total
                
                