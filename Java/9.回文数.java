/*
 * @lc app=leetcode.cn id=9 lang=java
 *
 * [9] 回文数
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        Boolean res = true;

        String str = String.valueOf(x);

        for (int i = 0; i < str.length() / 2 && x >= 0; i++) {
            if (str.charAt(i) != str.charAt(str.length() - i -1))
                res = false;
        }
        
        if (x < 0)
            res = false;

        return res;
    }
}
// @lc code=end

