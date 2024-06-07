class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")
        result = ""
        dictionary = sorted(dictionary, key=len)[::-1]
        for word in sentence:
            string = word 
            for lex in dictionary:
                if lex == word[:len(lex)]:
                    string = lex 
            result += string + " "  
        return result[:-1]
    
    
                
                
            
            