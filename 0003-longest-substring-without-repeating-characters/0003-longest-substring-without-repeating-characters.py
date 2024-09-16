class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        act_let = set()
        second = 0
        max_l = 1
        
        if not s:
            return 0
        
        for first in range(len(s)):
            
            while s[first] in act_let and second < first:
                
                act_let.remove(s[second])
                second += 1
                
            act_let.add(s[first])
            
            max_l = max(max_l, first - second + 1)
            
            
        return max_l
        