#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = True
        string = str(x)
        length = len(string)

        if x >= 0:
            for i in range(length // 2):
                if string[i] != string[length - i - 1]:
                    res = False
        else:
            res = False

        return res   
# @lc code=end

