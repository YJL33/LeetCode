/* Copyright [2017] <YJLee>

5. Longest Palindromic Substring

    Total Accepted: 169798
    Total Submissions: 686389
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
#include <iostream>
#include <string>

using std::string;
using std::cout;
using std::endl;

class Solution {
 public:
    std::string longestPalindrome(std::string s) {
        if (s.size() < 2)
            return s;
        int wordlen = s.size(), start = 0, pldlen = 1, left, right;
        for (int i = 0; (i + pldlen / 2) < wordlen;) {
            left = right = i;
            while (right < wordlen - 1 && s[right + 1] == s[right])
                ++right;
            i = right + 1;
            while (right < wordlen - 1 && left > 0 && s[right + 1] == s[left - 1]) {
                ++right;
                --left;
            }
            if (pldlen < right - left + 1) {
                start = left;
                pldlen = right - left + 1;
            }
        }
        return s.substr(start, pldlen);
    }
};

int main(int argc, const char * argv[]) {
    Solution sol = Solution();
    std::string word = "babad";
    std::string word2 = "a";
    std::string word3 = "uriwhfooxooxxookkkkkfjshpopopopopopopopopiiiiipopopopojjjj";
    std::cout << word << " => " << sol.longestPalindrome(word) << std::endl;
    std::cout << word2 << " => " << sol.longestPalindrome(word2) << std::endl;
    std::cout << word3 << " => " << sol.longestPalindrome(word3) << std::endl;
    return 0;
}
