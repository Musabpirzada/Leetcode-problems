class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []

        # Convert the problem into intervals format
        for i, r in enumerate(ranges):
            intervals.append((max(i - r, 0), min(i + r, n)))

        intervals.sort()  # Sort intervals based on the starting point

        min_taps = 0
        farthest_reach = 0
        current_index = 0

        while farthest_reach < n:
            max_reach = farthest_reach
            # Find the interval with the maximum reach that can be covered from the current position
            while current_index < len(intervals) and intervals[current_index][0] <= farthest_reach:
                max_reach = max(max_reach, intervals[current_index][1])
                current_index += 1
            # If we couldn't find any interval to cover from the current position, return -1
            if max_reach == farthest_reach:
                return -1
            # Increment tap count and update the current position
            min_taps += 1
            farthest_reach = max_reach

        return min_taps
