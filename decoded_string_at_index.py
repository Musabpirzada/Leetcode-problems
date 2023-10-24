class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_length = 0

        # Calculate the total length of the decoded string without actually decoding it.
        for char in s:
            if char.isalpha():
                total_length += 1
            else:
                total_length *= int(char)

        # Iterate through the string in reverse and update k and total_length accordingly.
        for char in reversed(s):
            k %= total_length  # Reduce k to its equivalent position in the current segment.
            if k == 0 and char.isalpha():
                return char  # If k becomes 0 and the current character is a letter, return it.

            # Update the total_length for the current segment.
            if char.isalpha():
                total_length -= 1
            else:
                total_length //= int(char)

# Example usage:
solution = Solution()
print(solution.decodeAtIndex("leet2code3", 10))  # Output: "o"
print(solution.decodeAtIndex("ha22", 5))        # Output: "h"
print(solution.decodeAtIndex("a2345678999999999999999", 1))  # Output: "a"
