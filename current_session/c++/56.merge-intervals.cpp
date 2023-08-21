/*
 * @lc app=leetcode id=56 lang=cpp
 *
 * [56] Merge Intervals
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> merge(vector<vector<int>>& intervals) {
    // for each i, find next j and j+1 s.t.
    // A[j][0] < A[i][1] && A[j+1][0] > A[i][1]

    sort(intervals.begin(), intervals.end());
    vector<vector<int>> res;
    int i=0;
    while (i<intervals.size()) {
      int start = intervals[i][0], end = intervals[i][1];
      int j = i+1;
      while (j<intervals.size() && intervals[j][0] <= end) {
        end = max(intervals[j++][1], end);
      }
      res.push_back(vector<int>{start, end});
      i = j;
    }
    return res;
  }
};
// @lc code=end

