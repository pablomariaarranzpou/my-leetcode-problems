class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        paragraph = re.findall(r'\w+', paragraph.lower())

        banned = set(banned)
        
        max_w = ""
        max_l = 0
        mapa = {}
        for word in paragraph:
            
            word = ''.join(e for e in word if e.isalnum())

            if word in banned:
                continue
            if word not in mapa:
                mapa[word] = 1
            else:    
                mapa[word] += 1
                
            if mapa[word] > max_l:
                max_l = mapa[word]
                max_w = word
                    
        
        return max_w            
                
            
            
            
            
            
            
        