class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)  # Convert the list of stones to a set for efficient lookup

        dp = {}  # Create a dictionary to store the results of subproblems

        # Define a recursive function to check if the frog can reach the target stone
        def can_reach(current, jump):
            if current == stones[-1]:
                return True

            if (current, jump) in dp:
                return dp[(current, jump)]

            for next_jump in [jump - 1, jump, jump + 1]:
                if next_jump > 0 and current + next_jump in stone_set:
                    if can_reach(current + next_jump, next_jump):
                        dp[(current, jump)] = True
                        return True

            dp[(current, jump)] = False
            return False

        return can_reach(0, 0)

# Example usage
solution = Solution()
stones1 = [0, 1, 3, 5, 6, 8, 12, 17]
print(solution.canCross(stones1))  # Output: True

stones2 = [0, 1, 2, 3, 4, 8, 9, 11]
print(solution.canCross(stones2))  # Output: False
