class Solution {
    public boolean canJump(int[] nums) {
        int farReach = 0;
        int i = 0;
        while (i <= farReach && farReach < nums.length) {
            farReach = Math.max(i+nums[i], farReach);
            i += 1;
        }
        return (farReach >= nums.length-1);
    }

    // cp 55.java Solution.java && javac Solution.java && java Solution
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] test1 = {2,3,1,1,5};
        int[] test2 = {3,2,1,0,4};
        int[] test3 = {0};
        
        boolean ans1 = sol.canJump(test1);
        boolean ans2 = sol.canJump(test2);
        boolean ans3 = sol.canJump(test3);
        
        System.out.println(ans1 + " should be true");
        System.out.println(ans2 + " should be false");
        System.out.println(ans3 + " should be true");

    }
}
