class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
 
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        i = 0
        j = len(nums) - 1
        
        
        while i < j:
            
            one = nums[i]
            two = nums[j]
            
            suma = one[1] + two[1]
            
            if suma == target:
                return [one[0], two[0]]   
            elif suma < target:
                i += 1   
            else:
                j -= 1
                
                
        return []
  