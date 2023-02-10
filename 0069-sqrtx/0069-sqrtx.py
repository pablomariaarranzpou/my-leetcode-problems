class Solution:
    def mySqrt(self, x: int) -> int:
        
        prev = 0
        
        if x == 0:
            return 0
        
        for i in range(x + 1):

            if i*i >  x:
                return prev
            elif i*i == x:
                return i
            else:
                prev = i
        