/*
122

(rename the file to Solution.java and compile)
cp 122.java Solution.java; javac Solution.java; java Solution
*/
class Solution {
    public static int maxProfit(int[] prices) {
        // dp
        if (prices.length == 0) return 0;
        int b = -1*prices[0];
        int s = 0;
        for (int i=1; i<prices.length; i++) {
            int nb = Math.max(b, s-prices[i]);
            int ns = Math.max(s, b+prices[i]);
            b = nb;
            s = ns;
        }
        return s;
    }
    public static void main(String[] args) {
        int[] input = {1,1,2,2,3,3,};
        System.out.println(maxProfit(input));
    }
}