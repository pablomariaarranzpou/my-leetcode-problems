class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        final = []
        
        if m * n != len(original):
            return []
        
        for i in range(m):

            start = i * n

            row = []
            
            for i in range(start, start + n):
                row.append(original[i])
                
            final.append(row)
                
            
                
        return final
                
                
        