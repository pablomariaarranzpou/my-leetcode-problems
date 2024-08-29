class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)

        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)

        conect_comp = 0
        visited = [False] * n

        def _dfs(stone):
            visited[stone] = True
            for neig in graph[stone]:
                if not visited[neig]:
                    _dfs(neig)

        for i in range(n):
            if not visited[i]:
                _dfs(i)
                conect_comp += 1

        return n - conect_comp