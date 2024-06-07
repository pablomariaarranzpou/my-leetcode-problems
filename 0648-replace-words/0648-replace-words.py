class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")
        result = ""
        for word in sentence:
            string = word 
            for lex in dictionary:
                if lex == word[:len(lex)] and len(lex) < len(string):
                    string = lex 
            result += string + " "  
        return result[:-1]
    
    
                
                
            
            