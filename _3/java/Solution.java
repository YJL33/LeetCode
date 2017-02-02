/*
// Copyright [2017] <YJLee>
//  3. Longest Substring Without Repeating Characters

//     Total Accepted: 239091
//     Total Submissions: 1007165
//     Difficulty: Medium
//     Contributors: Admin

// Given a string, find the length of the longest substring without repeating characters.

// Examples:

// Given "abcabcbb", the answer is "abc", which the length is 3.
// Given "bbbbb", the answer is "b", with the length of 1.
// Given "pwwkew", the answer is "wke", with the length of 3.
// Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/
// import java.util.*;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> charPos = new HashMap<Character, Integer>();
        int start = 0, maxlen = 0;
        for (int i = 0; i < s.length(); i++) {
            if (charPos.containsKey(s.charAt(i)) && start <= charPos.get(s.charAt(i))) {
                start = charPos.get(s.charAt(i)) + 1;   // update the starting position
            }
            else if (maxlen < i - start + 1) {
                maxlen = i - start + 1;                 // update maxlen
            }
            charPos.put(s.charAt(i), i);
        }
        return maxlen;
    }
    // public static void main(String[] args) {
    //     Solution sol = new Solution();
    //     System.out.println(sol.lengthOfLongestSubstring("abcabcbb"));
    //     System.out.println(sol.lengthOfLongestSubstring("bbbbb"));
    //     System.out.println(sol.lengthOfLongestSubstring("pwwkew"));
    // }
}