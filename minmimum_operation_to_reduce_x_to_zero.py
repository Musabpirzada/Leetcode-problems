class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Calculate the total sum of the array
        total_sum = sum(nums)

        # Calculate the target sum
        target_sum = total_sum - x

        if target_sum < 0:
            return -1  # If the target sum is negative, it's not possible

        left, right = 0, 0
        current_sum = 0
        max_length = -1  # To track the length of the longest subarray

        while right < len(nums):
            current_sum += nums[right]
            right += 1

            while current_sum > target_sum:
                current_sum -= nums[left]
                left += 1

            if current_sum == target_sum:
                max_length = max(max_length, right - left)

        # If max_length is still -1, it means no subarray was found
        return -1 if max_length == -1 else len(nums) - max_length
