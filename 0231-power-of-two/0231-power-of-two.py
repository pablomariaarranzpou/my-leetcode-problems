class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False 
        
        c = list(bin(n)[2:]).count("1")

        if c > 1 or c == 0:
            return False

        return True
        
        