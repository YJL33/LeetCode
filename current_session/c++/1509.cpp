#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int minDifference(vector<int>& nums) {
    if (nums.size() <= 4) return 0;
    sort(nums.begin(), nums.end());
    int minDiff = INT_MAX;
    int l=0, r=nums.size()-4;
    while (r<nums.size()) {
      // cout << "l:" << l << "  " << nums[l] << endl;
      // cout << "r:" << r << "  " << nums[r] << endl;
      minDiff = min(minDiff, nums[r]-nums[l]);
      r++;
      l++;
    }
    return minDiff;
  }
};