class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        dic = {}
        
        for i in range(len(s)):
            
            char = s[i]
            
            if char not in dic:
                dic[char] = [1, i]
            else:
                dic[char][0] += 1 
                
                
        for char in s:
            
            if dic[char][0] == 1:
                return dic[char][1]
            
        return -1
                
                
                
            
            
            
            