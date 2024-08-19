class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        res = []
        intervals = sorted(intervals, key=lambda x: (x[0],x[1]))
        
        mini = intervals[0][0]
        maxi = intervals[0][1]
        
        if len(intervals) == 1:
            return intervals
        
        for i in range(1, len(intervals)):
            
            next_i_min, next_i_max = intervals[i]
            
            if intervals[i][0] <= mini <= intervals[i][0]:
                
                mini = intervals[i][0]
      
            if intervals[i][0] <= maxi <= intervals[i][1]:
                maxi = intervals[i][1]
                
            if mini <= intervals[i][0] <= maxi or mini <= intervals[i][1] <= maxi:
                pass
                
            else:
                
                res.append([mini, maxi])
                maxi = intervals[i][1]
                mini = intervals[i][0]
                
            if(i == len(intervals) - 1):
                res.append([mini, maxi])  
                    
        return res