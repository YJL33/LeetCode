#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
  int pivotIndex(vector<int>& nums) {
    int leftSum = 0;
    int totalSum = accumulate(nums.begin(), nums.end(), 0);
    for (int i=0; i<nums.size(); ++i) {
      if (2*leftSum == totalSum-nums[i]) return i;
      leftSum += nums[i];
    }
    return -1;
  }
};