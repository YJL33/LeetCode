class Solution {
    public int maxProfit(int[] prices) {
        int buy = -1*prices[0];         // profit after buy at day 0
        int notBuy = 0;                 // profit of do nothing at day 0
        for (int i = 0; i < prices.length; ++i) {
            int prevNotBuy = notBuy;
            notBuy = Math.max(notBuy, buy+prices[i]);
            buy = Math.max(buy, prevNotBuy-prices[i]);
        }
        return notBuy;
    }    

    public static void main(String[] args) {
        // cp 122_redo.java Solution.java && javac Solution.java && java Solution
        Solution sol = new Solution();
        int[] test1 = {1,1,2,2,3,3};
        int[] test2 = {7,1,5,3,6,4};
        int[] test3 = {1,2,3,4,5};
        int[] test4 = {7,6,5,4,1};
        System.out.println(sol.maxProfit(test1));
        System.out.println(sol.maxProfit(test2));
        System.out.println(sol.maxProfit(test3));
        System.out.println(sol.maxProfit(test4));
    }
}