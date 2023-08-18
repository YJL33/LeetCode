/*
 * @lc app=leetcode id=167 lang=cpp
 *
 * [167] Two Sum II - Input Array Is Sorted
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int>& A, int target) {
    // use two pointer
    int l = 0, r = A.size()-1;
    while (A[l] + A[r] != target) {
      if (A[l] + A[r] < target) {
        l++;
      } else {
        r--;
      }
    }
    return {l+1, r+1};
  }
};
// @lc code=end

