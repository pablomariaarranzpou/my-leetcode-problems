class Solution:
    def maxArea(self, height: List[int]) -> int:
        f = 0
        r = len(height) - 1
        m = 0
        while f < r:
            h_f = height[f]
            h_r = height[r]
            a = (r - f) * min(h_f,h_r)
            if a > m: 
                m = a  
            if h_f > h_r:
                r -= 1
            else:
                f += 1       
        return m             