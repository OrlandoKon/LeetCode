#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = n * [True]
        start = 0
        end = 0
        size = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < j and j - 1 > i:
                    dp[j] = dp[j - 1] and (s[i] == s[j])
                else:
                    dp[j] = (s[i] == s[j])

                if dp[j] and j - i + 1 > size:
                    size = j - i + 1
                    start = i
                    end = j

        return s[start:end+1]
                
        
# @lc code=end

