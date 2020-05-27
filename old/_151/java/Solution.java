/*
 151. Reverse Words in a String

    Total Accepted: 141210
    Total Submissions: 898175
    Difficulty: Medium
    Contributors: Admin

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
*/

public class Solution {
    public String reverseWords(String s) {
        // 1. reverse
        // 2. flip word
        // 3. eliminate spaces
        if (s.length() == 0) {
            return s;
        }

        int start = s.length()-1;
        while (start >= 0 && s.charAt(start) == ' ') {
            start--;
        }
        if (start == -1) return "";

        StringBuilder res = new StringBuilder(s).reverse();
        int i = 0;
        while (i < res.length()) {
            int left = i;
            while (i != res.length() && res.charAt(i) != ' ') {
                i++;
            }
            int right = i;
            StringBuilder word = new StringBuilder(res.substring(left, right));
            res.replace(left, right, word.reverse().toString());
            i++;
        }

        // deleteCharAt()
        while (res.charAt(0) == ' ') {
            res.deleteCharAt(0);
        }
        while (res.charAt(res.length()-1) == ' ') {
            res.deleteCharAt(res.length()-1);
        }
        int j = 0;
        while (j < res.length()) {
            if (res.charAt(j) == ' ' && res.charAt(j+1) == ' ')  {
                res.deleteCharAt(j);
            }
            else {
                j++;
            }
        }
        // System.out.println(res.length());
        return res.toString();
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.reverseWords("the sky is blue"));
        System.out.println(sol.reverseWords("     a  b     "));
        System.out.println(sol.reverseWords(" "));
    }
}
