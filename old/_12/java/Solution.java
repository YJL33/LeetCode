/* Copyright [2017] <YJLee>
 12. Integer to Roman

    Total Accepted: 92222
    Total Submissions: 214117
    Difficulty: Medium
    Contributors: Admin

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
*/
import java.util.*;

public class Solution {
    public String intToRoman(int num) {
        Map<Integer, Character> roman = new HashMap<Integer, Character>();
        roman.put(1, 'I');
        roman.put(5, 'V');
        roman.put(10, 'X');
        roman.put(50, 'L');
        roman.put(100, 'C');
        roman.put(500, 'D');
        roman.put(1000, 'M');
        roman.put(5000, 'Q');
        StringBuilder ans = new StringBuilder();
        int divisor = 1000;
        while (divisor != 0) {
            if (num/divisor == 4) {
                ans.append(roman.get(divisor));
                ans.append(roman.get(5*divisor));
            }
            else if (num/divisor == 9) {
                ans.append(roman.get(divisor));
                ans.append(roman.get(10*divisor));
            }
            else if (num/divisor >= 5) {
                ans.append(roman.get(5*divisor));
                for (int i = 0; i < num/divisor-5; i++) {
                    ans.append(roman.get(divisor));
                }
            }
            else if (num/divisor != 0) {
                for (int i = 0; i < num/divisor; i++) {
                    ans.append(roman.get(divisor));
                }
            }
            num = num%divisor;
            divisor /= 10;
        }
        return ans.toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.intToRoman(2906));
    }
}
