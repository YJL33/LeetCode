/*Copyright [2017] <YJLee>
 3. Longest Substring Without Repeating Characters

    Total Accepted: 239091
    Total Submissions: 1007165
    Difficulty: Medium
    Contributors: Admin

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/
#include <iostream>
#include <string>
#include <algorithm>
#include <map>

using std::map;
using std::string;
using std::max;
using std::cout;
using std::endl;

class Solution {
 public:
    int lengthOfLongestSubstring(string s) {
        std::map<char, int> dct;
        int start = 0, maxlen = 0;
        for (int i = 0; i < s.size(); i++) {
            if (dct.find(s[i]) != dct.end() && start <= dct[s[i]]) {
                start = dct[s[i]] + 1;              // update start position
            } else if (maxlen < i-start+1) {
                maxlen = i - start + 1;             // update maxlen
            }
            dct[s[i]] = i;      // update the appearance
        }
        return maxlen;
    }
};
int main(int argc, const char * argv[]) {
    Solution sol = Solution();
    cout << sol.lengthOfLongestSubstring("abcabcbb") << endl;
    cout << sol.lengthOfLongestSubstring("bbbbb") << endl;
    cout << sol.lengthOfLongestSubstring("pwwkew") << endl;
}
