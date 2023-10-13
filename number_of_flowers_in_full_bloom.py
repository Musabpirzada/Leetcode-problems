from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # Extract the start and end times of flowers into separate lists and sort them
        start_times = sorted([s for s, _ in flowers])
        end_times = sorted([e for _, e in flowers])

        # Initialize an empty list to store the results
        result = []

        # For each person in the 'people' list, calculate the number of flowers in bloom at their time
        for t in people:
            # Calculate the count of flowers that have bloomed before or at time 't' (bisect_right)
            count_before_t = bisect_right(start_times, t)

            # Calculate the count of flowers that have wilted before time 't' (bisect_left)
            count_wilted_before_t = bisect_left(end_times, t)

            # Calculate the difference between the two counts to get the number of full bloom flowers
            full_bloom_count = count_before_t - count_wilted_before_t

            # Append the result to the 'result' list
            result.append(full_bloom_count)

        return result
