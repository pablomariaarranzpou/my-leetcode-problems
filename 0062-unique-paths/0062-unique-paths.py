class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        row = [1] * n
        
        
        for i in range(m - 1):
            
            new_row = [0] * n
            new_row[-1] = 1
            
            for j in range(n - 2, -1, -1):
                
                new_row[j] = row[j] + new_row[j + 1]
                
            row = new_row
            
        return row[0]
                
        