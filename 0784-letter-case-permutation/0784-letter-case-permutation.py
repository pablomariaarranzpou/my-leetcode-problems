class Solution:
    
    def __init__(self):
        self.solution = []
        
    def letterCasePermutation(self, s: str) -> List[str]:
        
        self.letter_backtrack(s, 0, "")
        
        return self.solution
        
        
        
    def letter_backtrack(self, s: str, index: int, actual: str):
        
        if index == len(s):
            if actual not in self.solution:
                self.solution.append(actual)
                
        else:
            if s[index].isalpha():

                if s[index].islower():
                    
                    actual += s[index]
                    
                    if (self.letter_backtrack(s, index + 1, actual)):
                        return True
                    
                    actual = actual[:-1]
                    
                    actual += s[index].upper()

                    if (self.letter_backtrack(s, index + 1, actual)):
                        return True
                    
                    s[index].lower()
                    actual = actual[:-1]

                else:

                    actual += s[index]
                    
                    if (self.letter_backtrack(s, index + 1, actual)):
                        return True
                    
                    actual = actual[:-1]
                    actual += s[index].lower()

                    if (self.letter_backtrack(s, index + 1, actual)):
                        return True
                    
                    s[index].upper()
                    actual = actual[:-1]
            else:
                actual += s[index]

                if (self.letter_backtrack(s, index + 1, actual)):
                        return True

                actual = actual[:-1]

                
                
                
            
            
            
        