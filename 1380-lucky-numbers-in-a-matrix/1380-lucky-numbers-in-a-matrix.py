class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        minims = set()
        maxs = set()
        
        for i in range(len(matrix)):
            minims.add(min(matrix[i]))
            
        for i in range(len(matrix[0])):
            maxi = 0
            for j in range(len(matrix)):
                if matrix[j][i] > maxi:
                    maxi = matrix[j][i]
                    
            maxs.add(maxi)
            
        return minims & maxs
            
            
            
        