class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [0 for _ in range(len(nums))]

        for i in range(n):
            for j in range(i + 1, i + nums[i] + 1):              
                
                if j >= n:
                    break
                if dp[j] != 0:
                    dp[j] = min(dp[j], dp[i] + 1)
                else:
                    dp[j] = dp[i] + 1

        return dp[-1]