class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        hashmap = {}
        
        for i in range(len(nums)):
            
            # target = nums[i] + complement
            complement = target - nums[i]
            
            if complement in hashmap:
                return [i, hashmap[complement]]
            
            hashmap[nums[i]] = i
            
        return []
  