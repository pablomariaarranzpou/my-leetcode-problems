class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        row = []
        final = []
        h = len(original)
        
        if m * n != h:
            return []
        
        for i in range(h):
            
            if len(row) < n:
                row.append(original[i])
            else:
                final.append(row)
                row = [original[i]]
                
        if row:
            final.append(row)
                
        return final
                
                
        