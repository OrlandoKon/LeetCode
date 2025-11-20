/*
 * @lc app=leetcode.cn id=31 lang=java
 *
 * [31] 下一个排列
 */

// @lc code=start
class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int i = n - 2, j = n - 1;

        while(i >= 0 && nums[i] >= nums[i + 1])
            i--;

        while(i >= 0 && j >= 0 && nums[j] <= nums[i])
            j--;

        if(i >= 0)
            swap(nums, i, j);

        i++;
        j = n - 1;
        
        while(i < j)
            swap(nums, i++, j--);
    }

    public void swap(int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
// @lc code=end

