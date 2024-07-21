class Solution:
    def maxArea(self, height: List[int]) -> int:
        front = 0
        rear = len(height) - 1
        maxi = 0
        while front < rear:
            h_f = height[front]
            h_r = height[rear]
            area = (rear - front) * min(h_f,h_r)
            if area > maxi: 
                maxi = area  
            if h_f > h_r:
                rear -= 1
            else:
                front += 1       
        return maxi             