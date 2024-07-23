class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        values = []
        dicta = {}
        res = []
        for i in nums:
            
            if i not in dicta.keys():
                dicta[i] = 1
            else:
                dicta[i] += 1
                
        for i in dicta.keys():
            values.append((dicta[i], i))
            
        for i in sorted(values, key = lambda x:(x[0], -x[1])):
            res += ([i[1]]*i[0])

        return res
            
            
        