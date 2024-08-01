class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0
        
        for citizen in details:
            if(int(citizen[11:13]) > 60):
                count += 1
                
        return count
                    
                    
        