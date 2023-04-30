class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        maxi = 0
        
        for i in sentences:
            v = len(i.split(" "))
            if v > maxi:
                maxi = v
        return maxi

        