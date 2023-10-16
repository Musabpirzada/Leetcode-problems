class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # Initialize the dp array
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        # Initialize base cases
        for j in range(1, m + 1):
            dp[1][j][1] = 1

        # Build the dp table
        for a in range(2, n + 1):
            for b in range(1, m + 1):
                for c in range(1, k + 1):
                    # If we choose the same number as the previous index, the search cost doesn't increase.
                    dp[a][b][c] += b * dp[a - 1][b][c] % MOD
                    dp[a][b][c] %= MOD

                    # Otherwise, we choose a different number, which increases the search cost by 1.
                    for prev_num in range(1, b):
                        dp[a][b][c] += dp[a - 1][prev_num][c - 1] % MOD
                        dp[a][b][c] %= MOD

        # Sum up the ways to build the array with length n, max element m, and search cost k
        ans = sum(dp[n][j][k] for j in range(1, m + 1)) % MOD

        return ans
