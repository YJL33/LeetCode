/*
 * @lc app=leetcode id=80 lang=cpp
 *
 * [80] Remove Duplicates from Sorted Array II
 */

// @lc code=start

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int removeDuplicates(vector<int>& nums) {
    // record the previous element and its count
    // go through the whole array
    // if prev == element, check its count
    //   if count == 1, simply count+1 more move cursor
    //   if count > 1, continue
    // else (prev != elelment)
    //   replace one and update prev and count
    int prev = nums[0];
    int prev_count = 1;
    int cur = 1;      // place where new element should be
    for (int i=1; i<nums.size(); i++) {
      if (nums[i] != prev) {
        nums[cur++] = nums[i];
        prev = nums[i];
        prev_count = 1;
      } else if (prev_count != 1) {
        continue;
      } else {
        nums[cur++] = nums[i];
        prev_count++;
      }
    }
    return cur;
  }
};
// @lc code=end

