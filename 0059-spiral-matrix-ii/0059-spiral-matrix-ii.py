class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        m, n = len(matrix), len(matrix[0])
        direction = 1
        i, j = 0, -1
        start = 1
        while m*n > 0:
            for _ in range(n):
                j += direction
                matrix[i][j] = start
                start += 1
            m-= 1
            for _ in range(m):
                i += direction
                matrix[i][j] = start
                start += 1
            n-=1
            direction *= -1
        return matrix
        