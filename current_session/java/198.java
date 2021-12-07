/*
cp 198.java Solution.java | javac Solution.java | java Solution
*/
class Solution {
    public int rob(int[] nums) {
        int rob = 0, notRob = 0;
        for (int i = 0; i < nums.length; ++i) {
            int tmp = notRob+nums[i];
            notRob = Math.max(rob, notRob);
            rob = tmp;
        }
        return Math.max(rob, notRob);
    }
}