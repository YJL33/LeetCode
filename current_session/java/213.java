/*
cp 213.java Solution.java | javac Solution.java | java Solution
*/
import java.util.Arrays;

class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        int[] a = Arrays.copyOfRange(nums, 0, nums.length-1);
        int[] b = Arrays.copyOfRange(nums, 1, nums.length);
        return Math.max(finder(a), finder(b));
    }
    private int finder(int[] houses) {
        int rob = 0, notRob = 0;
        for (int i = 0; i < houses.length; ++i ) {
            int tmp = notRob + houses[i];
            notRob = Math.max(rob, notRob);
            rob = tmp;
        }
        return Math.max(rob, notRob);
    }

    public static void main(String[] args) {
        int[] input = {2,3,2};
        Solution sol = new Solution();
        System.out.println(sol.rob(input));
    }
}