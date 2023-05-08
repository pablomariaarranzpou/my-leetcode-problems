class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        init, fin = 0, len(mat[0]) - 1
        suma = 0

        for i in range(len(mat)):
            
            suma += mat[i][i]
            if init != fin:
                suma += mat[init][fin] 
            init += 1
            fin -= 1
        return suma