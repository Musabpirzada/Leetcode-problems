import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Initialize the minimum effort array with infinity
        min_effort = [[float('inf')] * cols for _ in range(rows)]
        min_effort[0][0] = 0  # Starting cell

        # Create a min heap (priority queue) to keep track of cells to explore
        min_heap = [(0, 0, 0)]  # (effort, row, col)

        while min_heap:
            effort, row, col = heapq.heappop(min_heap)

            # If we've reached the bottom-right cell, return the minimum effort
            if row == rows - 1 and col == cols - 1:
                return effort

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                # Check if the next cell is within bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Calculate the new effort required to reach the next cell
                    new_effort = max(effort, abs(heights[row][col] - heights[nr][nc]))

                    # If the new effort is less than the minimum effort recorded for the cell, update it
                    if new_effort < min_effort[nr][nc]:
                        min_effort[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))
