class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        res = 0
        
        while(numBottles >= numExchange):
            res += numExchange
            numBottles -= numExchange
            numBottles += 1
            
        return res + numBottles