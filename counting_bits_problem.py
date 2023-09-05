class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize a list to store the count of 1's for each number from 0 to n.
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # To count the number of 1's in i, we can use the following formula:
            # dp[i] = dp[i // 2] + (i % 2)
            # dp[i // 2] represents the count of 1's in the binary representation of i // 2,
            # and (i % 2) will be 1 if i is odd and 0 if i is even.
            dp[i] = dp[i // 2] + (i % 2)

        return dp
