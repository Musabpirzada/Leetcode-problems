class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort the pairs by the second element (righti)
        pairs.sort(key=lambda x: x[1])

        # Initialize variables for counting and tracking the end of the current chain
        longest_chain = 0
        current_end = float('-inf')

        for pair in pairs:
            # If the lefti of the current pair is greater than or equal to the current chain's end,
            # then we can add this pair to the chain
            if pair[0] > current_end:
                longest_chain += 1
                current_end = pair[1]

        return longest_chain
