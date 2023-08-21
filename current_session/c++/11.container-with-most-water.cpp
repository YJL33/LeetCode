/*
 * @lc app=leetcode id=11 lang=cpp
 *
 * [11] Container With Most Water
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxArea(vector<int>& H) {
    // use two poiners from both end
    // calculate the water area and move the shorter side inward
    // For example, say h is the min(H[r], H[l]), and w is (r-l)
    // gradually move r or l inwoard, and update h*w.
    // calculate only when we have a new h
    // TC: O(n)
    int l = 0, r = H.size()-1;
    int max_seen = 0;
    while (l < r) {
      int h = min(H[l], H[r]);
      max_seen = max(max_seen, h*(r-l));
      if (H[l] < H[r]) {
        while (H[l] <= h and l+1 < H.size()) l++;
      } else {
        while (H[r] <= h and r-1 >= 0) r--;
      }
    }
    return max_seen;
  }
};
// @lc code=end

