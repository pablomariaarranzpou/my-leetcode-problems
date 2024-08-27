class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        time_node = {i: float('inf') for i in range(n)}
        
        graph = {i: [] for i in range(n)}
        
        for from_n, to_n, time_i in roads:
            graph[from_n].append((to_n, time_i))
            graph[to_n].append((from_n, time_i))
            
        
        time_node[0] = 0
        pq = []
        min_time = None
        heappush(pq, (0, 0))
        ways = [[0] for i in range(n)]
        ways[0] = 1
        
        while pq:
            
            act_time, act_node = heappop(pq)
            
            if act_node == n - 1:
                if not min_time:
                    min_time = act_time
                elif min_time < act_time:
                    break
            
            if act_time > time_node[act_node]:
                continue

            for neig_node, neig_time in graph[act_node]:
                
                calc = neig_time + act_time
                if calc < time_node[neig_node]:
                    time_node[neig_node] = calc
                    heappush(pq, (calc, neig_node))
                    ways[neig_node] = ways[act_node]
                elif calc == time_node[neig_node]:
                    ways[neig_node] = (ways[neig_node] + ways[act_node]) % 1000000007
                        
        return ways[n-1]
                    
                    
            
            
        