from typing import List

# 使用Set，但是速度太慢
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                v = nums[i] + nums[l] + nums[r]

                if v == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif v > 0:
                    r -= 1
                elif v < 0:
                    l += 1
        return list(map(list,result)) # 使用了map内置函数，
        # map(function, iterable, ...)
        # 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nlen = len(nums)
        if (nlen < 3):
            return []
        answer = []
        nums.sort()
        for i in range(nlen):
            if (nums[i] > 0):
                return answer
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            l = i + 1
            r = nlen - 1
            while (l < r):
                if (nums[i] + nums[l] + nums[r] == 0):
                    answer.append([nums[i], nums[l], nums[r]])
                    while (l < r and nums[l] == nums[l + 1]):
                        l += 1
                    while (l < r and nums[r] == nums[r - 1]):
                        r -= 1
                    l += 1
                    r -= 1
                elif (nums[i] + nums[l] + nums[r] < 0):
                    l += 1
                else:
                    r -= 1
        return answer
'''
tree = Solution()
result = tree.threeSum([-1, 0, 1, 2, -1, 4])
print(result)