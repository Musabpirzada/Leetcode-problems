class Solution:
    def find132pattern(self, nums):
        n = len(nums)
        if n < 3:
            return False

        stack = []  # Initialize an empty stack
        min_i = [nums[0]]  # Initialize a list to store the minimum value up to index i

        # Find the minimum value for each index i
        for i in range(1, n):
            min_i.append(min(min_i[-1], nums[i]))

        # Iterate from the end of the array to find 132 patterns
        for j in range(n - 1, -1, -1):
            if nums[j] > min_i[j]:
                # Check if there's a value greater than min_i[j] in the stack
                while stack and stack[-1] <= min_i[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])

        return False

# Example usage:
nums1 = [1, 2, 3, 4]
solution = Solution()
print(solution.find132pattern(nums1))  # Output: False

nums2 = [3, 1, 4, 2]
print(solution.find132pattern(nums2))  # Output: True

nums3 = [-1, 3, 2, 0]
print(solution.find132pattern(nums3))  # Output: True
