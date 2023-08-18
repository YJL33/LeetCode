/*
 * @lc app=leetcode id=941 lang=cpp
 *
 * [941] Valid Mountain Array
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
  bool validMountainArray(vector<int>& arr) {
    if (arr.size() < 3) return false;
    int l = 0, r =arr.size()-1;
    while (l+1 < arr.size() && arr[l+1] > arr[l]) {
      l++;
    }
    while (r-1 >= 0 && arr[r-1] > arr[r]) {
      r--;
    }
    return (0 < l && l == r && r < arr.size()-1);
  }
};
// @lc code=end

