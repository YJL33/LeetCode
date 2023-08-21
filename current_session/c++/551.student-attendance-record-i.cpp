/*
 * @lc app=leetcode id=551 lang=cpp
 *
 * [551] Student Attendance Record I
 */

// @lc code=start
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool checkRecord(string s) {
        int absent_count = 0, late_consecutive_count = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s.at(i) == 'P') {
                late_consecutive_count = 0;
                continue;
            } else if (s.at(i) == 'A') {
                late_consecutive_count = 0;
                if (++absent_count == 2) return false;
            } else {
                if (++late_consecutive_count == 3) return false;
            }
        }
        return true;
    }
};
// @lc code=end

