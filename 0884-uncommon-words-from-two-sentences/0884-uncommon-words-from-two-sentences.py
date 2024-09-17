class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        counter = {}
        
        
        for word in (s1 + " " + s2).split(" "):
            
            if word not in counter:
                
                counter[word] = 1
                
            else:
                counter[word] += 1
                
        return [word for word in counter if counter[word] == 1]
        