class Solution:
    def minimumPushes(self, word: str) -> int:
        
        if not word:
            return 0
        
        values = [0] + sorted(Counter(word).values(), reverse=True)
        
        factor = 1
        total = 0
        
        
        for i in range(1, len(values)):
            
            total += (factor * values[i])
            
            if(i % 8 == 0):
                factor += 1

            
            
        return total
            
        