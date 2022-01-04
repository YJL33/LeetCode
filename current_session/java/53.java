/*
cp 53.java Solution.java && javac Solution.java && java Solution
*/
class Solution {
    public int maxSubArray(int[] nums) {
        int globalMax = -10000, localMax = -10000;
        for (int i = 0; i < nums.length; ++i) {
            localMax = Math.max(nums[i], localMax+nums[i]);
            globalMax = Math.max(globalMax, localMax);
        }
        return globalMax;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] test1 = {-2,1,-3,4,-1,2,1,-5,4};
        int[] test2 = {1};
        int[] test3 = {5,4,-1,7,8};
        
        int ans1 = sol.maxSubArray(test1);
        int ans2 = sol.maxSubArray(test2);
        int ans3 = sol.maxSubArray(test3);
        
        System.out.println(ans1 + " should be 6");
        System.out.println(ans2 + " should be 1");
        System.out.println(ans3 + " should be 23");

    }
}