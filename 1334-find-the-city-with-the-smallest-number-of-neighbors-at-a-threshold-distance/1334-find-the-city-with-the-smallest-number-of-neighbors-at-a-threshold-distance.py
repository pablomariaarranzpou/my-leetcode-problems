import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Crear una lista de adyacencia para el grafo
        graph = {i: [] for i in range(n)}
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))
        
        def dijkstra(start):
            distances = {i: float('inf') for i in range(n)}
            distances[start] = 0
            pq = [(0, start)]
            visited = set()
            
            while pq:
                current_distance, node = heapq.heappop(pq)
                
                if node in visited:
                    continue
                
                visited.add(node)
                
                for neighbor, weight in graph[node]:
                    distance = current_distance + weight
                    
                    if distance < distances[neighbor] and distance <= distanceThreshold:
                        distances[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))
            
            return len(visited)
        
        cities_reached = []
        for i in range(n):
            reach_count = dijkstra(i)
            cities_reached.append((reach_count, i))
        
        
        cities_reached.sort(key=lambda x: (x[0], -x[1]))
        
        
        return cities_reached[0][1]

           
            
                            
                            
                
                    
                    
            
    