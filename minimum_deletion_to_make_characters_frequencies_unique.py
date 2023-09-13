class Solution:
    def minDeletions(self, s: str) -> int:
        # Step 1: Calculate character frequencies
        char_freq = {}
        for char in s:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        # Step 2 and 3
        used_frequencies = set()
        deletions = 0

        # Step 4
        for char in char_freq:
            freq = char_freq[char]
            while freq in used_frequencies:
                freq -= 1
                deletions += 1
            if freq > 0:
                used_frequencies.add(freq)

        # Step 5: Return the minimum number of deletions
        return deletions
