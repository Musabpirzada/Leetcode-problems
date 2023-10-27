class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()  # Sort the array to ensure smaller numbers are processed first
        mod = 10**9 + 7
        dp = {}
        for num in arr:
            dp[num] = 1  # Each element can be a single node tree

            for left in dp:  # Iterate through the elements that have been processed already
                if num % left == 0:  # Check if a factor exists
                    right = num // left
                    if right in dp:  # Check if the complement exists in the array
                        dp[num] += dp[left] * dp[right]  # Accumulate the number of trees possible

            # Modulo to prevent overflow
            dp[num] %= mod

        # Sum up the results for each element
        return sum(dp.values()) % mod
