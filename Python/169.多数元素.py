#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        map = {}

        for num in nums:
            if num in map.keys():
                map[num] += 1
            else:
                map[num] = 1

        for key, value in map.items():
            if value > length / 2:
                return key
# @lc code=end

