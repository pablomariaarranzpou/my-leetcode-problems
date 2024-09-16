class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        new = []
        mini = float('inf')
        
        for i in timePoints:
            
            new.append(int(i.split(':')[0])*60 + int(i.split(':')[1]))

        
        new.sort()
        
        for i in range(len(new) - 1):
            
            mini = min(mini, new[i+1] - new[i])
            
        return min(mini, 24 * 60 - new[-1] + new[0])