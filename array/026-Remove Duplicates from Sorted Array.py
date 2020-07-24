from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        for i in range(1, len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                #缺少更改数组的代码
                length += 1
        return length
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_new =0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                nums[next_new] = nums[i]
                next_new += 1
        return next_new
'''

s = Solution()
result = s.removeDuplicates([1,1,2])
print(result)



