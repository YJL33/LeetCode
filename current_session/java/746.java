/*
cd java/
cp 746.java Solution.java
javac Solution.java
java Solution
*/
public class Solution {
    public int minCostClimbingStairs(int[] cost) {
        if (cost.length == 2) return Math.min(cost[0], cost[1]);
        int a = 0, b = 0;
        for (int i = 2; i<=cost.length; i++) {
          int tmp = Math.min(a+cost[i-2], b+cost[i-1]);
          a = b;
          b = tmp;
        }
        return b;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] test1 = {10,15,20};
        int[] test2 = {1,100,1,1,1,100,1,1,100,1};
        int ans1 = sol.minCostClimbingStairs(test1);
        int ans2 = sol.minCostClimbingStairs(test2);
        System.out.println(ans1);
        System.out.println(ans2);
    }
}