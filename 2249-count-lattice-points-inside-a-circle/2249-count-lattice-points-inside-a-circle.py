class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        
        for circle in circles:
            x, y, r = circle
            
            for i in range(-r, r + 1):
                max_j = int((r**2 - i**2)**0.5)
                for j in range(-max_j, max_j + 1):
                    points.add((x + i, y + j))
        
        return len(points)


                    
                    
                    
                    
                
                
                
                
                
                
                