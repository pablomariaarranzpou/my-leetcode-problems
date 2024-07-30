class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n < 3:
            return n - 1

        a = 0
        b = 1
        c = 1

        for i in range(3, n+1):
            
            aux = a + b + c
            a = b
            b = c
            c = aux

        return c