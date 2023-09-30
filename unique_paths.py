class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array to store the number of unique paths for each cell
        unique_paths = [[0] * n for _ in range(m)]

        # Initialize the top-left cell to 1, as there is only one way to reach it
        unique_paths[0][0] = 1

        # Fill the first row and first column with 1 since there is only one way to move right or down
        for i in range(1, m):
            unique_paths[i][0] = 1
        for j in range(1, n):
            unique_paths[0][j] = 1

        # Calculate the number of unique paths for each cell by summing the paths from the cells above and to the left
        for i in range(1, m):
            for j in range(1, n):
                unique_paths[i][j] = unique_paths[i - 1][j] + unique_paths[i][j - 1]

        # The result is stored in the bottom-right cell
        return unique_paths[m - 1][n - 1]
