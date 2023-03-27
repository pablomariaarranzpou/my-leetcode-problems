class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = [[float("inf")] * (cols+1) for i in range(rows+1)]
        ans[rows-1][cols] = 0
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                ans[i][j] = grid[i][j] + min(ans[i + 1][j], ans[i][j + 1])
        return ans[0][0]