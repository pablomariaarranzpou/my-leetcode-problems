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
      
            if next_i_min <= maxi <= next_i_max:
                maxi = next_i_max
                
            if mini <= next_i_min <= maxi or mini <= next_i_max <= maxi:
                pass
                
            else:
                
                res.append([mini, maxi])
                maxi = next_i_max
                mini = next_i_min
                
            if(i == len(intervals) - 1):
                res.append([mini, maxi])  
                    
        return res