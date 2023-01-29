class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1],[1,1]]

        dp = [[1]*(_ + 1) for _ in range(numRows)]

        dp[0] = [1]
        dp[1] = [1,1]
    

        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp



        