class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]
        if len(cost) ==2:
            return min(cost)
        i = 2
        while i <= len(cost) - 1:
            cost[i] = min(cost[i-2], cost[i-1]) + cost[i]
            i += 1
        return min(cost[-1], cost[-2])

    

        



