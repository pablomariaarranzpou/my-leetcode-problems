class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        c = 1
        
        numerated_sorted = sorted(enumerate(arr), key=lambda x: x[1])
        response = [0] * len(arr)
        prev = float("-inf")

        for i in range(len(arr)):
            ind, value = numerated_sorted[i]
            if value != prev:
                response[ind] = c
                prev = value
            else:
                c -= 1
                response[ind] = c
            
            c+= 1
        return response
        
        
        
        