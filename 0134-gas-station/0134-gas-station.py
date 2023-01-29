class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        tank=0
        usage = 0
        index = -1
        if (sum(cost) - sum(gas))>0:
            return -1
        for i in range(len(gas)):
            
            if tank+gas[i]>=cost[i]:
                if tank==0:
                    index = i
                tank +=(gas[i]-cost[i])
            else:
                tank = 0
                index = -1
        return index