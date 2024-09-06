class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        opened = {'[':']', '(':')', '{':'}'}
        
        for p in s:
            
            if p in opened.keys():
                stack.append(p)
            else:
                
                if not stack:
                    return False
                
                if opened[stack.pop()] != p:
                    return False
                
                
        if not stack:
            return True
        
        else:
            return False
        