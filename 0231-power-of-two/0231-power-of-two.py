class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 1:
            return True
        
        if n < 1:
            return False
        
        while n != 2:
            
            if n % 2 == 0:
                n /= 2
                
            else:
                return False
            
        return True