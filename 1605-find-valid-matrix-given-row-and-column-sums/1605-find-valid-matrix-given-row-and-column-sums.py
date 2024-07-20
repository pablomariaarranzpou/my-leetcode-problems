class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = []
        for i in range(len(rowSum)):
            r = []
            for j in range(len(colSum)):
                r_v = rowSum[i]
                c_v = colSum[j]
                if(r_v == 0):
                    r.append(r_v)
                    rowSum[i] -= r_v
                    colSum[j] -= r_v
                elif(c_v == 0):
                    r.append(c_v)
                    rowSum[i] -= c_v
                    colSum[j] -= c_v
                elif(r_v <= c_v):
                    r.append(r_v)
                    rowSum[i] -= r_v
                    colSum[j] -= r_v
                else:
                    r.append(c_v)
                    rowSum[i] -= c_v
                    colSum[j] -= c_v     
            m.append(r)           
        return m        