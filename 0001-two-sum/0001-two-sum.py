class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_s = set(nums)
        indexes = [(num, i) for i, num in enumerate(nums)]
        
        indexes = sorted(indexes)
        
        for i in range(len(nums)):
            num_with_index = indexes[i]
            
            opt = target - num_with_index[0]
            if(opt in nums_s):
                for j in indexes:
                    
                    if j[0] == opt and num_with_index[1] != j[1]:
                        return [j[1], num_with_index[1]]
            
  