"""
494. Target Sum

    User Accepted: 247
    User Tried: 348
    Total Accepted: 254
    Total Submissions: 812
    Difficulty: Medium

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:

    The length of the given array is positive and will not exceed 20.
    The sum of elements in the given array will not exceed 1000.
    Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
public class Solution {
    int[] numsarr;
    public int findTargetSumWays(int[] nums, int s) {
        numsarr = new int[nums.length];
        for (int i=0; i<nums.length; i++) numsarr[i] = nums[i];
        return dfs(nums.length, 0, s);
    }
    public int dfs(int lim, int cur, int tgt) {
        if (cur == lim) return (tgt == 0) ? 1 : 0;
        return dfs(lim, cur+1, tgt+numsarr[cur]) + dfs(lim, cur+1, tgt-numsarr[cur]);
    }
    
}