/*
 * @lc app=leetcode id=937 lang=cpp
 *
 * [937] Reorder Data in Log Files
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<string> reorderLogFiles(vector<string>& logs) {
    vector<string> digitLogs, ans;
    vector<pair<string, string>> letterLogs;
    for (string &s : logs) {
      int i = 0;
      while (s[i] != ' ') ++i;
      if (isalpha(s[i + 1])) letterLogs.emplace_back(s.substr(0, i), s.substr(i + 1));
      else digitLogs.push_back(s);
    }
    sort(letterLogs.begin(), letterLogs.end(), [&](auto& a, auto& b) {
      return a.second == b.second ? a.first < b.first : a.second < b.second;
    });
    for (auto &p : letterLogs) ans.push_back(p.first + " " + p.second);
    for (string &s : digitLogs) ans.push_back(s);
    return ans;
  }
};
// @lc code=end

