class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ""
        
        both = min(len(word1), len(word2))
        
        for i in range(both):
            
            res += word1[i]
            res += word2[i]
            
            
        if len(word1) > both:
            
            res += word1[both:]
            
        else:
            res += word2[both:]
            
        return res
        