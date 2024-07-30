class Solution:
    def countBits(self, n: int) -> List[int]:
        res =[0,1]
        if n == 0:
            return [0]
        pot = 1
        for i in range(2, n+1):
            act = res[i//2]
            if (i % 2 == 0):
                res.append(act)
            else:
                res.append(act + 1)
                
        return res
        
        
        
            