from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = [0] * n  # dp[i] represents the maximum sum of subsequence ending at index i
        dq = deque()  # to store the indices with decreasing sums

        result = float('-inf')  # to store the maximum sum

        for i in range(n):
            # pop elements not in the current window from the front
            while dq and dq[0] < i - k:
                dq.popleft()

            # get the maximum sum within the current window
            dp[i] = max(nums[i], nums[i] + (dp[dq[0]] if dq else 0))

            # pop elements with smaller sums from the back
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()

            dq.append(i)
            result = max(result, dp[i])

        return result
