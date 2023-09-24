class Solution:
    def checkString(self, s: str) -> bool:
        
        for i in range(0, len(s) - 1):
            if int(s[i] > s[i + 1]):
                return False
        return True
        