class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize slow and fast pointers
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find the intersection point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # Return the duplicate number
        return slow

#--------------------------------
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            count = sum(1 for num in nums if num <= mid)

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left
