/*
 * @lc app=leetcode id=88 lang=cpp
 *
 * [88] Merge Sorted Array
 */

// @lc code=start

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    // simply use two pointer
    // first copy all m numbers in nums1 to the latter part
    // TC: O(m)+O(m)+O(n)
    // SC: N/A
    if (n == 0) return;

    // normal case
    for (int i = m-1; i >= 0; i--) {
      nums1[i+n] = nums1[i];
    }
    int i = n, j = 0, k = 0;
    while (k < m+n) {
      if (i == m+n) {
        nums1[k] = nums2[j];
        j++;
      } else if (j == n) {
        nums1[k] = nums1[i];
        i++;
      } else if (nums1[i] <= nums2[j]) {
        nums1[k] = nums1[i];
        i++;
      } else {
        nums1[k] = nums2[j];
        j++;
      }
      k++;
    }
    return;
  }
};
// @lc code=end

