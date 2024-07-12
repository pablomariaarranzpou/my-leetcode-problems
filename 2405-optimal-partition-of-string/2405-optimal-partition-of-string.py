class Solution:
    def partitionString(self, s: str) -> int:
        
        act = s[0]
        co = 1
        
        for i in range(1, len(s)):
            
            if s[i] not in act:
                act += s[i]
            else:
                co += 1
                print(act)
                act = s[i]
                
        return co
                
            
            
        