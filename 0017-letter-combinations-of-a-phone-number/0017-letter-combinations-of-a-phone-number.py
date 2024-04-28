class Solution:
    
    import itertools
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        numbers = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
                   '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        product, response = [], []
        
        for digit in digits:
            product.append(numbers[digit])
        
        for i in itertools.product(*product):
            response.append("".join(i))
                  
        return response
                    
        

        