class Solution:
    def robe(self, nums: List[int], n: int) -> int:
        if n <= 2:
            return max(nums)
        dp = [0]*n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.robe(nums[1:], n - 1),
         self.robe(nums[:-1], n - 1))
    