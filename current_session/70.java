class Solution {
    public int climbStairs(int n) {
        if (n <= 3) return n;
        int a = 2;      // n-2
        int b = 3;      // n-1
        int cur = 3;
        while (cur != n) {
            int tmp = b;
            b = a+b;
            a = tmp;
            cur++;
        }
        return b;
    }
}