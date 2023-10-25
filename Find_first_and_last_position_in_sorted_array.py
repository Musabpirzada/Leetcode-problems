class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_leftmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_rightmost(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_idx = find_leftmost(nums, target)
        right_idx = find_rightmost(nums, target)

        if left_idx <= right_idx:
            return [left_idx, right_idx]
        else:
            return [-1, -1]
