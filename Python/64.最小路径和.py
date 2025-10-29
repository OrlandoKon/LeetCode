#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from math import inf
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = n * [inf]
        dp[0] = 0

        for i in range(m):
            for j in range(n):
                if j - 1 >= 0:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
                else:
                    dp[j] += grid[i][j]

        return dp[-1]
# @lc code=end

