import heapq
class Solution:
    
    
    def nthUglyNumber(self, n: int) -> int:
        
        # si n es menor que 3 ese es el numerp
        if n <= 3:
            return n
        
        visited = set()
        lista = [1]
        
        for i in range(n+5):
            number = heapq.heappop(lista)
            if i == n - 1:
                return number
        
            
            for factor in [2,3,5]:
                if number*factor not in visited:
                    visited.add(number*factor)
                    heapq.heappush(lista, number*factor)
        return 0
        