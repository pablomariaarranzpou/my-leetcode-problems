class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        dic_s = {}
        dic_t = {}
        for i in range(n):
            
            char = s[i]
            if char not in dic_s:
                dic_s[char] = 1
            else:
                dic_s[char] += 1
                
            char = t[i]
            if char not in dic_t:
                dic_t[char] = 1
            else:
                dic_t[char] += 1
            
        return dic_t == dic_s
            