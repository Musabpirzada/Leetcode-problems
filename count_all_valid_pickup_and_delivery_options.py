class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7

        # Initialize a DP array to store the number of valid sequences for each n.
        dp = [0] * (n + 1)

        # Base case: there is only one valid sequence for n=1.
        dp[1] = 1

        for i in range(2, n + 1):
            # Calculate the number of ways to insert pickup and delivery for n=i
            # based on the result for n=i-1.
            dp[i] = (dp[i - 1] * (2 * i - 1) * i) % MOD

        return dp[n]
