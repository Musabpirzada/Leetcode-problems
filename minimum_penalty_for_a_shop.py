class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix_n_count = [0] * (n + 1)
        suffix_y_count = [0] * (n + 1)

        # Calculate prefix count of 'N'
        for i in range(1, n + 1):
            prefix_n_count[i] = prefix_n_count[i - 1] + (customers[i - 1] == 'N')

        # Calculate suffix count of 'Y'
        for i in range(n - 1, -1, -1):
            suffix_y_count[i] = suffix_y_count[i + 1] + (customers[i] == 'Y')

        min_penalty = float('inf')
        best_hour = 0

        # Calculate penalty for each hour and find the minimum
        for hour in range(n + 1):
            penalty = prefix_n_count[hour] + suffix_y_count[hour]

            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = hour

        return best_hour

# Example usage
solution = Solution()
print(solution.bestClosingTime("YYNY"))  # Output: 2
print(solution.bestClosingTime("NNNNN"))  # Output: 0
print(solution.bestClosingTime("YYYY"))   # Output: 4
