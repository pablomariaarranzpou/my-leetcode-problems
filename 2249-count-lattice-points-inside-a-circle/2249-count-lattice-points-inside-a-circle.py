class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        
        for circle in circles:
            x, y, r = circle
            
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i - x) ** 2 + (j - y) ** 2 <= r ** 2:
                        points.add((i, j))
        
        return len(points)

                    
                    
                    
                    
                
                
                
                
                
                
                