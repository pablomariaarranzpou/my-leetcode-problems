class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        dic = {}
        
        for i in range(len(s)):
            
            char = s[i]
            
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1 
                
                
        for i in range(len(s)):
            
            char = s[i]
            
            if dic[char] == 1:
                return i
            
        return -1
                
                
                
            
            
            
            