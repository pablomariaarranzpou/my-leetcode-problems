class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:


        sentence = sentence.split(" ")
        
        result = ""
        
        dictionary_set = set(dictionary)
        
        for word in sentence:
            
            i = 0
            string = word
            
            for lex in dictionary:
                
                if lex == word[:len(lex)] and lex in dictionary_set and len(lex) < len(string):
                    string = lex
                    
                    
            result += string + " "
                 
                
        return result[:-1]
    
    
                
                
            
            