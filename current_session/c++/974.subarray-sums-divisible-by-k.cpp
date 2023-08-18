/*
 * @lc app=leetcode id=974 lang=cpp
 *
 * [974] Subarray Sums Divisible by K
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

// use mod
// use partial sum
class Solution {
public:
  int subarraysDivByK(vector<int>& nums, int k) {
    int lsum = 0;
    int cnt = 0;
    vector<int> modVec(k, 0);
    // std::copy(modVec.begin(), modVec.end(), std::ostream_iterator<int>(std::cout));
    for (int i=0; i<nums.size(); ++i) {
      lsum = (lsum+nums[i])%k;
      if (lsum < 0) lsum+=k;
      if (lsum == 0) {
        cnt += 1;
      }
      if (modVec[lsum] > 0) {
        cnt += modVec[lsum];
      }
      ++modVec[lsum];
    }
    return cnt;
  }
};
// @lc code=end

