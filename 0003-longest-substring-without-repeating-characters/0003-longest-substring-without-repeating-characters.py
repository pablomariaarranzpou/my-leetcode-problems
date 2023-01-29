class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        subst=""
        max_subst=0
        for i in s:
            if i not in subst:
                subst+=i
            else:
                ind=subst.index(i)+1
                subst=subst[ind:]+i
                
            if len(subst)>max_subst:
                max_subst=len(subst)
        return max_subst

