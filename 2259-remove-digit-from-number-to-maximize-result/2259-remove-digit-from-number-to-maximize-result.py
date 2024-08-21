class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        maxi = float("-inf")
        
        for i in range(len(number)):
            
            if number[i] == digit and maxi < int(number[:i] + number[i + 1:]):
                maxi = int(number[:i] + number[i + 1:])
                
        return str(maxi)
        
        