class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                for x in range(1, min(2 * M, n - i) + 1):
                    dp[i][M] = max(dp[i][M], suffix_sum[i] - dp[i + x][max(M, x)])
        return dp[0][1]       