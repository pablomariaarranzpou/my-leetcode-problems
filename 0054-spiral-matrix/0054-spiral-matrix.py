class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        res = []
        
        while top <= bottom and left <= right:
            
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res

              