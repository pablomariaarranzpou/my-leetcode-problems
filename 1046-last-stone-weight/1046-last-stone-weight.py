class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            calc = stones[-1] - stones[-2]
            
            stones[-2] = calc
            stones.pop()
            if calc == 0:
                stones.pop()

        if stones:
            return stones[0]
        else:
            return 0
                
                