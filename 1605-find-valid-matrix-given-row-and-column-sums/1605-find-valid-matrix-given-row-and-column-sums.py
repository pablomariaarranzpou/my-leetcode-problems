class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        dp = []
        
        for i in range(len(rowSum)):
            
            row = []
            for j in range(len(colSum)):
                
                minimum = min(rowSum[i], colSum[j])
                
                row.append(minimum)
                
                rowSum[i] -= minimum
                colSum[j] -= minimum
            dp.append(row)
                
                        
        return dp
                
    
        