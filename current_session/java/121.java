class Solution {
    public int maxProfit(int[] prices) {
        int buy = prices[0], maxProfit = 0;
        for (int i = 1; i < prices.length; ++i) {
            maxProfit = Math.max(maxProfit, prices[i]-buy);
            buy = Math.min(prices[i], buy);
        }
        return maxProfit;
    }
    // cp 121.java Solution.java && javac Solution.java && java Solution
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] test1 = {7,1,5,3,6,4};
        int[] test2 = {7,6,4,3,1};
        System.out.println(sol.maxProfit(test1));
        System.out.println(sol.maxProfit(test2));
    }
}