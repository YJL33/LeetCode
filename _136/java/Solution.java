/* Copyright [2017] <YJLee>
 136. Single Number

    Total Accepted: 191187
    Total Submissions: 360705
    Difficulty: Easy
    Contributors: Admin

Given an array of integers,
every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
*/

public class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for (int i = 0; i < nums.length; i++)  {
            res ^= nums[i];
        }
        return res;
    }
    public static void main(String[] args) {
        int[] test = {1,2,3,6,5,4,7,8,9,7,8,4,1,2,3,6,9};
        Solution sol = new Solution();
        int ans = sol.singleNumber(test);
        System.out.println(ans);
    }
}
