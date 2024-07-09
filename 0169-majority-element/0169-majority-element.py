class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dicta = {}
        for i in nums:
            if i not in dicta:
                dicta[i] = 1
            else:
                dicta[i] += 1
                
        return max(dicta, key=lambda key: dicta[key])
        