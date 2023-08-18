/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int removeDuplicates(vector<int>& nums) {
    // simply use a cursor
    int cur = 0;
    for (auto n : nums) {
      if (n == nums[cur]) continue;
      nums[++cur] = n;
    }
    return cur+1;
  }
};
// @lc code=end

