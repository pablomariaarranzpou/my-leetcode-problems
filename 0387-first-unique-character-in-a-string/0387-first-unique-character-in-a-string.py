class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hashmap = {}
        
        for char in s:
            
            if char not in hashmap:
                hashmap[char] = 1
                
            else:
                hashmap[char] += 1
                
        for index, char in enumerate(s):
            
            if hashmap[char] == 1:
                return index
            
        return -1
            
            
        