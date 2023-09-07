class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dp = [[num] for num in nums] 
            
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        
        max_subset = max(dp, key=len)
        return max_subset 