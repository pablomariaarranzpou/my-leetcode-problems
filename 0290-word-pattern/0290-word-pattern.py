class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        
        s_l = s.split(' ')
        dict_s = {}
        dict_p = {}
        n = len(s_l)
        
        if len(pattern) != n:
            return False
        
        for i in range(n):
            
            char = s_l[i]
            pt_char = pattern[i]
            
            if char not in dict_s and pt_char not in dict_s.values():
                dict_s[char] = pt_char
            
            elif pt_char in dict_s.values() and char not in dict_s:
                return False
            
            elif dict_s[char] != pt_char:
                return False
            
        return True
                

            
            
            
        