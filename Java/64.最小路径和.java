/*
 * @lc app=leetcode.cn id=64 lang=java
 *
 * [64] 最小路径和
 */

// @lc code=start
class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int dp[] = new int[n];

        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(j - 1 >= 0)
                    dp[j] = Math.min(dp[j], dp[j - 1]) + grid[i][j];
                else
                    dp[j] += grid[i][j];
            }
        }

        return dp[n - 1];
    }
}
// @lc code=end

