class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        dic = defaultdict(int)
        
        
        for i in range(len(s)):
            dic[s[i]] += 1 
                
                
        for i, char in enumerate(s):
            
            if dic[char] == 1:
                return i
            
        return -1
                
                
                
            
            
            
            