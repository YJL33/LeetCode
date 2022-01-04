class Solution {
    public int jump(int[] nums) {
        int count = 0, canReach = 0, end = 0;
        for (int i = 0; i < nums.length-1; ++i) {
            canReach = Math.max(canReach, i+nums[i]);
            if (i == end) {
                count += 1;
                end = canReach;
            }
        }
        return count;
    }
    // cp 45.java Solution.java && javac Solution.java && java Solution
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] test1 = {2,3,1,1,4};
        int[] test2 = {2,3,0,1,4};
        int[] test3 = {2,1};
        
        int ans1 = sol.jump(test1);
        int ans2 = sol.jump(test2);
        int ans3 = sol.jump(test3);
        
        System.out.println(ans1 + " should be 2");
        System.out.println(ans2 + " should be 2");
        System.out.println(ans3 + " should be 1");

    }

}