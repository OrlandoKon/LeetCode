/*
 * @lc app=leetcode.cn id=169 lang=java
 *
 * [169] 多数元素
 */

// @lc code=start
class Solution {
    public int majorityElement(int[] nums) {
        int candidate = -1, count = 0;

        for(int num : nums){
            if(count == 0)
                candidate = num;
            
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }
}
// @lc code=end

