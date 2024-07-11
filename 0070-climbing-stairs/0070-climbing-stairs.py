class Solution:
    def climbStairs(self, n: int) -> int:

        if(n <= 3):
            return n
        
        a = 2
        b = 3

        for i in range(3, n):
            res = a + b
            aux = b
            b = res
            a = aux

        return res

