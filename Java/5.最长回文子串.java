/*
 * @lc app=leetcode.cn id=5 lang=java
 *
 * [5] 最长回文子串
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        int n = s.length(), start = 0, end = 0, max = 1;
        boolean dp[][] = new boolean[n][n];

        for(int i = 0; i < n; i++)
            dp[i][i] = true;

        for(int i = n - 1; i >= 0; i--){
            for(int j = 0; j < n; j++){
                if(i + 1 < j &&  j - 1 > i)
                    dp[i][j] = dp[i + 1][j - 1] && (s.charAt(i) == s.charAt(j));
                else
                    dp[i][j] = (s.charAt(i) == s.charAt(j));

                if(dp[i][j] && j - i + 1 > max){
                    start = i;
                    end = j;
                    max = j - i + 1;
                }
            }
        }

        return s.substring(start, end + 1);
    }
}
// @lc code=end

