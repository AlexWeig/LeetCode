from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = 0
        while left <= right:
            # mid = (left + right) // 2
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        if nums[mid] < target:
            return mid + 1
        elif nums[mid] > target:
            return mid