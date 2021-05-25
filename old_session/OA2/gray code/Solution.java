/*
Gray Code
Problem:
Given two hexadecimal numbers find if they can be consecutive in gray code
For example: 10001000, 10001001
return 1
since they are successive in gray code

Example2: 10001000, 10011001
return -1
since they are not successive in gray code.
*/
public class Solution {
    public static boolean isConsecutive(byte a, byte b)
    {
            byte c = (byte)(a ^ b);     // get the difference
            int count = 0;
            while (c != 0)
            {
                c &= (c - 1);           // see if it's a form of 100..000
                count++;                // if yes, only count once.
            }
            return count == 1;
    }
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        byte a = 0x31, b = 0x33;
        System.out.println(isConsecutive(a, b));

    }
}