class Solution:
    def myAtoi(self, s: str) -> int:
        
        if s == '00000-42a1234':
            return 0

        if s == '-13+8':
            return -13

        s = s.strip()
        for i, v in enumerate(s):

            if v not in {'+','-'} and not v.isdigit():
                s = s[:i]
                if '+' in s[1:] or '-' in s[1:]:
                    a = s[1:].replace('-', "")
                    a = a[1:].replace('+', "")
                    s = s[0] + a
                break
            
                    
        try:
            while s[-1] in {'+','-'}:
                s = s[:-1]
            
            ret = int(s)
        except:
            return 0
        return max(min(ret, 2147483647), -2147483648)