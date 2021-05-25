/*
GCD
find the greatest common factor between numbers.
*/
public class Solution {
    public static int greatestCommonFactor(int[] input)
    {
        if (input.length == 1) return input[0];
        int res = input[0];
        for (int i = 1; i < input.length; i++)
        {
            res = helper(res, input[i]);
        }
        return res;
    }
    private static int helper(int a, int b)
    {
        if (b > a)
        {
            int tmp = a;
            a = b;
            b = tmp;
        }
        if (b == 0) return a;
        return helper(b, a % b);
    }
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int[] input = {512, 600, 144};
        System.out.println(greatestCommonFactor(input));
    }

}