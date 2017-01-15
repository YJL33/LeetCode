/*
5. Longest Palindromic Substring

    Total Accepted: 131355
    Total Submissions: 550707
    Difficulty: Medium

Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
*/
public class Solution {
    public String longestPalindrome(String s) {
        char[] sc = s.toCharArray();
        int length = 0;
        StringBuilder longest = new StringBuilder();
        for (int i = 0; i < sc.length; i++) {
            int r = i, l = i, r2 = i, l2 = i;
            if ((r+(length/2)) > sc.length) break;
            // check even
            if (i+1 < sc.length && sc[i] == sc[i+1]) {
                r++;
                while (l-1 >= 0 && r+1 < sc.length && sc[r+1] == sc[l-1]) {
                    r++;
                    l--;
                }
            }
            while (l2-1 >= 0 && r2+1 < sc.length && sc[r2+1] == sc[l2-1]) {
                r2++;
                l2--;
            }
            if (r2 > r || l2 < l) {
                r = r2;
                l = l2;
            }
            if ((r-l+1) > length) {
                length = r-l+1;
                longest = new StringBuilder();
                for (int j = l; j <= r; j++)
                    longest.append(sc[j]);
            }
        }
        return longest.toString();
    }
}