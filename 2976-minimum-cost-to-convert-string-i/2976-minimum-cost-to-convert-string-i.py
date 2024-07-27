import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        def dijkstra(src: str, graph: Dict[str, List[Tuple[str, int]]]) -> Dict[str, int]:
            heap = [(0, src)]
            distances = {chr(i): float('inf') for i in range(ord('a'), ord('z') + 1)}
            distances[src] = 0
            
            while heap:
                dist, letter = heapq.heappop(heap)
                
                if dist > distances[letter]:
                    continue
                
                for neighbor, cost in graph[letter]:
                    new_dist = dist + cost
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))
               
            return distances

        graph = {chr(i): [] for i in range(ord('a'), ord('z') + 1)}
        
        for i in range(len(original)):
            letter = original[i]
            letter_changed = changed[i]
            cost_change = cost[i]
            
            found = False
            for j in range(len(graph[letter])):
                if graph[letter][j][0] == letter_changed:
                    if cost_change < graph[letter][j][1]:
                        graph[letter][j] = (letter_changed, cost_change)
                    found = True
                    break
            if not found:
                graph[letter].append((letter_changed, cost_change))
        
        distances_cache = {}
        total_cost = 0
        
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            
            if source[i] not in distances_cache:
                distances_cache[source[i]] = dijkstra(source[i], graph)
                
            result = distances_cache[source[i]].get(target[i], float('inf'))
            
            if result == float('inf'):
                return -1
            else:
                total_cost += result
        
        return total_cost
        
        
                            
                            
            
                
                
        
            
        