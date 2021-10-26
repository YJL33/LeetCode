class Solution {
public:
  int maxSubArray(vector<int>& nums) {
    // localMax and globalMax
    int localMax = nums[0], globalMax = nums[0];
    for (int i = 1; i < nums.size(); ++i ) {
      localMax = max(nums[i], localMax+nums[i]);
      globalMax = max(globalMax, localMax);
    }
    return globalMax;
  }
};