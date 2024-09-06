class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        dic = collections.OrderedDict()
        
        for i in range(len(s)):
            
            char = s[i]
            
            if char not in dic:
                dic[char] = [1, i]
            else:
                dic[char][0] += 1 
                
                
        for k, v in dic.items():
            
            if v[0] == 1:
                return v[1]
            
        return -1
                
                
                
            
            
            
            