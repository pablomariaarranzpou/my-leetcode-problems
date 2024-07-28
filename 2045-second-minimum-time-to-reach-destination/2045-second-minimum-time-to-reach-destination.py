import heapq
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        
        pq = [(0, 1)]
        visited = set()
        graph = {}
        distance = {i: [float('inf'), float('inf')] for i in range(1, n + 1)}
        distance[1][0] = 0
            
            
        for edge in edges:
            
            if edge[0] not in graph.keys():
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])
                
                
            if edge[1] not in graph.keys():
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0]) 
                
        
        while pq:
            
            act_time, node = heapq.heappop(pq)
                
            for neihgbour in graph[node]:
                

                if (act_time // change) % 2 == 1:
                    new_time = (act_time // change + 1) * change + time
                else:
                    new_time = act_time + time
                
                if new_time < distance[neihgbour][0]:
                    distance[neihgbour][1] = distance[neihgbour][0]
                    distance[neihgbour][0] = new_time
                    heapq.heappush(pq, (new_time, neihgbour))
                elif distance[neihgbour][0] < new_time < distance[neihgbour][1]:
                    distance[neihgbour][1] = new_time
                    heapq.heappush(pq, (new_time, neihgbour))
                    

        return distance[n][1]
        