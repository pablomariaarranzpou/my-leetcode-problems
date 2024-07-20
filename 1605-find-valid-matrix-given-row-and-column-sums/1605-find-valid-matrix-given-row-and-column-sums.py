class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        dp = [[0 for j in range(len(colSum))] for i in range(len(rowSum))]
        
        for i in range(len(rowSum)):
            
            for j in range(len(colSum)):
                
                minimum = min(rowSum[i], colSum[j])
                
                dp[i][j] = minimum
                
                rowSum[i] -= minimum
                colSum[j] -= minimum
                
                        
        return dp
                
    
        