class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c = 0
        if n < 0:
            return False 
        
        for i in bin(n)[2:]:
            if i == '1':
                c += 1
            if c == 2:
                return False
        if c == 0:
            return False
        return True
        
        