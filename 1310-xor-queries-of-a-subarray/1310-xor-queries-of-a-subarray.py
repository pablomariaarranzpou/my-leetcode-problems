class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        

        prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]

        res = [prefix[second + 1] ^ prefix[first] for first, second in queries]
        return res
            
        