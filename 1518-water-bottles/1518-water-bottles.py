class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        res = 0
        
        while(numBottles >= numExchange):
            var = numBottles // numExchange
            res += numExchange * var
            numBottles -= numExchange * var
            
            numBottles += var
            
        return res + numBottles