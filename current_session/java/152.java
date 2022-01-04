class Solution {
    public int maxProduct(int[] nums) {
        int localMax = nums[0], localMin = nums[0], globalMax = nums[0];
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] < 0) {
                int tmp = localMax;
                localMax = localMin;
                localMin = tmp;
            }
            localMax = Math.max(nums[i], nums[i]*localMax);
            localMin = Math.min(nums[i], nums[i]*localMin);
            globalMax = Math.max(localMax, globalMax);
        }
        return globalMax;
    }
    // cp 152.java Solution.java && javac Solution.java && java Solution
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] test1 = {2,3,-2,4};
        int[] test2 = {-2,0,-1};
        int[] test3 = {-2};
        int[] test4 = {-4,-3,-2};
        int ans1 = sol.maxProduct(test1);
        int ans2 = sol.maxProduct(test2);
        int ans3 = sol.maxProduct(test3);
        int ans4 = sol.maxProduct(test4);
        System.out.println(ans1 + " should be 6");
        System.out.println(ans2 + " should be 0");
        System.out.println(ans3 + " should be -2");
        System.out.println(ans4 + " should be 12");
    }
}