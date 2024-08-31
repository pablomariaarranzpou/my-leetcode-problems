class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        max_prob = {}
        
        for i in range(len(edges)):
            if succProb[i]:
                prob = -(math.log(succProb[i]))
                graph[edges[i][0]].append((prob, edges[i][1]))
                graph[edges[i][1]].append((prob, edges[i][0]))
        
        
        for i in range(n):
            max_prob[i] = float('inf')
                
        max_prob[start_node] = 0
        pq = [(0, start_node)]
        
        visited = set()
        
        
        while pq:
            
            prob_node, node = heapq.heappop(pq)
            
            if node == end_node:
                return math.exp(-prob_node)
            
            if node not in visited:
                
                visited.add(node)
            
                for neig_prob, neig in graph[node]:

                    calc = prob_node + neig_prob

                    if calc < max_prob[neig]:
                        max_prob[neig] = calc
                        heapq.heappush(pq, (calc, neig))
    
        return 0.0

                        
                        
               
        