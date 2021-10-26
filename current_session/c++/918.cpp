#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxSubarraySumCircular(vector<int>& nums) {
    int sumOfArray = 0;
    for (auto n: nums) {
      sumOfArray += n;
    }
    return max(maxSubarraySum(nums), sumOfArray-minSubarraySum(nums));
  }
  int maxSubarraySum(vector<int>& nums) {
    int localMax = nums[0], globalMax = nums[0];
    for (int i = 1; i < nums.size(); ++i) {
      localMax = max(localMax+nums[i], nums[i]);
      globalMax = max(localMax, globalMax);
    }
    // cout << "global max: " << globalMax << endl;
    return globalMax;
  }
  int minSubarraySum(vector<int>& nums) {
    if (nums.size() <= 2) return 0;
    int localMin = nums[1], globalMin = nums[1];    
    for (int i = 2; i < nums.size()-1; ++i) {
      localMin = min(localMin+nums[i], nums[i]);
      globalMin = min(globalMin, localMin);
    }
    // cout << "global min: " << globalMin << endl;
    return globalMin;
  }
};

int main() {
  vector<int> test = {-5,3,5};
  vector<int> test2 = {2,-2,2,7,8,0};
  vector<int> test3 = {-2,-3,-1};
  // cout << Solution().maxSubarraySumCircular(test) << " should be 8" << endl;
  // cout << Solution().maxSubarraySumCircular(test2) << " should be 19" << endl;
  cout << Solution().maxSubarraySumCircular(test3) << " should be -1" << endl;
}