#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p1 = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1

            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]

                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]

                p0 += 1
                p1 += 1

        
# @lc code=end

