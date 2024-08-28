class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def _dfs(grid1, grid2, i, j):
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True
            
            grid2[i][j] = 0
            
            is_sub_island = True
            
            if grid1[i][j] == 0:
                is_sub_island = False
            
            if not _dfs(grid1, grid2, i - 1, j):
                is_sub_island = False
            if not _dfs(grid1, grid2, i + 1, j):
                is_sub_island = False
            if not _dfs(grid1, grid2, i, j - 1):
                is_sub_island = False
            if not _dfs(grid1, grid2, i, j + 1):
                is_sub_island = False
            
            return is_sub_island
        
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    if _dfs(grid1, grid2, i, j):
                        count += 1
        
        return count
