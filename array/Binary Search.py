from typing import List


class Search():
    def BinarySearch(self, nums:List[int], target:int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
