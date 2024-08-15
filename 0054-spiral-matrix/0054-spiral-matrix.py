class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])

        left, right, top, bottom = 0, m-1, 0, n-1
        res = []

        while(left <= right and top <= bottom):
            
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if(bottom >= top):
                for i in range(right, left-1,-1):
                    res.append(matrix[bottom][i])
                bottom -=1

            if(right >= left):
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
              