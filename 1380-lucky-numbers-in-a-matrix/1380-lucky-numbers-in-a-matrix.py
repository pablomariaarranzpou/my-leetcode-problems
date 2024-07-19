class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minims = set()  
        for i in range(len(matrix[0])):
            maxi = 0
            for j in range(len(matrix)):
                minims.add(min(matrix[j]))
                v = matrix[j][i]
                if v > maxi:
                    maxi = v       
            if maxi in minims:
                return [maxi]   
        return []      