class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            print("Comparando:", nums[i - 1] + nums[i], "o dejo", nums[i])
            if nums[i - 1] + nums[i] > nums[i]:
                nums[i] = nums[i - 1] + nums[i]
            
        return max(nums)
            