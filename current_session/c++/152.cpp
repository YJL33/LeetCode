#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxProduct(vector<int>& nums) {
    // use dp, dp[i] = solution at i
    int localmin = nums[0], localmax = nums[0], globalmax = nums[0];
    for (int i=1;i<nums.size();++i) {
      if (nums[i]<0) swap(localmin, localmax);
      localmin = min(nums[i], nums[i]*localmin);
      localmax = max(nums[i], nums[i]*localmax);
      globalmax = max(globalmax, localmax);
    }
    return globalmax;
  }
};