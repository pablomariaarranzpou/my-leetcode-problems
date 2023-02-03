class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            for j in range(i, n):
                
                aux = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = aux
                
            matrix[i].reverse()
        
                
        