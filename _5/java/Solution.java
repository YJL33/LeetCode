/*
 5. Longest Palindromic Substring

    Total Accepted: 169910
    Total Submissions: 686720
    Difficulty: Medium
    Contributors: Admin

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"
Output: "bb"
*/

import java.util.*;

public class Solution {
    public String longestPalindrome(String s) {
        int start = 0, pldlen = 0, wordlen = s.length();
        if (wordlen < 2) return s;
        for (int i = 0; (i+pldlen/2) < wordlen; i++) {
            int right = i, left = i;
            // check even
            while (right+1 < wordlen && s.charAt(right+1) == s.charAt(i)) {
                ++right;
            }
            // check odd
            while (right+1 < wordlen && left-1 >= 0 && s.charAt(right+1) == s.charAt(left-1)) {
                ++right;
                --left;
            }
            if (right-left+1 > pldlen) {
                start = left;
                pldlen = right-left+1;
            }
        }
        return s.substring(start, start+pldlen);
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        String a = "babad";
        String b = "a";
        String c = "uriowsiuwrhroiwhfooxooxxoxookkkkkkkfjshpopopopopopopopopiiiiiiipopopopojjjjjj";
        System.out.println(sol.longestPalindrome(a));
        System.out.println(sol.longestPalindrome(b));
        System.out.println(sol.longestPalindrome(c));
    }
}
