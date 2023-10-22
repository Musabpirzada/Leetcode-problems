class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize a list to store the number of combinations for each target value.
        dp = [0] * (target + 1)

        # There is one way to achieve a target of 0, which is to not select any element.
        dp[0] = 1

        # Iterate through all possible target values from 1 to the given target.
        for i in range(1, target + 1):
            for num in nums:
                # If the current target value is greater than or equal to the current number,
                # then add the number of combinations for the remaining target value (i - num).
                if i >= num:
                    dp[i] += dp[i - num]

        # The final value in dp[target] will contain the number of combinations to reach the target.
        return dp[target]
