class Solution:
    def minOperations(self, s: str) -> int:
        
        start_1 = 0
        start_0 = 0
        
        
        for i in range(len(s)):
            
            if(i % 2 == 0):
                chara_start_1 = '1'
                chara_start_0 = '0'
            else:
                chara_start_1 = '0'
                chara_start_0 = '1'
                      
            if(s[i] != chara_start_1):
                start_1 += 1
            
            if(s[i] != chara_start_0):
                start_0 += 1
                
                
        return min(start_1, start_0)