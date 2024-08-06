class Solution:
    def minimumPushes(self, word: str) -> int:
        
        if not word:
            return 0
        
        values = sorted(Counter(word).values(), reverse=True)
        
        factor = 1
        total = 0
        
        
        for i in range(len(values)):
            
            total += (factor * values[i])
            
            if((i+1) % 8 == 0):
                factor += 1
                
        return total
            
        