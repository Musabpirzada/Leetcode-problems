class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_moves = 0
        bob_moves = 0
        n = len(colors)

        # Check if there are no valid moves for Alice or Bob at the beginning
        if 'AAA' not in colors and 'BBB' not in colors:
            return False

        # Count the number of valid moves for Alice and Bob
        for i in range(1, n - 1):
            if colors[i - 1] == colors[i] == colors[i + 1] == 'A':
                alice_moves += 1
            elif colors[i - 1] == colors[i] == colors[i + 1] == 'B':
                bob_moves += 1

        # Alice wins if she has more moves than Bob
        return alice_moves > bob_moves

# Example usage:
solution = Solution()
print(solution.winnerOfGame("ABBBBBBBAAA"))  # Output: False
