#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from typing import List
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        j = n - 1

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        while i >= 0 and j >= 0 and nums[j] <= nums[i]:
            j -= 1

        if i >= 0:
            nums[i], nums[j] = nums[j], nums[i]

        i += 1
        j = n - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
# @lc code=end

