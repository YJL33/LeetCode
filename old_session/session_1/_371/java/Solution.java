/* <Copyright> [2017] YJLee
 371. Sum of Two Integers

    Total Accepted: 56070
    Total Submissions: 109556
    Difficulty: Easy
    Contributors: Admin

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
*/
public class Solution {
    public int getSum(int a, int b) {
        if (b == 0) {
            return a;
        }
        int add = a^b;
        int carry = (a&b)<<1;
        return getSum(add, carry);
    }
    // public static void main(String[] args) {
    //     Solution sol = new Solution();
    //     System.out.println(sol.getSum(10,5));
    // }
}