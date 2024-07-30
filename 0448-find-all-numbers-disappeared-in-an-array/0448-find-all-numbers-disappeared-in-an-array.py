class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        not_fond = []
        nums_s = set(nums)
        
        
        for i in range(1, len(nums)+1):
            if i not in nums_s:
                not_fond.append(i)
                
        return not_fond
            