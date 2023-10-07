class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words
        words = s.split()

        # Reverse each word and join them back together with space
        reversed_words = [word[::-1] for word in words]

        # Join the reversed words to form the final sentence
        result = ' '.join(reversed_words)

        return result
