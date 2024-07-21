class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_s = set(nums)
        dicti = {}
        
        for i, num in enumerate(nums):
            if num not in dicti.keys():
                dicti[num] = [i]
                
            else:
                dicti[num].append(i)
        
        
        
        for i in range(len(nums)):
            opt = target - nums[i]
            if opt in nums_s:
                for j in dicti[opt]:
                    if j != i:
                        return [j, i]
        
        return []
  