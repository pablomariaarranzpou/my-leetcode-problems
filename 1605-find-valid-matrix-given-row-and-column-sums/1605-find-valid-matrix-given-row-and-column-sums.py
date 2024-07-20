class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = []
        for i in range(len(rowSum)):
            r = []
            for j in range(len(colSum)):
                minimum = min(rowSum[i], colSum[j])
                r.append(minimum)
                rowSum[i] -= minimum
                colSum[j] -= minimum
            m.append(r)           
        return m
                
    
        