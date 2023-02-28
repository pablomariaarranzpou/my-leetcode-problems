# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        i = 1
        j = n
        
        while i<=j:
            
            p = (i + j)//2
            
            val = guess(p)
            
            if val == 0:
                return p
            elif(val == 1):
                i = p + 1
            else:
                j = p - 1  
        
                
                
            
        