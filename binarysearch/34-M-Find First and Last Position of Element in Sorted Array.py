from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        if left <= right:
            return (left, right)
        else:
            return [-1, -1]
s = Solution()
print(s.searchRange([4,5,5,6,7,7],7))