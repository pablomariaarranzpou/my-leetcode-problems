class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            if succProb[i]:
                prob = -(math.log(succProb[i]))
                graph[edges[i][0]].append((edges[i][1], prob))
                graph[edges[i][1]].append((edges[i][0], prob))
        
        dist = {start_node: 0}
        pq = [(0, start_node)]
        
        while pq:
            prob_node, node = heapq.heappop(pq)
            
            if node == end_node:
                return math.exp(-prob_node)
            
            for neig_node, neig_prob in graph[node]:
                calc = prob_node + neig_prob
                
                if calc < dist.get(neig_node, float('inf')):
                    dist[neig_node] = calc
                    heapq.heappush(pq, (calc, neig_node))
    
        return 0.0

                        
                        
               
        