/*
 * @lc app=leetcode.cn id=41 lang=java
 *
 * [41] 缺失的第一个正数
 */

// @lc code=start
class Solution {
    public int firstMissingPositive(int[] nums) {
        int res = 0, n = nums.length;

        for (int i = 0; i < n; i++) {
            if(nums[i] <= 0)
                nums[i] = n + 1;
        }

        for (int i = 0; i < n; i++) {
            int absNum = Math.abs(nums[i]);

            if (absNum > 0 && absNum <= n && nums[absNum - 1] > 0)
                nums[absNum - 1] *= -1;
        }
        
        while (res < n && nums[res] < 0)
            res++;

        return res + 1;
    }
}
// @lc code=end

