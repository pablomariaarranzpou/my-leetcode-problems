class Solution:
    def fib(self, n: int) -> int:
        
        a, b = 1, 1
        
        if n == 2 or n == 1:
            return 1
        if n == 0:
            return 0
        
        
        for i in range(n-2):
            aux = a + b
            a = b
            b = aux
            
            
        return b