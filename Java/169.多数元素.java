/*
 * @lc app=leetcode.cn id=169 lang=java
 *
 * [169] 多数元素
 */

// @lc code=start
class Solution {
    public int majorityElement(int[] nums) {
        int length = nums.length, res = -1;
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int num : nums)
            map.put(num, map.getOrDefault(num, 0) + 1);

        for(int key : map.keySet()){
            if(map.get(key) > length / 2){
                res = key;
                break;
            }
        }

        return res;
    }
}
// @lc code=end

