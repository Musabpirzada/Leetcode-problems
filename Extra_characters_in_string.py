class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        dictionary_set = set(dictionary)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            for l in range(1, i + 1):
                if s[i - l:i] in dictionary_set:
                    dp[i] = min(dp[i], dp[i - l])

        return dp[n]
