class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the count of each number
        num_count = {}

        # Iterate through the input array and count the occurrences of each number
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        # Initialize a variable to keep track of the total count of good pairs
        total_good_pairs = 0

        # Iterate through the dictionary and calculate the good pairs for each number
        for count in num_count.values():
            if count > 1:
                # Calculate the number of good pairs for this count using nC2 formula
                total_good_pairs += (count * (count - 1)) // 2

        return total_good_pairs
