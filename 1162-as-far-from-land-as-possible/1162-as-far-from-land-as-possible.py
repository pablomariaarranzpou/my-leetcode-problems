class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        if all(grid[i][j] == 0 for i in range(len(grid)) for j in range(len(grid))) or all(grid[i][j] == 1 for i in range(len(grid)) for j in range(len(grid))):
            return -1
        dp = [[float('inf')]*len(grid) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                
                if grid[i][j] == 1:
                    
                    dp[i][j] = float('inf')
                    dp = self.bfs(i, j, set(), grid, dp, i, j)

        return max(map(max, dp))
    
    def bfs(self, i, j, visited, grid, dp, ini_i, ini_j):
            
        queue = [(i, j, 0)]
            
        while queue:
                
            i, j, dist = queue.pop(0)
                
            if (i, j) in visited:
                continue
                    
            visited.add((i, j))
            
            if (grid[i][j] != 1 or (i == ini_i and ini_j == j)):
                
                dp[i][j] = min(dp[i][j], dist)
                
                if dp[i][j] >= dist:
                    
                    dp[i][j] = dist
                else:
                    continue  

                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid):
                        queue.append((x, y, dist+1))
                        
        return dp
                    