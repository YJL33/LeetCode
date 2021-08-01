#include <iostream>
#include <vector>
#include <map>

using namespace std;

// use backtrack

class Solution {
public:
  vector<vector<int>> res;
  vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    helper(candidates, vector<int>{}, 0, target);
    return res;
  }
  void helper(vector<int>& nums, vector<int> tmp, int start, int tgt) {
    if (tgt<0) {
      return;
    } else if (tgt==0) {
      res.push_back(tmp);
    } else {
      for (int i=start; i<nums.size(); ++i) {
        tmp.push_back(nums[i]);
        helper(nums, tmp, i, tgt-nums[i]);
        tmp.pop_back();
      }
    }
  }
};