from typing import List

# my solution
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_free = 0
        for i, num in enumerate(nums):
            if num !=val:
                nums[next_free] = num
                next_free += 1
        return next_free

