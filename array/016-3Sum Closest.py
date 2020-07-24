from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2): # 减去2 为了防止越界
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(result - target):
                    result = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return result

'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        res = []
        nums.sort()
        closestDiff = sys.maxint
        sign = 1
        for i in xrange(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(target - s) < closestDiff:
                    sign = -1 if target - s < 0 else 1
                closestDiff = min(abs(target - s), closestDiff)
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        return target - (closestDiff * sign)
'''

