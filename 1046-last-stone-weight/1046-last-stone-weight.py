class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

  
        while len(stones) > 1:
        
            stones = sorted(stones)
            

            stones[-2] = stones[-1] - stones[-2]
            
            stones.pop()
            
  
        if len(stones) == 0:
            return 0
        else:
            return stones[0]
                
                