/*
 * @lc app=leetcode id=283 lang=cpp
 *
 * [283] Move Zeroes
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  void moveZeroes(vector<int>& nums) {
    int cur = 0;
    for (auto n : nums) {
      if (n == 0) continue;
      nums[cur] = n;
      cur++;
    }
    while (cur < nums.size()) {
      nums[cur] = 0;
      cur++;
    }
    return;
  }
};
// @lc code=end

