/*
 * @lc app=leetcode.cn id=75 lang=java
 *
 * [75] 颜色分类
 */

// @lc code=start
class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length, p0 = 0, p1 = 0;

        for(int i = 0; i < n; i++){
            if(nums[i] == 1)
                swap(nums, i, p1++);
            else if(nums[i] == 0){
                swap(nums, i, p0);

                if(p0 < p1)
                    swap(nums, i, p1);

                p0++;
                p1++;
            }
        }
    }

    public void swap(int[] nums, int a, int b){
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }
}
// @lc code=end

