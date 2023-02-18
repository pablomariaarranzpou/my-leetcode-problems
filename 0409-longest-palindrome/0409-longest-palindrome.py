class Solution:
    def longestPalindrome(self, s: str) -> int:
        

        app = {}
        _max = 0
        _inv = False
        
        for i in s:
            
            if i not in app.keys():
                app[i] = 1
            else:
                app[i] += 1
                
        
        for i in app.keys():

            if app[i] % 2 == 0:
                _max += app[i]
                
            else:
                _max += app[i] - 1
                _inv = True
                
        
        extra = _max % 2
        
        if(_inv):
            extra = 1
        else:
            extra = 0
        
        return _max + extra
        
        
            
            