#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
from typing import List
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            abs_num = abs(nums[i])

            if abs_num > 0 and abs_num <= n and nums[abs_num - 1] > 0:
                nums[abs_num - 1] *= -1

        while res < n and nums[res] < 0:
            res += 1

        return res + 1
        
# @lc code=end