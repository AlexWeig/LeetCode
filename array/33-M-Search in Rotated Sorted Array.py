from typing import List

"""
# my solution has many bugs
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        l, i, r = 0, 0, len(nums) - 1
        while nums[i + 1] > nums[i]: # 越界
             i += 1

        j = i + 1
        if target < nums[0]:
            while j <= r:
                mid = (j + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    j = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
        elif target > nums[0]:
            while l <= i:
                mid = (l + i) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    i = mid + 1
        return -1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # LHS is sorted
                if target >= nums[left] and target < nums[mid]:
                    #target is on LHS
                    right = mid - 1
                else:
                    left = mid + 1
            else: # RHS is sorted
                if target <= nums[right] and target > nums[mid]:
                    # target is on RHS
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
s = Solution()
# result = s.search([4,5,6,7,0,1,2],3)
result = s.search([1,3,1,1,1], 3)
print(result)






