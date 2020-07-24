from typing import List

# Runtime: 32 ms
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []
        for i in nums:
            for j in nums:
                if i + j == target and nums.index(i) not in list and nums.index(j) not in list:
                    list.append(nums.index(i))
                    list.append(nums.index(j))
        return list
s = Solution()
s.twoSum([2,7,11,15],9)
'''

# 40ms
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n],i]
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], i]
            num_to_index[num] = i
        return []

s = Solution()
print(s.twoSum([2,7,11,15],9))


