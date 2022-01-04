class Solution {
    public int getMaxLen(int[] nums) {
        int lnc = 0, lpc = 0, gnc = 0, gpc = 0;
        for (int i = 0; i < nums.length; ++i ) {
            if (nums[i] == 0) {
                lpc = 0;
                lnc = 0;
            } else if (nums[i] > 0) {
                lpc += 1;
                lnc = (lnc == 0) ? 0 : lnc+1;
            } else {
                int tmp = lpc;
                lpc = (lnc == 0) ? 0: lnc+1;
                lnc = Math.max(tmp+1, 1);
            }
            gpc = Math.max(lpc, gpc);
            gnc = Math.max(lnc, gnc);
        }
        return gpc;
    }
    // cp 1567.java Solution.java && javac Solution.java && java Solution
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] test1 = {1,-2,-3,4};
        int[] test2 = {0,1,-2,-3,-4};
        int[] test3 = {0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,1,0};
        
        int ans1 = sol.getMaxLen(test1);
        int ans2 = sol.getMaxLen(test2);
        int ans3 = sol.getMaxLen(test3);
        
        System.out.println(ans1 + " should be 4");
        System.out.println(ans2 + " should be 3");
        System.out.println(ans3 + " should be 2");
    }
}