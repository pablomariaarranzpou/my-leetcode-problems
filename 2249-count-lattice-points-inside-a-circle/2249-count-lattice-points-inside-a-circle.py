class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        
        for circle in circles:
            x, y, r = circle
            for i in range(-r, r + 1):
                for j in range(-r, r + 1):
                    if i**2 + j**2 <= r**2:
                        points.add((x + i, y + j))
                        points.add((x - i, y + j))
                        points.add((x + i, y - j))
                        points.add((x - i, y - j))
        
        return len(points)


                    
                    
                    
                    
                
                
                
                
                
                
                