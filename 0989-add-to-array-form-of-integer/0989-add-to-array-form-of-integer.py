class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        
        n = k + int(''.join(str(i) for i in num))
        
        
        
        result = []
        
        for i in str(n):
            result.append(int(i))
            
        return result