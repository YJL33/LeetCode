/*
7. Reverse Integer

    Total Accepted: 203936
    Total Submissions: 860888
    Difficulty: Easy
    Contributors: Admin

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
*/
import java.util.*;

public class Solution {
    public int reverse(int x) {
        Long result = 0L;
        int remain = Math.abs(x);
        while (remain != 0) {
            result = result * 10 + remain % 10;
            remain /= 10;
        }
        if (x < 0) result *= -1;
        return (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) ? 0 : result.intValue();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int a = 123;
        int b = -123;
        System.out.println(a);
        System.out.println(b);
        System.out.println(sol.reverse(a));
        System.out.println(sol.reverse(b));
    }
}