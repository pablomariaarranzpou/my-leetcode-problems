class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        
        sets = []
        
        for arr in nums:
            sets.append(set(arr))
            
        return sorted(set.intersection(*sets))
        