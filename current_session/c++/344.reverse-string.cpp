/*
 * @lc app=leetcode id=344 lang=cpp
 *
 * [344] Reverse String
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int l = 0, r = s.size()-1;
        while (l < r) {
            char tmp = s.at(l);
            s.at(l++) = s.at(r);
            s.at(r--) = tmp;
        }
        return;
    }
};
// @lc code=end

