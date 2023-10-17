class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(
                    dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1],  # Include both nums1[i-1] and nums2[j-1]
                    dp[i - 1][j],  # Exclude nums1[i-1]
                    dp[i][j - 1],  # Exclude nums2[j-1]
                    nums1[i - 1] * nums2[j - 1]  # Start a new subsequence with nums1[i-1] and nums2[j-1]
                )

        return dp[m][n]
