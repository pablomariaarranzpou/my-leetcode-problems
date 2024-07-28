class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        
        graph = {}
        distance = {}
        
        for i in range(1, n + 1):
            graph[i] = []
            distance[i] = float('inf')
            
        pq = [(0, k)]
        distance[k] = 0
        visited = set()
        
        
        for edge in times:
            graph[edge[0]].append((edge[1], edge[2]))
                
                
        while pq:
            
            dist, node = heapq.heappop(pq)
            
            if node not in visited:
                
                visited.add(node)
                
                for neig in graph[node]:

                    new_dist = dist + neig[1]
                    
                    if new_dist < distance[neig[0]]:
                        distance[neig[0]] = new_dist
                        
                        heapq.heappush(pq, (new_dist, neig[0]))
                        
        
        max_d = max(distance.values())
        
        if max_d == float('inf'):
            return -1
        else:
            return max_d
        