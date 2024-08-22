class Solution:
    def findComplement(self, num: int) -> int:
        
        res = ''
        
        while num > 0:

            res = str(1 if num % 2 == 0 else 0) + res
            
            num //= 2
            
            
        return int(res, 2)
        