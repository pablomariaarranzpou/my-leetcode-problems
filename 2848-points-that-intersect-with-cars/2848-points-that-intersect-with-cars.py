class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        nums = sorted(nums, key=lambda x: x[0])
        suma = 0
        mini = nums[0][0]
        maxi = nums[0][1]
        suma = maxi - mini + 1
        for i in range(1, len(nums)):
            if nums[i][0] <= maxi <= nums[i][1]:
                mini = maxi + 1
            elif maxi > nums[i][1]:
                continue
            else:
                mini = nums[i][0]
            maxi = nums[i][1]
            suma += maxi - mini + 1
        return suma
                
                
                
        
        