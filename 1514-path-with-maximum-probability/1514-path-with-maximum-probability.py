class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        
        # Construir el grafo usando -log(p)
        for i in range(len(edges)):
            prob = -math.log(succProb[i])
            graph[edges[i][0]].append((edges[i][1], prob))
            graph[edges[i][1]].append((edges[i][0], prob))
        
        # Inicialización de la cola de prioridad y distancias
        dist = {start_node: 0}
        pq = [(0, start_node)]
        
        while pq:
            prob_node, node = heapq.heappop(pq)
            
            # Si llegamos al nodo objetivo, devolvemos el resultado
            if node == end_node:
                return math.exp(-prob_node)
            
            # Procesar los vecinos
            for neig_node, neig_prob in graph[node]:
                calc = prob_node + neig_prob
                
                if calc < dist.get(neig_node, float('inf')):
                    dist[neig_node] = calc
                    heapq.heappush(pq, (calc, neig_node))
        
        # Si no encontramos un camino, devolvemos 0.0
        return 0.0

                        
                        
               
        