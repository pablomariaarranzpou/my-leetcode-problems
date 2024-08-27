class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        
        visited = set()
        graph = {i:[] for i in range(n)}
        dist = {i: float('inf') for i in range(n)}
        
        for i in range(len(edges)):
            prob = -log(succProb[i])
            graph[edges[i][0]].append((edges[i][1], prob))
            graph[edges[i][1]].append((edges[i][0], prob))
        
        dist[start_node] = 0
        pq = [(0,start_node)]
        
        while pq:
            
            prob_node, node = heappop(pq)
            
            if node == end_node:
                return exp(-prob_node)
            
            
            if node not in visited:
                
                visited.add(node)
                
                for neig in graph[node]:
                    
                    neig_prob = neig[1]
                    neig_node = neig[0]
                    
                    calc = neig_prob + prob_node
                    
                    if calc < dist[neig[0]]:
                        dist[neig[0]] = calc
                        heappush(pq, (calc, neig[0]))
                        
                        
        return 0.0
                        
                        
               
        